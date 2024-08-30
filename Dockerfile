FROM --platform=${BUILDPLATFORM} python:3.11-slim-buster

WORKDIR /app

ENV GIT_PYTHON_REFRESH=quiet

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r tempuser -g 1000 \
    && useradd -r -u 1000 -g tempuser tempuser \
    && chown -R tempuser:tempuser /app

USER tempuser

ENV PATH=/home/tempuser/.local/bin:$PATH

RUN pip install --no-cache-dir --user --upgrade readmeai

ENTRYPOINT ["readmeai"]
CMD ["--help"]
