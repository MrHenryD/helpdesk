# Define the Python version as a variable
ARG PYTHON_VERSION=3.11-slim

# Use the official Python image from the Docker Hub
FROM python:${PYTHON_VERSION}

# Set the working directory in the container
WORKDIR /opt/helpdesk

# Copy the Poetry lock file and pyproject.toml into the container
COPY src/pyproject.toml .

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install the dependencies
RUN poetry install --no-root

# Copy the rest of the application code into the container
COPY src/. .

# Copy entrypoint
COPY docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

# Expose the port the app runs on
EXPOSE 8000

# Use an entrypoint file to run the application
ENTRYPOINT ["sh", "entrypoint.sh"]
