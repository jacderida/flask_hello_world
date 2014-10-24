import sys

sys.path.append('/var/www/hello_world/current')
activate_this = '/var/www/hello_world/current/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from hello import app as application
