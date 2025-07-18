PYTHON_VERSION=3.11.9
PYTHON_PATH=app
POETRY_DIR=src

fmt_dir := src

PHONY: all

activate:
	pyenv local $(PYTHON_VERSION)

add-base-dep:
	poetry add $(PACKAGE)

add-dev-dep:
	poetry add $(PACKAGE) --dev

style: activate
	poetry -C $(POETRY_DIR) run ruff check --select I --fix .
	poetry -C $(POETRY_DIR) run ruff format .

lint: activate
	poetry -C $(POETRY_DIR) run ruff check .

test:
	PYTHONPATH=$(PYTHON_PATH) poetry -C $(POETRY_DIR) run pytest

migration:
	poetry -C $(POETRY_DIR) run alembic init migrations

run-local: cleanup
	docker-compose up --build

cleanup:
	docker-compose down

helm-lint:
	helm lint helm/

helm-dryrun:
	helm install helpdesk helm/ --dry-run --debug

port-forward-app:
	kubectl port-forward service/helpdesk 8000:8000

restart-app:
	kubectl rollout restart deployment/helpdesk
