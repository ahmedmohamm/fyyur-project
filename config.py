import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# my db server hase a password
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:01023078169@local:5432/fyyur'
