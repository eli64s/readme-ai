# Use a base image with Python 3.9 installed
FROM python:3.9-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y git tree

# Set working directory
WORKDIR /app

# Set environment variable for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Copy the project files to the container
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run your project
CMD ["python", "src/main.py"]
