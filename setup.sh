#!/bin/bash

# Define the virtual environment name
VIRTUAL_ENV_NAME="venv"

# Activate the virtual environment
source ${VIRTUAL_ENV_NAME}/bin/activate

# Install requirements
pip3 install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

# Deactivate the virtual environment (optional)
# deactivate
