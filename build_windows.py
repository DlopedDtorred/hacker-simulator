#!/usr/bin/env python3
"""
Build script for Windows executable
"""

import os
import sys
import subprocess

def build_windows():
    """Build Windows executable using PyInstaller"""
    
    print("🚀 Building Windows executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name", "HackerSimulator2077",
        "--console",
        "--add-data", "logo.png:.",
        "--clean",
        "cyberdex.py"
    ]
    
    # Run PyInstaller
    subprocess.run(cmd, check=True)
    
    print("✅ Build complete! Check dist/HackerSimulator2077.exe")

if __name__ == "__main__":
    build_windows()