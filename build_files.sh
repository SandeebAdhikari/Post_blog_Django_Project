#!/bin/bash

# Ensure pip is available
python3.9 -m ensurepip --upgrade

# Upgrade pip
python3.9 -m pip install --upgrade pip

# Install the requirements
python3.9 -m pip install -r requirements.txt

# Run collectstatic
python3.9 manage.py collectstatic --noinput

# Run migrations
python3.9 manage.py migrate
