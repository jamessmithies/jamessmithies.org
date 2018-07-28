
https://www.humankode.com/ssl/how-to-set-up-free-ssl-certificates-from-lets-encrypt-using-docker-and-nginx

#####For dev you just need to make sure fullchain.pem + privkey.pem are in /docker-volumes/etc/letsencrypt. 

#####Boot up the temporary cert-issue-site

cd web/ssl/cert-issue-site
make cert-site-up

#####Run the staging command for issuing a new certificate:

sudo docker run -it --rm \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt/ \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/ \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
certonly --webroot \
--register-unsafely-without-email --agree-tos \
--webroot-path=/data/web/ssl/cert-issue-site/ \
--staging \
-d jsorg.space -d www.jsorg.space

#####Clean up staging artifacts:

sudo rm -rf /docker-volumes/

#####Request a production certificate:

sudo docker run -it --rm \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/ \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
certonly --webroot \
--email jamessmithies.smtp@gmail.com --agree-tos --no-eff-email \
--webroot-path=/data/web/ssl/cert-issue-site/ \
-d jsorg.space -d www.jsorg.space


#####If everything ran successfully, run a docker-compose down command to stop the temporary Nginx site

make cert-site-down

#####Ensure cron is set to renew certs
sudo crontab -e
0 23 * * * docker run --rm -it --name certbot -v "/docker-volumes/etc/letsencrypt:/etc/letsencrypt" -v "/docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt" -v "/docker-volumes/data/letsencrypt:/data/letsencrypt" -v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" certbot/certbot renew --webroot -w /data/letsencrypt --quiet && docker kill --signal=HUP production-nginx-container