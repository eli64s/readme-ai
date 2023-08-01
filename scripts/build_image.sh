#!/usr/bin/env bash

set -e

IMAGE="readme-ai"
VERSION="latest"

echo "Building new image: zeroxeli/${IMAGE}:${VERSION}"

: '
docker build -t zeroxeli/${IMAGE}:${VERSION} .
docker push zeroxeli/${IMAGE}:${VERSION}
'
docker buildx create --use
docker pull moby/buildkit:buildx-stable-1
docker buildx build --push --tag zeroxeli/${IMAGE}:${VERSION} --platform linux/amd64,linux/arm64 .

echo "Successfully pushed new image: zeroxeli/${IMAGE}:${VERSION}"
