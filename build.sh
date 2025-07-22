#!/usr/bin/env bash

# Ensure pip is up to date
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Export mock mode ON if no API keys found (optional)
export MOCK_MODE=True
