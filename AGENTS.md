# Repository Guidelines

## Project Structure & Module Organization
- `core/`: Django project config (`settings.py`, `urls.py`, `wsgi.py`).
- `django_htmx_infinite_scroll/`: App code — models, views, management commands, and templates under `templates/`.
- `tests/`: Unit tests (`test_models.py`, `test_views.py`, `test_management_commands.py`).
- `Makefile`: Common dev/test/CI commands. `manage.py` runs Django tasks. Scripts in `scripts/`.
- Local DB is `db.sqlite3` (dev only). Requirements in `requirements*.txt`.

## Build, Test, and Development Commands
- `make run`: Start the dev server at `http://localhost:8000`.
- `make init-db`: Migrate and seed sample pages.
- `make migrate` / `make shell`: Migrations and Django shell.
- `make test`, `make test-verbose`: Run tests; add `-k <expr>` to filter.
- `make test-coverage`: Coverage report + XML; sources limited to the app.
- `make check`, `make check-migrations`: Django checks and migration drift.
- `make lint`: Run pre-commit (ruff, mypy, formatting). `make ci`: Local CI bundle.

## Coding Style & Naming Conventions
- Indentation: 4 spaces; prefer type hints (mypy configured).
- Line length: 100 for app code, 99 in `tests/` (auto-enforced by pre-commit).
- Imports: ordered and grouped by ruff; avoid unused symbols.
- Naming: modules and functions `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE_CASE`.
- Tools: ruff (lint/format), mypy (types), flake8/pylint minimal configs present.

## Testing Guidelines
- Framework: Django’s test runner (unittest style). Place tests in `tests/` and name files `test_*.py`.
- Focus on view behavior, pagination/HTMX responses, and management commands.
- Run selective suites: `make test-views`, `make test-models`, `make test-commands`.
- Aim for meaningful coverage; use `make test-coverage` before opening a PR.

## Commit & Pull Request Guidelines
- Commits: short, imperative, present tense (e.g., "ruff linter", "fix template syntax"). Scope optional; keep under ~72 chars.
- PRs: include a clear description, linked issues, screenshots of UI changes, and reproduction steps.
- Require green local checks: `make ci` must pass; include migration files when models change.

## Security & Configuration Tips
- Do not reuse the included `SECRET_KEY` in production; configure via env vars and set `DEBUG=False`.
- Never commit secrets or `.env` files. Use SQLite only for development.
