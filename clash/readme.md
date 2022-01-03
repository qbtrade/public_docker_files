## usage
docker run -it --rm play clash_entry  --server-host 1.2.3.4 --server-password xx -p 3000:1080

## check
https_proxy=http://localhost:3000 curl https://ipinfo.io
