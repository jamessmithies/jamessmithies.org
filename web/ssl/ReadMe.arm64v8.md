
Based on: https://hub.docker.com/r/intrepidde/rpi-certbot/

#####To prepare for prod deployment, rename / toggle to arm64v8 and/or edit:
* .docker-compose.yml; 
* nginx/default.conf; 
* nginx/Dockerfile; 
* ssl/nginx.conf. 
* Be sure to find/replace jsorg.space with jamessmithies.org in those files.

#####Boot up the temporary cert-issue-site

cd web/ssl/
make cert-site-up

#####Run the staging command for issuing a new certificate (uses intrepidde/rpi-certbot):

docker run -ti --rm \
--name certbot-nginx --hostname certbot-nginx \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/ \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt"/ \
intrepidde/rpi-certbot certbot certonly --staging --webroot -w /data/web/ssl/cert-issue-site/ -d jamessmithies.org -d www.jamessmithies.org -m jamessmithies.smtp@gmail.com --agree-tos

#####Clean up staging artifacts:

sudo rm -rf /docker-volumes/

#####Request a production certificate:

docker run -ti --rm \
--name certbot-nginx --hostname certbot-nginx \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt:rw \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/:rw \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt"/:rw \
intrepidde/rpi-certbot certbot certonly --webroot -w /data/web/ssl/cert-issue-site/ -d jamessmithies.org -d www.jamessmithies.org -m jamessmithies.smtp@gmail.com --agree-tos


#####If everything ran successfully, run a docker-compose down command to stop the temporary Nginx site

make cert-site-down

#####Boot prod
##Create env and secrets files
sudo nano env
sudo nano web/projectfiles/settings/secrets.py
cd ../../
make build-up
make load

#####Ensure cron is set to renew certs
sudo crontab -e

0 23 * * * docker run --rm -it --name certbot -v "/docker-volumes/etc/letsencrypt:/etc/letsencrypt" -v "/docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt" -v "/docker-volumes/data/letsencrypt:/data/letsencrypt" -v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" certbot/certbot renew --webroot -w /data/letsencrypt --quiet && docker kill --signal=HUP Nginx