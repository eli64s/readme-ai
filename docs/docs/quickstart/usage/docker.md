# Running with Docker

To run `readme-ai` in a Docker container, you can either pull the latest Docker image from Docker Hub or build the Docker image from the source code.

### Pull the Docker Image

Pull the latest `readme-ai` Docker image from Docker Hub using the following command:

```sh
docker pull zeroxeli/readme-ai:latest
```

### Run the Docker Container

Run the `readme-ai` Docker container using the following command:

```sh
docker run -it \
        -e OPENAI_API_KEY=$OPENAI_API_KEY \
        -v "$(pwd)":/app zeroxeli/readme-ai:latest \
        -r https://github.com/eli64s/readme-ai
```
