#!/bin/bash

pip install virtualenv
virtualenv venv --system-site-packages
source venv/bin/activate
pip install -r requirements.txt
