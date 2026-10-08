import unittest

from update_installs import (
    InstallsError,
    apply_buckets,
    collect_app_ids,
    extract_bucket,
    format_bucket,
    format_total,
    parse_bucket,
)

RU = (
    '<!--installs-total--><img src="https://img.shields.io/badge/6_000+-установок-1F6FEB"><!--/installs-total-->\n'
    "| **[Мафия](...)** | **<!--installs:soft.divan.mafia-->5 тыс.+<!--/installs-->** |\n"
    "| **[Таймер](...)** | **<!--installs:soft.divan.rubik_sclock-->1 тыс.+<!--/installs-->** |\n"
)
EN = (
    '<!--installs-total--><img src="https://img.shields.io/badge/6,000+-installs-1F6FEB"><!--/installs-total-->\n'
    "| **[Mafia](...)** | **<!--installs:soft.divan.mafia-->5K+<!--/installs-->** |\n"
    "| **[Timer](...)** | **<!--installs:soft.divan.rubik_sclock-->1K+<!--/installs-->** |\n"
)


class FormatTest(unittest.TestCase):
    def test_format_bucket(self):
        cases = [(500, "500+", "500+"), (1_000, "1 тыс.+", "1K+"), (100_000, "100 тыс.+", "100K+"),
                 (5_000_000, "5 млн+", "5M+")]
        for n, ru, en in cases:
            self.assertEqual(format_bucket(n, "ru"), ru)
            self.assertEqual(format_bucket(n, "en"), en)

    def test_parse_is_inverse_of_format(self):
        for n in (100, 500, 1_000, 50_000, 500_000, 1_000_000):
            for lang in ("ru", "en"):
                self.assertEqual(parse_bucket(format_bucket(n, lang)), n)

    def test_format_total_floors_to_thousands(self):
        self.assertEqual(format_total([100_000, 5_000, 1_000, 1_000, 500], "ru"), "107_000")
        self.assertEqual(format_total([100_000, 5_000, 1_000, 1_000, 500], "en"), "107,000")
        self.assertEqual(format_total([500], "en"), "500")


class ExtractTest(unittest.TestCase):
    def test_english_page(self):
        self.assertEqual(extract_bucket('x["5,000+",5000,7899,"5K+"]y', "app"), 5000)

    def test_russian_page_with_nbsp(self):
        self.assertEqual(extract_bucket('x["5 000+",5000,7899,"5 тыс.+"]y', "app"), 5000)

    def test_missing_block(self):
        with self.assertRaises(InstallsError):
            extract_bucket("<html>consent page</html>", "app")

    def test_value_outside_ladder(self):
        with self.assertRaises(InstallsError):
            extract_bucket('["3,000+",3000,3500,"3K+"]', "app")

    def test_exact_less_than_bucket(self):
        with self.assertRaises(InstallsError):
            extract_bucket('["5,000+",5000,4000,"5K+"]', "app")

    def test_shown_text_disagrees_with_number(self):
        with self.assertRaises(InstallsError):
            extract_bucket('["1,000+",5000,7899,"5K+"]', "app")


class ApplyTest(unittest.TestCase):
    def test_unchanged_values_keep_text_identical(self):
        buckets = {"soft.divan.mafia": 5_000, "soft.divan.rubik_sclock": 1_000}
        self.assertEqual(apply_buckets(RU, "ru", buckets), RU)
        self.assertEqual(apply_buckets(EN, "en", buckets), EN)

    def test_growth_updates_cells_and_total(self):
        buckets = {"soft.divan.mafia": 10_000, "soft.divan.rubik_sclock": 5_000}
        ru = apply_buckets(RU, "ru", buckets)
        en = apply_buckets(EN, "en", buckets)
        self.assertIn("<!--installs:soft.divan.mafia-->10 тыс.+<!--/installs-->", ru)
        self.assertIn("<!--installs:soft.divan.rubik_sclock-->5 тыс.+<!--/installs-->", ru)
        self.assertIn("badge/15_000+-установок", ru)
        self.assertIn("<!--installs:soft.divan.mafia-->10K+<!--/installs-->", en)
        self.assertIn("badge/15,000+-installs", en)

    def test_decrease_is_rejected(self):
        with self.assertRaises(InstallsError):
            apply_buckets(RU, "ru", {"soft.divan.mafia": 1_000, "soft.divan.rubik_sclock": 1_000})


class CollectTest(unittest.TestCase):
    def test_ids_from_markers(self):
        ids = collect_app_ids({"README.md": RU, "README.en.md": EN})
        self.assertEqual(ids, ["soft.divan.mafia", "soft.divan.rubik_sclock"])

    def test_files_must_list_same_apps(self):
        en_without_timer = EN.split("| **[Timer]")[0]
        with self.assertRaises(InstallsError):
            collect_app_ids({"README.md": RU, "README.en.md": en_without_timer})

    def test_total_marker_required(self):
        ru_without_total = RU.split("\n", 1)[1]
        with self.assertRaises(InstallsError):
            collect_app_ids({"README.md": ru_without_total, "README.en.md": EN})


if __name__ == "__main__":
    unittest.main()
