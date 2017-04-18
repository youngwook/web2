#! /usr/bin/python

from hello import app as application
import sys

sys.stdout = sys.stderr
sys.path.insert(0, '/home/root/test/web2/')

activate_this = '/home/root/test/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

