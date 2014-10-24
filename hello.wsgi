import sys

sys.path.append('/var/www/hello_world')
activate_this = '/var/www/hello_world/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from hello import app as application
