#!/bin/sh

export PYTHONPATH=app

# Function to run Alembic migrations
run_migrations() {
    echo "Running Alembic migrations..."
    exec poetry run alembic upgrade head
}

autogenerate_migrations() {
    echo "Running Alembic migrations..."
    exec poetry run alembic revision --autogenerate -m "<message>"
}

# Function to start the FastAPI application
debug_app() {
    echo "Starting FastAPI application..."
    exec poetry run opentelemetry-instrument \
         uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
}

start_app() {
    echo "Starting FastAPI application..."
    exec poetry run opentelemetry-instrument \
         uvicorn app.main:app --host 0.0.0.0 --port 8000
}

# Function to run tests
run_tests() {
    echo "Running tests..."
    exec poetry run pytest
}

# Check the first argument passed to the script
case "$1" in
    migrate)
        run_migrations
        ;;
    debug)
        debug_app
        ;;
    start)
        start_app
        ;;
    test)
        run_tests
        ;;
    *)
        echo "Usage: $0 {alembic|debug|start|test}"
        exit 1
        ;;
esac