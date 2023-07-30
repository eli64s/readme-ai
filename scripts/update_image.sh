#!/usr/bin/env bash

VERSION="0.0.5"

echo "Building new image: zeroxeli/readme-ai:${VERSION}"

docker build -t zeroxeli/readme-ai:${VERSION} .
docker push zeroxeli/readme-ai:${VERSION}

echo "Successfully pushed new image: zeroxeli/readme-ai:${VERSION}"
