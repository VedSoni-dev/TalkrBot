#!/bin/bash
# Usage: source load_env.sh
# Loads environment variables from .env into the current shell

if [ ! -f .env ]; then
  echo ".env file not found in current directory."
  return 1
fi

set -a
source .env
set +a

echo "✅ Environment variables loaded from .env"
