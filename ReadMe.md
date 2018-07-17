#http://jamessmithies.org. 

A description can be found at Smithies, J. (2016). 'Full Stack DH: Building a Virtual Research Environment on a Raspberry Pi'. In Digital Humanities 2016: Conference Abstracts. Jagiellonian University & Pedagogical University, Kraków, pp. 364-36.

The project is hobbyist quality.

#Note:
Remove 'env_default' and add appropriate settings to 'env'.
Remove 'web/projectfiles/settings/secrets.py_default', and add appropriate settings to 'web/projectfiles/settings/secrets.py'.
Remove 'web/projectfiles/templates/zotero/zot.py_default' and add appropriate settings to 'web/projectfiles/templates/zotero/zot.py'.

#To deploy on x86: 
- cd jsorg_docker-compose
- make build-up
- make load

#To deploy on aarch64/arm64v8 (ARM): 
- cd jsorg_docker-compose
- mv docker-compose.yml docker-compose.yml.bak
- mv docker-compose-aarch64.yml docker-compose.yml
- make build-up
- make load