
Based on: https://hub.docker.com/r/intrepidde/rpi-certbot/

#####To prepare for prod deployment,
##Rename / toggle to arm64v8 and edit as required:
* .docker-compose.yml; 
* nginx/default.conf; 
* nginx/Dockerfile; 
* ssl/nginx.conf. 
* Be sure to find/replace jsorg.space with jamessmithies.org in those files.

#####Destroy images, back up current install, and fetch new version
cd /webapps/jamessmithies.org
make destroy
cd ../
sudo mv jamessmithies.org jamessmithies.bak
sudo git clone https://github.com/jamessmithies/jamessmithies.org.git
cd jamessmithies.org

##Create env and secrets files (using secret content from local repository)
sudo nano env
sudo nano web/projectfiles/settings/secrets.py
cd /webapps/jamessmithies.org/web/projectfiles/templates/zotero/
sudo mv zot.py_default zot.py (large file: Only copy secrets)
sudo nano zot.py (large file: Only copy secrets)

#####If you don't need a new cert
make build-up
make load
STOP

#####If you need a new cert: Boot up the temporary cert-issue-site
cd web/ssl/
make cert-site-up

#####If you need a new cert: Run the staging command for issuing a new certificate (uses intrepidde/rpi-certbot):

docker run -ti --rm \
--name certbot-nginx --hostname certbot-nginx \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/ \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt"/ \
intrepidde/rpi-certbot certbot certonly --staging --webroot -w /data/web/ssl/cert-issue-site/ -d jamessmithies.org -d www.jamessmithies.org -m jamessmithies.smtp@gmail.com --agree-tos

#####If you need a new cert: Clean up staging artifacts:

sudo rm -rf /docker-volumes/

#####If you need a new cert: Request a production certificate:

docker run -ti --rm \
--name certbot-nginx --hostname certbot-nginx \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt:rw \
-v /webapps/jamessmithies.org/web/ssl/cert-issue-site:/data/web/ssl/cert-issue-site/:rw \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt"/:rw \
intrepidde/rpi-certbot certbot certonly --webroot -w /data/web/ssl/cert-issue-site/ -d jamessmithies.org -d www.jamessmithies.org -m jamessmithies.smtp@gmail.com --agree-tos


#####If you need a new cert: If everything ran successfully, run a docker-compose down command to stop the temporary Nginx site

make cert-site-down

#####If you need a new cert: Boot prod
sudo nano env
sudo nano web/projectfiles/settings/secrets.py
cd /webapps/jamessmithies.org/web/projectfiles/templates/zotero/
sudo mv zot.py_default zot.py (large file: Only copy secrets)
sudo nano zot.py (large file: Only copy secrets)
cd ../../
make build-up
make load

#####Ensure cron is set to renew certs
sudo crontab -e

0 23 * * * docker run --rm -it --name certbot -v "/docker-volumes/etc/letsencrypt:/etc/letsencrypt" -v "/docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt" -v "/docker-volumes/data/letsencrypt:/data/letsencrypt" -v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" certbot/certbot renew --webroot -w /data/letsencrypt --quiet && docker kill --signal=HUP Nginx