FROM --platform=${BUILDPLATFORM} python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade readmeai

# Create a non-root user with a higher UID to avoid conflicts
RUN groupadd -r tempuser && useradd -r -g tempuser tempuser

USER tempuser

ENTRYPOINT ["readmeai"]
CMD ["--help"]
