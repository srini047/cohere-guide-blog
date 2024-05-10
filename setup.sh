#!/bin/bash

# Define the virtual environment name
VIRTUAL_ENV_NAME="venv"

# Create a virtual environment
python3 -m venv ${VIRTUAL_ENV_NAME}

# Activate the virtual environment
source ${VIRTUAL_ENV_NAME}/bin/activate

# Install requirements
pip3 install -r requirements.txt
