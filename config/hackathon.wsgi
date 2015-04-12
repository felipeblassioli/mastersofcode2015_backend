import os
import site
from os.path import join,dirname,abspath

import sys
sys.stdout = sys.stderr

VENV_PACKAGES = join(dirname(abspath(__file__)), 'env/lib/python2.7/site-packages')
site.addsitedir(VENV_PACKAGES)

from app import app as application
