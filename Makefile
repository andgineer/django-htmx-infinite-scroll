.HELP: shell  ## Django shell
shell:
	python manage.py shell

.HELP: migrate  ## Migrate DB to current models
migrate:
	python manage.py makemigrations
	python manage.py migrate

.HELP: add-pages  ## Add pages to DB
add-pages:
	python manage.py add-pages

.HELP: init-db  ## Create tables and add pages to DB
init-db: migrate add-pages

.HELP: run  ## Run local server
run:
	python manage.py runserver

.HELP: test  ## Run tests with coverage (usage: make test or make test tests.test_models)
test:
	coverage run --source='django_htmx_infinite_scroll' manage.py test $(or $(ARGS),$(filter-out $@,$(MAKECMDGOALS)),tests)
	coverage report --show-missing
	coverage xml

# Catch-all target to allow passing arguments after test target
%:
	@:

.HELP: check  ## Run Django system checks
check:
	python manage.py check

.HELP: check-migrations  ## Check for missing migrations
check-migrations:
	python manage.py makemigrations --check --dry-run

.HELP: lint  ## Run pre-commit hooks (linting, formatting, type checking)
lint:
	pre-commit run --all-files

.HELP: ci  ## Run full CI pipeline locally
ci: check check-migrations lint test

.HELP: reqs  ## Upgrade requirements including pre-commit
reqs:
	pre-commit autoupdate
	bash ./scripts/compile_requirements.sh
	pip install -r requirements.dev.txt
	pip install -r requirements.txt

.HELP: help  ## Display this message
help:
	@grep -E \
		'^.HELP: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".HELP: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'
