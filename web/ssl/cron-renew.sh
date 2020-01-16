#!/bin/sh

docker run -it --rm \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/ \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
--quiet \
certonly --webroot \
--email jamessmithies.smtp@gmail.com --agree-tos --no-eff-email \
--webroot-path=/data/web/ssl/cert-issue-site/ \
-d jamessmithies.org -d www.jamessmithies.org

