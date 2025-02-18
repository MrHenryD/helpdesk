PYTHON_VERSION=3.11.9
PYTHONPATH=src
POETRY=src

fmt_dir := src

activate:
	pyenv local $(PYTHON_VERSION)

add-base-dep:
	poetry add $(PACKAGE)

add-dev-dep:
	poetry add $(PACKAGE) --dev

style: activate
	poetry -C $(POETRY) run ruff check --select I --fix .
	poetry -C $(POETRY) run ruff format .

lint: activate
	poetry -C $(POETRY) run ruff check .

test:
	poetry -C $(POETRY) run pytest

migration:
	poetry -C $(POETRY) run alembic init migrations

run-local: cleanup
	docker-compose up --build

cleanup:
	docker-compose down