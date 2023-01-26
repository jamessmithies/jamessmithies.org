#! /usr/bin/python
# 
import subprocess
import os

directory = "scripts/zotero/" # Replace with the actual path

for filename in os.listdir(directory):
    if filename.endswith(".py"):
        subprocess.run(["python", os.path.join(directory, filename)])
