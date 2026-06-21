#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - INSTALLER
==================================
Descarga e instala el juego automáticamente desde internet.
"""

import os
import sys
import json
import urllib.request
import subprocess
import platform
import time
import zipfile
import shutil
from pathlib import Path

# ============================================
# COLORES
# ============================================

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_header(text):
    print(f"\n{Colors.CYAN}{'═'*50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{'═'*50}{Colors.RESET}")

# ============================================
# CONFIGURACIÓN
# ============================================

GITHUB_REPO = "DlopedDtorred/hacker-simulator"
GITHUB_API = f"https://api.github.com/repos/{GITHUB_REPO}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main"

INSTALL_DIR = Path.home() / ".hacker_simulator"
GAME_FILE = "hacker_simulator_ui.py"

# ============================================
# DETECTAR SISTEMA
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
# DESCARGA DE ARCHIVOS
# ============================================

def download_file(url, dest):
    """Descarga un archivo con barra de progreso"""
    print(f"{Colors.BLUE}📥 Descargando: {url}{Colors.RESET}")
    
    try:
        response = urllib.request.urlopen(url)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        downloaded = 0
        
        with open(dest, 'wb') as f:
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                downloaded += len(buffer)
                f.write(buffer)
                
                if total_size > 0:
                    percent = int((downloaded / total_size) * 100)
                    bar = "█" * int(percent / 2) + "░" * (50 - int(percent / 2))
                    print(f"\r  [{bar}] {percent}%", end='')
        
        print(f"\n{Colors.GREEN}✅ Descarga completada{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        return False

# ============================================
# INSTALAR DEPENDENCIAS
# ============================================

def install_dependencies():
    """Instala PyQt5 si es necesario"""
    print_header("📦 Instalando dependencias...")
    
    try:
        import PyQt5
        print(f"{Colors.GREEN}✅ PyQt5 ya está instalado{Colors.RESET}")
        return True
    except ImportError:
        print(f"{Colors.YELLOW}⚠️ PyQt5 no está instalado. Instalando...{Colors.RESET}")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "PyQt5"], check=True)
            print(f"{Colors.GREEN}✅ PyQt5 instalado correctamente{Colors.RESET}")
            return True
        except:
            print(f"{Colors.RED}❌ Error al instalar PyQt5{Colors.RESET}")
            return False

# ============================================
# INSTALAR EL JUEGO
# ============================================

def install_game():
    """Descarga e instala el juego"""
    print_header("🖥️ Instalando Hacker Simulator 2077")
    
    # Crear directorio de instalación
    INSTALL_DIR.mkdir(exist_ok=True)
    print(f"{Colors.BLUE}📁 Directorio: {INSTALL_DIR}{Colors.RESET}")
    
    # Descargar el juego
    game_url = f"{GITHUB_RAW}/hacker_simulator_ui.py"
    game_path = INSTALL_DIR / GAME_FILE
    
    print(f"{Colors.YELLOW}⬇️ Descargando el juego...{Colors.RESET}")
    if not download_file(game_url, game_path):
        print(f"{Colors.RED}❌ Error al descargar el juego{Colors.RESET}")
        return False
    
    print(f"{Colors.GREEN}✅ Juego descargado correctamente{Colors.RESET}")
    
    # Instalar dependencias
    install_dependencies()
    
    # Crear script de inicio
    os_name = detect_os()
    
    if os_name == "windows":
        bat_content = f"""@echo off
echo 🚀 HACKER SIMULATOR 2077
echo =========================
echo.
python "{game_path}"
echo.
pause
"""
        bat_path = INSTALL_DIR / "HackerSimulator_UI.bat"
        with open(bat_path, 'w') as f:
            f.write(bat_content)
        print(f"{Colors.GREEN}✅ Script de inicio creado: HackerSimulator_UI.bat{Colors.RESET}")
        
        # Acceso directo en el escritorio (Windows)
        try:
            desktop = Path.home() / "Desktop"
            shortcut = desktop / "HackerSimulator_UI.bat"
            shutil.copy(bat_path, shortcut)
            print(f"{Colors.GREEN}✅ Acceso directo creado en el escritorio{Colors.RESET}")
        except:
            pass
    
    else:  # Linux/Mac
        sh_content = f"""#!/bin/bash
