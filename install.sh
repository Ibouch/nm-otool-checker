#!/bin/bash

pip install --user virtualenv
python $HOME/Library/Python/2.7/lib/python/site-packages/virtualenv.py venv --system-site-packages -p /usr/bin/python2.7 --distribute
source venv/bin/activate
pip install -r requirements.txt
