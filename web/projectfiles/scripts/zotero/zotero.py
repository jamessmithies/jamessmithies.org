#!/usr/bin/env python3

# Runs all individual Zotero category scripts
# Called from primary makefile, and index/management/commands/updatezotero.py (called from Django admin)

import glob,os
os.getcwd()  # locate ourselves in the directory
for script in sorted(glob.glob("*.py")):
    with open(script) as f:
       contents = f.read()
    exec(contents)