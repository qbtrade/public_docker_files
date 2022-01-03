## usage
docker run -it --rm qbtradepub/clash -p 9111:1080 clash_entry  --server-host 1.2.3.4 --server-password xx 

## production
docker rm -f clash
docker run -d --name clash -p 9111:1080 qbtradepub/clash clash_entry  --server-host 1.2.3.4 --server-password xx

## check
https_proxy=http://localhost:9111 curl https://ipinfo.io


