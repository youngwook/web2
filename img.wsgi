from hello import app as application
import sys

sys.path.insert(0, '/home/webapp/test/web/')

activate_this = '/home/webapp/test/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

