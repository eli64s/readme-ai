"""Unit tests for parsing Docker files."""

import pytest

from readmeai.parsers.docker import DockerComposeParser, DockerfileParser

dockerfile_content = """
# Use a base image with Python 3.10 installed (multi-platform)
FROM --platform=${BUILDPLATFORM} python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Set environment variable for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Install system dependencies and clean up apt cache
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user with a specific UID and GID (i.e. 1000 in this case)
RUN groupadd -r tempuser -g 1000 && \
    useradd -r -u 1000 -g tempuser tempuser && \
    mkdir -p /home/tempuser && \
    chown -R tempuser:tempuser /home/tempuser

# Set permissions for the working directory to the new user
RUN chown tempuser:tempuser /app

# Switch to the new user
USER tempuser

# Add the directory where pip installs user scripts to the PATH
ENV PATH=/home/tempuser/.local/bin:$PATH

# Install the readmeai package from PyPI with a pinned version
RUN pip install --no-cache-dir --user --upgrade readmeai

# Set the command to run the CLI
ENTRYPOINT ["readmeai"]
CMD ["--help"]
"""

content = """
version: '3'
x-airflow-common:
  &airflow-common
  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.0.2}
  environment:

  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
  user: "${AIRFLOW_UID:-50000}:${AIRFLOW_GID:-50000}"
  depends_on:
    redis:
      condition: service_healthy
    postgres:
      condition: service_healthy

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    restart: always

  redis:
    image: redis:latest
    ports:
      - 6379:6379
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 30s
      retries: 50
    restart: always

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - 8080:8080
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8080/health"]
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler
    restart: always

  airflow-worker:
    <<: *airflow-common
    command: celery worker
    restart: always

  flower:
    <<: *airflow-common
    command: celery flower
    ports:
      - 5555:5555
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:5555/"]
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always

volumes:
  postgres-db-volume:
"""

docker_compose_valid = """
version: '3.8'
services:
  service1:
    build: .
    volumes:
      - "./service1:/usr/local/service1"
    ports:
      - "5001:5000"

  service2:
    image: myimage:latest
    depends_on:
      - service1
"""

SAMPLE_DOCKER_COMPOSE_VALID = """
version: '3.8'
services:
  web:
    image: nginx:latest
  db:
    image: mysql:latest
"""

SAMPLE_DOCKER_COMPOSE_INVALID = "Invalid YAML syntax"


@pytest.fixture
def docker_parser():
    """Return DockerParser instance."""
    return DockerComposeParser()


@pytest.fixture
def content_docker_compose_valid(tmp_path):
    """Return valid docker-compose.yaml file."""
    docker_compose_file = tmp_path / "docker-compose.yml"
    docker_compose_file.write_text(SAMPLE_DOCKER_COMPOSE_VALID)
    return docker_compose_file


@pytest.fixture
def content_docker_compose_invalid():
    """Return invalid docker-compose.yaml file."""
    return SAMPLE_DOCKER_COMPOSE_INVALID


def test_docker_parser():
    """Test parsing docker-compose.yaml file."""
    parser = DockerComposeParser()
    assert parser.parse(content) == [
        "postgres",
        "redis",
        "airflow-webserver",
        "airflow-scheduler",
        "airflow-worker",
        "flower",
    ]


def test_docker_parser_valid():
    """Test parsing docker-compose.yaml file."""
    content = docker_compose_valid
    parser = DockerComposeParser()
    expected_values = ["service1", "service2"]
    values = parser.parse(content)
    assert expected_values == values


def test_docker_parser_invalid():
    """Test parsing docker-compose.yaml file."""
    content = ""
    parser = DockerComposeParser()
    result = parser.parse(content)
    assert result is None


def test_dockerfile_parser(docker_parser):
    """Test parsing Dockerfile."""
    parser = DockerfileParser()
    assert parser.parse(dockerfile_content) == [
        ("python", "3.10-slim-buster"),
    ]
