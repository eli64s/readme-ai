#!/usr/bin/env bash

VERSION="latest"

echo "Building new image: zeroxeli/readme-ai:${VERSION}"

: '
docker build -t zeroxeli/readme-ai:${VERSION} .
docker push zeroxeli/readme-ai:${VERSION}
'
docker buildx create --use
docker pull moby/buildkit:buildx-stable-1
docker buildx build --push --tag zeroxeli/readme-ai:${VERSION} --platform linux/amd64,linux/arm64 .

echo "Successfully pushed new image: zeroxeli/readme-ai:${VERSION}"
