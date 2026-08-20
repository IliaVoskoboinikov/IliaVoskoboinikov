<h1 align="center">Илья Воскобойников</h1>
<p align="center"><b>Android Engineer</b> · Kotlin · Jetpack Compose · Kotlin Multiplatform · 4+ года коммерческого опыта</p>

<p align="center">
  <a href="https://github.com/IliaVoskoboinikov/cv/blob/main/ilia_voskoboinikov_android_cv_ru.pdf"><img src="https://img.shields.io/badge/Резюме_PDF-181717?style=for-the-badge&logo=github&logoColor=white" alt="CV"></a>
  <a href="https://t.me/VoskoboinikovIS"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="mailto:ilia.voskoboinikov@mail.ru"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Открыт_к_предложениям-2EA44F?style=flat-square" alt="Открыт к предложениям">
  <img src="https://img.shields.io/badge/5_приложений-Google_Play-3DDC84?style=flat-square&logo=googleplay&logoColor=white" alt="Google Play">
  <img src="https://img.shields.io/badge/2_приложения-Kotlin_Multiplatform-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin Multiplatform">
  <img src="https://img.shields.io/badge/107_000+-установок-blue?style=flat-square" alt="Установки">
</p>

---

## 👋 Обо мне

Android-разработчик с 4+ годами коммерческого опыта. Делал мобильные приложения с нуля: от анализа
требований и проектирования архитектуры до публикации в сторах и дальнейшего развития.
Модернизировал существующие решения — внедрение современных Android-подходов и повышение качества
разработки. Проводил технические собеседования, менторил разработчиков, выступал на конференциях
и писал технические статьи.

