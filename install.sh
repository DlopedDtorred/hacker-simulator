#!/bin/bash
# Hacker Simulator 2077 - Installer

echo "HACKER SIMULATOR 2077 - INSTALLER"
echo "=================================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed"
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install colorama

# Run
echo "✅ Installation complete!"
echo "Run ./run.sh to start the game"