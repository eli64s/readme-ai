from readmeai.parsers.docker import DockerComposeParser, DockerfileParser


def test_dockerfile_empty(dockerfile_parser: DockerfileParser):
    """Test parsing empty Dockerfile."""
    result = dockerfile_parser.parse("")
    assert result == []


def test_docker_compose_empty(docker_compose_parser: DockerComposeParser):
    """Test parsing empty docker-compose.yaml."""
    result = docker_compose_parser.parse("")
    assert result == []


def test_dockerfile_parser(
    dockerfile_parser: DockerfileParser, dockerfile_content: str
):
    """Test parsing Dockerfile."""
    result = dockerfile_parser.parse(dockerfile_content)
    assert result == ["python: 3.10-slim-buster"]


def test_docker_compose_parser_services(
    docker_compose_parser: DockerComposeParser, docker_compose_content: str
):
    """Test getting services from docker-compose.yaml."""
    docker_compose_parser.parse(docker_compose_content)
    expected_services = ["broker", "backend", "audio", "euro", "api", "client"]
    assert docker_compose_parser.get_services() == expected_services


def test_docker_compose_parser_service_details(
    docker_compose_parser: DockerComposeParser, docker_compose_content: str
):
    """Test getting detailed service information from docker-compose.yaml."""
    docker_compose_parser.parse(docker_compose_content)
    service_details = docker_compose_parser.get_all_service_details()[0]
    # Validate details for broker service
    assert "broker" in service_details
    assert service_details["broker"]["image"] == "rabbitmq:3.8.2-management-alpine"
    assert service_details["broker"]["ports"] == ["8080:15672", "5672:5672"]
    # Validate details for backend service
    assert "backend" in service_details
    assert service_details["backend"]["image"] == "redis:5.0.7"
    assert (
        service_details["backend"]["command"] == "redis-server --requirepass password"
    )
    # Validate details for audio service
    assert "audio" in service_details
    assert "REDIS_HOST=backend" in service_details["audio"]["environment"]
    assert service_details["audio"]["command"] == (
        "celery worker -A audio.worker.audio --loglevel=INFO --concurrency=2 --hostname=wAudio@%h --queues audio -E --config=audio.config"
    )
