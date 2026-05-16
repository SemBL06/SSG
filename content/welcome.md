---
title: "Welcome"
sitemap:
  lastmod: "2026-05-15"
  changefreq: "monthly"
  priority: "0.5"
---

# Puddinator / Flan OS Docs

Welcome! This repo contains a tiny FlanLang runtime (the “OS”) plus a growing set of built-in modules, drivers, and installable extensions. The goal is simple: **write friendly scripts**, run them on small hardware, and keep the script APIs stable while the hardware layer evolves.

## Where to start

- New here? Start with:
  - [Overview](http://127.0.0.1:3000/public/getting-started/overview.html)
  - `language/quickstart.md`
- Looking for a specific command? Jump to `modules/`.
- Hacking on the runtime itself? See `internals/architecture.md`.
- Adding hardware or features? See `extensions/`.

## Docs map

### Getting started

- `getting-started/overview.md`
- `getting-started/project-layout.md`

### FlanLang (the DSL)

- `language/quickstart.md`
- `language/syntax.md`

### Built-in modules (script API)

- `modules/display.md`
- `modules/log.md`
- `modules/system.md`
- `modules/ui.md`
- `modules/controls.md`
- `modules/button.md`
- `modules/data.md`
- `modules/config.md` (compat wrapper around `data file="main"`)
- `modules/csv.md`
- `modules/comm.md`
- `modules/input.md`
- `modules/output.md`
- `modules/list.md`
- `modules/math.md`
- `modules/string.md`
- `modules/options.md` (legacy-compatible wrapper)
- `modules/description.md` (legacy-compatible wrapper)

### Runtime internals

- `internals/architecture.md`

### Extensions (drivers & custom modules)

- `extensions/drivers.md`
- `extensions/custom-modules.md`
