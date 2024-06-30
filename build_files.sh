#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the requirements
pip install -r requirements.txt

# Run collectstatic
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
