FROM ubuntu:focal-20211006
RUN  sed -i 's/archive.ubuntu/mirrors.163/g' /etc/apt/sources.list
RUN apt update && apt install wget -y && rm -rf /var/lib/apt/lists/*
RUN cd /tmp && wget https://github.com/Dreamacro/clash/releases/download/v1.9.0/clash-linux-amd64-v1.9.0.gz -O clash.gz && gzip -d clash.gz && ls
