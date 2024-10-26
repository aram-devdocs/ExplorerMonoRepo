#!/bin/bash

echo "Installing Jupyter and setting up Poetry kernel..."
# Install Jupyter and ipykernel in the Poetry environment
poetry add --group dev jupyter ipykernel

# Add the Poetry environment as a Jupyter kernel
poetry run python -m ipykernel install --user --name=poetry-env --display-name "Python (Poetry)"

echo "Installation complete! Your Poetry environment is now available as a Jupyter kernel."
