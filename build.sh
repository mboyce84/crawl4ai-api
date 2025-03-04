#!/bin/bash
set -e  # Exit on first error
pip install -r requirements.txt  # Install Python dependencies
python -m playwright install --with-deps  # Install Playwright & dependencies
