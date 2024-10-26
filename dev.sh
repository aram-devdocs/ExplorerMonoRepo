#!/bin/bash

echo "Starting development server..."
export FLASK_APP=apps/flask-api/app.py
export FLASK_ENV=development
flask run