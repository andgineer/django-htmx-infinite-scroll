# Django + HTMX Infinite Scroll

Implement infinite scrolling without JavaScript using Django and HTMX.

### Quick Start

```bash
. ./activate.sh  # note the leading dot and space
make init-db
make run
```

Visit http://localhost:8000

### Available Commands

Use `make help` to see all available commands, or use any of these:

**Development:**
- `make run` - Run local development server
- `make shell` - Open Django shell
- `make migrate` - Run database migrations
- `make init-db` - Initialize database with sample data

**Testing:**
- `make test` - Run all tests with coverage
- `make test tests.test_models` - Run model tests only
- `make test tests.test_models.TestBookPage` - Run specific test class

**Quality Checks:**
- `make check` - Run Django system checks
- `make check-migrations` - Check for missing migrations
- `make lint` - Run linting, formatting, and type checking
- `make ci` - Run full CI pipeline locally

**Maintenance:**
- `make add-pages` - Add sample pages to database
- `make reqs` - Update requirements and pre-commit hooks

### Learn More

For a detailed explanation of how this works, check out the full article:
[Django HTMX Infinite Scroll Tutorial](https://sorokin.engineer/posts/en/django_htmx_infinite_scroll.html)
