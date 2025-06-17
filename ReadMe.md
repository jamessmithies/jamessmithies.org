https://jamessmithies.org. 

A description can be found at Smithies, J. (2016). 'Full Stack DH: Building a Virtual Research Environment on a Raspberry Pi'. In Digital Humanities 2016: Conference Abstracts. Jagiellonian University & Pedagogical University, Kraków, pp. 364-36.

The project is hobbyist quality, used to help me udnerstand various aspects of web design and hosting. It was initially created using Wordpress then manually copied into Django and hosted on various  hardware (EC2, Raspberry Pi) before being converted to an offline (Dango) -> static (GitHub Pages) solution. It's a Frankensteined solution but works well enough for something ~15 years old. If, for some unlikely reason, you'd like to use the project:

1] Edit secrets files
* Remove 'env_default' and add appropriate settings in an 'env' file.
* Remove 'web/projectfiles/settings/secrets.py_default', and add appropriate settings to a 'web/projectfiles/settings/secrets.py' file.
* Remove 'web/projectfiles/templates/zotero/zot.py_default' and add appropriate settings to a 'web/projectfiles/templates/zotero/zot.py' file.

2] Build the docker containers and load the database (this will of course be the database for jamessmithies.org but could be replaced)
* make build
* make load

The website can be accessed at ```localhost```. Log in at http://localhost/admin/login/admin/ to add blog posts etc.

3] The makefile contains actions that can be performed: update the Zotero bibliography, make the static files, run the Mastodon update process, publish the static files, export ('dump') the database etc.