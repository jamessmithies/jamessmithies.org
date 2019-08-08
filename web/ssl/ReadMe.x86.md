
Based on: https://www.humankode.com/ssl/how-to-set-up-free-ssl-certificates-from-lets-encrypt-using-docker-and-nginx

#####For prod deployment to arm64v8 see ReadMe.arm64v8.md.

#####If necessary rename / toggle to x86 and/or edit:
* .docker-compose.yml; 
* nginx/default.conf; 
* nginx/Dockerfile; 
* ssl/nginx.conf. 


#####For dev - unless you are developing on jsorg.space VM (in which case replace all instances of jamessmithies.org with jsorg.space) - you just need to make sure old fullchain.pem + privkey.pem files are in /docker-volumes/etc/letsencrypt/live/jamessmithies.org on the local machine, rather than going through cert-issue process via the temporary site. 

#####Create env and secrets files (using secret content from local repository)
sudo nano env
sudo nano web/projectfiles/settings/secrets.py
sudo mv /webapps/jamessmithies.org/web/projectfiles/templates/zotero/settings_default.py /webapps/jamessmithies.org/web/projectfiles/templates/zotero/settings.py 
sudo nano /webapps/jamessmithies.org/web/projectfiles/templates/zotero/settings.py (large file: Only copy secrets)

#####Boot up the temporary cert-issue-site

cd web/ssl/
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
-d jamessmithies.org -d www.jamessmithies.org

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
-d jamessmithies.org -d www.jamessmithies.org


#####If everything ran successfully, run a docker-compose down command to stop the temporary Nginx site

make cert-site-down

#####Boot up the dev site
cd ../../
make build-up
make load

#####Ensure cron is set to renew certs
sudo crontab -e
0 23 * * * docker run --rm -it --name certbot -v "/docker-volumes/etc/letsencrypt:/etc/letsencrypt" -v "/docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt" -v "/docker-volumes/data/letsencrypt:/data/letsencrypt" -v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" certbot/certbot renew --webroot -w /data/letsencrypt --quiet && docker kill --signal=HUP nginx

