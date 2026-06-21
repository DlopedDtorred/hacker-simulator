#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - ULTIMATE EDITION v10.1
================================================
Terminal hacking game with arrow key navigation.
"""

import random
import os
import time
import sys
import json
import urllib.request
from datetime import datetime
from colorama import init, Fore, Back, Style

# ============================================
# INITIAL SETUP
# ============================================

init(autoreset=True, convert=True)
os.system('cls' if os.name == 'nt' else 'clear')

VERSION = "10.0.3"
AUTHOR = "DlopedDtorred"
GITHUB_URL = "https://github.com/DlopedDtorred/hacker-simulator"
CONFIG_FILE = "config.json"
SAVE_FILE = "save.json"

# ============================================
# CHECK FOR UPDATES
# ============================================

def check_for_updates():
    """Check if a new version is available on GitHub"""
    try:
        current = VERSION
        url = "https://api.github.com/repos/DlopedDtorred/hacker-simulator/releases/latest"
        req = urllib.request.Request(url, headers={'User-Agent': 'HackerSimulator'})
        response = urllib.request.urlopen(req, timeout=5)
        data = json.loads(response.read().decode())
        latest = data.get("tag_name", current)
        
        if latest != current:
            print(f"\n{Fore.YELLOW}╔═══════════════════════════════════════════╗")
            print(f"║  📦 NEW VERSION AVAILABLE!              ║")
            print(f"║  Current: {current}                        ║")
            print(f"║  Latest:  {latest}                        ║")
            print(f"║  Download: {GITHUB_URL}/releases        ║")
            print(f"╚═══════════════════════════════════════════╝{Style.RESET_ALL}\n")
            time.sleep(1.5)
            return True
        else:
            return False
    except:
        return False

# ============================================
# KEYBOARD INPUT (ARROW KEYS)
# ============================================

def get_key():
    """Get a single key press - works on all platforms"""
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0':
            arrow = msvcrt.getch()
            if arrow == b'H':
                return 'up'
            elif arrow == b'P':
                return 'down'
            elif arrow == b'M':
                return 'right'
            elif arrow == b'K':
                return 'left'
        elif key == b'\r':
            return 'enter'
        elif key == b'\x1b':
            return 'escape'
        else:
            try:
                return key.decode('utf-8').lower()
            except:
                return ''
    else:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(3)
            if ch == '\x1b[A':
                return 'up'
            elif ch == '\x1b[B':
                return 'down'
            elif ch == '\x1b[C':
                return 'right'
            elif ch == '\x1b[D':
                return 'left'
            elif ch == '\r' or ch == '\n':
                return 'enter'
            elif ch == '\x1b':
                return 'escape'
            else:
                return ch.strip().lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

def select_with_arrows(options, title="", lang="es"):
    """Select an option using arrow keys"""
    selected = 0
    text = get_text(lang)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_header()
        
        if title:
            print(f"\n{Fore.CYAN}{title}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        for i, option in enumerate(options):
            if i == selected:
                print(f"{Fore.GREEN}▶ {option}{Style.RESET_ALL}")
            else:
                print(f"  {option}")
        
        print(f"\n{Fore.YELLOW}↑ ↓ Navigate | Enter Select{Style.RESET_ALL}")
        
        key = get_key()
        if key == 'up':
            selected = (selected - 1) % len(options)
        elif key == 'down':
            selected = (selected + 1) % len(options)
        elif key == 'enter':
            return selected
        elif key == 'escape':
            return -1

# ============================================
# LANGUAGE SYSTEM
# ============================================

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        return None

def save_config(language, name="Zero_Cool"):
    config = {
        "language": language,
        "name": name,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def first_time_setup():
    """First-time setup - only appears once"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║  {Fore.YELLOW}🌍 WELCOME TO HACKER SIMULATOR 2077{Fore.CYAN}                      ║
{Fore.CYAN}║  {Fore.WHITE}First-time setup - Let's configure your profile{Fore.CYAN}           ║
{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """)
    
    print(f"\n{Fore.CYAN}📝 Select your language / Selecciona tu idioma:{Style.RESET_ALL}")
    lang_options = ["🇪🇸 Español", "🇬🇧 English"]
    lang_idx = select_with_arrows(lang_options, "", "es")
    if lang_idx == -1:
        lang_idx = 0
    language = "es" if lang_idx == 0 else "en"
    
    print(f"\n{Fore.CYAN}👤 Enter your hacker name / Introduce tu nombre:{Style.RESET_ALL}")
    name = input("➡️  ").strip() or "Zero_Cool"
    
    save_config(language, name)
    
    print(f"\n{Fore.GREEN}✅ Configuration saved! / Configuración guardada!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✅ Welcome / Bienvenido, {name}!{Style.RESET_ALL}")
    time.sleep(1.5)
    
    return language, name

def get_text(lang="es"):
    if lang == "es":
        return TEXTO_ES
    else:
        return TEXTO_EN

# ============================================
# TEXT DICTIONARIES
# ============================================

TEXTO_ES = {
    "menu_hack": "🌐 Hackear servidor",
    "menu_daily": "📅 Misión diaria (¡DOBLE!)",
    "menu_train": "🛠️ Entrenar",
    "menu_shop": "🛒 Tienda",
    "menu_stats": "📊 Estadísticas",
    "menu_ranking": "🏆 Ranking",
    "menu_settings": "⚙️ Ajustes",
    "menu_save": "💾 Guardar partida",
    "menu_guide": "📖 Guía",
    "menu_exit": "🚪 Salir",
    
    "settings": "⚙️ AJUSTES",
    "change_theme": "🎨 Cambiar tema",
    "change_language": "🌍 Cambiar idioma",
    "delete_account": "🗑️ ELIMINAR CUENTA",
    "back": "🔙 Volver",
    "themes": "🎨 SELECCIONAR TEMA",
    "current_theme": "Tema actual: {}",
    "language_changed": "✅ Idioma cambiado. Reinicia el juego para aplicar.",
    "theme_changed": "✅ Tema cambiado a: {}",
    
    "delete_warning": "⚠️ ¡ADVERTENCIA! Esto ELIMINARÁ PERMANENTEMENTE todos tus datos.",
    "confirm_delete": "¿Estás SEGURO? (escribe 'ELIMINAR' para confirmar): ",
    "deleted": "🗑️ Cuenta eliminada permanentemente.",
    "delete_cancelled": "❌ Eliminación cancelada.",
    
    "welcome": "👤 Bienvenido al mundo del hacking digital.",
    "connection": "✅ Conexión establecida. ¡Bienvenido, {}!",
    "guide_hint": "💡 Escribe '9' para la guía.",
    "goodbye": "👋 ¡Hasta luego, {}!",
    "error": "❌ Error: {}",
    "saved": "✅ Partida guardada",
    "save_error": "❌ Error al guardar",
    "invalid": "❌ Opción inválida",
    "no_credits": "❌ Sin créditos",
    "purchased": "✅ ¡Comprado!",
    "already_have": "⚠️ Ya la tienes",
    
    "servers": "🌐 SERVIDORES DISPONIBLES:",
    "max_level": "💡 Nivel máx: {}",
    "choose_server": "➡️ Elige: ",
    "mission": "🎯 MISIÓN: HACKEAR {}",
    "id": "📋 ID: {}",
    "difficulty": "⭐ Dificultad: {} ★",
    "reward": "💰 Recompensa: {} créditos",
    "desc": "📝 {}",
    "clue": "🔍 PISTA: {}",
    "phase1": "🛡️ FASE 1: ELUDIR FIREWALL",
    "phase2": "🔑 FASE 2: DESCIFRAR CONTRASEÑA",
    "phase3": "🕵️ FASE 3: SEGURIDAD EXTRA",
    "firewall_detected": "🔥 ¡FIREWALL DETECTADO! Memoriza la secuencia:",
    "attempts": "🛡️ Tienes {} intentos",
    "memorize": "🧠 Memoriza... tienes 2 segundos",
    "repeat": "⌨️ Repite la secuencia (números separados por espacio):",
    "firewall_passed": "✅ ¡Firewall evadido!",
    "firewall_failed": "❌ Incorrecto.",
    "firewall_detected2": "💀 Has sido detectado.",
    "attempts_left": "🔐 Intentos: {}",
    "help_hint": "💡 Escribe 'help' para pista extra",
    "password_correct": "✅ ¡Acceso concedido!",
    "password_incorrect": "❌ Incorrecto.",
    "password_failed": "💀 Fallaste.",
    "real_password": "🔑 Contraseña: {}",
    "mission_failed": "💀 Misión fallida.",
    "mission_complete": "🎉 ¡MISIÓN COMPLETADA!",
    "reward_total": "💰 +{} créditos",
    "exp_total": "📈 +{} EXP",
    "streak_bonus": "🔥 Bonus racha: +{} créditos",
    "streak_current": "🔥 ¡Racha de {}!",
    "extra_protection": "⚠️ Protección adicional...",
    "discovered": "💀 Descubierto.",
    
    "daily_mission": "📅 MISIÓN DIARIA",
    "already_done": "⚠️ Ya completaste la de hoy.",
    "today_mission": "🌟 Misión de hoy:",
    "double_reward": "💰 Recompensa: {} créditos (¡DOBLE!)",
    "daily_complete": "🎉 ¡MISIÓN DIARIA COMPLETADA!",
    
    "shop": "🛒 TIENDA DE HERRAMIENTAS",
    "your_tools": "🛠️ Tus herramientas: {}",
    "buy_exp": "💰 Comprar EXP (100 créditos = 10 EXP)",
    "exit_shop": "🚪 Salir",
    "exp_gained": "✅ +10 EXP",
    
    "stats": "📊 ESTADÍSTICAS DE {}",
    "progress": "📈 Progreso:",
    "level": "  • Nivel: {}",
    "exp_current": "  • EXP: {}/{}",
    "rank": "  • Rango: {}",
    "resources": "💰 Recursos:",
    "credits_current": "  • Créditos: {}",
    "tools_count": "  • Herramientas: {}",
    "missions_stats": "🎯 Misiones:",
    "completed": "  • Completadas: {}",
    "failed": "  • Fallidas: {}",
    "streak_current2": "  • Racha actual: {}",
    "best_streak2": "  • Mejor racha: {}",
    "unique_servers": "  • Servidores únicos: {}/{}",
    "hacked_servers": "🖥️ Servidores hackeados:",
    "none": "  • Ninguno",
    "achievements": "🏆 Logros ({}/{}):",
    "no_achievements": "  • Ninguno",
    
    "ranking": "🏆 RANKING DE HACKERS",
    "position": "Posición │ Hacker │ Nivel │ Misiones",
    "rank_up": "💡 Completa misiones para subir.",
    
    "training": "🛠️ ENTRENAMIENTO",
    "firewall": "Firewall",
    "cryptography": "Criptografía",
    "sql": "SQL Injection",
    "puzzles": "Puzzles",
    "keep_practicing": "💪 Sigue practicando",
    
    "guide": "📖 GUÍA DE USUARIO",
    "guide_text": """
🎯 ¿QUÉ ES?
Un juego de hacking en terminal. Hackea servidores, evita firewalls
y descifra contraseñas usando pistas.

🕹️ CONTROLES
↑↓ - Navegar con flechas
Enter - Seleccionar
1 - Hackear servidor
2 - Misión diaria (DOBLE recompensa)
3 - Entrenar
4 - Tienda
5 - Estadísticas
6 - Ranking
7 - Ajustes
8 - Guardar partida
9 - Guía de usuario
0 - Salir

💡 CONSEJOS
• Las pistas son CLAVE para descifrar contraseñas
• Compra herramientas en la tienda
• Mantén la racha para bonificaciones
• Misiones diarias = DOBLE recompensa
• Los logros dan créditos extra

⚡ TECNOLOGÍAS
• Python 3.8+
• Colorama (colores)
• JSON (guardado)

🔗 ENLACES
• GitHub: {}
• Issues: {}/issues

🙏 ¡GRACIAS POR JUGAR!
""",
}

TEXTO_EN = {
    "menu_hack": "🌐 Hack server",
    "menu_daily": "📅 Daily mission (DOUBLE!)",
    "menu_train": "🛠️ Train",
    "menu_shop": "🛒 Shop",
    "menu_stats": "📊 Statistics",
    "menu_ranking": "🏆 Ranking",
    "menu_settings": "⚙️ Settings",
    "menu_save": "💾 Save game",
    "menu_guide": "📖 Guide",
    "menu_exit": "🚪 Exit",
    
    "settings": "⚙️ SETTINGS",
    "change_theme": "🎨 Change theme",
    "change_language": "🌍 Change language",
    "delete_account": "🗑️ DELETE ACCOUNT",
    "back": "🔙 Back",
    "themes": "🎨 SELECT THEME",
    "current_theme": "Current theme: {}",
    "language_changed": "✅ Language changed. Restart the game to apply.",
    "theme_changed": "✅ Theme changed to: {}",
    
    "delete_warning": "⚠️ WARNING! This will PERMANENTLY DELETE all your data.",
    "confirm_delete": "Are you SURE? (type 'DELETE' to confirm): ",
    "deleted": "🗑️ Account permanently deleted.",
    "delete_cancelled": "❌ Deletion cancelled.",
    
    "welcome": "👤 Welcome to the world of digital hacking.",
    "connection": "✅ Connection established. Welcome, {}!",
    "guide_hint": "💡 Type '9' for the guide.",
    "goodbye": "👋 Goodbye, {}!",
    "error": "❌ Error: {}",
    "saved": "✅ Game saved",
    "save_error": "❌ Error saving",
    "invalid": "❌ Invalid option",
    "no_credits": "❌ Not enough credits",
    "purchased": "✅ Purchased!",
    "already_have": "⚠️ You already have it",
    
    "servers": "🌐 AVAILABLE SERVERS:",
    "max_level": "💡 Max level: {}",
    "choose_server": "➡️ Choose: ",
    "mission": "🎯 MISSION: HACK {}",
    "id": "📋 ID: {}",
    "difficulty": "⭐ Difficulty: {} ★",
    "reward": "💰 Reward: {} credits",
    "desc": "📝 {}",
    "clue": "🔍 CLUE: {}",
    "phase1": "🛡️ PHASE 1: EVADE FIREWALL",
    "phase2": "🔑 PHASE 2: CRACK PASSWORD",
    "phase3": "🕵️ PHASE 3: EXTRA SECURITY",
    "firewall_detected": "🔥 FIREWALL DETECTED! Memorize the sequence:",
    "attempts": "🛡️ You have {} attempts",
    "memorize": "🧠 Memorize... you have 2 seconds",
    "repeat": "⌨️ Repeat the sequence (numbers separated by space):",
    "firewall_passed": "✅ Firewall evaded!",
    "firewall_failed": "❌ Incorrect.",
    "firewall_detected2": "💀 You've been detected.",
    "attempts_left": "🔐 Attempts: {}",
    "help_hint": "💡 Type 'help' for extra clue",
    "password_correct": "✅ Access granted!",
    "password_incorrect": "❌ Incorrect.",
    "password_failed": "💀 You failed.",
    "real_password": "🔑 Password: {}",
    "mission_failed": "💀 Mission failed.",
    "mission_complete": "🎉 MISSION COMPLETED!",
    "reward_total": "💰 +{} credits",
    "exp_total": "📈 +{} EXP",
    "streak_bonus": "🔥 Streak bonus: +{} credits",
    "streak_current": "🔥 {} streak!",
    "extra_protection": "⚠️ Extra protection...",
    "discovered": "💀 Discovered.",
    
    "daily_mission": "📅 DAILY MISSION",
    "already_done": "⚠️ You already completed today's mission.",
    "today_mission": "🌟 Today's mission:",
    "double_reward": "💰 Reward: {} credits (DOUBLE!)",
    "daily_complete": "🎉 DAILY MISSION COMPLETED!",
    
    "shop": "🛒 TOOL SHOP",
    "your_tools": "🛠️ Your tools: {}",
    "buy_exp": "💰 Buy EXP (100 credits = 10 EXP)",
    "exit_shop": "🚪 Exit",
    "exp_gained": "✅ +10 EXP",
    
    "stats": "📊 STATISTICS OF {}",
    "progress": "📈 Progress:",
    "level": "  • Level: {}",
    "exp_current": "  • EXP: {}/{}",
    "rank": "  • Rank: {}",
    "resources": "💰 Resources:",
    "credits_current": "  • Credits: {}",
    "tools_count": "  • Tools: {}",
    "missions_stats": "🎯 Missions:",
    "completed": "  • Completed: {}",
    "failed": "  • Failed: {}",
    "streak_current2": "  • Current streak: {}",
    "best_streak2": "  • Best streak: {}",
    "unique_servers": "  • Unique servers: {}/{}",
    "hacked_servers": "🖥️ Hacked servers:",
    "none": "  • None",
    "achievements": "🏆 Achievements ({}/{}):",
    "no_achievements": "  • None",
    
    "ranking": "🏆 HACKER RANKING",
    "position": "Position │ Hacker │ Level │ Missions",
    "rank_up": "💡 Complete missions to rank up.",
    
    "training": "🛠️ TRAINING",
    "firewall": "Firewall",
    "cryptography": "Cryptography",
    "sql": "SQL Injection",
    "puzzles": "Puzzles",
    "keep_practicing": "💪 Keep practicing",
    
    "guide": "📖 USER GUIDE",
    "guide_text": """
🎯 WHAT IS IT?
A terminal hacking game. Hack servers, evade firewalls
and crack passwords using clues.

🕹️ CONTROLS
↑↓ - Navigate with arrows
Enter - Select
1 - Hack server
2 - Daily mission (DOUBLE reward)
3 - Train
4 - Shop
5 - Statistics
6 - Ranking
7 - Settings
8 - Save game
9 - User guide
0 - Exit

💡 TIPS
• Clues are KEY to cracking passwords
• Buy tools from the shop
• Keep your streak for bonuses
• Daily missions = DOUBLE reward
• Achievements give extra credits

⚡ TECHNOLOGIES
• Python 3.8+
• Colorama (colors)
• JSON (save)

🔗 LINKS
• GitHub: {}
• Issues: {}/issues

🙏 THANKS FOR PLAYING!
""",
}

# ============================================
# THEME SYSTEM
# ============================================

THEMES = {
    "matrix": {"primary": Fore.GREEN, "secondary": Fore.LIGHTGREEN_EX, "text": Fore.WHITE, "success": Fore.GREEN, "error": Fore.RED, "warning": Fore.YELLOW, "info": Fore.CYAN},
    "cyberpunk": {"primary": Fore.MAGENTA, "secondary": Fore.LIGHTMAGENTA_EX, "text": Fore.WHITE, "success": Fore.GREEN, "error": Fore.RED, "warning": Fore.YELLOW, "info": Fore.BLUE},
    "classic": {"primary": Fore.BLUE, "secondary": Fore.LIGHTBLUE_EX, "text": Fore.WHITE, "success": Fore.GREEN, "error": Fore.RED, "warning": Fore.YELLOW, "info": Fore.CYAN},
    "dark": {"primary": Fore.LIGHTBLACK_EX, "secondary": Fore.WHITE, "text": Fore.WHITE, "success": Fore.GREEN, "error": Fore.RED, "warning": Fore.YELLOW, "info": Fore.CYAN}
}

def get_theme(name):
    return THEMES.get(name, THEMES["matrix"])

# ============================================
# DATA - 20 SERVERS
# ============================================

SERVERS = [
    {"id": "SRV-001", "name": "MegaCorp Alpha", "difficulty": 1, "reward": 150,
     "clue_es": "🐱 El gato del CEO se llama 'Michi' con 'fu' al final",
     "clue_en": "🐱 The CEO's cat is named 'Michi' with 'fu' at the end",
     "password": "michifu", "desc_es": "Servidor corporativo básico", "desc_en": "Basic corporate server"},
    {"id": "SRV-002", "name": "DarkNet Vault", "difficulty": 2, "reward": 250,
     "clue_es": "👿 El número de la bestia sin el 6 final (tres dígitos)",
     "clue_en": "👿 The number of the beast without the final 6 (three digits)",
     "password": "666", "desc_es": "Custodia en red oscura", "desc_en": "Dark web custody"},
    {"id": "SRV-003", "name": "ShadowNet", "difficulty": 2, "reward": 300,
     "clue_es": "🏢 Fundado en el año del estreno de 'El Hobbit' (2015)",
     "clue_en": "🏢 Founded in the year 'The Hobbit' premiered (2015)",
     "password": "2015", "desc_es": "Red de datos sombra", "desc_en": "Shadow data network"},
    {"id": "SRV-004", "name": "CyberDyne Systems", "difficulty": 3, "reward": 400,
     "clue_es": "🎬 Blade Runner se estrenó en 2019 (año de la película)",
     "clue_en": "🎬 Blade Runner was released in 2019 (the movie year)",
     "password": "2019", "desc_es": "Sistemas de IA", "desc_en": "AI systems"},
    {"id": "SRV-005", "name": "NeoTokyo Grid", "difficulty": 4, "reward": 600,
     "clue_es": "🇯🇵 Código postal de Shibuya: 150-0042 (sin guión)",
     "clue_en": "🇯🇵 Shibuya postal code: 150-0042 (without dash)",
     "password": "1500042", "desc_es": "Red de ciudad digital", "desc_en": "Digital city network"},
    {"id": "SRV-006", "name": "A.I. Core", "difficulty": 5, "reward": 1000,
     "clue_es": "🔢 Fibonacci: 1,1,2,3,5,8,13... el número en la posición 13 es 233",
     "clue_en": "🔢 Fibonacci: 1,1,2,3,5,8,13... the number at position 13 is 233",
     "password": "233", "desc_es": "Núcleo de IA", "desc_en": "AI Core"},
    {"id": "SRV-007", "name": "Quantum Nexus", "difficulty": 6, "reward": 1500,
     "clue_es": "⚛️ Constante de Planck: 6.626... (primeros 3 dígitos: 662)",
     "clue_en": "⚛️ Planck constant: 6.626... (first 3 digits: 662)",
     "password": "662", "desc_es": "Servidor cuántico", "desc_en": "Quantum server"},
    {"id": "SRV-008", "name": "NanoTech Labs", "difficulty": 7, "reward": 2000,
     "clue_es": "🔬 El carbono es el elemento número 6 de la tabla periódica",
     "clue_en": "🔬 Carbon is element number 6 on the periodic table",
     "password": "6", "desc_es": "Laboratorio nanotecnológico", "desc_en": "Nanotech lab"},
    {"id": "SRV-009", "name": "Matrix Archive", "difficulty": 8, "reward": 3000,
     "clue_es": "🎬 La habitación de Neo en 'The Matrix' es la 303",
     "clue_en": "🎬 Neo's room in 'The Matrix' is 303",
     "password": "303", "desc_es": "Archivo de la resistencia", "desc_en": "Resistance archive"},
    {"id": "SRV-010", "name": "ChronoCore", "difficulty": 9, "reward": 5000,
     "clue_es": "⏳ El ADN fue descubierto en 1953",
     "clue_en": "⏳ DNA was discovered in 1953",
     "password": "1953", "desc_es": "Base de datos temporal", "desc_en": "Temporal database"},
    {"id": "SRV-011", "name": "Omega Station", "difficulty": 10, "reward": 10000,
     "clue_es": "☯️ 666 (número de la bestia) × 7 (número de la suerte) = 4662",
     "clue_en": "☯️ 666 (number of the beast) × 7 (lucky number) = 4662",
     "password": "4662", "desc_es": "El servidor definitivo", "desc_en": "The ultimate server"},
    {"id": "SRV-012", "name": "Void Network", "difficulty": 9, "reward": 4500,
     "clue_es": "🔮 7 (número de la suerte) elevado al cubo = 343",
     "clue_en": "🔮 7 (lucky number) cubed = 343",
     "password": "343", "desc_es": "Red en el vacío digital", "desc_en": "Digital void network"},
    {"id": "SRV-013", "name": "Eclipse Core", "difficulty": 11, "reward": 15000,
     "clue_es": "🌑 El primer eclipse total del siglo XXI fue en 2001",
     "clue_en": "🌑 The first total eclipse of the 21st century was in 2001",
     "password": "2001", "desc_es": "Núcleo de la sombra", "desc_en": "Shadow core"},
    {"id": "SRV-014", "name": "Nebula Archive", "difficulty": 12, "reward": 20000,
     "clue_es": "🌌 El código postal de la NASA es 77058 (Texas)",
     "clue_en": "🌌 NASA's zip code is 77058 (Texas)",
     "password": "77058", "desc_es": "Archivo espacial", "desc_en": "Space archive"},
    {"id": "SRV-015", "name": "Genesis Point", "difficulty": 13, "reward": 30000,
     "clue_es": "🌀 La primera computadora electrónica fue creada en 1941",
     "clue_en": "🌀 The first electronic computer was created in 1941",
     "password": "1941", "desc_es": "El origen de todo", "desc_en": "The origin of everything"},
    {"id": "SRV-016", "name": "Apollo Core", "difficulty": 14, "reward": 40000,
     "clue_es": "🚀 El primer alunizaje fue en 1969 (Apolo 11)",
     "clue_en": "🚀 The first moon landing was in 1969 (Apollo 11)",
     "password": "1969", "desc_es": "Núcleo de la misión Apolo", "desc_en": "Apollo mission core"},
    {"id": "SRV-017", "name": "Digital Abyss", "difficulty": 15, "reward": 50000,
     "clue_es": "🌊 La fosa de las Marianas mide 11.034 metros de profundidad",
     "clue_en": "🌊 The Mariana Trench is 11,034 meters deep",
     "password": "11034", "desc_es": "El abismo digital", "desc_en": "The digital abyss"},
    {"id": "SRV-018", "name": "Phoenix Protocol", "difficulty": 16, "reward": 75000,
     "clue_es": "🔥 La serie de Phoenix resurgió en 2002",
     "clue_en": "🔥 The Phoenix series was revived in 2002",
     "password": "2002", "desc_es": "Protocolo de resurrección", "desc_en": "Resurrection protocol"},
    {"id": "SRV-019", "name": "Eternal Archive", "difficulty": 18, "reward": 100000,
     "clue_es": "∞ El símbolo del infinito es un 8 acostado",
     "clue_en": "∞ The infinity symbol is a sideways 8",
     "password": "8", "desc_es": "Archivo eterno", "desc_en": "Eternal archive"},
    {"id": "SRV-020", "name": "Omega Point", "difficulty": 20, "reward": 200000,
     "clue_es": "☯️ 666 × 666 = 443556",
     "clue_en": "☯️ 666 × 666 = 443556",
     "password": "443556", "desc_es": "El punto final de todo", "desc_en": "The final point"}
]

# ============================================
# ACHIEVEMENTS
# ============================================

ACHIEVEMENTS = {
    "first_hack": {"name_es": "🚀 Primer Hackeo", "name_en": "🚀 First Hack", "desc_es": "Completa tu primera misión", "desc_en": "Complete your first mission", "reward": 50},
    "five_missions": {"name_es": "💪 Cinco Misiones", "name_en": "💪 Five Missions", "desc_es": "Completa 5 misiones", "desc_en": "Complete 5 missions", "reward": 100},
    "ten_missions": {"name_es": "🏆 Diez Misiones", "name_en": "🏆 Ten Missions", "desc_es": "Completa 10 misiones", "desc_en": "Complete 10 missions", "reward": 200},
    "twenty_five": {"name_es": "👑 Leyenda", "name_en": "👑 Legend", "desc_es": "Completa 25 misiones", "desc_en": "Complete 25 missions", "reward": 500},
    "fifty_missions": {"name_es": "🌟 Maestro", "name_en": "🌟 Master", "desc_es": "Completa 50 misiones", "desc_en": "Complete 50 missions", "reward": 1000},
    "hundred_missions": {"name_es": "💎 Dios", "name_en": "💎 God", "desc_es": "Completa 100 misiones", "desc_en": "Complete 100 missions", "reward": 5000},
    "level_5": {"name_es": "⚡ Nivel 5", "name_en": "⚡ Level 5", "desc_es": "Alcanza el nivel 5", "desc_en": "Reach level 5", "reward": 150},
    "level_10": {"name_es": "🌟 Nivel 10", "name_en": "🌟 Level 10", "desc_es": "Alcanza el nivel 10", "desc_en": "Reach level 10", "reward": 300},
    "level_15": {"name_es": "👑 Nivel 15", "name_en": "👑 Level 15", "desc_es": "Alcanza el nivel 15", "desc_en": "Reach level 15", "reward": 500},
    "level_20": {"name_es": "💎 Nivel 20", "name_en": "💎 Level 20", "desc_es": "Alcanza el nivel 20", "desc_en": "Reach level 20", "reward": 1000},
    "level_30": {"name_es": "🔥 Nivel 30", "name_en": "🔥 Level 30", "desc_es": "Alcanza el nivel 30", "desc_en": "Reach level 30", "reward": 5000},
    "millionaire": {"name_es": "💰 Millonario", "name_en": "💰 Millionaire", "desc_es": "Acumula 1000 créditos", "desc_en": "Accumulate 1000 credits", "reward": 100},
    "billionaire": {"name_es": "💎 Billonario", "name_en": "💎 Billionaire", "desc_es": "Acumula 5000 créditos", "desc_en": "Accumulate 5000 credits", "reward": 300},
    "trillionaire": {"name_es": "👑 Trillonario", "name_en": "👑 Trillionaire", "desc_es": "Acumula 10000 créditos", "desc_en": "Accumulate 10000 credits", "reward": 500},
    "multi_millionaire": {"name_es": "💸 Multimillonario", "name_en": "💸 Multi-millionaire", "desc_es": "Acumula 50000 créditos", "desc_en": "Accumulate 50000 credits", "reward": 2000},
    "perfect": {"name_es": "🎯 Perfecto", "name_en": "🎯 Perfect", "desc_es": "Completa 5 misiones sin fallar", "desc_en": "Complete 5 missions without failing", "reward": 200},
    "streak_5": {"name_es": "🔥 Racha 5", "name_en": "🔥 Streak 5", "desc_es": "5 misiones seguidas", "desc_en": "5 missions in a row", "reward": 100},
    "streak_10": {"name_es": "🔥🔥 Racha 10", "name_en": "🔥🔥 Streak 10", "desc_es": "10 misiones seguidas", "desc_en": "10 missions in a row", "reward": 200},
    "streak_20": {"name_es": "🔥🔥🔥 Racha 20", "name_en": "🔥🔥🔥 Streak 20", "desc_es": "20 misiones seguidas", "desc_en": "20 missions in a row", "reward": 500},
    "streak_50": {"name_es": "🔥🔥🔥🔥 Racha 50", "name_en": "🔥🔥🔥🔥 Streak 50", "desc_es": "50 misiones seguidas", "desc_en": "50 missions in a row", "reward": 2000},
    "collector": {"name_es": "🛠️ Coleccionista", "name_en": "🛠️ Collector", "desc_es": "Todas las herramientas", "desc_en": "All tools", "reward": 500},
    "omega": {"name_es": "☯️ Omega", "name_en": "☯️ Omega", "desc_es": "Completa Omega Station", "desc_en": "Complete Omega Station", "reward": 1000},
    "legend": {"name_es": "⚡ Leyenda", "name_en": "⚡ Legend", "desc_es": "Completa todos los servidores", "desc_en": "Complete all servers", "reward": 5000},
    "god": {"name_es": "👑 Dios", "name_en": "👑 God", "desc_es": "Completa Omega Point", "desc_en": "Complete Omega Point", "reward": 10000},
    "explorer": {"name_es": "🧭 Explorador", "name_en": "🧭 Explorer", "desc_es": "Hackea 10 servidores diferentes", "desc_en": "Hack 10 different servers", "reward": 300}
}

# ============================================
# HACKER CLASS
# ============================================

class Hacker:
    def __init__(self, name="Zero_Cool"):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_needed = 10
        self.credits = 50
        self.tools = ["🔧 Basic Scanner"]
        self.missions_completed = 0
        self.failures = 0
        self.current_streak = 0
        self.best_streak = 0
        self.hacked_servers = []
        self.unlocked_achievements = []
        self.current_theme = "matrix"
        self.last_mission = None
        self.daily_done = False
        self.last_daily = None
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= self.exp_needed:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_needed = self.level * 15
        print(f"\n{Fore.MAGENTA}{'═'*50}")
        print(f"🌟 YOU REACHED LEVEL {self.level}! 🌟")
        print(f"{'═'*50}{Style.RESET_ALL}")
        if self.level % 2 == 0:
            self._give_tool()
        if self.level % 3 == 0:
            bonus = self.level * 50
            self.credits += bonus
            print(f"{Fore.GREEN}💰 Level bonus: +{bonus} credits{Style.RESET_ALL}")
        if self.level % 5 == 0:
            print(f"{Fore.YELLOW}🎁 Special level {self.level} reward!{Style.RESET_ALL}")
            self.credits += 200
            if self.level % 10 == 0:
                self.credits += 500
                print(f"{Fore.CYAN}🌟 EXTRA 500 CREDITS!{Style.RESET_ALL}")
    
    def _give_tool(self):
        tools = ["🔧 Advanced Scanner", "🛡️ Firewall Bypass", "🔑 Crypto Key",
                "⚡ Quantum Decryptor", "🔬 Nano Analyzer", "🎯 Matrix Key",
                "⏳ Chrono Analyzer", "☯️ Omega Key", "🌀 Void Key"]
        idx = (self.level // 2 - 1) % len(tools)
        new_tool = tools[idx]
        if new_tool not in self.tools:
            self.tools.append(new_tool)
            print(f"{Fore.CYAN}🔧 New tool: {new_tool}!{Style.RESET_ALL}")
    
    def check_achievements(self, lang="es"):
        new = []
        if self.missions_completed >= 1 and "first_hack" not in self.unlocked_achievements: new.append("first_hack")
        if self.missions_completed >= 5 and "five_missions" not in self.unlocked_achievements: new.append("five_missions")
        if self.missions_completed >= 10 and "ten_missions" not in self.unlocked_achievements: new.append("ten_missions")
        if self.missions_completed >= 25 and "twenty_five" not in self.unlocked_achievements: new.append("twenty_five")
        if self.missions_completed >= 50 and "fifty_missions" not in self.unlocked_achievements: new.append("fifty_missions")
        if self.missions_completed >= 100 and "hundred_missions" not in self.unlocked_achievements: new.append("hundred_missions")
        if self.level >= 5 and "level_5" not in self.unlocked_achievements: new.append("level_5")
        if self.level >= 10 and "level_10" not in self.unlocked_achievements: new.append("level_10")
        if self.level >= 15 and "level_15" not in self.unlocked_achievements: new.append("level_15")
        if self.level >= 20 and "level_20" not in self.unlocked_achievements: new.append("level_20")
        if self.level >= 30 and "level_30" not in self.unlocked_achievements: new.append("level_30")
        if self.credits >= 1000 and "millionaire" not in self.unlocked_achievements: new.append("millionaire")
        if self.credits >= 5000 and "billionaire" not in self.unlocked_achievements: new.append("billionaire")
        if self.credits >= 10000 and "trillionaire" not in self.unlocked_achievements: new.append("trillionaire")
        if self.credits >= 50000 and "multi_millionaire" not in self.unlocked_achievements: new.append("multi_millionaire")
        if self.best_streak >= 5 and "streak_5" not in self.unlocked_achievements: new.append("streak_5")
        if self.best_streak >= 10 and "streak_10" not in self.unlocked_achievements: new.append("streak_10")
        if self.best_streak >= 20 and "streak_20" not in self.unlocked_achievements: new.append("streak_20")
        if self.best_streak >= 50 and "streak_50" not in self.unlocked_achievements: new.append("streak_50")
        if self.missions_completed >= 5 and self.failures == 0 and "perfect" not in self.unlocked_achievements: new.append("perfect")
        if len(self.tools) >= 9 and "collector" not in self.unlocked_achievements: new.append("collector")
        if "Omega Station" in self.hacked_servers and "omega" not in self.unlocked_achievements: new.append("omega")
        if len(set(self.hacked_servers)) >= 10 and "explorer" not in self.unlocked_achievements: new.append("explorer")
        if len(set(self.hacked_servers)) >= len(SERVERS) and "legend" not in self.unlocked_achievements: new.append("legend")
        if "Omega Point" in self.hacked_servers and "god" not in self.unlocked_achievements: new.append("god")
        
        for ach_id in new:
            self.unlocked_achievements.append(ach_id)
            ach = ACHIEVEMENTS[ach_id]
            name = ach.get(f"name_{lang}", ach.get("name_es", ach_id))
            desc = ach.get(f"desc_{lang}", ach.get("desc_es", ""))
            print(f"{Fore.YELLOW}🏆 ACHIEVEMENT: {name}!{Style.RESET_ALL}")
            print(f"{Fore.WHITE}   📝 {desc}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}   💰 +{ach['reward']} credits{Style.RESET_ALL}")
            self.credits += ach['reward']
    
    def get_rank(self):
        if self.level >= 25: return "👑 LEGENDARY HACKER"
        elif self.level >= 20: return "⚡ ELITE HACKER"
        elif self.level >= 15: return "🔥 SENIOR HACKER"
        elif self.level >= 10: return "💻 JUNIOR HACKER"
        elif self.level >= 5: return "🔰 APPRENTICE"
        else: return "🐣 NOVICE"
    
    def save_game(self):
        data = {"name": self.name, "level": self.level, "exp": self.exp, "exp_needed": self.exp_needed,
                "credits": self.credits, "tools": self.tools, "missions_completed": self.missions_completed,
                "failures": self.failures, "current_streak": self.current_streak, "best_streak": self.best_streak,
                "hacked_servers": self.hacked_servers, "unlocked_achievements": self.unlocked_achievements,
                "current_theme": self.current_theme, "last_mission": self.last_mission,
                "daily_done": self.daily_done, "last_daily": self.last_daily, "created_date": self.created_date}
        try:
            with open(SAVE_FILE, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except:
            return False
    
    def load_game(self):
        try:
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            return True
        except:
            return False
    
    def delete_account(self):
        try:
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            return True
        except:
            return False
    
    def __str__(self):
        theme = get_theme(self.current_theme)
        bar = "█" * int((self.exp / self.exp_needed) * 15) if self.exp_needed > 0 else ""
        empty = "░" * (15 - len(bar))
        return f"""
{theme['primary']}╔══════════════════════════════════════════════════════════╗
{theme['primary']}║ {theme['text']}👤 {self.name} {theme['primary']}│ {theme['success']}Lv.{self.level} {theme['primary']}│ {theme['warning']}💰 {self.credits} credits
{theme['primary']}║ {theme['text']}📊 EXP [{bar}{empty}] {self.exp}/{self.exp_needed}
{theme['primary']}║ {theme['text']}🏆 {self.get_rank()}
{theme['primary']}║ {theme['text']}🛠️  {', '.join(self.tools)}
{theme['primary']}║ {theme['text']}📈 Streaks: {self.current_streak} now │ {self.best_streak} best
{theme['primary']}║ {theme['text']}🎯 Missions: {self.missions_completed} │ ❌ Failures: {self.failures}
{theme['primary']}║ {theme['text']}🗺️  Unique: {len(set(self.hacked_servers))}/{len(SERVERS)}
{theme['primary']}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

# ============================================
# MINI-GAMES
# ============================================

class MiniGames:
    @staticmethod
    def firewall_memory(difficulty, max_attempts, lang="es"):
        text = get_text(lang)
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔥 {text['firewall_detected']}")
        print(f"{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{text['attempts'].format(max_attempts)}{Style.RESET_ALL}")
        length = min(3 + difficulty // 2, 8)
        sequence = [str(random.randint(1, 9)) for _ in range(length)]
        for attempt in range(max_attempts):
            print(f"\n{Fore.CYAN}🧠 Attempt {attempt+1}/{max_attempts}:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}╔{'═' * (length * 2 + 2)}╗")
            print(f"║ {' '.join(sequence)} ║")
            print(f"╚{'═' * (length * 2 + 2)}╝{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}⏳ {text['memorize']}{Style.RESET_ALL}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.CYAN}⌨️  {text['repeat']}{Style.RESET_ALL}")
            answer = input("➡️  ").strip().split()
            if answer == sequence:
                print(f"{Fore.GREEN}✅ {text['firewall_passed']}{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}❌ {text['firewall_failed']}{Style.RESET_ALL}")
                if attempt < max_attempts - 1:
                    print(f"{Fore.YELLOW}💡 The sequence was: {' '.join(sequence)}{Style.RESET_ALL}")
        print(f"{Fore.RED}💀 {text['firewall_detected2']}{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def caesar_cipher(difficulty, lang="es"):
        text = get_text(lang)
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔐 ENCRYPTED CODE! Decrypt the message:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        words = ["HACKER", "SYSTEM", "SECURE", "DATA", "NET", "CYBER", "NEXUS", "QUANTUM", "MATRIX", "OMEGA", "SHADOW", "VOID"]
        word = random.choice(words)
        shift = random.randint(1, 5) + difficulty // 2
        encrypted = ""
        for char in word:
            if char.isalpha():
                code = ord(char) + shift
                if code > 90:
                    code -= 26
                encrypted += chr(code)
            else:
                encrypted += char
        print(f"{Fore.CYAN}📨 Encrypted message:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}╔{'═' * (len(encrypted) + 4)}╗")
        print(f"║  {encrypted}  ║")
        print(f"╚{'═' * (len(encrypted) + 4)}╝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔑 Hint: Caesar shift (1-{shift}){Style.RESET_ALL}")
        attempts = 3
        while attempts > 0:
            print(f"\n{Fore.CYAN}💡 Attempts left: {attempts}{Style.RESET_ALL}")
            answer = input("➡️  Decrypted message: ").strip().upper()
            if answer == word:
                print(f"{Fore.GREEN}✅ Correct!{Style.RESET_ALL}")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"{Fore.RED}❌ Incorrect.{Style.RESET_ALL}")
        print(f"{Fore.RED}💀 You failed.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def sql_injection(difficulty, lang="es"):
        text = get_text(lang)
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"💉 SQL VULNERABILITY! Inject the code:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        tables = ["users", "data", "admin", "system", "logs", "config", "credentials"]
        table = random.choice(tables)
        codes = [f"SELECT * FROM {table} WHERE 1=1; --", f"' OR '1'='1", f"'; DROP TABLE {table}; --", f"' UNION SELECT null,null,null--", f"' OR 1=1 --"]
        correct = random.choice(codes)
        print(f"{Fore.CYAN}💻 Target: Access '{table}' table{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔍 Hint: SQL code that is always true{Style.RESET_ALL}")
        attempts = 3
        while attempts > 0:
            print(f"\n{Fore.CYAN}💡 Attempts left: {attempts}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📝 Enter SQL code (help for examples):{Style.RESET_ALL}")
            answer = input("➡️  ").strip()
            if answer.lower() == 'help':
                print(f"{Fore.YELLOW}💡 Examples:")
                print("  - ' OR '1'='1")
                print("  - SELECT * FROM table WHERE 1=1; --")
                continue
            if answer == correct:
                print(f"{Fore.GREEN}✅ Injection successful!{Style.RESET_ALL}")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"{Fore.RED}❌ Incorrect.{Style.RESET_ALL}")
        print(f"{Fore.RED}💀 You've been blocked.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def logic_puzzle(difficulty, lang="es"):
        text = get_text(lang)
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🧩 LOGIC PUZZLE! Find the missing number:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        types = ["sum", "multiply", "fibonacci", "squares", "primes", "evens", "odds"]
        t = random.choice(types)
        if t == "sum":
            inc = random.randint(2, 5); start = random.randint(1, 10)
            seq = [start + i * inc for i in range(4)]; answer = seq[-1] + inc; hint = f"Adds {inc} each time"
        elif t == "multiply":
            mult = random.randint(2, 4); start = random.randint(1, 3)
            seq = [start * (mult ** i) for i in range(4)]; answer = seq[-1] * mult; hint = f"Multiply by {mult}"
        elif t == "fibonacci":
            seq = [1, 1, 2, 3, 5]; answer = 8; hint = "Fibonacci: sum of previous two"
        elif t == "squares":
            seq = [1, 4, 9, 16, 25]; answer = 36; hint = "Square numbers: 1², 2², 3²..."
        elif t == "primes":
            seq = [2, 3, 5, 7, 11]; answer = 13; hint = "Prime numbers"
        elif t == "evens":
            seq = [2, 4, 6, 8, 10]; answer = 12; hint = "Even numbers"
        else:
            seq = [1, 3, 5, 7, 9]; answer = 11; hint = "Odd numbers"
        print(f"{Fore.CYAN}📊 Sequence:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}╔{'═' * (len(seq) * 5 + 10)}╗")
        print(f"║  {'  →  '.join(map(str, seq))}  →  ?  ║")
        print(f"╚{'═' * (len(seq) * 5 + 10)}╝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💡 Hint: {hint}{Style.RESET_ALL}")
        attempts = 3
        while attempts > 0:
            print(f"\n{Fore.CYAN}💡 Attempts left: {attempts}{Style.RESET_ALL}")
            try:
                user = int(input("➡️  Missing number: ").strip())
                if user == answer:
                    print(f"{Fore.GREEN}✅ Correct!{Style.RESET_ALL}")
                    return True
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"{Fore.RED}❌ Incorrect.{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}❌ Enter a valid number.{Style.RESET_ALL}")
        print(f"{Fore.RED}💀 You couldn't solve it.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Answer: {answer}{Style.RESET_ALL}")
        return False

# ============================================
# UI FUNCTIONS
# ============================================

def show_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════════════════════╗
{Fore.GREEN}║  {Fore.CYAN}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗  {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}███████║███████║██║     █████╔╝ █████╗  ██████╔╝ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {Fore.GREEN}       ║
{Fore.GREEN}║     {Fore.YELLOW}HACKER SIMULATOR 2077 - ULTIMATE EDITION v{VERSION}{Fore.GREEN} ║
{Fore.GREEN}║     {Fore.WHITE}by {AUTHOR} {Fore.GREEN}| {Fore.CYAN}⭐ {GITHUB_URL}{Fore.GREEN}     ║
{Fore.GREEN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
""")

def get_clue(server, lang="es"):
    return server.get(f"clue_{lang}", server.get("clue_es", "No clue"))

def get_desc(server, lang="es"):
    return server.get(f"desc_{lang}", server.get("desc_es", "No description"))

# ============================================
# GAME FUNCTIONS
# ============================================

def hack_mission(hacker, server, lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.GREEN}{text['mission'].format(server['name'].upper())}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{text['id'].format(server['id'])}")
    print(f"{text['difficulty'].format(server['difficulty'])}")
    print(f"{text['reward'].format(server['reward'])}")
    print(f"{text['desc'].format(get_desc(server, lang))}")
    print(f"{text['clue'].format(get_clue(server, lang))}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{text['phase1']}{Style.RESET_ALL}")
    max_attempts = max(3, 5 - server['difficulty'] // 2)
    if not MiniGames.firewall_memory(server['difficulty'], max_attempts, lang):
        print(f"\n{Fore.RED}{text['mission_failed']}{Style.RESET_ALL}")
        hacker.failures += 1
        hacker.current_streak = 0
        return False
    
    print(f"\n{Fore.CYAN}{text['phase2']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{text['clue']}: {get_clue(server, lang)}{Style.RESET_ALL}")
    attempts = max(3, 5 - server['difficulty'] + 1)
    correct = False
    while attempts > 0 and not correct:
        print(f"\n{Fore.CYAN}{text['attempts_left'].format(attempts)}{Style.RESET_ALL}")
        if "🔑 Crypto Key" in hacker.tools:
            print(f"{Fore.YELLOW}{text['help_hint']}{Style.RESET_ALL}")
        password = input("➡️  Password: ").strip().lower()
        if password == 'help' and "🔑 Crypto Key" in hacker.tools:
            print(f"{Fore.CYAN}💡 Length: {len(server['password'])} chars{Style.RESET_ALL}")
            continue
        if password == server['password']:
            correct = True
            print(f"{Fore.GREEN}{text['password_correct']}{Style.RESET_ALL}")
        else:
            attempts -= 1
            if attempts > 0:
                print(f"{Fore.RED}{text['password_incorrect']}{Style.RESET_ALL}")
    if not correct:
        print(f"\n{Fore.RED}{text['password_failed']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{text['real_password'].format(server['password'])}{Style.RESET_ALL}")
        hacker.failures += 1
        hacker.current_streak = 0
        return False
    
    if server['difficulty'] >= 5:
        print(f"\n{Fore.CYAN}{text['phase3']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{text['extra_protection']}{Style.RESET_ALL}")
        mini = random.choice([MiniGames.caesar_cipher, MiniGames.sql_injection, MiniGames.logic_puzzle])
        if not mini(server['difficulty'], lang):
            print(f"{Fore.RED}{text['discovered']}{Style.RESET_ALL}")
            hacker.failures += 1
            hacker.current_streak = 0
            return False
    
    print(f"\n{Fore.GREEN}{'═'*50}")
    print(f"🎉 {text['mission_complete']}")
    print(f"{'═'*50}{Style.RESET_ALL}")
    reward = server['reward']
    bonus = min(hacker.current_streak * 25, 200)
    total = reward + bonus
    if hacker.level >= 5:
        total = int(total * 1.2)
    hacker.credits += total
    hacker.missions_completed += 1
    hacker.current_streak += 1
    if hacker.current_streak > hacker.best_streak:
        hacker.best_streak = hacker.current_streak
    if server['name'] not in hacker.hacked_servers:
        hacker.hacked_servers.append(server['name'])
    hacker.last_mission = server['name']
    exp = server['difficulty'] * 5 + hacker.current_streak * 2
    hacker.gain_exp(exp)
    print(f"{Fore.GREEN}{text['reward_total'].format(total)}")
    print(f"{text['exp_total'].format(exp)}")
    if bonus > 0:
        print(f"{text['streak_bonus'].format(bonus)}")
    if hacker.current_streak >= 3:
        print(f"{Fore.MAGENTA}{text['streak_current'].format(hacker.current_streak)}{Style.RESET_ALL}")
    hacker.check_achievements(lang)
    return True

def daily_mission(hacker, lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"{text['daily_mission']}")
    print(f"{'═'*50}{Style.RESET_ALL}")
    if hacker.daily_done:
        print(f"{Fore.YELLOW}{text['already_done']}{Style.RESET_ALL}")
        input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        return
    available = [s for s in SERVERS if s['difficulty'] <= 5]
    server = random.choice(available)
    print(f"{Fore.YELLOW}{text['today_mission']}{Style.RESET_ALL}")
    print(f"🎯 {server['name']} (★{server['difficulty']})")
    print(f"{Fore.GREEN}{text['double_reward'].format(server['reward'] * 2)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{text['clue']}: {get_clue(server, lang)}{Style.RESET_ALL}")
    print(f"\n{Fore.CYAN}{text['phase1']}{Style.RESET_ALL}")
    if not MiniGames.firewall_memory(server['difficulty'], 4, lang):
        print(f"{Fore.RED}{text['mission_failed']}{Style.RESET_ALL}")
        return
    print(f"\n{Fore.CYAN}{text['phase2']}{Style.RESET_ALL}")
    attempts = 3
    correct = False
    while attempts > 0 and not correct:
        print(f"\n{Fore.CYAN}{text['attempts_left'].format(attempts)}{Style.RESET_ALL}")
        password = input("➡️  Password: ").strip().lower()
        if password == server['password']:
            correct = True
            print(f"{Fore.GREEN}{text['password_correct']}{Style.RESET_ALL}")
        else:
            attempts -= 1
            if attempts > 0:
                print(f"{Fore.RED}{text['password_incorrect']}{Style.RESET_ALL}")
    if not correct:
        print(f"{Fore.RED}{text['password_failed']}{Style.RESET_ALL}")
        return
    print(f"\n{Fore.GREEN}{'═'*50}")
    print(f"🎉 {text['daily_complete']}")
    print(f"{'═'*50}{Style.RESET_ALL}")
    reward = server['reward'] * 2
    hacker.credits += reward
    hacker.missions_completed += 1
    hacker.daily_done = True
    hacker.last_daily = datetime.now().strftime("%Y-%m-%d")
    exp = server['difficulty'] * 8
    hacker.gain_exp(exp)
    print(f"{Fore.GREEN}{text['reward_total'].format(reward)}")
    print(f"{text['exp_total'].format(exp)}{Style.RESET_ALL}")
    hacker.check_achievements(lang)
    input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

def shop(hacker, lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"{text['shop']}")
    print(f"{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{text['credits_current'].format(hacker.credits)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{text['your_tools'].format(', '.join(hacker.tools))}{Style.RESET_ALL}")
    print(f"{'═'*50}")
    items = [
        {"name": "🔧 Advanced Scanner", "price": 100, "desc_es": "+2 intentos", "desc_en": "+2 attempts"},
        {"name": "🛡️ Firewall Bypass", "price": 200, "desc_es": "Firewall -1", "desc_en": "Firewall -1"},
        {"name": "🔑 Crypto Key", "price": 300, "desc_es": "Pistas extra", "desc_en": "Extra clues"},
        {"name": "⚡ Quantum Decryptor", "price": 500, "desc_es": "Descifra automático", "desc_en": "Auto-decrypt"},
        {"name": "🔬 Nano Analyzer", "price": 700, "desc_es": "Analiza servidores", "desc_en": "Analyze servers"},
        {"name": "🎯 Matrix Key", "price": 1000, "desc_es": "Acceso élite", "desc_en": "Elite access"},
        {"name": "⏳ Chrono Analyzer", "price": 1500, "desc_es": "Predice contraseñas", "desc_en": "Predict passwords"},
        {"name": "☯️ Omega Key", "price": 2500, "desc_es": "Acceso Omega", "desc_en": "Omega access"},
        {"name": "🌀 Void Key", "price": 5000, "desc_es": "Acceso Void", "desc_en": "Void access"}
    ]
    for i, item in enumerate(items, 1):
        owned = "✅" if item['name'] in hacker.tools else "❌"
        desc = item[f"desc_{lang}"]
        print(f"[{i}] {owned} {item['name']}")
        print(f"    {Fore.WHITE}💰 {item['price']} credits │ 📝 {desc}{Style.RESET_ALL}")
    print("[9] 💰 Buy EXP (100 credits = 10 EXP)")
    print("[0] 🚪 Exit")
    try:
        option = int(input("\n➡️  ").strip())
        if option == 0:
            return
        elif option == 9:
            if hacker.credits >= 100:
                hacker.credits -= 100
                hacker.gain_exp(10)
                print(f"{Fore.GREEN}{text['exp_gained']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{text['no_credits']}{Style.RESET_ALL}")
            time.sleep(1)
            return
        elif 1 <= option <= len(items):
            item = items[option-1]
            if item['name'] in hacker.tools:
                print(f"{Fore.YELLOW}{text['already_have']}{Style.RESET_ALL}")
            elif hacker.credits >= item['price']:
                hacker.credits -= item['price']
                hacker.tools.append(item['name'])
                print(f"{Fore.GREEN}{text['purchased']}{Style.RESET_ALL}")
                hacker.check_achievements(lang)
            else:
                print(f"{Fore.RED}{text['no_credits']}{Style.RESET_ALL}")
            time.sleep(1)
        else:
            print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
            time.sleep(1)
    except:
        print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
        time.sleep(1)

def show_stats(hacker, lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}{text['stats'].format(hacker.name.upper())}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{text['progress']}")
    print(f"  • {text['level'].format(hacker.level)}")
    print(f"  • {text['exp_current'].format(hacker.exp, hacker.exp_needed)}")
    print(f"  • {text['rank'].format(hacker.get_rank())}")
    print(f"\n{Fore.WHITE}{text['resources']}")
    print(f"  • {text['credits_current'].format(hacker.credits)}")
    print(f"  • {text['tools_count'].format(len(hacker.tools))}")
    print(f"\n{Fore.WHITE}{text['missions_stats']}")
    print(f"  • {text['completed'].format(hacker.missions_completed)}")
    print(f"  • {text['failed'].format(hacker.failures)}")
    print(f"  • {text['streak_current2'].format(hacker.current_streak)}")
    print(f"  • {text['best_streak2'].format(hacker.best_streak)}")
    print(f"  • {text['unique_servers'].format(len(set(hacker.hacked_servers)), len(SERVERS))}")
    print(f"\n{Fore.WHITE}{text['hacked_servers']}")
    if hacker.hacked_servers:
        for s in sorted(set(hacker.hacked_servers)):
            print(f"  • ✅ {s}")
    else:
        print(f"  • {text['none']}")
    print(f"\n{Fore.WHITE}{text['achievements'].format(len(hacker.unlocked_achievements), len(ACHIEVEMENTS))}")
    if hacker.unlocked_achievements:
        for ach_id in hacker.unlocked_achievements:
            ach = ACHIEVEMENTS[ach_id]
            name = ach.get(f"name_{lang}", ach.get("name_es", ach_id))
            print(f"  • {name}")
    else:
        print(f"  • {text['no_achievements']}")
    print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")

def show_ranking(hacker, lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}{text['ranking']}")
    print(f"{'═'*50}{Style.RESET_ALL}")
    opponents = [("Shadow", 8, 12), ("Neon", 7, 10), ("Vortex", 6, 8), ("Ghost", 5, 7), ("Phoenix", 4, 5), ("Cipher", 3, 4), ("Nova", 9, 15), ("Crystal", 11, 18), ("Zen", 12, 20), ("Omega", 15, 25)]
    print(f"{Fore.WHITE}{text['position']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🏆 #1  │ {hacker.name} │ {hacker.level}     │ {hacker.missions_completed}{Style.RESET_ALL}")
    for i, (name, level, missions) in enumerate(opponents, 2):
        if random.random() > 0.2:
            print(f"#{i}  │ {name} │ {level}     │ {missions}")
    print(f"\n{Fore.CYAN}{text['rank_up']}{Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

def show_guide(lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.CYAN}{'═'*60}")
    print(f"{Fore.YELLOW}{text['guide']}")
    print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
    print(text['guide_text'].format(GITHUB_URL, GITHUB_URL))
    input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

def settings_menu(hacker, lang="es"):
    text = get_text(lang)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_header()
        print(f"\n{Fore.CYAN}{'═'*50}")
        print(f"{Fore.YELLOW}{text['settings']}")
        print(f"{'═'*50}{Style.RESET_ALL}")
        print(f"[1] {text['change_theme']} (current: {hacker.current_theme})")
        print(f"[2] {text['change_language']}")
        print(f"[3] {Fore.RED}{text['delete_account']}{Style.RESET_ALL}")
        print(f"[4] {text['back']}")
        
        try:
            choice = input("➡️  ").strip()
            if choice == "4" or choice == "0":
                return lang
            elif choice == "1":
                print(f"\n{Fore.CYAN}{text['themes']}{Style.RESET_ALL}")
                themes = ["matrix", "cyberpunk", "classic", "dark"]
                for i, t in enumerate(themes, 1):
                    check = "✅" if hacker.current_theme == t else ""
                    print(f"[{i}] {check} {t}")
                try:
                    t_choice = int(input("➡️  ").strip()) - 1
                    if 0 <= t_choice < len(themes):
                        hacker.current_theme = themes[t_choice]
                        print(f"{Fore.GREEN}{text['theme_changed'].format(hacker.current_theme)}{Style.RESET_ALL}")
                        time.sleep(1)
                except:
                    print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
                    time.sleep(1)
            elif choice == "2":
                print(f"\n{Fore.CYAN}🌍 Select language / Selecciona idioma:{Style.RESET_ALL}")
                print("[1] 🇪🇸 Español")
                print("[2] 🇬🇧 English")
                l_choice = input("➡️  ").strip()
                if l_choice == "1":
                    save_config("es", hacker.name)
                    print(f"{Fore.GREEN}{text['language_changed']}{Style.RESET_ALL}")
                    time.sleep(2)
                    return "es"
                elif l_choice == "2":
                    save_config("en", hacker.name)
                    print(f"{Fore.GREEN}{text['language_changed']}{Style.RESET_ALL}")
                    time.sleep(2)
                    return "en"
                else:
                    print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
                    time.sleep(1)
            elif choice == "3":
                print(f"\n{Fore.RED}{'═'*50}")
                print(f"{Fore.YELLOW}⚠️ DELETE ACCOUNT ⚠️")
                print(f"{'═'*50}{Style.RESET_ALL}")
                print(f"{Fore.RED}{text['delete_warning']}{Style.RESET_ALL}")
                confirm = input(f"\n{Fore.RED}{text['confirm_delete']}{Style.RESET_ALL}").strip().upper()
                if confirm == "ELIMINAR" or confirm == "DELETE":
                    if hacker.delete_account():
                        print(f"\n{Fore.RED}{text['deleted']}{Style.RESET_ALL}")
                        time.sleep(2)
                        return "deleted"
                    else:
                        print(f"{Fore.RED}{text['error'].format('Could not delete')}{Style.RESET_ALL}")
                        time.sleep(1)
                else:
                    print(f"{Fore.YELLOW}{text['delete_cancelled']}{Style.RESET_ALL}")
                    time.sleep(1)
            else:
                print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
                time.sleep(1)
        except:
            print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
            time.sleep(1)

def training(hacker, lang="es"):
    text = get_text(lang)
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{text['training']}")
    print(f"{'═'*50}{Style.RESET_ALL}")
    print(f"[1] {text['firewall']}")
    print(f"[2] {text['cryptography']}")
    print(f"[3] {text['sql']}")
    print(f"[4] {text['puzzles']}")
    try:
        sub = input("➡️  ").strip()
        diff = random.randint(1, 3)
        success = False
        if sub == "1":
            success = MiniGames.firewall_memory(diff, 3, lang)
        elif sub == "2":
            success = MiniGames.caesar_cipher(diff, lang)
        elif sub == "3":
            success = MiniGames.sql_injection(diff, lang)
        elif sub == "4":
            success = MiniGames.logic_puzzle(diff, lang)
        else:
            print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
            time.sleep(1)
            return
        if success:
            exp = diff * 3 + random.randint(1, 3)
            hacker.gain_exp(exp)
            print(f"{Fore.GREEN}📈 +{exp} EXP{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{text['keep_practicing']}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
        time.sleep(1)

# ============================================
# MAIN MENU WITH ARROW NAVIGATION
# ============================================

def main_menu(hacker, lang="es"):
    text = get_text(lang)
    
    # Menu options
    menu_options = [
        text['menu_hack'],
        text['menu_daily'],
        text['menu_train'],
        text['menu_shop'],
        text['menu_stats'],
        text['menu_ranking'],
        text['menu_settings'],
        text['menu_save'],
        text['menu_guide'],
        text['menu_exit']
    ]
    
    while True:
        selected = select_with_arrows(menu_options, "📡 MAIN MENU", lang)
        
        if selected == -1:
            continue
        
        if selected == 0:  # Hack server
            print(f"\n{Fore.CYAN}{text['servers']}{Style.RESET_ALL}")
            available = [s for s in SERVERS if s['difficulty'] <= hacker.level + 1]
            for i, s in enumerate(available, 1):
                hacked = "✅" if s['name'] in hacker.hacked_servers else "❌"
                print(f"[{i}] {hacked} {s['name']} (★{s['difficulty']})")
                print(f"    {Fore.WHITE}{text['clue']}: {get_clue(s, lang)}{Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}{text['max_level'].format(hacker.level + 1)}{Style.RESET_ALL}")
            try:
                idx = int(input(f"{text['choose_server']}")) - 1
                if 0 <= idx < len(available):
                    hack_mission(hacker, available[idx], lang)
                else:
                    print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}{text['invalid']}{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif selected == 1:  # Daily mission
            daily_mission(hacker, lang)
        
        elif selected == 2:  # Train
            training(hacker, lang)
        
        elif selected == 3:  # Shop
            shop(hacker, lang)
        
        elif selected == 4:  # Statistics
            show_stats(hacker, lang)
            input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif selected == 5:  # Ranking
            show_ranking(hacker, lang)
        
        elif selected == 6:  # Settings
            new_lang = settings_menu(hacker, lang)
            if new_lang == "deleted":
                return False
            elif new_lang in ["es", "en"]:
                lang = new_lang
                text = get_text(lang)
        
        elif selected == 7:  # Save
            if hacker.save_game():
                print(f"{Fore.GREEN}{text['saved']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{text['save_error']}{Style.RESET_ALL}")
            time.sleep(1)
        
        elif selected == 8:  # Guide
            show_guide(lang)
        
        elif selected == 9:  # Exit
            if hacker.save_game():
                print(f"{Fore.GREEN}{text['saved']}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}{text['goodbye'].format(hacker.name)}{Style.RESET_ALL}")
            return False

# ============================================
# MAIN
# ============================================

def main():
    try:
        config = load_config()
        if config and "language" in config:
            language = config["language"]
            name = config.get("name", "Zero_Cool")
        else:
            language, name = first_time_setup()
        text = get_text(language)
        hacker = Hacker(name)
        if not hacker.load_game():
            hacker.save_game()
        
        show_header()
        
        # Check for updates
        check_for_updates()
        
        print(f"\n{Fore.GREEN}{text['connection'].format(hacker.name)}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{text['guide_hint']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Use ↑↓ arrows to navigate the menu{Style.RESET_ALL}")
        time.sleep(1.5)
        main_menu(hacker, language)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Session terminated.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        input(f"{Fore.CYAN}⏎ Press Enter to exit...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()