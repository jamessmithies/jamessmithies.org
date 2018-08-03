https://jamessmithies.org. 

A description can be found at Smithies, J. (2016). 'Full Stack DH: Building a Virtual Research Environment on a Raspberry Pi'. In Digital Humanities 2016: Conference Abstracts. Jagiellonian University & Pedagogical University, Kraków, pp. 364-36.

The project is hobbyist quality.

If, for some unlikely reason, you'd like to use the project:

1] Edit secrets files
* Remove 'env_default' and add appropriate settings in an 'env' file.
* Remove 'web/projectfiles/settings/secrets.py_default', and add appropriate settings to a 'web/projectfiles/settings/secrets.py' file.
* Remove 'web/projectfiles/templates/zotero/zot.py_default' and add appropriate settings to a 'web/projectfiles/templates/zotero/zot.py' file.

2] This project uses Dockerised instances of letsencrypt / certbot to generate SSL certs. It also has x86 and arm64v8 deployment modes (I use x86 for dev/test and host the project on an arm64v8 Rock 64), which complicates things. See .ssl/ReadMe files for an explanation of how to toggle between the two architectures, and generate certs. tl;dr = you need to edit the following files to toggle between x86 and arm64v8 deployment modes before you (optionally) generate certs.
* .docker-compose.yml; 
* nginx/default.conf; 
* nginx/Dockerfile; 
* ssl/nginx.conf. 

3] As per the ReadMe files, after 1 and 2 are completed it's a simple matter of
* cd web
* make build-up
* make load