echo "🚀 HACKER SIMULATOR 2077"
echo "========================="
echo
python3 "{game_path}"
echo
read -p "Presiona Enter para salir..."
"""
        sh_path = INSTALL_DIR / "HackerSimulator_UI.sh"
        with open(sh_path, 'w') as f:
            f.write(sh_content)
        sh_path.chmod(0o755)
        print(f"{Colors.GREEN}✅ Script de inicio creado: HackerSimulator_UI.sh{Colors.RESET}")
        
        # Enlace simbólico global
        try:
            symlink = Path("/usr/local/bin/hacker-simulator")
            if symlink.exists():
                symlink.unlink()
            os.symlink(sh_path, symlink)
            print(f"{Colors.GREEN}✅ Comando global 'hacker-simulator' creado{Colors.RESET}")
        except:
            print(f"{Colors.YELLOW}⚠️ No se pudo crear el enlace simbólico (necesitas sudo){Colors.RESET}")
    
    return True

# ============================================
# DESINSTALAR
# ============================================

def uninstall():
    print_header("🗑️ Desinstalando...")
    
    if INSTALL_DIR.exists():
        shutil.rmtree(INSTALL_DIR)
        print(f"{Colors.GREEN}✅ Eliminado: {INSTALL_DIR}{Colors.RESET}")
    
    try:
        if Path("/usr/local/bin/hacker-simulator").exists():
            os.remove("/usr/local/bin/hacker-simulator")
            print(f"{Colors.GREEN}✅ Eliminado enlace simbólico{Colors.RESET}")
    except:
        pass
    
    print(f"{Colors.GREEN}✅ Desinstalación completada{Colors.RESET}")

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
    
    print(f"{Colors.BOLD}Bienvenido al instalador de Hacker Simulator 2077{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}[1]{Colors.RESET} {Colors.WHITE}Instalar juego{Colors.RESET} {Colors.BLUE}(Descarga la última versión){Colors.RESET}")
    print(f"{Colors.YELLOW}[2]{Colors.RESET} {Colors.WHITE}Desinstalar{Colors.RESET} {Colors.BLUE}(Eliminar todos los archivos){Colors.RESET}")
    print(f"{Colors.YELLOW}[3]{Colors.RESET} {Colors.WHITE}Salir{Colors.RESET}")
    
    choice = input(f"\n{Colors.CYAN}➜ Elige una opción (1-3): {Colors.RESET}").strip()
    
    if choice == "1":
        if install_game():
            print(f"\n{Colors.GREEN}{'═'*50}{Colors.RESET}")
            print(f"{Colors.GREEN}✅ ¡Instalación completada con éxito!{Colors.RESET}")
            print(f"{Colors.YELLOW}💡 Para ejecutar el juego:{Colors.RESET}")
            if detect_os() == "windows":
                print(f"   {Colors.CYAN}📁 Busca el acceso directo en el escritorio{Colors.RESET}")
            else:
                print(f"   {Colors.CYAN}📁 Ejecuta: hacker-simulator (Linux/Mac){Colors.RESET}")
                print(f"   {Colors.CYAN}📁 O ve a: {INSTALL_DIR}/HackerSimulator_UI.sh{Colors.RESET}")
            print(f"{Colors.GREEN}{'═'*50}{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Error en la instalación{Colors.RESET}")
    elif choice == "2":
        uninstall()
    elif choice == "3":
        print(f"{Colors.GREEN}👋 ¡Hasta luego!{Colors.RESET}")
        sys.exit(0)
    else:
        print(f"{Colors.RED}❌ Opción inválida{Colors.RESET}")
    
    input(f"\n{Colors.CYAN}Presiona Enter para salir...{Colors.RESET}")

if __name__ == "__main__":
    main()