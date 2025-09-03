#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Check if git is installed
if ! command -v git >/dev/null 2>&1; then
    echo "Error: git is not installed. Please install it and try again."
    exit 1
fi

# Get the absolute path to the scenario directory
WORK_DIR=$(realpath "$(dirname "$0")")

# TODO: specify a version
# Clone the termux-web-scraper repository
git clone https://github.com/kpliuta/termux-web-scraper.git "$WORK_DIR/termux-web-scraper"

# Execute the scraper script
"$WORK_DIR/termux-web-scraper/scripts/run.sh" \
    --scenarios-dir "$WORK_DIR/src" \
    --script simple.py \
    --upgrade \
    --output-dir /sdcard/termux-web-scraper:/mnt/scraper/out
