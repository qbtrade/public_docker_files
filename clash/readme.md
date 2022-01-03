## usage
docker run -it --rm qbtradepub/clash -p 9111:1080 clash_entry  --server-host 1.2.3.4 --server-password xx 

docker run -it --rm --net host qbtradepub/clash clash_entry  --server-host 1.2.3.4 --server-password xx --http-port 9111 --socks-port 9112

## production
```shell
docker rm -f clash ; docker run -d --restart always --name clash -p 9111:1080 qbtradepub/clash clash_entry  --server-host 1.2.3.4 --server-password xx

docker logs -f clash
```

## check
https_proxy=http://localhost:9111 curl https://ipinfo.io


