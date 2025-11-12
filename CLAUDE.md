# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Start

```bash
# Activate virtual environment and install dependencies
source ./activate.sh

# Initialize database and add sample data
source ./activate.sh && make init-db

# Run development server
source ./activate.sh && make run
```

**IMPORTANT**: Always activate the virtual environment before running any commands. Use `source ./activate.sh` before each command.

Visit http://localhost:8000 to view the application.

## Development Commands

Use the Makefile for common development tasks:

- `source ./activate.sh && make run` - Start Django development server
- `source ./activate.sh && make shell` - Open Django shell
- `source ./activate.sh && make migrate` - Run database migrations (makemigrations + migrate)
- `source ./activate.sh && make add-pages` - Add 100 sample book pages to database
- `source ./activate.sh && make init-db` - Initialize database with migrations and sample data
- `source ./activate.sh && make reqs` - Update requirements and pre-commit hooks
- `source ./activate.sh && make help` - Show all available commands

## Environment Setup

This project uses Astral's UV for package management and virtual environments. The `activate.sh` script:
- Creates a Python 3.12 virtual environment in `.venv/` if it doesn't exist
- Installs development dependencies from `requirements.dev.txt`
- Must be sourced with `. ./activate.sh`

## Architecture

This is a Django demo project showcasing infinite scroll with HTMX. Key components:

### Core Structure
- **core/**: Django project configuration
  - `settings.py`: Main Django settings (SQLite database, basic configuration)
  - `urls.py`: Root URL configuration
- **django_htmx_infinite_scroll/**: Main Django app
  - `models.py`: BookPage model with number and content fields
  - `views.py`: Two views - `book()` for full page, `book_page()` for HTMX partial responses
  - `templates/`: HTML templates using Bootstrap 5 and HTMX
  - `management/commands/add-pages.py`: Custom command to generate sample data using Faker

### Key Features
- **Infinite Scroll**: Uses HTMX to load book pages dynamically without JavaScript
- **BookPage Model**: Simple model with page number and content (ordered by number)
- **HTMX Integration**: Base template includes HTMX 1.9.6 via CDN
- **Bootstrap Styling**: Uses Bootstrap 5 for UI components

## Code Quality Tools

The project uses comprehensive linting and type checking:

### Pre-commit Hooks
- **Ruff**: Python linter with extensive rule set (line length 100)
  - Includes Pylint, security, complexity, and style checks
  - Different configuration for tests (line length 99)
- **MyPy**: Type checking with Django stubs
- **Standard hooks**: YAML validation, whitespace fixes

### Manual Commands
- `source ./activate.sh && pre-commit run --all-files` - Run all pre-commit hooks
- `source ./activate.sh && python manage.py check` - Run Django system checks
- `source ./activate.sh && python manage.py makemigrations --check --dry-run` - Check for missing migrations

**IMPORTANT**: Always use `pre-commit run --all-files` for code quality checks. Never run ruff or mypy directly.

### Makefile Quality Commands
- `source ./activate.sh && make lint` - Run all pre-commit hooks (linting, formatting, type checking)
- `source ./activate.sh && make check` - Run Django system checks
- `source ./activate.sh && make check-migrations` - Check for missing migrations

## Testing

Tests are organized in the `tests/` directory at project root with comprehensive coverage:

### Test Structure
- `tests/test_models.py` - BookPage model tests
- `tests/test_views.py` - View tests for book and book_page endpoints
- `tests/test_management_commands.py` - Management command tests

### Running Tests
- `source ./activate.sh && python manage.py test tests` - Run all tests
- `source ./activate.sh && python manage.py test tests --verbosity=2` - Run tests with verbose output
- `source ./activate.sh && python manage.py test tests.test_models` - Run model tests only
- `source ./activate.sh && python manage.py test tests.test_views` - Run view tests only
- `source ./activate.sh && python manage.py test tests.test_management_commands` - Run management command tests only
- `source ./activate.sh && coverage run --source='django_htmx_infinite_scroll' manage.py test tests` - Run with coverage
- `source ./activate.sh && coverage report --show-missing` - Show coverage report

### Makefile Commands
All test commands are also available via Make:
- `source ./activate.sh && make test` - Run all tests
- `source ./activate.sh && make test-verbose` - Run tests with verbose output
- `source ./activate.sh && make test-coverage` - Run tests with coverage report
- `source ./activate.sh && make test-models` - Run model tests only
- `source ./activate.sh && make test-views` - Run view tests only
- `source ./activate.sh && make test-commands` - Run management command tests only
- `source ./activate.sh && make ci` - Run full CI pipeline locally (checks + linting + coverage)

### CI/CD
GitHub workflows automatically run on push/PR:
- `.github/workflows/static.yml` - Static code analysis with pre-commit hooks
- `.github/workflows/ci.yml` - Comprehensive test matrix with quality checks and coverage

**Test Matrix:**
- Python versions: 3.11, 3.12, 3.13
- Operating systems: Ubuntu, Windows, macOS
- Total test combinations: 9 (3 Python × 3 OS)

All workflows use UV for fast dependency management and maintain 100% test coverage with 80% minimum requirement.

## Database

Uses SQLite for development (db.sqlite3). The BookPage model is designed for demonstration purposes with simple pagination through page numbers.

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
