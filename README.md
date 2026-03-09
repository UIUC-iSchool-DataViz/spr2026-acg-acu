# Course Website Template

This is a template repository for creating course websites using Jekyll. It is designed to be modular and easy to maintain.

## Structure

- `_modules/`: Contains reusable course content (lessons, labs, readings).
- `_weeks/`: Defines the weekly schedule, referencing modules.
- `_data/`: Configuration for class info, menu items, and topics.
- `_layouts/`: Jekyll layouts for weeks, modules, lectures (Reveal.js), and more.
- `scripts/`: Scaffolding tools for adding new content.

## Getting Started

1.  **Configure**: Update `_config.yml` and `_data/class.yml` with your course details.
2.  **Scaffold**: Use the provided `Makefile` or Python script to add content.
    - `make module NAME=my_module`
    - `make week NUM=1`
3.  **Serve**: Run `make serve` to preview the site locally.

## Modular Content

Each week in `_weeks/` can include one or more modules from `_modules/` by referencing their slug in the `modules` front-matter list.

```yaml
---
layout: week
title: Introduction
modules:
  - course_intro
  - basic_setup
---
```

## Scaffolding Tool

The `scripts/scaffold.py` script helps you quickly create new modules and weeks.

```bash
python3 scripts/scaffold.py module introduction
python3 scripts/scaffold.py week 1
```

## Requirements

- Ruby and Jekyll
- Python 3 (for scaffolding)