- 🧩 Специализация: Kotlin, Jetpack Compose, Clean Architecture, многомодульные проекты
- 🌍 Kotlin Multiplatform — «Монетка» и «Генератор паролей»; «Монетка» собрана под Android и iOS из одной кодовой базы
- 💰 Полный цикл продукта: релизы в сторах, аналитика и Crashlytics, монетизация через рекламу и in-app покупки
- 🛠️ Люблю то, что ускоряет команду: convention plugins, кастомные Lint-правила, CI/CD
- 📄 Резюме: **[PDF](https://github.com/IliaVoskoboinikov/cv/blob/main/ilia_voskoboinikov_android_cv_ru.pdf)** · [репозиторий](https://github.com/IliaVoskoboinikov/cv)

---

## 📲 Мои приложения в сторах

| Приложение | Установок | Стек |
|---|---|---|
| **[Монетка: ДА/НЕТ](https://play.google.com/store/apps/details?id=v500a5v.ilua.admin.monetka)** · [App Store](https://apps.apple.com/ru/app/coin-yes-no/id6756816990)<br><sub>Симулятор подбрасывания монетки для быстрых решений. Android и iOS из одной кодовой базы; iOS-версия издана на аккаунте партнёра.</sub> | **100 тыс.+** | Kotlin Multiplatform · Compose Multiplatform · Koin · multiplatform-settings · Firebase Analytics/Crashlytics |
| **[Мафия: карточки](https://play.google.com/store/apps/details?id=soft.divan.mafia)**<br><sub>Оффлайн-ведущий для настольной «Мафии»: до 30 игроков, раздача ролей, настройка набора.</sub> | **5 тыс.+** | Kotlin · Compose (Material 3) · Hilt · Navigation Compose · DataStore · Play Billing · Yandex Ads |
| **[Генератор паролей](https://play.google.com/store/apps/details?id=soft.divan.admin.password)**<br><sub>Генерация надёжных паролей с настраиваемой длиной и набором символов.</sub> | **1 тыс.+** | Kotlin Multiplatform · Compose Multiplatform · Coroutines · Firebase Analytics/Crashlytics |
| **[Rubik's Timer](https://play.google.com/store/apps/details?id=soft.divan.rubik_sclock)**<br><sub>Таймер для спидкубинга: миллисекундная точность, скрамблы, история и статистика сборок.</sub> | **1 тыс.+** | Kotlin 2.3 · Compose (Material 3) · Hilt + KSP · Room · DataStore · Navigation Compose |
| **[World Words](https://play.google.com/store/apps/details?id=soft.divan.world.words)**<br><sub>Карточки для изучения иностранных слов: категории, примеры, синхронизация аккаунта.</sub> | **500+** | Kotlin · XML + Navigation (SafeArgs) · Koin · Room · Paging 3 · Firebase (Auth, Firestore, Storage, App Check) · Glide |

<sub>Установки — по данным Google Play, август 2026.</sub>

**Что за этим стоит:** Firebase Auth + Firestore + Storage с App Check (Play Integrity) в World Words,
Google Play Billing в «Мафии», Yandex MobileAds и Play In-App Review в четырёх приложениях,
Crashlytics и аналитика во всех. Актуальные версии инструментов — вплоть до AGP 9 / Kotlin 2.3 / compileSdk 36.

---

## 🚀 Проекты

### [Finance Manager](https://github.com/IliaVoskoboinikov/Finance-Manager) — учёт личных финансов

Pet-проект, в котором важна не «ещё одна CRUD-ка на Compose», а инженерная часть: многомодульность,
свои инструменты качества кода и рабочий CI/CD.

<p>
  <a href="https://github.com/IliaVoskoboinikov/Finance-Manager/actions/workflows/ci.yml"><img src="https://github.com/IliaVoskoboinikov/Finance-Manager/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?logo=kotlin&logoColor=white" alt="Kotlin">
  <img src="https://img.shields.io/badge/Compose-Material_3-4285F4?logo=jetpackcompose&logoColor=white" alt="Compose">
</p>

- **Архитектура:** Clean Architecture + MVVM, модули `core:*` / `feature:*`, version catalog и **convention plugins** в `build-logic`
- **Качество кода:** Detekt со своими правилами, ktlint, модуль `:lint` с **кастомными Lint-чекерами**
- **Данные:** Room + DataStore, Retrofit/OkHttp со своими интерсепторами (Auth, Retry, NetworkConnection, Logging)
- **Фон и безопасность:** синхронизация через WorkManager (`:sync`), PIN и биометрия (`feature:security`), JWT
- **CI/CD:** сборка и тесты на PR, релизный пайплайн, генерация графа навигации

| Расходы | Счета | Аналитика | Категории | Настройки |
|---|---|---|---|---|
| <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/main/docs/screens/expenses.jpeg" width="150"> | <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/main/docs/screens/accounts.jpeg" width="150"> | <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/main/docs/screens/analytics.jpeg" width="150"> | <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/main/docs/screens/category.jpeg" width="150"> | <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/main/docs/screens/settings.jpeg" width="150"> |

### [Design Patterns](https://github.com/IliaVoskoboinikov/design-patterns)
Реализации паттернов проектирования на Kotlin с примерами применения в Android.

---

## 🛠 Стек

<p>
  <img src="https://skillicons.dev/icons?i=kotlin,java,androidstudio,gradle,firebase,git,github,figma&theme=dark" alt="Стек">
</p>

|  |  |
|---|---|
| **Языки** | Kotlin, Java |
| **Платформы** | Android, Kotlin Multiplatform (Android + iOS) |
| **UI** | Jetpack Compose, Compose Multiplatform, Material 3, XML, Custom Views, анимации |
| **Архитектура** | Clean Architecture, MVVM, SOLID, многомодульность |
| **DI** | Dagger 2, Hilt, Koin |
| **Асинхронность** | Coroutines, Flow |
| **Данные** | Room, SQLite, Realm, DataStore, Paging 3, multiplatform-settings |
| **Сеть и backend** | Retrofit, OkHttp, Ktor, WebSockets, Firebase (Auth, Firestore, Storage, App Check) |
| **Продукт** | Google Play Billing, Yandex MobileAds, Play In-App Review, Analytics, Crashlytics |
| **Качество** | JUnit, Mockito, Espresso, Detekt, ktlint, Android Lint (кастомные правила) |
| **Инфраструктура** | Gradle (KTS, version catalog, convention plugins), KSP, GitHub Actions |

---

## 📊 GitHub

<p>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=IliaVoskoboinikov&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&locale=ru&theme=github_dark">
    <img height="165" src="https://github-readme-stats.vercel.app/api?username=IliaVoskoboinikov&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&locale=ru" alt="GitHub статистика">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=IliaVoskoboinikov&layout=compact&hide_border=true&langs_count=8&locale=ru&theme=github_dark">
    <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=IliaVoskoboinikov&layout=compact&hide_border=true&langs_count=8&locale=ru" alt="Языки">
  </picture>
</p>

<p>
  <img width="49%" src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github_dark/3-stats.svg" alt="Статистика">
  <img width="49%" src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github_dark/4-productive-time.svg" alt="Продуктивное время">
</p>

---

## 📫 Контакты

- 📧 **Email:** [ilia.voskoboinikov@mail.ru](mailto:ilia.voskoboinikov@mail.ru)
- 📱 **Telegram:** [@VoskoboinikovIS](https://t.me/VoskoboinikovIS)
- 📄 **Резюме:** [PDF](https://github.com/IliaVoskoboinikov/cv/blob/main/ilia_voskoboinikov_android_cv_ru.pdf)
