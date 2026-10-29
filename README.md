<h1 align="center">Hi 👋, I'm Laxit</h1>
<h3 align="center">Senior Software Engineer · I ship AI into production systems · Laravel, Go, Kotlin · cloud reliability</h3>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=laxit-patel&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</p>

I build production platforms end to end, from the database schema to the deploy pipeline. For most of my career that has
meant **Laravel**: storefronts, ERP and SAP integrations, warehouse and marketplace platforms, SaaS products and APIs. More
recently it means putting **AI inside those systems**: agents that answer from live data, with guardrails, evals and
observability around them.
Outside work I build tools, libraries and odd experiments in Go, Kotlin, PHP, Python and Flutter.

- 🤖 **Now:** AI agents in **Laravel** with LLM tool calling, **MCP** servers, guardrails and golden-set evals
- ☁️ **Shipping with:** Docker, Kamal, OpenTofu/Terraform, AWS (Lambda, Step Functions, Fargate, RDS), GitLab CI
- 📱 **Mobile:** Flutter and native Android (Kotlin, Compose, CameraX)
- ✍️ **Writing** on [Medium](https://laxitpatel.medium.com/) · 💼 [LinkedIn](https://in.linkedin.com/in/lankit) · 📫 **laxxitpatel@gmail.com**

## 🎯 Where I'm heading

Aiming for **Forward Deployed Engineer** or **Site Reliability Engineer** roles, with **Kotlin** and **Go** as my main languages.

- **FDE:** I already work this way: I sit with a client's real systems and data, and ship AI into them, from a storefront
  customer-service agent and a voice agent on phone lines to report pipelines over their marketplace data
- **SRE:** infrastructure as code (OpenTofu, Terraform), zero-downtime deploys with rollback, secrets and observability
  (Langfuse, CloudWatch), memory and cost work on multi-GB pipelines, and a scanner that warns before the APIs our code
  depends on are retired
- **Kotlin and Go:** a native Android camera app, a Kotlin ad-placement engine and order-management service, a Go report
  engine on AWS, a Go video-call backend with a double-entry ledger, and Go CLIs and tools

## 📜 Certifications

| Certification | Issuer | Valid | Verify |
| --- | --- | --- | --- |
| **AWS Certified Developer – Associate** | Amazon Web Services | Jun 2025 – Jun 2028 (first earned Jan 2022) | [current credential](https://cp.certmetrics.com/amazon/en/public/verify/credential/7ea5b9dca9624f87bca79dd799a6c03d) · [2022 badge](https://www.credly.com/badges/1f6e79b9-d805-42a4-8eb0-5ebb3b09eade) |
| **Building with the Claude API** | Anthropic | issued Jul 2026 | [credential](https://verify.skilljar.com/c/sttesat9m6vw) |

## 🧪 Open source

| Project | What it is |
| --- | --- |
| [**Sigil**](https://github.com/laxit-patel/sigil) | Turns any integer into one recognisable Cistercian-style glyph. One spec with cross-language golden vectors, two implementations: [PHP](https://github.com/laxit-patel/php-sigil) (Packagist `laxit/sigil`: SVG, ASCII, DXF) and [JavaScript](https://github.com/laxit-patel/js-sigil) (npm: SVG, Canvas, a `<sigil-glyph>` element, zero dependencies) |
| [**clover-to-lcov**](https://github.com/laxit-patel/clover-to-lcov) | Converts PHPUnit's Clover XML coverage into the universal LCOV format |
| [**keychan**](https://github.com/laxit-patel/keychan) | Descriptive, human-readable tag and id generator for PHP |
| [**queryclash**](https://github.com/laxit-patel/queryclash) | A friendly SQL performance duel: who writes the faster query? |
| [**zsh**](https://github.com/laxit-patel/zsh) | My terminal setup: zsh, Oh My Zsh, Powerlevel10k, Catppuccin and modern CLI tools |

## 🛠️ Things I've built

The full list, with the stack of each project, is in [inventory.json](inventory.json); [EXPOSURE.md](EXPOSURE.md) sums it up by
technology: how many projects used it, how many reached production and when I last used it.

**Side projects**

- **Promptest** — "Pest for prompts": tests, gates and refines Laravel system prompts with PHP attributes, an LLM judge (G-Eval),
  embedding scorers, judge-versus-human calibration, a prompt linter and CI gates
- **Sightline** — a headless out-of-home advertising engine: an ad brief in, ranked and explainable billboard picks under a budget out.
  Contract-first (OpenAPI spec, byte-identical golden vectors, property tests), Kotlin, about 1.3 ms p50
- **Tradebot** — research on Indian index options (NIFTY, SENSEX): pricing, Greeks, an end-of-day data loader and walk-forward
  LightGBM models with leakage-safe folds. Paper trading only, and honest about finding no edge
- **Phuse** — a Go CLI and terminal UI (Cobra, Bubble Tea) that captures a project's PHP runtime as TOML and rebuilds it, isolated, anywhere
- **TigerBeetle for PHP** — a Laravel client for the TigerBeetle ledger: exact 128-byte wire structs, two-phase stock reservations
  and linked wallet transfers
- **Protomorph** — a prompt becomes a structured project vision, rendered as Excalidraw diagrams and pitch decks by a Laravel AI agent
- **Datingwala** — a woman-safe dating app MVP: Kotlin backend, native Android and Expo clients
- **Mythos** — an esoteric programming language where programs are written as sagas, with its own compiler and VM
- **Voxel sandbox** — chunks, hoppers and item flow, first in Go and then ported to Odin with raylib

**Professional work** (client names left out)

- An **AI customer-service agent** for an e-commerce storefront, built as a sidecar service: typed tools over the warehouse
  database, a classifier guardrail, the same tools exposed over **MCP**, Langfuse tracing and a golden-question eval set as the
  release gate
- An **AI voice agent** that phones online-store customers about failed deliveries, in Hindi and Hinglish: LiveKit agents,
  Temporal workflows, calling-hours and do-not-disturb compliance, and a Shopify admin app
- A **marketplace report ingestion engine** in Go: Lambda stages under Step Functions, report types defined as YAML mappings,
  a fake vendor API for tests, one Terraform apply per client
- A **scanner that finds code calling vendor APIs before they are retired**, down to file and line with a sourced date. It is
  deterministic and needs no LLM, keeps AI-found leads in a separate validated tier, and runs on a schedule across a 50+ repo fleet
- **Report pipelines handling multi-GB files:** cut memory about 20× before loading into DuckDB, streamed JSON into partitioned
  Parquet for Athena, and handed oversized jobs from Lambda to Fargate
- A **paid 1:1 video-call platform**: Go backend with a TigerBeetle double-entry ledger, per-minute prepaid metering and payouts,
  plus a Kotlin/Compose Android client on LiveKit
- A **GPS map camera** on Google Play, taken over as an inherited Flutter app, re-architected to MVVM and then rebuilt natively
  in Kotlin, Compose and CameraX. What you see in the preview is what gets saved, and capture survives the app being killed
- **AI email parsing:** Gmail messages and attachments turned into rows in Google Sheets by custom rules and an LLM
- **Legacy modernisation:** moved a serverless PHP marketplace platform's plan onto ECS Fargate, swept 961 files for PHP 8.3, and
  found and fixed a cross-tenant data-access hole in an MCP server

## ✍️ Latest posts
<!-- BLOG-POST-LIST:START -->
- [Supercharge your Role And Permission management with Custom Laravel Helper Commands &amp; Spatie](https://laxitpatel.medium.com/supercharge-your-role-permission-management-with-custom-laravel-helper-commands-spatie-ef9d2bf357ce?source=rss-a3bc257a964e------2)
<!-- BLOG-POST-LIST:END -->

## 🧰 Tools I work with

**Backend and web**<br/>
<img src="https://skillicons.dev/icons?i=php,laravel,symfony,go,kotlin,python,nodejs,js,ts,react,vue,nextjs,tailwind" alt="Backend and web" />

**Mobile**<br/>
<img src="https://skillicons.dev/icons?i=flutter,dart,kotlin,androidstudio" alt="Mobile" />

**Data and messaging**<br/>
<img src="https://skillicons.dev/icons?i=postgres,mysql,redis,mongodb,sqlite,rabbitmq,kafka,graphql" alt="Data and messaging" />

**Cloud and DevOps**<br/>
<img src="https://skillicons.dev/icons?i=docker,kubernetes,aws,terraform,nginx,linux,bash,git,gitlab,githubactions" alt="Cloud and DevOps" />

**Also explored**<br/>
<img src="https://skillicons.dev/icons?i=rust,cpp,godot,django,flask,pytorch" alt="Also explored" />

## 📈 GitHub activity

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=laxit-patel&theme=transparent" alt="GitHub streak" />
</p>
