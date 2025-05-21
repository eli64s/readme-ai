"""Pytest fixtures to reuse across readmeai.parsers submodule."""

import pytest

from readmeai.parsers.docker import DockerComposeParser, DockerfileParser
from readmeai.parsers.properties import PropertiesParser

# -- Dockerfile ----------------------------------------------------------


@pytest.fixture(scope="module")
def dockerfile_content() -> str:
    """Fixture for sample Dockerfile content."""
    return """
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


@pytest.fixture
def dockerfile_parser() -> DockerfileParser:
    """Fixture for DockerfileParser."""
    return DockerfileParser()


# -- docker-compose.yaml -------------------------------------------------------


@pytest.fixture(scope="module")
def docker_compose_content() -> str:
    """Fixture for sample docker-compose.yaml content."""
    return """
version: '3.4'

services:
    broker:
        container_name: celery-broker
        image: rabbitmq:3.8.2-management-alpine
        ports:
            - "8080:15672"
            - "5672:5672"
        networks:
            - network

    backend:
        container_name: celery-backend
        image: redis:5.0.7
        ports:
            - "6379:6379"
        networks:
            - network
        command: redis-server --requirepass password

    audio:
        build: ./src/workers
        container_name: celery-wAudio
        environment:
            - REDIS_HOST=backend
            - REDIS_PORT=6379
            - REDIS_DB=0
            - REDIS_PASS=password
            - RABBITMQ_HOST=broker
            - RABBITMQ_PORT=5672
            - RABBITMQ_USER=guest
            - RABBITMQ_PASS=guest
        links:
            - backend:backend
            - broker:broker
        networks:
            - network
        command: celery worker -A audio.worker.audio --loglevel=INFO --concurrency=2 --hostname=wAudio@%h --queues audio -E --config=audio.config

    euro:
        build: ./src/workers
        container_name: celery-wEuro
        environment:
            - REDIS_HOST=backend
            - REDIS_PORT=6379
            - REDIS_DB=0
            - REDIS_PASS=password
            - RABBITMQ_HOST=broker
            - RABBITMQ_PORT=5672
            - RABBITMQ_USER=guest
            - RABBITMQ_PASS=guest
        links:
            - backend:backend
            - broker:broker
        networks:
            - network
        command: celery worker -A euro.worker.euro --loglevel=INFO --concurrency=2 --hostname=wEuro@%h --queues euro -E --config=euro.config

    api:
        build: ./src/api
        container_name: celery-api
        environment:
            - REDIS_HOST=backend
            - RABBITMQ_HOST=broker
        links:
            - backend:backend
            - broker:broker
        ports:
            - "5000:5000"
        networks:
            - network

    client:
        build: ./src/client
        container_name: celery-client
        environment:
            - API_URL=http://api:5000
        links:
            - api:api
        networks:
            - network

networks:
    network: {}
"""


@pytest.fixture(scope="module")
def docker_compose_parser() -> DockerComposeParser:
    """Fixture for DockerComposeParser."""
    return DockerComposeParser()


# -- *.properties ---------------------------------------------------------


@pytest.fixture(scope="module")
def properties_content() -> str:
    """Fixture for sample .properties content."""
    return """
version=3.4.0-SNAPSHOT
latestVersion=true
spring.build-type=oss
org.gradle.caching=true
org.gradle.parallel=true
org.gradle.jvmargs=-Xmx2g -Dfile.encoding=UTF-8
assertjVersion=3.26.3
checkstyleToolVersion=10.12.4
commonsCodecVersion=1.17.1
graalVersion=22.3
hamcrestVersion=2.2
jacksonVersion=2.17.2
javaFormatVersion=0.0.43
junitJupiterVersion=5.11.0
kotlinVersion=1.9.25
mavenVersion=3.9.4
mockitoVersion=5.13.0
nativeBuildToolsVersion=0.10.3
snakeYamlVersion=2.3
springFrameworkVersion=6.2.0-RC1
springFramework60xVersion=6.0.23
tomcatVersion=10.1.30
kotlin.stdlib.default.dependency=false
"""


@pytest.fixture(scope="module")
def properties_parser() -> PropertiesParser:
    """Fixture for .properties parser."""
    return PropertiesParser()
