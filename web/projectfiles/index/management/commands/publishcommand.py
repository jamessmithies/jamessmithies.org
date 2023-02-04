#!/usr/bin/env python3
from django.core.management.base import BaseCommand, CommandError

import subprocess

class Command(BaseCommand):
	def handle(self, *args, **options):
		subprocess.call(["sh", "makestatic.sh"])
