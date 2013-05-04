import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

try:
    SCHOOLAX_ENV = os.environ['BIRTHDAYSTARTER_ENV']
    if SCHOOLAX_ENV == 'PROD':
        from settings_prod import *
    elif SCHOOLAX_ENV == 'QA':
        from settings_qa import *
    else:
        from settings_dev import *
except KeyError:
    from settings_dev import *

# You can add a settings_extra.py file for additional personal configurations
if os.path.isfile(os.path.join(PROJECT_ROOT, 'settings_extra.py')):
    from settings_extra import *
