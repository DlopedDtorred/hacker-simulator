#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - UI EDITION v2.4
========================================
Interfaz gráfica estilo hacker con PyQt5
"""

import sys
import os
import json
import random
import time
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# ============================================
# CONFIGURACIÓN
# ============================================

VERSION = "2.4.0"
AUTHOR = "DlopedDtorred"
GITHUB_URL = "https://github.com/DlopedDtorred/hacker-simulator"
CONFIG_FILE = "config_ui.json"
SAVE_FILE = "save_ui.json"

# ============================================
# DATOS DEL JUEGO
# ============================================

SERVERS = [
    {"id": "SRV-001", "name": "MegaCorp Alpha", "difficulty": 1, "reward": 150,
     "clue": "El gato del CEO se llama 'Michi' con 'fu' al final",
     "password": "michifu", "desc": "Servidor corporativo básico"},
    {"id": "SRV-002", "name": "DarkNet Vault", "difficulty": 2, "reward": 250,
     "clue": "El número de la bestia sin el 6 final",
     "password": "666", "desc": "Custodia en red oscura"},
    {"id": "SRV-003", "name": "ShadowNet", "difficulty": 2, "reward": 300,
     "clue": "Fundado en el año del estreno de 'El Hobbit'",
     "password": "2015", "desc": "Red de datos sombra"},
    {"id": "SRV-004", "name": "CyberDyne Systems", "difficulty": 3, "reward": 400,
     "clue": "Blade Runner se estrenó en 2019",
     "password": "2019", "desc": "Sistemas de IA"},
    {"id": "SRV-005", "name": "NeoTokyo Grid", "difficulty": 4, "reward": 600,
     "clue": "Código postal de Shibuya: 150-0042",
     "password": "1500042", "desc": "Red de ciudad digital"},
    {"id": "SRV-006", "name": "A.I. Core", "difficulty": 5, "reward": 1000,
     "clue": "Fibonacci posición 13 es 233",
     "password": "233", "desc": "Núcleo de IA"},
    {"id": "SRV-007", "name": "Quantum Nexus", "difficulty": 6, "reward": 1500,
     "clue": "Constante de Planck: 6.626... (primeros 3 dígitos)",
     "password": "662", "desc": "Servidor cuántico"},
    {"id": "SRV-008", "name": "NanoTech Labs", "difficulty": 7, "reward": 2000,
     "clue": "El carbono es el elemento número 6",
     "password": "6", "desc": "Laboratorio nanotecnológico"},
    {"id": "SRV-009", "name": "Matrix Archive", "difficulty": 8, "reward": 3000,
     "clue": "La habitación de Neo en 'The Matrix' es la 303",
     "password": "303", "desc": "Archivo de la resistencia"},
    {"id": "SRV-010", "name": "ChronoCore", "difficulty": 9, "reward": 5000,
     "clue": "El ADN fue descubierto en 1953",
     "password": "1953", "desc": "Base de datos temporal"},
    {"id": "SRV-011", "name": "Omega Station", "difficulty": 10, "reward": 10000,
     "clue": "666 × 7 = 4662",
     "password": "4662", "desc": "El servidor definitivo"},
    {"id": "SRV-012", "name": "Void Network", "difficulty": 9, "reward": 4500,
     "clue": "7³ = 343",
     "password": "343", "desc": "Red en el vacío digital"},
    {"id": "SRV-013", "name": "Eclipse Core", "difficulty": 11, "reward": 15000,
     "clue": "Primer eclipse total del siglo XXI: 2001",
     "password": "2001", "desc": "Núcleo de la sombra"},
    {"id": "SRV-014", "name": "Nebula Archive", "difficulty": 12, "reward": 20000,
     "clue": "Código postal de la NASA: 77058",
     "password": "77058", "desc": "Archivo espacial"},
    {"id": "SRV-015", "name": "Genesis Point", "difficulty": 13, "reward": 30000,
     "clue": "Primera computadora electrónica: 1941",
     "password": "1941", "desc": "El origen de todo"},
    {"id": "SRV-016", "name": "Apollo Core", "difficulty": 14, "reward": 40000,
     "clue": "Primer alunizaje: 1969",
     "password": "1969", "desc": "Núcleo de la misión Apolo"},
    {"id": "SRV-017", "name": "Digital Abyss", "difficulty": 15, "reward": 50000,
     "clue": "Fosa de las Marianas: 11.034 metros",
     "password": "11034", "desc": "El abismo digital"},
    {"id": "SRV-018", "name": "Phoenix Protocol", "difficulty": 16, "reward": 75000,
     "clue": "Serie Phoenix resurgió en 2002",
     "password": "2002", "desc": "Protocolo de resurrección"},
    {"id": "SRV-019", "name": "Eternal Archive", "difficulty": 18, "reward": 100000,
     "clue": "Símbolo del infinito es un 8 acostado",
     "password": "8", "desc": "Archivo eterno"},
    {"id": "SRV-020", "name": "Omega Point", "difficulty": 20, "reward": 200000,
     "clue": "666 × 666 = 443556",
     "password": "443556", "desc": "El punto final de todo"}
]

# ============================================
# CLASE HACKER
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
        self.daily_done = False
        self.last_daily = None
        self.save_file = SAVE_FILE
        
    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= self.exp_needed:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_needed = self.level * 15
        if self.level % 2 == 0:
            self._give_tool()
        if self.level % 3 == 0:
            self.credits += self.level * 50
        if self.level % 5 == 0:
            self.credits += 200
            if self.level % 10 == 0:
                self.credits += 500
    
    def _give_tool(self):
        tools = ["🔧 Advanced Scanner", "🛡️ Firewall Bypass", "🔑 Crypto Key",
                "⚡ Quantum Decryptor", "🔬 Nano Analyzer", "🎯 Matrix Key",
                "⏳ Chrono Analyzer", "☯️ Omega Key", "🌀 Void Key"]
        idx = (self.level // 2 - 1) % len(tools)
        new_tool = tools[idx]
        if new_tool not in self.tools:
            self.tools.append(new_tool)
    
    def get_rank(self):
        if self.level >= 25: return "👑 LEGENDARY HACKER"
        elif self.level >= 20: return "⚡ ELITE HACKER"
        elif self.level >= 15: return "🔥 SENIOR HACKER"
        elif self.level >= 10: return "💻 JUNIOR HACKER"
        elif self.level >= 5: return "🔰 APPRENTICE"
        else: return "🐣 NOVICE"
    
    def save_game(self):
        data = {
            "name": self.name, "level": self.level, "exp": self.exp,
            "exp_needed": self.exp_needed, "credits": self.credits,
            "tools": self.tools, "missions_completed": self.missions_completed,
            "failures": self.failures, "current_streak": self.current_streak,
            "best_streak": self.best_streak, "hacked_servers": self.hacked_servers,
            "unlocked_achievements": self.unlocked_achievements,
            "current_theme": self.current_theme, "daily_done": self.daily_done,
            "last_daily": self.last_daily
        }
        try:
            with open(self.save_file, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except:
            return False
    
    def load_game(self):
        try:
            with open(self.save_file, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            return True
        except:
            return False

# ============================================
# DIÁLOGOS
# ============================================

class InputDialog(QDialog):
    def __init__(self, title, label, parent=None, placeholder=""):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(500, 200)
        self.setStyleSheet("""
            QDialog { background-color: #0a0a0a; }
            QLabel { color: #00ff41; font-family: 'Courier New', monospace; font-size: 15px; }
            QLineEdit {
                background-color: #1a1a1a; color: #00ff41;
                border: 2px solid #1a2a1a; border-radius: 8px;
                padding: 12px; font-size: 16px; font-family: 'Courier New', monospace;
            }
            QLineEdit:focus { border: 2px solid #00ff41; }
            QPushButton {
                background-color: #00ff41; color: #0a0a0a;
                border: none; border-radius: 8px;
                padding: 12px 24px; font-size: 15px; font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QPushButton:hover { background-color: #66ff88; }
        """)
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)
        self.label = QLabel(label)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)
        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        self.input.returnPressed.connect(self.accept)
        layout.addWidget(self.input)
        btn_layout = QHBoxLayout()
        btn_ok = QPushButton("✅ OK")
        btn_ok.clicked.connect(self.accept)
        btn_cancel = QPushButton("❌ Cancel")
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_ok)
        btn_layout.addWidget(btn_cancel)
        layout.addLayout(btn_layout)
        self.input.setFocus()
    
    def get_text(self):
        return self.input.text().strip()

class SelectDialog(QDialog):
    def __init__(self, items, title="🌐 Select", label="Choose:", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(600, 450)
        self.setStyleSheet("""
            QDialog { background-color: #0a0a0a; }
            QLabel { color: #00ff41; font-family: 'Courier New', monospace; font-size: 15px; }
            QListWidget {
                background-color: #1a1a1a; color: #00ff41;
                border: 2px solid #1a2a1a; border-radius: 8px;
                font-family: 'Courier New', monospace; font-size: 14px;
                padding: 5px;
            }
            QListWidget::item { padding: 12px 10px; border-bottom: 1px solid #1a2a1a; }
            QListWidget::item:selected { background-color: #00ff41; color: #0a0a0a; }
            QListWidget::item:hover { background-color: #2a2a2a; }
            QPushButton {
                background-color: #00ff41; color: #0a0a0a;
                border: none; border-radius: 8px;
                padding: 12px 24px; font-size: 15px; font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QPushButton:hover { background-color: #66ff88; }
        """)
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)
        self.label = QLabel(label)
        layout.addWidget(self.label)
        self.list = QListWidget()
        self.items = items
        for item in items:
            if isinstance(item, dict):
                text = item.get('name', str(item))
            else:
                text = str(item)
            self.list.addItem(text)
        layout.addWidget(self.list)
        self.info_label = QLabel("💡 Select an option from the list")
        self.info_label.setStyleSheet("color: #666666; font-size: 13px;")
        layout.addWidget(self.info_label)
        btn_layout = QHBoxLayout()
        btn_ok = QPushButton("✅ Select")
        btn_ok.clicked.connect(self.accept)
        btn_cancel = QPushButton("❌ Cancel")
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_ok)
        btn_layout.addWidget(btn_cancel)
        layout.addLayout(btn_layout)
    
    def get_selected(self):
        idx = self.list.currentRow()
        if 0 <= idx < len(self.items):
            return self.items[idx]
        return None

class FirewallDialog(QDialog):
    def __init__(self, sequence, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🔥 FIREWALL CHALLENGE")
        self.setFixedSize(550, 320)
        self.setStyleSheet("""
            QDialog { background-color: #0a0a0a; }
            QLabel { color: #00ff41; font-family: 'Courier New', monospace; font-size: 16px; }
            QLineEdit {
                background-color: #1a1a1a; color: #00ff41;
                border: 2px solid #1a2a1a; border-radius: 8px;
                padding: 12px; font-size: 18px; font-family: 'Courier New', monospace;
            }
            QLineEdit:focus { border: 2px solid #00ff41; }
            QPushButton {
                background-color: #00ff41; color: #0a0a0a;
                border: none; border-radius: 8px;
                padding: 12px 24px; font-size: 15px; font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QPushButton:hover { background-color: #66ff88; }
        """)
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)
        title_label = QLabel("🛡️ FIREWALL DETECTED")
        title_label.setStyleSheet("color: #ff4444; font-size: 20px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        self.label = QLabel("🔥 Memorize this sequence of numbers:")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.seq_label = QLabel(" ".join(sequence))
        self.seq_label.setStyleSheet("color: #ffcc00; font-size: 32px; font-weight: bold; letter-spacing: 4px;")
        self.seq_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.seq_label)
        self.timer_label = QLabel("⏳ You have 3 seconds to memorize...")
        self.timer_label.setStyleSheet("color: #ff8800; font-size: 14px;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_label)
        input_label = QLabel("⌨️ Enter the sequence (numbers separated by space):")
        layout.addWidget(input_label)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Example: 1 2 3 4")
        self.input.setEnabled(False)
        layout.addWidget(self.input)
        btn_layout = QHBoxLayout()
        self.btn_ok = QPushButton("✅ VERIFY")
        self.btn_ok.clicked.connect(self.accept)
        self.btn_ok.setEnabled(False)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_ok)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        self.sequence = sequence
        self.timer = QTimer()
        self.timer.timeout.connect(self.enable_input)
        self.timer.start(3000)
    
    def enable_input(self):
        self.timer.stop()
        self.timer_label.setText("⌨️ Enter the sequence now:")
        self.timer_label.setStyleSheet("color: #00ff41; font-size: 14px;")
        self.input.setEnabled(True)
        self.btn_ok.setEnabled(True)
        self.input.setFocus()
    
    def get_result(self):
        return self.input.text().strip().split()

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

def first_time_setup():
    dialog = QDialog()
    dialog.setWindowTitle("⚡ First Time Setup")
    dialog.setFixedSize(600, 500)
    dialog.setStyleSheet("""
        QDialog { background-color: #0a0a0a; }
        QLabel { color: #00ff41; font-family: 'Courier New', monospace; font-size: 15px; }
        QLineEdit {
            background-color: #1a1a1a; color: #00ff41;
            border: 2px solid #1a2a1a; border-radius: 8px;
            padding: 12px; font-size: 16px; font-family: 'Courier New', monospace;
        }
        QLineEdit:focus { border: 2px solid #00ff41; }
        QComboBox {
            background-color: #1a1a1a; color: #00ff41;
            border: 2px solid #1a2a1a; border-radius: 8px;
            padding: 10px; font-size: 15px; font-family: 'Courier New', monospace;
        }
        QPushButton {
            background-color: #00ff41; color: #0a0a0a;
            border: none; border-radius: 8px;
            padding: 14px 28px; font-size: 18px; font-weight: bold;
            font-family: 'Courier New', monospace;
        }
        QPushButton:hover { background-color: #66ff88; }
    """)
    layout = QVBoxLayout(dialog)
    layout.setSpacing(18)
    layout.setContentsMargins(35, 35, 35, 35)
    title = QLabel("🌍 WELCOME TO HACKER SIMULATOR 2077")
    title.setStyleSheet("font-size: 22px; font-weight: bold; color: #66ff88;")
    title.setAlignment(Qt.AlignCenter)
    layout.addWidget(title)
    subtitle = QLabel("⚡ First-time setup - Configure your profile")
    subtitle.setStyleSheet("font-size: 14px; color: #666666;")
    subtitle.setAlignment(Qt.AlignCenter)
    layout.addWidget(subtitle)
    layout.addSpacing(10)
    lang_label = QLabel("🌐 Select your language / Selecciona tu idioma:")
    layout.addWidget(lang_label)
    lang_combo = QComboBox()
    lang_combo.addItems(["🇪🇸 Español", "🇬🇧 English"])
    layout.addWidget(lang_combo)
    layout.addSpacing(10)
    name_label = QLabel("👤 Enter your hacker name:")
    layout.addWidget(name_label)
    name_input = QLineEdit()
    name_input.setPlaceholderText("Zero_Cool")
    layout.addWidget(name_input)
    layout.addSpacing(20)
    info = QLabel("💡 Your progress will be saved automatically")
    info.setStyleSheet("color: #666666; font-size: 13px;")
    info.setAlignment(Qt.AlignCenter)
    layout.addWidget(info)
    layout.addSpacing(15)
    btn = QPushButton("🚀 START HACKING")
    btn.setStyleSheet("font-size: 20px; padding: 16px;")
    layout.addWidget(btn)
    result = {"language": "es", "name": "Zero_Cool", "accepted": False}
    def on_accept():
        result["language"] = "es" if lang_combo.currentIndex() == 0 else "en"
        result["name"] = name_input.text().strip() or "Zero_Cool"
        result["accepted"] = True
        dialog.accept()
    btn.clicked.connect(on_accept)
    dialog.exec_()
    return result

# ============================================
# VENTANA PRINCIPAL
# ============================================

class HackerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.language = "es"
        self.hacker_name = "Zero_Cool"
        self.load_config()
        self.hacker = Hacker(self.hacker_name)
        self.hacker.load_game()
        self.initUI()
        self.setup_terminal_style()
        self.update_display()
        self.show_welcome()
        
    def load_config(self):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                self.language = config.get("language", "es")
                self.hacker_name = config.get("name", "Zero_Cool")
        except:
            result = first_time_setup()
            if result["accepted"]:
                self.language = result["language"]
                self.hacker_name = result["name"]
                with open(CONFIG_FILE, 'w') as f:
                    json.dump({"language": self.language, "name": self.hacker_name}, f, indent=4)
            else:
                self.language = "es"
                self.hacker_name = "Zero_Cool"
        
    def initUI(self):
        self.setWindowTitle(f"🖥️ HACKER SIMULATOR 2077 - {self.hacker_name}")
        self.setGeometry(100, 100, 1400, 900)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # ===== PANEL IZQUIERDO (TERMINAL) =====
        left_panel = QWidget()
        left_panel.setStyleSheet("background-color: #0a0a0a; border: none;")
        left_panel.setFixedWidth(850)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(5)
        left_layout.setContentsMargins(15, 15, 15, 15)
        terminal_title = QLabel("🖥️ TERMINAL")
        terminal_title.setStyleSheet("color: #00ff41; font-size: 14px; font-weight: bold; padding: 8px 12px; border-bottom: 1px solid #1a2a1a;")
        left_layout.addWidget(terminal_title)
        self.terminal_output = QTextEdit()
        self.terminal_output.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a0a; color: #00ff41;
                font-family: 'Courier New', monospace; font-size: 14px;
                border: 1px solid #1a2a1a; border-radius: 8px; padding: 12px;
            }
        """)
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setLineWrapMode(QTextEdit.NoWrap)
        left_layout.addWidget(self.terminal_output, 8)
        input_layout = QHBoxLayout()
        input_label = QLabel("➜")
        input_label.setStyleSheet("color: #00ff41; font-size: 18px; font-weight: bold;")
        input_layout.addWidget(input_label)
        self.terminal_input = QLineEdit()
        self.terminal_input.setStyleSheet("""
            QLineEdit {
                background-color: #0a0a0a; color: #00ff41;
                font-family: 'Courier New', monospace; font-size: 15px;
                border: 1px solid #1a2a1a; border-radius: 8px; padding: 12px;
            }
            QLineEdit:focus { border: 1px solid #00ff41; }
        """)
        self.terminal_input.setPlaceholderText("Type a command or use the buttons on the right...")
        self.terminal_input.returnPressed.connect(self.process_terminal_command)
        input_layout.addWidget(self.terminal_input, 8)
        self.send_btn = QPushButton("▶ EXECUTE")
        self.send_btn.setStyleSheet("""
            QPushButton {
                background-color: #00ff41; color: #0a0a0a;
                font-size: 14px; font-weight: bold;
                border: none; border-radius: 8px; padding: 12px 24px;
            }
            QPushButton:hover { background-color: #66ff88; }
        """)
        self.send_btn.clicked.connect(self.process_terminal_command)
        input_layout.addWidget(self.send_btn, 1)
        left_layout.addLayout(input_layout, 1)
        
        # ===== PANEL DERECHO =====
        right_panel = QWidget()
        right_panel.setStyleSheet("background-color: #0d0d0d; border-left: 1px solid #1a2a1a;")
        right_panel.setFixedWidth(450)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(10)
        right_layout.setContentsMargins(20, 20, 20, 20)
        title_label = QLabel("⚡ HACKER STATUS")
        title_label.setStyleSheet("color: #00ff41; font-size: 18px; font-weight: bold; padding: 10px; border-bottom: 1px solid #1a2a1a;")
        right_layout.addWidget(title_label)
        self.info_text = QTextEdit()
        self.info_text.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a0a; color: #88ff88;
                font-family: 'Courier New', monospace; font-size: 14px;
                border: 1px solid #1a2a1a; border-radius: 8px; padding: 12px;
            }
        """)
        self.info_text.setReadOnly(True)
        self.info_text.setMaximumHeight(300)
        right_layout.addWidget(self.info_text)
        sep = QLabel("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        sep.setStyleSheet("color: #1a2a1a; font-size: 10px;")
        right_layout.addWidget(sep)
        actions_title = QLabel("🎯 ACTIONS")
        actions_title.setStyleSheet("color: #666666; font-size: 13px; font-weight: bold; padding: 5px;")
        right_layout.addWidget(actions_title)
        buttons_layout = QGridLayout()
        buttons_layout.setSpacing(10)
        btn_style = """
            QPushButton {
                background-color: #1a1a1a; color: #00ff41;
                border: 1px solid #1a2a1a; border-radius: 8px;
                padding: 14px 10px; font-size: 13px; font-weight: bold;
                text-align: left;
            }
            QPushButton:hover { background-color: #2a2a2a; border: 1px solid #00ff41; }
            QPushButton:pressed { background-color: #00ff41; color: #0a0a0a; }
        """
        buttons = [
            ("🌐", "Hack Server", "Start a hacking mission", self.hack_server),
            ("📅", "Daily Mission", "Double rewards!", self.daily_mission),
            ("🛠️", "Training", "Practice your skills", self.train),
            ("🛒", "Tool Shop", "Buy upgrades", self.shop),
            ("📊", "Statistics", "View your progress", self.show_stats),
            ("🏆", "Ranking", "Hacker leaderboard", self.show_ranking),
            ("⚙️", "Settings", "Configure game", self.settings),
            ("💾", "Save Game", "Save your progress", self.save_game),
            ("📖", "User Guide", "How to play", self.show_guide),
            ("🚪", "Exit Game", "Quit", self.exit_game)
        ]
        for i, (icon, text, tooltip, func) in enumerate(buttons):
            btn = QPushButton(f"{icon} {text}")
            btn.setStyleSheet(btn_style)
            btn.setToolTip(tooltip)
            btn.clicked.connect(func)
            row = i // 2
            col = i % 2
            buttons_layout.addWidget(btn, row, col)
        right_layout.addLayout(buttons_layout)
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #0a0a0a; color: #00ff41;
                font-family: 'Courier New', monospace; font-size: 13px;
                border-top: 1px solid #1a2a1a;
            }
        """)
        self.setStatusBar(self.status_bar)
        main_layout.addWidget(left_panel, 7)
        main_layout.addWidget(right_panel, 3)
        self.terminal_input.setFocus()
        
    def setup_terminal_style(self):
        self.command_history = []
        self.history_index = -1
        
    def show_welcome(self):
        self.terminal_print("""
╔══════════════════════════════════════════════════════════════════╗
║  ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗               ║
║  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗              ║
║  ███████║███████║██║     █████╔╝ █████╗  ██████╔╝              ║
║  ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗              ║
║  ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║              ║
║  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝              ║
║     HACKER SIMULATOR 2077 - UI EDITION v2.4                    ║
╚══════════════════════════════════════════════════════════════════╝
""", "green")
        self.terminal_print(f"\n👤 Welcome back, {self.hacker.name}!", "cyan")
        self.terminal_print("💡 Use the buttons on the right or type commands in the terminal.", "yellow")
        self.terminal_print("🔧 Available commands: help, stats, save, exit, clear\n", "gray")
        self.update_display()
        
    def terminal_print(self, text, color="green"):
        colors = {
            "green": "#00ff41", "red": "#ff4444", "yellow": "#ffcc00",
            "blue": "#4488ff", "cyan": "#00ffcc", "white": "#ffffff",
            "gray": "#666666", "magenta": "#ff44ff", "orange": "#ff8800"
        }
        color_code = colors.get(color, "#00ff41")
        self.terminal_output.setTextColor(QColor(color_code))
        self.terminal_output.append(text)
        self.terminal_output.verticalScrollBar().setValue(
            self.terminal_output.verticalScrollBar().maximum()
        )
        
    def process_terminal_command(self):
        command = self.terminal_input.text().strip().lower()
        self.terminal_input.clear()
        if not command:
            return
        self.command_history.append(command)
        self.history_index = len(self.command_history)
        self.terminal_print(f"\n➜ {command}", "white")
        if command == "help":
            self.show_help()
        elif command in ["stats", "statistics"]:
            self.show_stats()
        elif command == "hack":
            self.hack_server()
        elif command == "daily":
            self.daily_mission()
        elif command == "train":
            self.train()
        elif command == "shop":
            self.shop()
        elif command in ["rank", "ranking"]:
            self.show_ranking()
        elif command == "save":
            self.save_game()
        elif command in ["exit", "quit"]:
            self.exit_game()
        elif command in ["clear", "cls"]:
            self.terminal_output.clear()
        elif command == "guide":
            self.show_guide()
        elif command == "theme":
            self.settings()
        else:
            self.terminal_print(f"❌ Unknown command: '{command}'. Type 'help' for commands.", "red")
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            if self.history_index > 0:
                self.history_index -= 1
                self.terminal_input.setText(self.command_history[self.history_index])
        elif event.key() == Qt.Key_Down:
            if self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                self.terminal_input.setText(self.command_history[self.history_index])
            else:
                self.history_index = len(self.command_history)
                self.terminal_input.clear()
        else:
            super().keyPressEvent(event)
            
    def update_display(self):
        h = self.hacker
        if h.exp_needed > 0:
            bar = "█" * int((h.exp / h.exp_needed) * 15)
            empty = "░" * (15 - len(bar))
        else:
            bar = ""
            empty = "░" * 15
        info = f"""
╔═══════════════════════════════════════════════════╗
║ 👤 {h.name}  │  Lv.{h.level}  │  💰 {h.credits} credits
║ 📊 EXP [{bar}{empty}] {h.exp}/{h.exp_needed}
║ 🏆 {h.get_rank()}
║ 🛠️  {', '.join(h.tools[:3])}{'...' if len(h.tools) > 3 else ''}
║ 📈 Streaks: {h.current_streak} now │ {h.best_streak} best
║ 🎯 Missions: {h.missions_completed} │ ❌ Failures: {h.failures}
║ 🗺️  Unique: {len(set(h.hacked_servers))}/{len(SERVERS)}
╚═══════════════════════════════════════════════════╝
"""
        self.info_text.setText(info)
        self.status_bar.showMessage(f"🟢 Connected as {h.name} | Level {h.level} | {h.credits} credits")
        
    def show_help(self):
        self.terminal_print("""
╔═══════════════════════════════════════════════════╗
║  📖 COMMAND LIST                                 ║
╠═══════════════════════════════════════════════════╣
║  help          - Show this help message          ║
║  hack          - Start a hacking mission         ║
║  daily         - Daily mission (DOUBLE reward)   ║
║  train         - Practice mini-games             ║
║  shop          - Visit the tool shop             ║
║  stats         - Show statistics                 ║
║  rank/ranking  - Show hacker ranking             ║
║  save          - Save game                       ║
║  guide         - Show user guide                 ║
║  clear/cls     - Clear terminal                  ║
║  exit/quit     - Exit game                       ║
╚═══════════════════════════════════════════════════╝
""", "yellow")
        
    def hack_server(self):
        available = [s for s in SERVERS if s['difficulty'] <= self.hacker.level + 1]
        if not available:
            self.terminal_print("❌ No servers available. Level up to unlock more!", "red")
            return
        options = []
        for s in available:
            hacked = "✅ " if s['name'] in self.hacker.hacked_servers else "⬜ "
            options.append({"name": f"{hacked}{s['name']} (★{s['difficulty']})", "server": s})
        dialog = SelectDialog(options, "🌐 SELECT SERVER", "Choose a server to hack:", self)
        if dialog.exec_() == QDialog.Accepted:
            selected = dialog.get_selected()
            if selected and 'server' in selected:
                self._execute_hack(selected['server'])
        
    def _execute_hack(self, server):
        self.terminal_print(f"\n🎯 MISSION: HACK {server['name'].upper()}", "green")
        self.terminal_print(f"📋 ID: {server['id']} | ⭐ Difficulty: {server['difficulty']} ★", "gray")
        self.terminal_print(f"💰 Reward: {server['reward']} credits", "yellow")
        self.terminal_print(f"📝 {server['desc']}", "gray")
        self.terminal_print(f"🔍 CLUE: {server['clue']}", "yellow")
        self.terminal_print("\n🛡️ PHASE 1: EVADE FIREWALL", "blue")
        sequence = [str(random.randint(1, 9)) for _ in range(4)]
        self.terminal_print(f"🔥 Memorize: {' '.join(sequence)}", "yellow")
        firewall_dialog = FirewallDialog(sequence, self)
        if firewall_dialog.exec_() == QDialog.Accepted:
            answer = firewall_dialog.get_result()
            if answer != sequence:
                self.terminal_print("❌ Firewall detected you!", "red")
                self.hacker.failures += 1
                self.hacker.current_streak = 0
                self.update_display()
                return
        else:
            self.terminal_print("❌ Firewall detected you!", "red")
            self.hacker.failures += 1
            self.hacker.current_streak = 0
            self.update_display()
            return
        self.terminal_print("✅ Firewall evaded!", "green")
        self.terminal_print("\n🔑 PHASE 2: CRACK PASSWORD", "blue")
        attempts = max(3, 5 - server['difficulty'] + 1)
        correct = False
        while attempts > 0 and not correct:
            self.terminal_print(f"🔐 Attempts left: {attempts}", "yellow")
            dialog = InputDialog("🔑 Password", f"CLUE: {server['clue']}", self, "Type the password...")
            if dialog.exec_() == QDialog.Accepted:
                password = dialog.get_text()
                if password.lower() == server['password']:
                    correct = True
                    self.terminal_print("✅ Access granted!", "green")
                else:
                    attempts -= 1
                    if attempts > 0:
                        self.terminal_print("❌ Incorrect. Try again.", "red")
            else:
                self.terminal_print("❌ Mission cancelled.", "red")
                return
        if not correct:
            self.terminal_print(f"💀 You failed. Password was: {server['password']}", "red")
            self.hacker.failures += 1
            self.hacker.current_streak = 0
            self.update_display()
            return
        self.terminal_print("\n🎉 MISSION COMPLETED!", "green")
        reward = server['reward']
        bonus = min(self.hacker.current_streak * 25, 200)
        total = reward + bonus
        if self.hacker.level >= 5:
            total = int(total * 1.2)
        self.hacker.credits += total
        self.hacker.missions_completed += 1
        self.hacker.current_streak += 1
        if self.hacker.current_streak > self.hacker.best_streak:
            self.hacker.best_streak = self.hacker.current_streak
        if server['name'] not in self.hacker.hacked_servers:
            self.hacker.hacked_servers.append(server['name'])
        exp = server['difficulty'] * 5 + self.hacker.current_streak * 2
        self.hacker.gain_exp(exp)
        self.terminal_print(f"💰 +{total} credits", "green")
        self.terminal_print(f"📈 +{exp} EXP", "green")
        if bonus > 0:
            self.terminal_print(f"🔥 Streak bonus: +{bonus} credits", "yellow")
        if self.hacker.current_streak >= 3:
            self.terminal_print(f"🔥 {self.hacker.current_streak} streak!", "magenta")
        self.update_display()
        
    def daily_mission(self):
        self.terminal_print("\n📅 DAILY MISSION", "yellow")
        if self.hacker.daily_done:
            self.terminal_print("⚠️ You already completed today's mission.", "red")
            return
        available = [s for s in SERVERS if s['difficulty'] <= 5]
        server = random.choice(available)
        self.terminal_print(f"🌟 Today's mission: {server['name']}", "green")
        self.terminal_print(f"💰 Reward: {server['reward'] * 2} credits (DOUBLE!)", "yellow")
        self.terminal_print(f"🔍 CLUE: {server['clue']}", "cyan")
        attempts = 3
        correct = False
        while attempts > 0 and not correct:
            self.terminal_print(f"🔐 Attempts left: {attempts}", "yellow")
            dialog = InputDialog("🔑 Password", f"CLUE: {server['clue']}", self, "Type the password...")
            if dialog.exec_() == QDialog.Accepted:
                password = dialog.get_text()
                if password.lower() == server['password']:
                    correct = True
                    self.terminal_print("✅ Access granted!", "green")
                else:
                    attempts -= 1
                    if attempts > 0:
                        self.terminal_print("❌ Incorrect.", "red")
            else:
                self.terminal_print("❌ Mission cancelled.", "red")
                return
        if not correct:
            self.terminal_print("💀 Daily mission failed.", "red")
            return
        reward = server['reward'] * 2
        self.hacker.credits += reward
        self.hacker.missions_completed += 1
        self.hacker.daily_done = True
        self.hacker.last_daily = datetime.now().strftime("%Y-%m-%d")
        exp = server['difficulty'] * 8
        self.hacker.gain_exp(exp)
        self.terminal_print(f"🎉 DAILY MISSION COMPLETED!", "green")
        self.terminal_print(f"💰 +{reward} credits", "green")
        self.terminal_print(f"📈 +{exp} EXP", "green")
        self.update_display()
        
    def train(self):
        self.terminal_print("\n🛠️ TRAINING", "blue")
        options = [
            {"name": "🔥 Firewall Memory", "desc": "Memorize number sequences"},
            {"name": "🔐 Caesar Cipher", "desc": "Decrypt messages"},
            {"name": "💉 SQL Injection", "desc": "Inject SQL code"},
            {"name": "🧩 Logic Puzzles", "desc": "Find number patterns"}
        ]
        dialog = SelectDialog(options, "🛠️ TRAINING", "Choose a mini-game to practice:", self)
        if dialog.exec_() == QDialog.Accepted:
            selected = dialog.get_selected()
            if not selected:
                return
            idx = options.index(selected) if selected in options else -1
            if idx == -1:
                return
            diff = random.randint(1, 3)
            success = False
            if idx == 0:
                self.terminal_print("🔥 Firewall training...", "yellow")
                sequence = [str(random.randint(1, 9)) for _ in range(3)]
                self.terminal_print(f"Memorize: {' '.join(sequence)}", "yellow")
                fw_dialog = FirewallDialog(sequence, self)
                if fw_dialog.exec_() == QDialog.Accepted:
                    answer = fw_dialog.get_result()
                    success = (answer == sequence)
                else:
                    success = False
            elif idx == 1:
                self.terminal_print("🔐 Caesar Cipher training...", "yellow")
                word = random.choice(["HACKER", "SYSTEM", "DATA", "CYBER", "NEXUS"])
                shift = random.randint(1, 5)
                encrypted = ""
                for c in word:
                    code = ord(c) + shift
                    if code > 90:
                        code -= 26
                    encrypted += chr(code)
                self.terminal_print(f"Encrypted: {encrypted}", "yellow")
                dialog = InputDialog("🔐 Caesar Cipher", f"Shift: {shift}", self, "Type the decrypted word...")
                if dialog.exec_() == QDialog.Accepted:
                    success = (dialog.get_text().upper() == word)
                else:
                    success = False
            elif idx == 2:
                self.terminal_print("💉 SQL Injection training...", "yellow")
                self.terminal_print("Target: 'users' table", "cyan")
                self.terminal_print("Hint: Code that is always true", "cyan")
                dialog = InputDialog("💉 SQL Injection", "Enter SQL code:", self, "Type your injection...")
                if dialog.exec_() == QDialog.Accepted:
                    ans = dialog.get_text()
                    success = (ans == "' OR 1=1 --" or ans == "' OR '1'='1")
                else:
                    success = False
            elif idx == 3:
                self.terminal_print("🧩 Logic Puzzle training...", "yellow")
                seq = [2, 4, 6, 8]
                self.terminal_print(f"Sequence: {', '.join(map(str, seq))}, ?", "yellow")
                dialog = InputDialog("🧩 Logic Puzzle", "Find the pattern:", self, "Type the missing number...")
                if dialog.exec_() == QDialog.Accepted:
                    try:
                        success = (int(dialog.get_text()) == 10)
                    except:
                        success = False
                else:
                    success = False
            if success:
                exp = diff * 3 + random.randint(1, 3)
                self.hacker.gain_exp(exp)
                self.terminal_print(f"✅ +{exp} EXP earned!", "green")
                self.update_display()
            else:
                self.terminal_print("💪 Keep practicing! You'll get it.", "yellow")
        else:
            self.terminal_print("❌ Training cancelled.", "red")
            
    def shop(self):
        self.terminal_print("\n🛒 TOOL SHOP", "yellow")
        self.terminal_print(f"💰 Credits: {self.hacker.credits}", "green")
        items = [
            {"name": "🔧 Advanced Scanner", "price": 100, "desc": "+2 password attempts"},
            {"name": "🛡️ Firewall Bypass", "price": 200, "desc": "Firewalls -1 difficulty"},
            {"name": "🔑 Crypto Key", "price": 300, "desc": "Reveals extra clues"},
            {"name": "⚡ Quantum Decryptor", "price": 500, "desc": "Auto-decrypts messages"},
            {"name": "🔬 Nano Analyzer", "price": 700, "desc": "Analyzes servers"},
            {"name": "🎯 Matrix Key", "price": 1000, "desc": "Access to elite servers"},
            {"name": "⏳ Chrono Analyzer", "price": 1500, "desc": "Predicts passwords"},
            {"name": "☯️ Omega Key", "price": 2500, "desc": "Full Omega access"},
            {"name": "🌀 Void Key", "price": 5000, "desc": "Void access"}
        ]
        options = []
        for item in items:
            owned = "✅ " if item['name'] in self.hacker.tools else "⬜ "
            options.append({"name": f"{owned}{item['name']} - {item['price']} credits", "item": item})
        dialog = SelectDialog(options, "🛒 TOOL SHOP", "Select a tool to buy:", self)
        if dialog.exec_() == QDialog.Accepted:
            selected = dialog.get_selected()
            if selected and 'item' in selected:
                item = selected['item']
                if item['name'] in self.hacker.tools:
                    self.terminal_print("⚠️ You already have this tool.", "yellow")
                elif self.hacker.credits >= item['price']:
                    self.hacker.credits -= item['price']
                    self.hacker.tools.append(item['name'])
                    self.terminal_print(f"✅ {item['name']} purchased!", "green")
                    self.update_display()
                else:
                    self.terminal_print(f"❌ Not enough credits. Need {item['price'] - self.hacker.credits} more.", "red")
        
    def show_stats(self):
        h = self.hacker
        self.terminal_print(f"\n📊 STATISTICS OF {h.name.upper()}", "blue")
        self.terminal_print(f"📈 Progress:", "green")
        self.terminal_print(f"  • Level: {h.level}", "white")
        self.terminal_print(f"  • EXP: {h.exp}/{h.exp_needed}", "white")
        self.terminal_print(f"  • Rank: {h.get_rank()}", "white")
        self.terminal_print(f"💰 Resources:", "green")
        self.terminal_print(f"  • Credits: {h.credits}", "white")
        self.terminal_print(f"  • Tools: {len(h.tools)}", "white")
        self.terminal_print(f"🎯 Missions:", "green")
        self.terminal_print(f"  • Completed: {h.missions_completed}", "white")
        self.terminal_print(f"  • Failed: {h.failures}", "white")
        self.terminal_print(f"  • Streak: {h.current_streak}", "white")
        self.terminal_print(f"  • Best streak: {h.best_streak}", "white")
        self.terminal_print(f"  • Unique servers: {len(set(h.hacked_servers))}/{len(SERVERS)}", "white")
        self.terminal_print(f"🖥️ Hacked servers:", "green")
        if h.hacked_servers:
            for s in sorted(set(h.hacked_servers)):
                self.terminal_print(f"  • ✅ {s}", "white")
        else:
            self.terminal_print(f"  • None yet", "gray")
        
    def show_ranking(self):
        self.terminal_print("\n🏆 HACKER RANKING", "yellow")
        opponents = [("Shadow", 8, 12), ("Neon", 7, 10), ("Vortex", 6, 8),
                    ("Ghost", 5, 7), ("Phoenix", 4, 5), ("Cipher", 3, 4)]
        self.terminal_print("Position │ Hacker │ Level │ Missions", "green")
        self.terminal_print("─" * 42, "gray")
        self.terminal_print(f"🏆 #1  │ {self.hacker.name} │ {self.hacker.level}     │ {self.hacker.missions_completed}", "green")
        for i, (name, level, missions) in enumerate(opponents, 2):
            self.terminal_print(f"#{i}  │ {name} │ {level}     │ {missions}", "white")
        self.terminal_print("─" * 42, "gray")
        self.terminal_print("💡 Complete more missions to climb the ranks!", "yellow")
            
    def settings(self):
        self.terminal_print("\n⚙️ SETTINGS", "blue")
        options = [
            {"name": "🎨 Change Theme", "desc": "Visual theme"},
            {"name": "👤 Change Name", "desc": "Your hacker name"},
            {"name": "🗑️ Delete Account", "desc": "Delete all data"},
            {"name": "🔙 Back", "desc": "Return to game"}
        ]
        dialog = SelectDialog(options, "⚙️ SETTINGS", "Select an option:", self)
        if dialog.exec_() == QDialog.Accepted:
            selected = dialog.get_selected()
            if not selected:
                return
            idx = options.index(selected) if selected in options else -1
            if idx == 0:
                themes = ["matrix", "cyberpunk", "classic", "dark"]
                theme_options = []
                for t in themes:
                    check = "✅ " if self.hacker.current_theme == t else "⬜ "
                    theme_options.append({"name": f"{check}{t}"})
                theme_dialog = SelectDialog(theme_options, "🎨 SELECT THEME", "Choose a visual theme:", self)
                if theme_dialog.exec_() == QDialog.Accepted:
                    t_idx = theme_dialog.list.currentRow()
                    if 0 <= t_idx < len(themes):
                        self.hacker.current_theme = themes[t_idx]
                        self.terminal_print(f"✅ Theme changed to: {themes[t_idx]}", "green")
            elif idx == 1:
                dialog = InputDialog("👤 Change Name", "Enter your new hacker name:", self, "New name...")
                if dialog.exec_() == QDialog.Accepted:
                    new_name = dialog.get_text()
                    if new_name:
                        self.hacker.name = new_name
                        self.setWindowTitle(f"🖥️ HACKER SIMULATOR 2077 - {self.hacker.name}")
                        with open(CONFIG_FILE, 'w') as f:
                            json.dump({"language": self.language, "name": self.hacker.name}, f, indent=4)
                        self.terminal_print(f"✅ Name changed to: {self.hacker.name}", "green")
                        self.update_display()
            elif idx == 2:
                self.terminal_print("⚠️ DELETE ACCOUNT - This will delete ALL your data!", "red")
                dialog = InputDialog("🗑️ Delete Account", "Type 'DELETE' to confirm:", self, "DELETE")
                if dialog.exec_() == QDialog.Accepted:
                    if dialog.get_text().upper() == "DELETE":
                        if os.path.exists(SAVE_FILE):
                            os.remove(SAVE_FILE)
                        if os.path.exists(CONFIG_FILE):
                            os.remove(CONFIG_FILE)
                        self.hacker = Hacker()
                        self.terminal_print("🗑️ Account deleted permanently.", "red")
                        self.update_display()
                    else:
                        self.terminal_print("❌ Deletion cancelled.", "yellow")
                        
    def save_game(self):
        if self.hacker.save_game():
            self.terminal_print("✅ Game saved successfully!", "green")
        else:
            self.terminal_print("❌ Error saving game.", "red")
            
    def show_guide(self):
        self.terminal_print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  📖 USER GUIDE                                              ║
╠═══════════════════════════════════════════════════════════════╣
║  🎯 WHAT IS IT?                                             ║
║  A terminal-style hacking game with a graphical interface.  ║
║                                                             ║
║  🕹️ HOW TO PLAY                                             ║
║  1. Click '🌐 Hack Server' to start a mission              ║
║  2. Evade the firewall (memorize the sequence)              ║
║  3. Crack the password using the clue                      ║
║  4. Earn credits and level up!                             ║
║                                                             ║
║  💡 TIPS                                                   ║
║  • Read clues carefully                                    ║
║  • Buy tools from the shop                                 ║
║  • Keep your streak for bonuses                            ║
║  • Do daily missions for double rewards                    ║
║                                                             ║
║  🔗 LINKS                                                  ║
║  • GitHub: {GITHUB_URL}                                         ║
║  • Issues: {GITHUB_URL}/issues                                 ║
╚═══════════════════════════════════════════════════════════════╝
""", "cyan")
        
    def exit_game(self):
        if self.hacker.save_game():
            self.terminal_print("💾 Game saved.", "green")
        self.terminal_print("👋 Goodbye, hacker!", "green")
        QTimer.singleShot(1000, self.close)

# ============================================
# MAIN
# ============================================

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("""
        QMainWindow { background-color: #0a0a0a; }
        QWidget { background-color: #0a0a0a; color: #00ff41; font-family: 'Courier New', monospace; }
        QToolTip { background-color: #1a1a1a; color: #00ff41; border: 1px solid #1a2a1a; }
    """)
    window = HackerUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()