#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - INSTALLER
==================================
Selecciona qué versión quieres instalar.
"""

import os
import sys
import shutil
import subprocess
import platform
from pathlib import Path

# ============================================
# COLORES PARA TERMINAL
# ============================================

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_header(text):
    print(f"\n{Colors.CYAN}{'═'*50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{'═'*50}{Colors.RESET}")

def print_option(num, text, desc=""):
    print(f"{Colors.YELLOW}[{num}]{Colors.RESET} {Colors.WHITE}{text}{Colors.RESET}")
    if desc:
        print(f"   {Colors.BLUE}{desc}{Colors.RESET}")

# ============================================
# DETECTAR SISTEMA OPERATIVO
# ============================================

def detect_os():
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Darwin":
        return "macos"
    else:
        return "linux"

# ============================================
# INSTALAR DEPENDENCIAS
# ============================================

def install_dependencies():
    print_header("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "colorama"], check=True)
        print(f"{Colors.GREEN}✅ colorama installed{Colors.RESET}")
    except:
        print(f"{Colors.RED}❌ Failed to install colorama{Colors.RESET}")
    return True

# ============================================
# INSTALAR VERSIÓN UI
# ============================================

def install_ui():
    print_header("🖥️ Installing UI Version...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "PyQt5"], check=True)
        print(f"{Colors.GREEN}✅ PyQt5 installed{Colors.RESET}")
    except:
        print(f"{Colors.RED}❌ Failed to install PyQt5{Colors.RESET}")
        return False
    
    os_name = detect_os()
    home = Path.home()
    install_dir = home / ".hacker_simulator"
    install_dir.mkdir(exist_ok=True)
    
    script_dir = Path(__file__).parent
    source = script_dir / "hacker_simulator_ui.py"
    dest = install_dir / "hacker_simulator_ui.py"
    
    if not source.exists():
        print(f"{Colors.RED}❌ hacker_simulator_ui.py not found!{Colors.RESET}")
        return False
    
    shutil.copy(source, dest)
    print(f"{Colors.GREEN}✅ hacker_simulator_ui.py copied{Colors.RESET}")
    
    if os_name == "windows":
        bat_content = f"""@echo off
python "{dest}" %*
pause
"""
        bat_path = install_dir / "hacker_ui.bat"
        with open(bat_path, 'w') as f:
            f.write(bat_content)
        print(f"{Colors.GREEN}✅ hacker_ui.bat created{Colors.RESET}")
        try:
            desktop = Path.home() / "Desktop"
            shortcut = desktop / "HackerSimulator_UI.bat"
            shutil.copy(bat_path, shortcut)
            print(f"{Colors.GREEN}✅ Desktop shortcut created{Colors.RESET}")
        except:
            pass
    else:
        sh_content = f"""#!/bin/bash
python3 "{dest}" "$@"
"""
        sh_path = install_dir / "hacker_ui.sh"
        with open(sh_path, 'w') as f:
            f.write(sh_content)
        sh_path.chmod(0o755)
        print(f"{Colors.GREEN}✅ hacker_ui.sh created{Colors.RESET}")
        try:
            symlink = Path("/usr/local/bin/hacker-ui")
            if symlink.exists():
                symlink.unlink()
            os.symlink(sh_path, symlink)
            print(f"{Colors.GREEN}✅ Global command 'hacker-ui' created{Colors.RESET}")
        except:
            print(f"{Colors.YELLOW}⚠️ Could not create symlink. Run with sudo?{Colors.RESET}")
    
    print(f"{Colors.GREEN}✅ UI version installed!{Colors.RESET}")
    print(f"{Colors.BLUE}📁 Location: {install_dir}{Colors.RESET}")
    return True

# ============================================
# DESINSTALAR
# ============================================

def uninstall():
    print_header("🗑️ Uninstalling...")
    home = Path.home()
    install_dir = home / ".hacker_simulator"
    if install_dir.exists():
        shutil.rmtree(install_dir)
        print(f"{Colors.GREEN}✅ Removed {install_dir}{Colors.RESET}")
    try:
        if Path("/usr/local/bin/hacker-ui").exists():
            os.remove("/usr/local/bin/hacker-ui")
        print(f"{Colors.GREEN}✅ Removed symlinks{Colors.RESET}")
    except:
        pass
    print(f"{Colors.GREEN}✅ Uninstall complete!{Colors.RESET}")

# ============================================
# MENÚ PRINCIPAL
# ============================================

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════════════╗
{Colors.GREEN}║  {Colors.CYAN}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗  {Colors.GREEN}       ║
{Colors.GREEN}║  {Colors.CYAN}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗ {Colors.GREEN}       ║
{Colors.GREEN}║  {Colors.CYAN}███████║███████║██║     █████╔╝ █████╗  ██████╔╝ {Colors.GREEN}       ║
{Colors.GREEN}║  {Colors.CYAN}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ {Colors.GREEN}       ║
{Colors.GREEN}║  {Colors.CYAN}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║ {Colors.GREEN}       ║
{Colors.GREEN}║  {Colors.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {Colors.GREEN}       ║
{Colors.GREEN}║     {Colors.YELLOW}HACKER SIMULATOR 2077 - INSTALLER{Colors.GREEN}               ║
{Colors.GREEN}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """)
    
    print(f"{Colors.BOLD}Welcome to Hacker Simulator 2077 Installer!{Colors.RESET}\n")
    print(f"{Colors.BLUE}Select the version you want to install:{Colors.RESET}")
    print_option("1", "UI Version", "Graphical interface with hacker style (PyQt5)")
    print_option("2", "Uninstall", "Remove all installed files")
    print_option("3", "Exit", "Close installer")
    
    choice = input(f"\n{Colors.CYAN}➜ Enter your choice (1-3): {Colors.RESET}").strip()
    
    if choice == "1":
        install_dependencies()
        install_ui()
    elif choice == "2":
        uninstall()
    elif choice == "3":
        print(f"{Colors.GREEN}👋 Goodbye!{Colors.RESET}")
        sys.exit(0)
    else:
        print(f"{Colors.RED}❌ Invalid choice!{Colors.RESET}")
        import time
        time.sleep(1)
        main()
        return
    
    print(f"\n{Colors.GREEN}✅ Installation complete!{Colors.RESET}")
    print(f"{Colors.BLUE}📁 Files installed in: ~/.hacker_simulator{Colors.RESET}")
    print(f"{Colors.YELLOW}💡 To run: 'hacker-ui' (Linux/Mac) or check Desktop for shortcut (Windows){Colors.RESET}")
    
    input(f"\n{Colors.CYAN}Press Enter to exit...{Colors.RESET}")

if __name__ == "__main__":
    import time
    main()