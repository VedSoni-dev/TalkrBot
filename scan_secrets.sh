#!/bin/bash
# Scan the repo for secrets using truffleHog
# Usage: bash scan_secrets.sh

if ! command -v trufflehog &> /dev/null; then
    echo "truffleHog not found. Installing..."
    pip install truffleHog
fi

trufflehog filesystem --no-update --json . 