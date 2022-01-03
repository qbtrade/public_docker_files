FROM ubuntu:focal-20211006
RUN  sed -i 's/archive.ubuntu/mirrors.163/g' /etc/apt/sources.list
RUN apt update && apt install wget python3 python3-pip -y && rm -rf /var/lib/apt/lists/*
RUN pip3 install docopt arrow
RUN cd /tmp && \
  wget https://github.com/Dreamacro/clash/releases/download/v1.9.0/clash-linux-amd64-v1.9.0.gz -O clash.gz && \
  gzip -d clash.gz && \
  chmod +x clash && \
  mv clash /usr/local/bin
COPY clash_entry.py /usr/local/bin/clash_entry
COPY clash_config.template /clash_config.template
RUN chmod +x /usr/local/bin/clash_entry
