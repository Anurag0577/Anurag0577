#!/bin/bash

# GitHub Stats Generator Runner
# This script loads environment variables and runs the Python script

# Check if .env file exists
if [ -f .env ]; then
    echo "Loading environment variables from .env..."
    export $(cat .env | xargs)
else
    echo "Warning: .env file not found."
    echo "Please set ACCESS_TOKEN and USER_NAME environment variables."
    echo ""
    echo "Usage:"
    echo "  export ACCESS_TOKEN='your_token'"
    echo "  export USER_NAME='your_username'"
    echo "  bash run.sh"
    echo ""
    exit 1
fi

# Check if required environment variables are set
if [ -z "$ACCESS_TOKEN" ] || [ -z "$USER_NAME" ]; then
    echo "Error: ACCESS_TOKEN and USER_NAME must be set"
    exit 1
fi

echo "Running GitHub Stats Generator..."
echo "Username: $USER_NAME"
echo ""

python today.py
