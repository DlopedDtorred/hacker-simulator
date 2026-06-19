#!/bin/bash
# Hacker Simulator 2077 - Launch script for Linux/Mac

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}╔═══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ${YELLOW}HACKER SIMULATOR 2077${GREEN}              ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════╝${NC}"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 is not installed!${NC}"
    echo -e "${YELLOW}💡 Install Python3:${NC}"
    echo "   Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "   Mac: brew install python3"
    exit 1
fi

# Check if colorama is installed
if ! python3 -c "import colorama" &> /dev/null; then
    echo -e "${YELLOW}📦 Installing colorama...${NC}"
    pip3 install colorama --user
fi

# Check if virtual environment exists
if [ -d ".venv" ]; then
    echo -e "${GREEN}✅ Activating virtual environment...${NC}"
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo -e "${GREEN}✅ Activating virtual environment...${NC}"
    source venv/bin/activate
fi

# Run the game
echo -e "${GREEN}🚀 Launching Hacker Simulator 2077...${NC}"
python3 cyberdex.py

# Deactivate virtual environment
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate 2>/dev/null
fi