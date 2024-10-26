#!/bin/bash

echo "Starting development server..."
# export FLASK_APP=apps.flask_api.app 
export FLASK_ENV=development
flask --app apps/flask_api run --reload