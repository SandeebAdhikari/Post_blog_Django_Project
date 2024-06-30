#!/bin/bash

# Ensure pip is available
python -m ensurepip --upgrade

# Install virtualenv if not already installed
python -m pip install --upgrade virtualenv

# Create a virtual environment
python -m virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Install the requirements
python -m pip install -r requirements.txt

# Run collectstatic
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
