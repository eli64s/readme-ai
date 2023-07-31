# Use a base image with Python 3.9 installed (multi-platform)
FROM --platform=${BUILDPLATFORM} python:3.9-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y git tree

# Set working directory
WORKDIR /app

# Set environment variable for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Install the readmeai package from PyPI
RUN pip install --no-cache-dir readmeai

# Set the command to run your project
CMD ["readmeai"]
