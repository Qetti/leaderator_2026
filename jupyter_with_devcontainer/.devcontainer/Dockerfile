FROM mcr.microsoft.com/devcontainers/python:3.12
ENV PYTHONDOWNWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /tmp/requirements.txt


RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
