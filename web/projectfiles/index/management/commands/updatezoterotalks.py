#!/usr/bin/env python
from django.core.management.base import BaseCommand, CommandError

import subprocess

class Command(BaseCommand):
	def handle(self, *args, **options):
		subprocess.call(["python3", "zot.py", "--settings=settings/settings-talks.py"], cwd='templates/zotero')
	
