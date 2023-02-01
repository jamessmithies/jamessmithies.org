#! /usr/bin/python3

import os
import shutil
import subprocess
from django.core.management import call_command

os.remove("fixtures/jsorg_backup.json.bak")
 
src_file = "fixtures/jsorg_backup.json"
destination = "fixtures/jsorg_backup.json.bak"
shutil.copy(src_file, destination)

subprocess.call(['sh', 'dump.sh'])






