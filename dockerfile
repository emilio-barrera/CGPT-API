# Install Basicdocker Dependencies (Python & PIP)
FROM ubuntu:22.10
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3-pip \
    && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

#Install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
