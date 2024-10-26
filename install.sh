#!/bin/bash

echo "Installing dependencies..."
poetry install

echo "Setting up database migrations..."
if [ ! -d "migrations" ]; then
  flask db init
fi

echo "Installation complete."