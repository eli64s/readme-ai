# Base image
FROM python:3.9-slim-buster as builder

# Set working directory
WORKDIR /src

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies and basic packages
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim-buster as runtime

WORKDIR /src

COPY --from=builder /src /src

# Uninstall build-essential to keep the image slim
RUN apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
