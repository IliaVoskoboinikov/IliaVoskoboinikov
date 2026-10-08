<p align="right">
  <a href="https://github.com/IliaVoskoboinikov">🇷🇺 Русский</a> · <b>🇬🇧 English</b>
</p>

<h1 align="center">Ilia Voskoboinikov</h1>
<p align="center"><b>Android Engineer</b> · Kotlin · Jetpack Compose · Kotlin Multiplatform · 4+ years of commercial experience</p>

<p align="center">
  <a href="https://github.com/IliaVoskoboinikov/cv/blob/main/ilia_voskoboinikov_android_cv_ru.pdf"><img src="https://img.shields.io/badge/CV_PDF_(RU)-181717?style=for-the-badge&logo=github&logoColor=white" alt="CV"></a>
  <a href="https://t.me/VoskoboinikovIS"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="mailto:ilia.voskoboinikov@mail.ru"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Open_to_work-2EA44F?style=flat-square" alt="Open to work">
  <img src="https://img.shields.io/badge/5_apps-Google_Play-3DDC84?style=flat-square&logo=googleplay&logoColor=white" alt="Google Play">
  <img src="https://img.shields.io/badge/2_apps-Kotlin_Multiplatform-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin Multiplatform">
  <!--installs-total--><img src="https://img.shields.io/badge/107,000+-installs-1F6FEB?style=flat-square" alt="Installs"><!--/installs-total-->
</p>

# 👋 About me

Android developer with 4+ years of commercial experience. I've built mobile apps from scratch: from
requirements analysis and architecture design to store release and further development.
I've modernized existing codebases by introducing modern Android practices and improving engineering
quality. I've conducted technical interviews, mentored developers, spoken at conferences,
and written technical articles.

