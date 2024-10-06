---
hide:
  - title
---

# Docker &nbsp;<img src="https://img.shields.io/docker/pulls/zeroxeli/readme-ai?color=2496ED&logo=docker&label=Docker%20Pulls&labelColor=2496ED&logoColor=white" alt="docker-pulls"></a>&nbsp;<a href="https://hub.docker.com/r/zeroxeli/readme-ai"><img src="https://img.shields.io/docker/image-size/zeroxeli/readme-ai?color=2496ED&logo=docker&label=Image%20Size&labelColor=2496ED&logoColor=white" alt="docker-size"></a></p>

Running readme-ai in a containerized environment using Docker offers isolation of the application and its dependencies from the host system. This section details how to pull the Docker image from Docker Hub, build the Docker image from the source code, and run the Docker container.

???+ note "Docker Installation"
    Before proceeding, ensure that Docker is installed and running on your system. If you haven't installed Docker yet, please visit the [official Docker documentation](https://docs.docker.com/get-docker/) for installation instructions.

## Pull the Docker Image

Pull the latest readme-ai image from Docker Hub:

```sh
docker pull zeroxeli/readme-ai:latest
```

## Build the Docker Image

Alternatively, you can build the Docker image from the source code. This assumes you have cloned the readme-ai repository.

```sh
docker buildx build --platform linux/amd64,linux/arm64 -t readme-ai --push .
```

???+ info "Buildx"
    Using `docker buildx` allows you to build multi-platform images, which means you can create Docker images that work on different architectures (e.g., amd64 and arm64). This is particularly useful if you want your Docker image to be compatible with a wider range of devices and environments, such as both standard servers and ARM-based devices like the Raspberry Pi.

## Run the Docker Container

Run the readme-ai Docker container with the following command:

```sh
docker run -it --rm \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  -v "$(pwd)":/app \
  zeroxeli/readme-ai:latest \
  -r https://github.com/eli64s/readme-ai
```

Explanation of the command arguments:

| Argument      | Function                           |
| ----------- | ------------------------------------ |
| `-it`       | Creates an interactive terminal.     |
| `--rm`      | Automatically removes the container when it exits. |
| `-e` | Passes your OpenAI API key as an environment variable. |
| `-v "$(pwd)":/app` | Mounts the current directory to the `/app` directory in the container, allowing access to the generated README file on your host system. |
| `-r`    | Specifies the GitHub repository to analyze. |

For Windows users, replace `$(pwd)` with `%cd%` in the command. For PowerShell, use `${PWD}` instead.

## Cleanup

If you want to remove the Docker image and container from your system, follow these steps.

**1. Identify the Container**

First, list all containers on your system.

```sh
docker ps -a
```

You should see output similar to the following:

```sh
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS     NAMES
abcdef123456   zeroxeli/readme-ai:latest   "python main.py -r h…"   2 minutes ago    Up 2 minutes
```

Look for the container with ID `abcdef123456`.

**2. Stop the Container**

Stop the container using its ID.

```sh
docker stop abcdef123456
```

**3. Remove the Container**

Remove the container using its ID.

```sh
docker rm abcdef123456
```

**4. Remove the Image**

Remove the Docker image from your system.

```sh
docker rmi zeroxeli/readme-ai:latest
```

## Troubleshooting

1. If you encounter permission issues, ensure your user has the right permissions to run Docker commands.
2. If the container fails to start, check that your `OPENAI_API_KEY` is correctly set and valid.
3. For network-related issues, verify your internet connection and firewall settings.

For more detailed troubleshooting, refer to the official [Docker documentation](https://docs.docker.com/config/daemon/#troubleshoot-the-daemon) or [open an issue](https://github.com/eli64s/readme-ai/issues) on GitHub.
