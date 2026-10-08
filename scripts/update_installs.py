"""Обновляет число установок приложений из Google Play в README.md и README.en.md.

Числа живут внутри маркеров, остальной README скрипт не трогает:
    <!--installs:soft.divan.mafia-->5 тыс.+<!--/installs-->
    <!--installs-total--><img src=".../badge/107_000+-установок-..."><!--/installs-total-->

Список приложений берётся из самих маркеров. При любой странности в данных
скрипт падает с кодом 1 и ничего не записывает.

    python3 scripts/update_installs.py                  # обновить README
    python3 scripts/update_installs.py --dry-run        # только показать изменения
    python3 scripts/update_installs.py --fixtures DIR   # брать страницы из DIR/<id>.html
"""
import argparse
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {"README.md": "ru", "README.en.md": "en"}

APP_MARKER = re.compile(r"<!--installs:([\w.]+)-->(.*?)<!--/installs-->")
TOTAL_MARKER = re.compile(r"(<!--installs-total-->)(.*?)(<!--/installs-total-->)", re.S)
TOTAL_NUMBER = re.compile(r"badge/[\d_,]+\+")

# Блок установок на странице Play: ["5,000+",5000,7899,"5K+"]
PLAY_INSTALLS = re.compile(r'\["([\d,\s ]+)\+",(\d+),(\d+),"[^"]+"\]')

# Пороги Google Play: 1, 5, 10, 50, ..., 5 млрд, 10 млрд
LADDER = sorted(m * 10 ** k for k in range(11) for m in (1, 5))

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


class InstallsError(Exception):
    pass


def format_bucket(n, lang):
    if lang == "ru":
        if n >= 1_000_000:
            return f"{n // 1_000_000} млн+"
        if n >= 1_000:
            return f"{n // 1_000} тыс.+"
        return f"{n}+"
    if n >= 1_000_000:
        return f"{n // 1_000_000}M+"
    if n >= 1_000:
        return f"{n // 1_000}K+"
    return f"{n}+"


def parse_bucket(text):
    """Обратное к format_bucket: «5 тыс.+» / «5K+» → 5000."""
    m = re.fullmatch(r"(\d+)\s*(тыс\.|млн|K|M)?\+", text.strip())
    if not m:
        raise InstallsError(f"не понимаю значение в маркере: {text!r}")
    mult = {"тыс.": 1_000, "K": 1_000, "млн": 1_000_000, "M": 1_000_000}.get(m.group(2), 1)
    return int(m.group(1)) * mult


def format_total(buckets, lang):
    total = sum(buckets)
    if total >= 1_000:
        total -= total % 1_000
    number = f"{total:,}"
    return number.replace(",", "_") if lang == "ru" else number


def extract_bucket(html, app_id):
    m = PLAY_INSTALLS.search(html)
    if not m:
        raise InstallsError(f"{app_id}: на странице не найден блок установок")
    shown = int(re.sub(r"\D", "", m.group(1)))
    bucket, exact = int(m.group(2)), int(m.group(3))
    if shown != bucket:
        raise InstallsError(f"{app_id}: порог {shown} не совпадает с {bucket} — разобран не тот блок")
    if bucket not in LADDER:
        raise InstallsError(f"{app_id}: {bucket} не является порогом Google Play")
    if exact < bucket:
        raise InstallsError(f"{app_id}: точное число {exact} меньше порога {bucket}")
    return bucket


def fetch_page(app_id, attempts=3):
    url = f"https://play.google.com/store/apps/details?id={app_id}&hl=en&gl=US"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as e:
            if attempt == attempts:
                raise InstallsError(f"{app_id}: не удалось загрузить страницу ({e})")
            time.sleep(10 * attempt)


def collect_app_ids(texts):
    """Проверяет, что маркеры во всех файлах согласованы, и возвращает список id."""
    ids_by_file = {}
    for name, text in texts.items():
        ids = [app_id for app_id, _ in APP_MARKER.findall(text)]
        if len(ids) != len(set(ids)):
            raise InstallsError(f"{name}: маркер приложения повторяется")
        if len(TOTAL_MARKER.findall(text)) != 1:
            raise InstallsError(f"{name}: должен быть ровно один маркер installs-total")
        ids_by_file[name] = ids
    reference = set(next(iter(ids_by_file.values())))
    for name, ids in ids_by_file.items():
        if set(ids) != reference:
            raise InstallsError(f"{name}: набор приложений отличается от других файлов")
    if not reference:
        raise InstallsError("в README не найдено ни одного маркера установок")
    return sorted(reference)


def apply_buckets(text, lang, buckets):
    def replace_app(m):
        app_id, current = m.group(1), m.group(2)
        if buckets[app_id] < parse_bucket(current):
            raise InstallsError(
                f"{app_id}: новый порог {buckets[app_id]} меньше текущего «{current}» — "
                "установки за всё время не уменьшаются, данные подозрительные"
            )
        return f"<!--installs:{app_id}-->{format_bucket(buckets[app_id], lang)}<!--/installs-->"

    text = APP_MARKER.sub(replace_app, text)
    total = format_total(buckets.values(), lang)

    def replace_total(m):
        inner, count = TOTAL_NUMBER.subn(f"badge/{total}+", m.group(2), count=1)
        if count != 1:
            raise InstallsError("внутри installs-total не найден бейдж с числом")
        return m.group(1) + inner + m.group(3)

    return TOTAL_MARKER.sub(replace_total, text)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="не записывать файлы")
    parser.add_argument("--fixtures", type=Path, help="брать страницы из DIR/<id>.html")
    args = parser.parse_args()

    texts = {name: (ROOT / name).read_text(encoding="utf-8") for name in FILES}
    app_ids = collect_app_ids(texts)

    buckets = {}
    for app_id in app_ids:
        if args.fixtures:
            html = (args.fixtures / f"{app_id}.html").read_text(encoding="utf-8")
        else:
            html = fetch_page(app_id)
        buckets[app_id] = extract_bucket(html, app_id)
        print(f"  {app_id:32} {format_bucket(buckets[app_id], 'en')}")

    updated = {name: apply_buckets(text, FILES[name], buckets) for name, text in texts.items()}
    changed = [name for name in FILES if updated[name] != texts[name]]

    print(f"Итого: {format_total(buckets.values(), 'en')}+ установок")
    if not changed:
        print("Изменений нет")
    else:
        print("Изменены: " + ", ".join(changed) + (" (dry-run, не записано)" if args.dry_run else ""))
        if not args.dry_run:
            for name in changed:
                (ROOT / name).write_text(updated[name], encoding="utf-8")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("| Приложение | Установок |\n|---|---|\n")
            f.writelines(f"| `{a}` | {format_bucket(b, 'en')} |\n" for a, b in buckets.items())
            f.write(f"\n{'Изменены: ' + ', '.join(changed) if changed else 'Изменений нет'}\n")


if __name__ == "__main__":
    try:
        main()
    except InstallsError as e:
        print(f"ОШИБКА: {e}", file=sys.stderr)
        sys.exit(1)