- 🧩 **Focus:** Kotlin, Jetpack Compose, Clean Architecture, multi-module projects
- 🌍 **Kotlin Multiplatform:** «Coin: Yes/No» ships to Android and iOS from a single codebase
- 💰 **Beyond code:** store releases, analytics and Crashlytics, ads and in-app purchases
- 🛠️ **Keeping projects healthy:** convention plugins, custom Lint rules, CI/CD, tests, documentation
- 📄 **CV:** [PDF (in Russian)](https://github.com/IliaVoskoboinikov/cv/blob/main/ilia_voskoboinikov_android_cv_ru.pdf) · [repository](https://github.com/IliaVoskoboinikov/cv)

# 📲 Published apps

| App | Installs | Stack |
|---|---|---|
| **[Coin: Yes/No](https://play.google.com/store/apps/details?id=v500a5v.ilua.admin.monetka&hl=en)** · [App Store](https://apps.apple.com/us/app/coin-yes-no/id6756816990)<br><sub>Coin-flip simulator for quick decisions. Android and iOS from a single codebase; the iOS version is published under a partner's account.</sub> | **<!--installs:v500a5v.ilua.admin.monetka-->100K+<!--/installs-->** | Kotlin Multiplatform · Compose Multiplatform · Koin · Firebase |
| **[Mafia: Card Game](https://play.google.com/store/apps/details?id=soft.divan.mafia&hl=en)**<br><sub>Offline host for the Mafia party game: up to 30 players, automatic role assignment.</sub> | **<!--installs:soft.divan.mafia-->5K+<!--/installs-->** | Kotlin · Compose (Material 3) · Hilt · DataStore · Play Billing · Yandex Ads |
| **[Password Generator](https://play.google.com/store/apps/details?id=soft.divan.admin.password&hl=en)**<br><sub>Strong passwords with configurable length and character sets.</sub> | **<!--installs:soft.divan.admin.password-->1K+<!--/installs-->** | Kotlin Multiplatform · Compose Multiplatform · Coroutines · Firebase |
| **[Rubik's Timer](https://play.google.com/store/apps/details?id=soft.divan.rubik_sclock&hl=en)**<br><sub>Speedcubing timer: millisecond precision, scrambles, solve statistics.</sub> | **<!--installs:soft.divan.rubik_sclock-->1K+<!--/installs-->** | Kotlin 2.3 · Compose (Material 3) · Hilt + KSP · Room · DataStore |
| **[World Words](https://play.google.com/store/apps/details?id=soft.divan.world.words&hl=en)**<br><sub>Vocabulary flashcards with categories and account sync.</sub> | **<!--installs:soft.divan.world.words-->500+<!--/installs-->** | Kotlin · XML + Navigation · Koin · Room · Paging 3 · Firebase (Auth, Firestore, App Check) |

<sub>Installs — Google Play data, updated automatically every week.</sub>

# 🏦 Finance Manager

<p>
  <a href="https://github.com/IliaVoskoboinikov/Finance-Manager/actions/workflows/ci.yml"><img src="https://github.com/IliaVoskoboinikov/Finance-Manager/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/Kotlin-2.4.0-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin 2.4">
  <img src="https://img.shields.io/badge/AGP-9.2.1-3DDC84?style=flat-square&logo=android&logoColor=white" alt="AGP 9.2">
  <img src="https://img.shields.io/badge/Compose_BOM-2026.05-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white" alt="Compose BOM">
  <img src="https://img.shields.io/badge/Navigation_3-1.1.5-4285F4?style=flat-square" alt="Navigation 3">
  <img src="https://img.shields.io/badge/modules-49-blue?style=flat-square" alt="49 modules">
  <img src="https://img.shields.io/badge/unit_tests-185-success?style=flat-square" alt="185 unit tests">
</p>

[**A personal finance tracker**](https://github.com/IliaVoskoboinikov/Finance-Manager) —
a pet project where I try out approaches that don't always fit into day-to-day work.
19 features, each split into `api` (contract) and `impl` (implementation), so features know nothing
about each other. [The graph of all 49 modules](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/graphs/modules_prodget/all_modules.png)
is generated automatically.

```mermaid
flowchart TD
    APP[":app"]
    SYNC[":sync — WorkManager"]

    subgraph FEAT["feature:* — 19 features × (api + impl)"]
        FAPI["feature:X:api<br/>contract"]
        FIMPL["feature:X:impl<br/>implementation + UI"]
    end

    subgraph CORE["core:* — shared layer"]
        CONTRACT[":core:feature-api"]
        UIKIT[":core:uikit"]
        DOMAIN[":core:domain"]
        DATA[":core:data"]
    end

    subgraph INFRA["infrastructure"]
        DB[":core:database<br/>Room"]
        NET[":core:network<br/>Retrofit"]
        COMMON[":core:common"]
        LOG[":core:logging-error"]
    end

    APP --> FIMPL
    APP --> SYNC
    FIMPL --> FAPI
    FAPI --> CONTRACT
    FIMPL --> UIKIT
    FIMPL --> DOMAIN
    FIMPL --> DATA
    SYNC --> DATA
    DATA --> DB
    DATA --> NET
    DATA --> COMMON
    DATA --> LOG
```

| | |
|---|---|
| **Build** | 49 Gradle modules, version catalog, **convention plugins** in `build-logic` — with functional tests for the plugins themselves |
| **Quality** | Detekt + Compose rules, ktlint, a `:lint` module with **custom Lint checks**, Kover for coverage, Spotify Ruler for APK size control |
| **Tests** | **185 unit tests**: JUnit, MockK, Robolectric, AssertJ, coroutines-test, work-testing |
| **UI** | Compose + Material 3, **Navigation 3**, Lottie animations, YCharts for charts, theme and color scheme picker |
| **Data** | Room + DataStore, Retrofit with custom interceptors (Auth, Retry, NetworkConnection, Logging), kotlinx.serialization |
| **Security** | PIN and biometrics (`androidx.biometric`), `security-crypto`, OAuth via Yandex Auth SDK, JWT |
| **Background** | Sync via WorkManager (`:sync`), push notifications via FCM, Crashlytics |
| **CI/CD** | 4 workflows: build and tests on PRs, release pipeline, automatic navigation graph generation |

<p align="center">
  <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/master/docs/screens/expenses.jpeg" width="17%" alt="Expenses">
  <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/master/docs/screens/accounts.jpeg" width="17%" alt="Accounts">
  <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/master/docs/screens/analytics.jpeg" width="17%" alt="Analytics">
  <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/master/docs/screens/category.jpeg" width="17%" alt="Categories">
  <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/Finance-Manager/master/docs/screens/settings.jpeg" width="17%" alt="Settings">
</p>

**Documentation** (in Russian): each of the 49 modules has its own `README.md`, plus 12 cross-cutting docs —
[architecture](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/architecture.md) ·
[modularization](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/modularization.md) ·
[Navigation 3](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/navigation3.md) ·
[testing](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/testing.md) ·
[CI/CD](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/ci-cd.md) ·
[synchronization](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/synchronization.md) ·
[notifications](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/notifications.md) ·
[database](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/bd.md) ·
[authorization](https://github.com/IliaVoskoboinikov/Finance-Manager/blob/master/docs/auth.md)

Also: **[design-patterns](https://github.com/IliaVoskoboinikov/design-patterns)** —
design patterns in Kotlin with examples of their use in Android.

# 🛠 Tech stack

<p>
  <img src="https://skillicons.dev/icons?i=kotlin,java,androidstudio,gradle,firebase,git,github,figma&theme=dark" alt="Tech stack">
</p>

|  |  |
|---|---|
| **Languages & platforms** | Kotlin, Java, Android, Kotlin Multiplatform (Android + iOS) |
| **UI** | Jetpack Compose, Compose Multiplatform, Material 3, Navigation 3, XML, Custom Views, Lottie, YCharts, Glide |
| **Architecture** | Clean Architecture, MVVM, SOLID, multi-module with `api` / `impl` split |
| **DI** | Hilt, Dagger 2, Koin |
| **Async & background** | Coroutines, Flow, WorkManager, FCM |
| **Data** | Room, SQLite, DataStore, Paging 3, kotlinx.serialization, multiplatform-settings |
| **Networking & backend** | Retrofit, OkHttp, Ktor, WebSockets, Firebase (Auth, Firestore, Storage, App Check) |
| **Security** | Biometric, security-crypto, OAuth (Yandex Auth SDK), JWT |
| **Testing** | JUnit, MockK, Mockito, Robolectric, AssertJ, Espresso, Kover |
| **Code quality** | Detekt (+ Compose rules), ktlint, Android Lint with custom checks, Spotify Ruler |
| **Build & CI/CD** | Gradle KTS, version catalog, convention plugins, KSP, GitHub Actions |
| **Product** | Google Play Billing, Play In-App Review, Yandex MobileAds, Crashlytics, Analytics |

# 📊 GitHub

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github_dark/0-profile-details.svg">
    <img width="99%" src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github/0-profile-details.svg" alt="Profile details">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github_dark/3-stats.svg">
    <img width="49%" src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github/3-stats.svg" alt="Stats">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github_dark/2-most-commit-language.svg">
    <img width="49%" src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github/2-most-commit-language.svg" alt="Top languages by commits">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github_dark/4-productive-time.svg">
    <img width="49%" src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/main/profile-summary-card-output/github/4-productive-time.svg" alt="Productive time">
  </picture>
</p>

<sub>Cards are regenerated daily by GitHub Actions and stored in this repository — no third-party services.</sub>

# 📫 Contacts

- 📧 **Email:** [ilia.voskoboinikov@mail.ru](mailto:ilia.voskoboinikov@mail.ru)
- 📱 **Telegram:** [@VoskoboinikovIS](https://t.me/VoskoboinikovIS)
- 📄 **CV:** [PDF (in Russian)](https://github.com/IliaVoskoboinikov/cv/blob/main/ilia_voskoboinikov_android_cv_ru.pdf)

---

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/output/github-snake-dark.svg">
    <img src="https://raw.githubusercontent.com/IliaVoskoboinikov/IliaVoskoboinikov/output/github-snake.svg" alt="Snake eating contributions">
  </picture>
</p>
