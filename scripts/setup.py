"""this simple script is used to install packages used in other scripts"""

import pip

def import_or_install(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])

import_or_install(['pandas', 'numpy', 'stockstats', 'matplotlib', ])
