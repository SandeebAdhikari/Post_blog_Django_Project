#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files and apply migrations
python manage.py collectstatic --noinput
python manage.py migrate
