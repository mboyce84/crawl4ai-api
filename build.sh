#!/bin/bash
set -e  # Exit on first error

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright Browsers *without requiring root access*
PLAYWRIGHT_BROWSERS_PATH=$(pwd)/ms-playwright python -m playwright install chromium
