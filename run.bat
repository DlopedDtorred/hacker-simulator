@echo off
:: Hacker Simulator 2077 - Launch script for Windows
title Hacker Simulator 2077
color 0A

echo ╔═══════════════════════════════════════════╗
echo ║  HACKER SIMULATOR 2077              ║
echo ╚═══════════════════════════════════════════╝

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo 💡 Download Python from: https://python.org
    pause
    exit /b 1
)

:: Check if colorama is installed
python -c "import colorama" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing colorama...
    pip install colorama
)

:: Activate virtual environment if exists
if exist .venv\Scripts\activate (
    echo ✅ Activating virtual environment...
    call .venv\Scripts\activate
)
if exist venv\Scripts\activate (
    echo ✅ Activating virtual environment...
    call venv\Scripts\activate
)

:: Run the game
echo 🚀 Launching Hacker Simulator 2077...
python cyberdex.py

pause