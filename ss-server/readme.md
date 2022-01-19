## usage

docker run -e PASSWORD=xxxx -p 9110:8388 -p 9110:8388/udp -d qbtradepub/ss-server

default setting as following:

ENV SERVER_ADDR 0.0.0.0 ENV SERVER_PORT 8388 ENV PASSWORD= ENV METHOD aes-256-gcm ENV TIMEOUT 300 ENV DNS_ADDRS
8.8.8.8,8.8.4.4 ENV TZ UTC ENV ARGS=

## production

```shell
docker rm -f ss-server ; docker run -d --restart always --name ss-server -e PASSWORD=xxxx -p 9110:8388 -p 9110:8388/udp -d qbtradepub/ss-server

docker logs -f ss-server
```

## check

https_proxy=http://localhost:9110 curl https://ipinfo.io


