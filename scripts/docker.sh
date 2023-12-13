#!/usr/bin/env bash

# Config
IMAGE="readme-ai"
VERSION="latest"
FULL_IMAGE_NAME="zeroxeli/${IMAGE}:${VERSION}"

# Helper functions
build_image() {
  echo "Building ${FULL_IMAGE_NAME}"
  docker build -t "${FULL_IMAGE_NAME}" .
}

publish_image() {
  echo "Pushing ${FULL_IMAGE_NAME}"
  docker push "${FULL_IMAGE_NAME}"
}

buildx_image() {
  echo "Building and pushing multi-platform image ${FULL_IMAGE_NAME}"
  docker buildx build \
    --platform linux/amd64,linux/arm64 \
    --tag "${FULL_IMAGE_NAME}" \
    --push .
}

# Main execution
echo "Setting up Docker Buildx"
docker buildx create --name mybuilder --use

echo "Starting build process"
build_image
publish_image
buildx_image

echo "Process completed. Published image: ${FULL_IMAGE_NAME}"
