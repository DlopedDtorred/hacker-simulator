#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - ULTIMATE EDITION v5.1
===============================================
"""

import random
import os
import time
import sys
import json
from datetime import datetime
from colorama import init, Fore, Back, Style

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

init(autoreset=True, convert=True)
os.system('cls' if os.name == 'nt' else 'clear')

VERSION = "5.1.0"
AUTOR = "DlopedDtorred"
GITHUB_URL = "https://github.com/DlopedDtorred/hacker-simulator"

# ============================================
# TEMAS (AHORA FUNCIONAN)
# ============================================

def aplicar_tema(tema):
    """Aplica un tema visual al juego."""
    temas = {
        "matrix": {
            "b1": Fore.GREEN, "b2": Fore.LIGHTGREEN_EX,
            "txt": Fore.WHITE, "ok": Fore.GREEN,
            "err": Fore.RED, "warn": Fore.YELLOW,
            "info": Fore.CYAN, "borde": "═"
        },
        "cyberpunk": {
            "b1": Fore.MAGENTA, "b2": Fore.LIGHTMAGENTA_EX,
            "txt": Fore.WHITE, "ok": Fore.GREEN,
            "err": Fore.RED, "warn": Fore.YELLOW,
            "info": Fore.BLUE, "borde": "▬"
        },
        "classic": {
            "b1": Fore.BLUE, "b2": Fore.LIGHTBLUE_EX,
            "txt": Fore.WHITE, "ok": Fore.GREEN,
            "err": Fore.RED, "warn": Fore.YELLOW,
            "info": Fore.CYAN, "borde": "─"
        },
        "dark": {
            "b1": Fore.LIGHTBLACK_EX, "b2": Fore.WHITE,
            "txt": Fore.WHITE, "ok": Fore.GREEN,
            "err": Fore.RED, "warn": Fore.YELLOW,
            "info": Fore.CYAN, "borde": "═"
        }
    }
    return temas.get(tema, temas["matrix"])

# ============================================
# 20 SERVIDORES (MÁS QUE NUNCA)
# ============================================

SERVIDORES = [
    # Nivel 1-3: Principiantes
    {
        "id": "SRV-001", "nombre": "MegaCorp Alpha",
        "dificultad": 1, "recompensa": 150,
        "pista": "🐱 Mascota del CEO (empieza con M)",
        "password": "michifu", "desc": "Servidor corporativo básico"
    },
    {
        "id": "SRV-002", "nombre": "DarkNet Vault",
        "dificultad": 2, "recompensa": 250,
        "pista": "👿 666 sin el 6 final",
        "password": "666", "desc": "Custodia en red oscura"
    },
    {
        "id": "SRV-003", "nombre": "ShadowNet",
        "dificultad": 2, "recompensa": 300,
        "pista": "🏢 Fundado en 2015",
        "password": "2015", "desc": "Red de datos sombra"
    },
    # Nivel 4-6: Intermedios
    {
        "id": "SRV-004", "nombre": "CyberDyne Systems",
        "dificultad": 3, "recompensa": 400,
        "pista": "🎬 Blade Runner se estrenó en...",
        "password": "2019", "desc": "Sistemas de IA"
    },
    {
        "id": "SRV-005", "nombre": "NeoTokyo Grid",
        "dificultad": 4, "recompensa": 600,
        "pista": "🇯🇵 Código postal Shibuya (7 dígitos)",
        "password": "1500042", "desc": "Red de ciudad digital"
    },
    {
        "id": "SRV-006", "nombre": "A.I. Core",
        "dificultad": 5, "recompensa": 1000,
        "pista": "🔢 Fibonacci posición 13",
        "password": "233", "desc": "Núcleo de inteligencia artificial"
    },
    # Nivel 7-9: Avanzados
    {
        "id": "SRV-007", "nombre": "Quantum Nexus",
        "dificultad": 6, "recompensa": 1500,
        "pista": "⚛️ Constante de Planck (3 dígitos)",
        "password": "662", "desc": "Servidor cuántico"
    },
    {
        "id": "SRV-008", "nombre": "NanoTech Labs",
        "dificultad": 7, "recompensa": 2000,
        "pista": "🔬 Número atómico del carbono",
        "password": "6", "desc": "Laboratorio nanotecnológico"
    },
    {
        "id": "SRV-009", "nombre": "Matrix Archive",
        "dificultad": 8, "recompensa": 3000,
        "pista": "🎬 Habitación de Neo (The Matrix)",
        "password": "303", "desc": "Archivo de la resistencia"
    },
    # Nivel 10-12: Expertos
    {
        "id": "SRV-010", "nombre": "ChronoCore",
        "dificultad": 9, "recompensa": 5000,
        "pista": "⏳ Descubrimiento del ADN (19XX)",
        "password": "1953", "desc": "Base de datos temporal"
    },
    {
        "id": "SRV-011", "nombre": "Omega Station",
        "dificultad": 10, "recompensa": 10000,
        "pista": "☯️ 666 × 7 = ?",
        "password": "4662", "desc": "El servidor definitivo"
    },
    {
        "id": "SRV-012", "nombre": "Void Network",
        "dificultad": 9, "recompensa": 4500,
        "pista": "🔮 7³ = ?",
        "password": "343", "desc": "Red en el vacío digital"
    },
    # Nivel 13-15: Legendarios
    {
        "id": "SRV-013", "nombre": "Eclipse Core",
        "dificultad": 11, "recompensa": 15000,
        "pista": "🌑 Primer eclipse total del siglo XXI",
        "password": "2001", "desc": "Núcleo de la sombra"
    },
    {
        "id": "SRV-014", "nombre": "Nebula Archive",
        "dificultad": 12, "recompensa": 20000,
        "pista": "🌌 Código postal NASA (5 dígitos)",
        "password": "77058", "desc": "Archivo espacial"
    },
    {
        "id": "SRV-015", "nombre": "Genesis Point",
        "dificultad": 13, "recompensa": 30000,
        "pista": "🌀 Primera computadora (19XX)",
        "password": "1941", "desc": "El origen de todo"
    },
    # Nivel 16-18: Épicos
    {
        "id": "SRV-016", "nombre": "Apollo Core",
        "dificultad": 14, "recompensa": 40000,
        "pista": "🚀 Año del primer alunizaje",
        "password": "1969", "desc": "Núcleo de la misión Apolo"
    },
    {
        "id": "SRV-017", "nombre": "Digital Abyss",
        "dificultad": 15, "recompensa": 50000,
        "pista": "🌊 Profundidad máxima del océano (metros)",
        "password": "11034", "desc": "El abismo digital"
    },
    {
        "id": "SRV-018", "nombre": "Phoenix Protocol",
        "dificultad": 16, "recompensa": 75000,
        "pista": "🔥 Año de resurrección de la serie",
        "password": "2002", "desc": "Protocolo de resurrección"
    },
    # Nivel 19-20: Dioses
    {
        "id": "SRV-019", "nombre": "Eternal Archive",
        "dificultad": 18, "recompensa": 100000,
        "pista": "∞ Número de la eternidad (símbolo)",
        "password": "8", "desc": "Archivo eterno"
    },
    {
        "id": "SRV-020", "nombre": "Omega Point",
        "dificultad": 20, "recompensa": 200000,
        "pista": "☯️ 666 × 666 = ?",
        "password": "443556", "desc": "El punto final de todo"
    }
]

# ============================================
# LOGROS (25+)
# ============================================

LOGROS = {
    "primer_hackeo": {"nombre": "🚀 Primer Hackeo", "desc": "Completa tu primera misión", "recompensa": 50},
    "cinco_misiones": {"nombre": "💪 Cinco Misiones", "desc": "Completa 5 misiones", "recompensa": 100},
    "diez_misiones": {"nombre": "🏆 Diez Misiones", "desc": "Completa 10 misiones", "recompensa": 200},
    "veinticinco_misiones": {"nombre": "👑 Leyenda", "desc": "Completa 25 misiones", "recompensa": 500},
    "cincuenta_misiones": {"nombre": "🌟 Maestro", "desc": "Completa 50 misiones", "recompensa": 1000},
    "cien_misiones": {"nombre": "💎 Dios", "desc": "Completa 100 misiones", "recompensa": 5000},
    "nivel_5": {"nombre": "⚡ Nivel 5", "desc": "Alcanza el nivel 5", "recompensa": 150},
    "nivel_10": {"nombre": "🌟 Nivel 10", "desc": "Alcanza el nivel 10", "recompensa": 300},
    "nivel_15": {"nombre": "👑 Nivel 15", "desc": "Alcanza el nivel 15", "recompensa": 500},
    "nivel_20": {"nombre": "💎 Nivel 20", "desc": "Alcanza el nivel 20", "recompensa": 1000},
    "nivel_30": {"nombre": "🔥 Nivel 30", "desc": "Alcanza el nivel 30", "recompensa": 5000},
    "millonario": {"nombre": "💰 Millonario", "desc": "Acumula 1000 créditos", "recompensa": 100},
    "billonario": {"nombre": "💎 Billonario", "desc": "Acumula 5000 créditos", "recompensa": 300},
    "trillonario": {"nombre": "👑 Trillonario", "desc": "Acumula 10000 créditos", "recompensa": 500},
    "multimillonario": {"nombre": "💸 Multimillonario", "desc": "Acumula 50000 créditos", "recompensa": 2000},
    "perfecto": {"nombre": "🎯 Perfecto", "desc": "Completa 5 misiones sin fallar", "recompensa": 200},
    "racha_5": {"nombre": "🔥 Racha 5", "desc": "5 misiones seguidas", "recompensa": 100},
    "racha_10": {"nombre": "🔥🔥 Racha 10", "desc": "10 misiones seguidas", "recompensa": 200},
    "racha_20": {"nombre": "🔥🔥🔥 Racha 20", "desc": "20 misiones seguidas", "recompensa": 500},
    "racha_50": {"nombre": "🔥🔥🔥🔥 Racha 50", "desc": "50 misiones seguidas", "recompensa": 2000},
    "coleccionista": {"nombre": "🛠️ Coleccionista", "desc": "Todas las herramientas", "recompensa": 500},
    "omega": {"nombre": "☯️ Omega", "desc": "Completa Omega Station", "recompensa": 1000},
    "leyenda": {"nombre": "⚡ Leyenda", "desc": "Completa todos los servidores", "recompensa": 5000},
    "dios": {"nombre": "👑 Dios", "desc": "Completa Omega Point", "recompensa": 10000},
    "explorador": {"nombre": "🧭 Explorador", "desc": "Hackea 10 servidores diferentes", "recompensa": 300},
    "velocidad": {"nombre": "🏃 Velocidad", "desc": "Completa 3 misiones en 1 minuto", "recompensa": 500}
}

# ============================================
# CLASE HACKER
# ============================================

class Hacker:
    def __init__(self, nombre=None):
        self.nombre = nombre or "Zero_Cool"
        self.nivel = 1
        self.exp = 0
        self.exp_necesaria = 10
        self.creditos = 50
        self.herramientas = ["🔧 Escáner básico"]
        self.misiones_completadas = 0
        self.fallos = 0
        self.racha_actual = 0
        self.mejor_racha = 0
        self.servidores_hackeados = []
        self.logros_desbloqueados = []
        self.tema_actual = "matrix"
        self.ultima_mision = None
        self.mision_diaria_completada = False
        self.ultima_mision_diaria = None
        self.tiempo_jugado = 0
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.nivel_maximo_alcanzado = 1
        
    def ganar_exp(self, cantidad):
        self.exp += cantidad
        while self.exp >= self.exp_necesaria:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.nivel_maximo_alcanzado = self.nivel
        self.exp = 0
        self.exp_necesaria = self.nivel * 15
        
        print(f"\n{Fore.MAGENTA}{'═'*50}")
        print(f"🌟 ¡SUBES AL NIVEL {self.nivel}! 🌟")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        if self.nivel % 2 == 0:
            self._dar_herramienta()
        
        if self.nivel % 3 == 0:
            bonus = self.nivel * 50
            self.creditos += bonus
            print(f"{Fore.GREEN}💰 Bonus de nivel: +{bonus} créditos{Style.RESET_ALL}")
        
        if self.nivel % 5 == 0:
            print(f"{Fore.YELLOW}🎁 ¡Recompensa especial por nivel {self.nivel}!{Style.RESET_ALL}")
            self.creditos += 200
            if self.nivel % 10 == 0:
                self.creditos += 500
                print(f"{Fore.CYAN}🌟 ¡BONUS EXTRA DE 500 CRÉDITOS!{Style.RESET_ALL}")
    
    def _dar_herramienta(self):
        herramientas = [
            "🔧 Escáner Avanzado", "🛡️ Firewall Bypass", "🔑 Crypto Key",
            "⚡ Quantum Decryptor", "🔬 Nano Analyzer", "🎯 Matrix Key",
            "⏳ Chrono Analyzer", "☯️ Omega Key", "🌀 Void Key"
        ]
        
        idx = (self.nivel // 2 - 1) % len(herramientas)
        nueva = herramientas[idx]
        
        if nueva not in self.herramientas:
            self.herramientas.append(nueva)
            print(f"{Fore.CYAN}🔧 ¡Nueva herramienta: {nueva}!{Style.RESET_ALL}")
    
    def verificar_logros(self):
        nuevos_logros = []
        
        # Misiones
        if self.misiones_completadas >= 1 and "primer_hackeo" not in self.logros_desbloqueados:
            nuevos_logros.append("primer_hackeo")
        if self.misiones_completadas >= 5 and "cinco_misiones" not in self.logros_desbloqueados:
            nuevos_logros.append("cinco_misiones")
        if self.misiones_completadas >= 10 and "diez_misiones" not in self.logros_desbloqueados:
            nuevos_logros.append("diez_misiones")
        if self.misiones_completadas >= 25 and "veinticinco_misiones" not in self.logros_desbloqueados:
            nuevos_logros.append("veinticinco_misiones")
        if self.misiones_completadas >= 50 and "cincuenta_misiones" not in self.logros_desbloqueados:
            nuevos_logros.append("cincuenta_misiones")
        if self.misiones_completadas >= 100 and "cien_misiones" not in self.logros_desbloqueados:
            nuevos_logros.append("cien_misiones")
        
        # Nivel
        if self.nivel >= 5 and "nivel_5" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_5")
        if self.nivel >= 10 and "nivel_10" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_10")
        if self.nivel >= 15 and "nivel_15" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_15")
        if self.nivel >= 20 and "nivel_20" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_20")
        if self.nivel >= 30 and "nivel_30" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_30")
        
        # Créditos
        if self.creditos >= 1000 and "millonario" not in self.logros_desbloqueados:
            nuevos_logros.append("millonario")
        if self.creditos >= 5000 and "billonario" not in self.logros_desbloqueados:
            nuevos_logros.append("billonario")
        if self.creditos >= 10000 and "trillonario" not in self.logros_desbloqueados:
            nuevos_logros.append("trillonario")
        if self.creditos >= 50000 and "multimillonario" not in self.logros_desbloqueados:
            nuevos_logros.append("multimillonario")
        
        # Rachas
        if self.mejor_racha >= 5 and "racha_5" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_5")
        if self.mejor_racha >= 10 and "racha_10" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_10")
        if self.mejor_racha >= 20 and "racha_20" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_20")
        if self.mejor_racha >= 50 and "racha_50" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_50")
        
        # Perfecto
        if self.misiones_completadas >= 5 and self.fallos == 0 and "perfecto" not in self.logros_desbloqueados:
            nuevos_logros.append("perfecto")
        
        # Coleccionista
        if len(self.herramientas) >= 9 and "coleccionista" not in self.logros_desbloqueados:
            nuevos_logros.append("coleccionista")
        
        # Omega
        if "Omega Station" in self.servidores_hackeados and "omega" not in self.logros_desbloqueados:
            nuevos_logros.append("omega")
        
        # Explorador
        if len(set(self.servidores_hackeados)) >= 10 and "explorador" not in self.logros_desbloqueados:
            nuevos_logros.append("explorador")
        
        # Leyenda
        if len(set(self.servidores_hackeados)) >= len(SERVIDORES) and "leyenda" not in self.logros_desbloqueados:
            nuevos_logros.append("leyenda")
        
        # Dios
        if "Omega Point" in self.servidores_hackeados and "dios" not in self.logros_desbloqueados:
            nuevos_logros.append("dios")
        
        # Desbloquear logros
        for logro_id in nuevos_logros:
            self.logros_desbloqueados.append(logro_id)
            logro = LOGROS[logro_id]
            print(f"{Fore.YELLOW}🏆 ¡LOGRO DESBLOQUEADO: {logro['nombre']}!{Style.RESET_ALL}")
            print(f"{Fore.WHITE}   📝 {logro['desc']}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}   💰 Recompensa: +{logro['recompensa']} créditos{Style.RESET_ALL}")
            self.creditos += logro['recompensa']
    
    def calcular_rango(self):
        if self.nivel >= 25:
            return "👑 LEGENDARY HACKER"
        elif self.nivel >= 20:
            return "⚡ ELITE HACKER"
        elif self.nivel >= 15:
            return "🔥 SENIOR HACKER"
        elif self.nivel >= 10:
            return "💻 JUNIOR HACKER"
        elif self.nivel >= 5:
            return "🔰 APRENDIZ"
        else:
            return "🐣 NOVATO"
    
    def guardar(self, filename="save.json"):
        datos = {
            "nombre": self.nombre, "nivel": self.nivel, "exp": self.exp,
            "exp_necesaria": self.exp_necesaria, "creditos": self.creditos,
            "herramientas": self.herramientas, "misiones_completadas": self.misiones_completadas,
            "fallos": self.fallos, "racha_actual": self.racha_actual,
            "mejor_racha": self.mejor_racha, "servidores_hackeados": self.servidores_hackeados,
            "logros_desbloqueados": self.logros_desbloqueados, "tema_actual": self.tema_actual,
            "ultima_mision": self.ultima_mision,
            "mision_diaria_completada": self.mision_diaria_completada,
            "ultima_mision_diaria": self.ultima_mision_diaria,
            "tiempo_jugado": self.tiempo_jugado, "fecha_creacion": self.fecha_creacion,
            "nivel_maximo_alcanzado": self.nivel_maximo_alcanzado, "version": VERSION
        }
        try:
            with open(filename, 'w') as f:
                json.dump(datos, f, indent=4)
            return True
        except:
            return False
    
    def cargar(self, filename="save.json"):
        try:
            with open(filename, 'r') as f:
                datos = json.load(f)
            for key, value in datos.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            return True
        except:
            return False
    
    def __str__(self):
        tema = aplicar_tema(self.tema_actual)
        if self.exp_necesaria > 0:
            barra = "█" * int((self.exp / self.exp_necesaria) * 15)
            vacio = "░" * (15 - len(barra))
        else:
            barra = ""
            vacio = "░" * 15
        
        return f"""
{tema['b1']}╔══════════════════════════════════════════════════════════╗
{tema['b1']}║ {tema['txt']}👤 {self.nombre} {tema['b1']}│ {tema['ok']}Nv.{self.nivel} {tema['b1']}│ {tema['warn']}💰 {self.creditos} créditos
{tema['b1']}║ {tema['txt']}📊 EXP [{barra}{vacio}] {self.exp}/{self.exp_necesaria}
{tema['b1']}║ {tema['txt']}🏆 {self.calcular_rango()}
{tema['b1']}║ {tema['txt']}🛠️  {', '.join(self.herramientas)}
{tema['b1']}║ {tema['txt']}📈 Rachas: {self.racha_actual} actual │ {self.mejor_racha} máxima
{tema['b1']}║ {tema['txt']}🎯 Misiones: {self.misiones_completadas} │ ❌ Fallos: {self.fallos}
{tema['b1']}║ {tema['txt']}🗺️  Servidores hackeados: {len(set(self.servidores_hackeados))}/{len(SERVIDORES)}
{tema['b1']}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

# ============================================
# MINI-JUEGOS (MEJORADOS)
# ============================================

class MiniJuegos:
    @staticmethod
    def firewall_memoria(dificultad, intentos_max):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔥 ¡FIREWALL DETECTADO! Memoriza la secuencia:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🛡️  Tienes {intentos_max} intentos{Style.RESET_ALL}")
        
        longitud = min(3 + dificultad // 2, 8)
        secuencia = [str(random.randint(1, 9)) for _ in range(longitud)]
        
        for intento in range(intentos_max):
            print(f"\n{Fore.CYAN}🧠 Intento {intento+1}/{intentos_max}:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}╔{'═' * (longitud * 2 + 2)}╗")
            print(f"║ {' '.join(secuencia)} ║")
            print(f"╚{'═' * (longitud * 2 + 2)}╝{Style.RESET_ALL}")
            
            print(f"\n{Fore.YELLOW}⏳ Memoriza... tienes 2 segundos{Style.RESET_ALL}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"{Fore.CYAN}⌨️  Repite la secuencia (números separados por espacio):{Style.RESET_ALL}")
            respuesta = input("➡️  ").strip().split()
            
            if respuesta == secuencia:
                print(f"{Fore.GREEN}✅ ¡Firewall evadido!{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
                if intento < intentos_max - 1:
                    print(f"{Fore.YELLOW}💡 La secuencia era: {' '.join(secuencia)}{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 Has sido detectado.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def descifrar_cesar(dificultad):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔐 ¡CÓDIGO ENCRIPTADO! Descifra el mensaje:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        palabras = ["HACKER", "SISTEMA", "SEGURO", "DATOS", "RED", "CYBER", 
                   "NEXUS", "QUANTUM", "MATRIX", "OMEGA", "SHADOW", "VOID",
                   "NEBULA", "GENESIS", "APOLLO"]
        palabra = random.choice(palabras)
        
        desplazamiento = random.randint(1, 5) + dificultad // 2
        encriptado = ""
        for letra in palabra:
            if letra.isalpha():
                codigo = ord(letra) - desplazamiento
                if codigo < 65:
                    codigo += 26
                encriptado += chr(codigo)
            else:
                encriptado += letra
        
        print(f"{Fore.CYAN}📨 Mensaje encriptado:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}╔{'═' * (len(encriptado) + 4)}╗")
        print(f"║  {encriptado}  ║")
        print(f"╚{'═' * (len(encriptado) + 4)}╝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔑 Pista: Desplazamiento César (1-{5 + dificultad // 2}){Style.RESET_ALL}")
        
        intentos = 3
        while intentos > 0:
            print(f"\n{Fore.CYAN}💡 Intentos restantes: {intentos}{Style.RESET_ALL}")
            respuesta = input("➡️  Mensaje descifrado: ").strip().upper()
            
            if respuesta == palabra:
                print(f"{Fore.GREEN}✅ ¡Correcto!{Style.RESET_ALL}")
                return True
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 No has podido descifrar.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def inyeccion_sql(dificultad):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"💉 ¡VULNERABILIDAD SQL! Inyecta el código:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        tablas = ["usuarios", "datos", "admin", "sistema", "logs", "config", 
                 "credenciales", "empleados", "clientes"]
        tabla = random.choice(tablas)
        
        codigos = [
            f"SELECT * FROM {tabla} WHERE 1=1; --",
            f"' OR '1'='1", f"'; DROP TABLE {tabla}; --",
            f"' UNION SELECT null,null,null--", f"' OR 1=1 --"
        ]
        
        codigo_correcto = random.choice(codigos)
        
        print(f"{Fore.CYAN}💻 Objetivo: Acceder a '{tabla}'{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔍 Pista: Código SQL siempre verdadero{Style.RESET_ALL}")
        
        intentos = 3
        while intentos > 0:
            print(f"\n{Fore.CYAN}💡 Intentos restantes: {intentos}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📝 Introduce tu código SQL (help para ayuda):{Style.RESET_ALL}")
            respuesta = input("➡️  ").strip()
            
            if respuesta.lower() == 'help':
                print(f"{Fore.YELLOW}💡 Ejemplos:")
                print("  - ' OR '1'='1")
                print("  - SELECT * FROM tabla WHERE 1=1; --")
                print("  - '; DROP TABLE tabla; --")
                continue
            
            if respuesta == codigo_correcto:
                print(f"{Fore.GREEN}✅ ¡Inyección exitosa!{Style.RESET_ALL}")
                return True
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 Has sido bloqueado.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def puzzle_logico(dificultad):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🧩 ¡PUZZLE LÓGICO! Encuentra el número:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        tipos = ["suma", "multiplica", "fibonacci", "cuadrados", "primos", "pares", "impares"]
        tipo = random.choice(tipos)
        
        if tipo == "suma":
            inc = random.randint(2, 5)
            ini = random.randint(1, 10)
            sec = [ini + i * inc for i in range(4)]
            resp = sec[-1] + inc
            pista = f"Suma {inc} cada vez"
        elif tipo == "multiplica":
            mult = random.randint(2, 4)
            ini = random.randint(1, 3)
            sec = [ini * (mult ** i) for i in range(4)]
            resp = sec[-1] * mult
            pista = f"Multiplica por {mult}"
        elif tipo == "fibonacci":
            sec = [1, 1, 2, 3, 5]
            resp = 8
            pista = "Fibonacci: suma de los dos anteriores"
        elif tipo == "cuadrados":
            sec = [1, 4, 9, 16, 25]
            resp = 36
            pista = "Números al cuadrado: 1², 2², 3²..."
        elif tipo == "primos":
            sec = [2, 3, 5, 7, 11]
            resp = 13
            pista = "Números primos en orden"
        elif tipo == "pares":
            sec = [2, 4, 6, 8, 10]
            resp = 12
            pista = "Números pares en orden"
        else:
            sec = [1, 3, 5, 7, 9]
            resp = 11
            pista = "Números impares en orden"
        
        print(f"{Fore.CYAN}📊 Secuencia:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}╔{'═' * (len(sec) * 5 + 10)}╗")
        print(f"║  {'  →  '.join(map(str, sec))}  →  ?  ║")
        print(f"╚{'═' * (len(sec) * 5 + 10)}╝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💡 Pista: {pista}{Style.RESET_ALL}")
        
        intentos = 3
        while intentos > 0:
            print(f"\n{Fore.CYAN}💡 Intentos restantes: {intentos}{Style.RESET_ALL}")
            try:
                usuario = int(input("➡️  Número que falta: ").strip())
                if usuario == resp:
                    print(f"{Fore.GREEN}✅ ¡Correcto!{Style.RESET_ALL}")
                    return True
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}❌ Introduce un número.{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 No has podido resolver.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Respuesta: {resp}{Style.RESET_ALL}")
        return False

# ============================================
# FUNCIONES DEL JUEGO
# ============================================

def mostrar_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════════════════════╗
{Fore.GREEN}║  {Fore.CYAN}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗  {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}███████║███████║██║     █████╔╝ █████╗  ██████╔╝ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {Fore.GREEN}       ║
{Fore.GREEN}║     {Fore.YELLOW}HACKER SIMULATOR 2077 - ULTIMATE EDITION v{VERSION}{Fore.GREEN}     ║
{Fore.GREEN}║     {Fore.WHITE}by {AUTOR} {Fore.GREEN}| {Fore.CYAN}⭐ {GITHUB_URL}{Fore.GREEN}     ║
{Fore.GREEN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
""")

def mision_hackeo(hacker, servidor):
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.GREEN}🎯 MISIÓN: HACKEAR {servidor['nombre'].upper()}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}📋 ID: {servidor['id']}")
    print(f"⭐ Dificultad: {servidor['dificultad']} ★")
    print(f"💰 Recompensa: {servidor['recompensa']} créditos")
    print(f"📝 {servidor['desc']}")
    print(f"🔍 PISTA: {Fore.WHITE}{servidor['pista']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    # FASE 1: Firewall
    print(f"\n{Fore.CYAN}🛡️  FASE 1: ELUDIR FIREWALL{Style.RESET_ALL}")
    intentos_firewall = max(3, 5 - servidor['dificultad'] // 2)
    
    if not MiniJuegos.firewall_memoria(servidor['dificultad'], intentos_firewall):
        print(f"\n{Fore.RED}💀 Misión fallida.{Style.RESET_ALL}")
        hacker.fallos += 1
        hacker.racha_actual = 0
        return False
    
    # FASE 2: Contraseña
    print(f"\n{Fore.CYAN}🔑 FASE 2: DESCIFRAR CONTRASEÑA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💡 Pista: {servidor['pista']}{Style.RESET_ALL}")
    
    intentos = max(3, 5 - servidor['dificultad'] + 1)
    acertado = False
    
    while intentos > 0 and not acertado:
        print(f"\n{Fore.CYAN}🔐 Intentos: {intentos}{Style.RESET_ALL}")
        
        if "🔑 Crypto Key" in hacker.herramientas:
            print(f"{Fore.YELLOW}💡 'help' para pista extra{Style.RESET_ALL}")
        
        password = input("➡️  Contraseña: ").strip().lower()
        
        if password == 'help' and "🔑 Crypto Key" in hacker.herramientas:
            print(f"{Fore.CYAN}💡 Tamaño: {len(servidor['password'])} caracteres{Style.RESET_ALL}")
            continue
        
        if password == servidor['password']:
            acertado = True
            print(f"{Fore.GREEN}✅ ¡Acceso concedido!{Style.RESET_ALL}")
        else:
            intentos -= 1
            if intentos > 0:
                print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
    
    if not acertado:
        print(f"\n{Fore.RED}💀 Fallaste.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🔑 Contraseña: {servidor['password']}{Style.RESET_ALL}")
        hacker.fallos += 1
        hacker.racha_actual = 0
        return False
    
    # FASE 3: Extra (dificultad >= 5)
    if servidor['dificultad'] >= 5:
        print(f"\n{Fore.CYAN}🕵️  FASE 3: SEGURIDAD EXTRA{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⚠️  Protección adicional...{Style.RESET_ALL}")
        
        mini_juego = random.choice([
            MiniJuegos.descifrar_cesar,
            MiniJuegos.inyeccion_sql,
            MiniJuegos.puzzle_logico
        ])
        
        if not mini_juego(servidor['dificultad']):
            print(f"{Fore.RED}💀 Descubierto.{Style.RESET_ALL}")
            hacker.fallos += 1
            hacker.racha_actual = 0
            return False
    
    # COMPLETADA
    print(f"\n{Fore.GREEN}{'═'*50}")
    print(f"🎉 ¡MISIÓN COMPLETADA! 🎉")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
    recompensa = servidor['recompensa']
    bonus = min(hacker.racha_actual * 25, 200)
    total = recompensa + bonus
    
    if hacker.nivel >= 5:
        total = int(total * 1.2)
    
    hacker.creditos += total
    hacker.misiones_completadas += 1
    hacker.racha_actual += 1
    
    if hacker.racha_actual > hacker.mejor_racha:
        hacker.mejor_racha = hacker.racha_actual
    
    if servidor['nombre'] not in hacker.servidores_hackeados:
        hacker.servidores_hackeados.append(servidor['nombre'])
    
    hacker.ultima_mision = servidor['nombre']
    
    exp = servidor['dificultad'] * 5 + hacker.racha_actual * 2
    hacker.ganar_exp(exp)
    
    print(f"{Fore.GREEN}💰 +{total} créditos")
    print(f"{Fore.GREEN}📈 +{exp} EXP")
    if bonus > 0:
        print(f"{Fore.GREEN}🔥 Bonus racha: +{bonus} créditos")
    if hacker.racha_actual >= 3:
        print(f"{Fore.MAGENTA}🔥 ¡Racha de {hacker.racha_actual}!{Style.RESET_ALL}")
    
    hacker.verificar_logros()
    return True

def mision_diaria(hacker):
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"📅 MISIÓN DIARIA")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
    if hacker.mision_diaria_completada:
        print(f"{Fore.YELLOW}⚠️ Ya completaste la de hoy.{Style.RESET_ALL}")
        input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        return
    
    disponibles = [s for s in SERVIDORES if s['dificultad'] <= 5]
    servidor = random.choice(disponibles)
    
    print(f"{Fore.YELLOW}🌟 Misión de hoy:{Style.RESET_ALL}")
    print(f"🎯 {servidor['nombre']} (★{servidor['dificultad']})")
    print(f"💰 Recompensa: {servidor['recompensa'] * 2} créditos (¡DOBLE!){Style.RESET_ALL}")
    print(f"🔍 Pista: {servidor['pista']}{Style.RESET_ALL}")
    
    # Firewall
    print(f"\n{Fore.CYAN}🛡️  FIREWALL{Style.RESET_ALL}")
    if not MiniJuegos.firewall_memoria(servidor['dificultad'], 4):
        print(f"{Fore.RED}💀 Fallaste.{Style.RESET_ALL}")
        return
    
    # Contraseña
    print(f"\n{Fore.CYAN}🔑 CONTRASEÑA{Style.RESET_ALL}")
    intentos = 3
    acertado = False
    
    while intentos > 0 and not acertado:
        print(f"\n{Fore.CYAN}🔐 Intentos: {intentos}{Style.RESET_ALL}")
        password = input("➡️  Contraseña: ").strip().lower()
        
        if password == servidor['password']:
            acertado = True
            print(f"{Fore.GREEN}✅ ¡Correcto!{Style.RESET_ALL}")
        else:
            intentos -= 1
            if intentos > 0:
                print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
    
    if not acertado:
        print(f"{Fore.RED}💀 Fallaste.{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.GREEN}🎉 ¡MISIÓN DIARIA COMPLETADA!{Style.RESET_ALL}")
    
    recompensa = servidor['recompensa'] * 2
    hacker.creditos += recompensa
    hacker.misiones_completadas += 1
    hacker.mision_diaria_completada = True
    hacker.ultima_mision_diaria = datetime.now().strftime("%Y-%m-%d")
    
    exp = servidor['dificultad'] * 8
    hacker.ganar_exp(exp)
    
    print(f"{Fore.GREEN}💰 +{recompensa} créditos (¡DOBLE!)")
    print(f"{Fore.GREEN}📈 +{exp} EXP{Style.RESET_ALL}")
    
    hacker.verificar_logros()
    input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

def tienda(hacker):
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"🛒 TIENDA DE HERRAMIENTAS")
    print(f"{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}💰 Créditos: {hacker.creditos}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🛠️  Tus herramientas: {', '.join(hacker.herramientas)}{Style.RESET_ALL}")
    print(f"{'═'*50}")
    
    items = [
        {"nombre": "🔧 Escáner Avanzado", "precio": 100, "desc": "+2 intentos"},
        {"nombre": "🛡️ Firewall Bypass", "precio": 200, "desc": "Firewall -1"},
        {"nombre": "🔑 Crypto Key", "precio": 300, "desc": "Pistas extra"},
        {"nombre": "⚡ Quantum Decryptor", "precio": 500, "desc": "Descifra automático"},
        {"nombre": "🔬 Nano Analyzer", "precio": 700, "desc": "Analiza servidores"},
        {"nombre": "🎯 Matrix Key", "precio": 1000, "desc": "Acceso élite"},
        {"nombre": "⏳ Chrono Analyzer", "precio": 1500, "desc": "Predice contraseñas"},
        {"nombre": "☯️ Omega Key", "precio": 2500, "desc": "Acceso Omega"},
        {"nombre": "🌀 Void Key", "precio": 5000, "desc": "Acceso Void"}
    ]
    
    for i, item in enumerate(items, 1):
        estado = "✅" if item['nombre'] in hacker.herramientas else "❌"
        print(f"[{i}] {estado} {item['nombre']}")
        print(f"    {Fore.WHITE}💰 {item['precio']} créditos │ 📝 {item['desc']}{Style.RESET_ALL}")
    
    print("[9] 💰 Comprar EXP (100 créditos = 10 EXP)")
    print("[0] 🚪 Salir")
    
    try:
        opcion = int(input("\n➡️  ").strip())
        
        if opcion == 0:
            return
        elif opcion == 9:
            if hacker.creditos >= 100:
                hacker.creditos -= 100
                hacker.ganar_exp(10)
                print(f"{Fore.GREEN}✅ +10 EXP{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Sin créditos{Style.RESET_ALL}")
            time.sleep(1)
            return
        elif 1 <= opcion <= len(items):
            item = items[opcion-1]
            if item['nombre'] in hacker.herramientas:
                print(f"{Fore.YELLOW}⚠️ Ya la tienes{Style.RESET_ALL}")
            elif hacker.creditos >= item['precio']:
                hacker.creditos -= item['precio']
                hacker.herramientas.append(item['nombre'])
                print(f"{Fore.GREEN}✅ ¡Comprado!{Style.RESET_ALL}")
                hacker.verificar_logros()
            else:
                print(f"{Fore.RED}❌ Sin créditos{Style.RESET_ALL}")
            time.sleep(1)
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)
    except:
        print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
        time.sleep(1)

def estadisticas(hacker):
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}📊 ESTADÍSTICAS DE {hacker.nombre.upper()}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    print(f"{Fore.WHITE}📈 Progreso:")
    print(f"  • Nivel: {hacker.nivel}")
    print(f"  • EXP: {hacker.exp}/{hacker.exp_necesaria}")
    print(f"  • Rango: {hacker.calcular_rango()}")
    
    print(f"\n{Fore.WHITE}💰 Recursos:")
    print(f"  • Créditos: {hacker.creditos}")
    print(f"  • Herramientas: {len(hacker.herramientas)}")
    
    print(f"\n{Fore.WHITE}🎯 Misiones:")
    print(f"  • Completadas: {hacker.misiones_completadas}")
    print(f"  • Fallidas: {hacker.fallos}")
    print(f"  • Racha actual: {hacker.racha_actual}")
    print(f"  • Mejor racha: {hacker.mejor_racha}")
    print(f"  • Servidores únicos: {len(set(hacker.servidores_hackeados))}/{len(SERVIDORES)}")
    
    print(f"\n{Fore.WHITE}🖥️  Servidores hackeados:")
    if hacker.servidores_hackeados:
        for s in sorted(set(hacker.servidores_hackeados)):
            print(f"  • ✅ {s}")
    else:
        print(f"  • Ninguno")
    
    print(f"\n{Fore.WHITE}🏆 Logros ({len(hacker.logros_desbloqueados)}/{len(LOGROS)}):")
    if hacker.logros_desbloqueados:
        for logro_id in hacker.logros_desbloqueados:
            logro = LOGROS[logro_id]
            print(f"  • {logro['nombre']}")
    else:
        print(f"  • Ninguno")
    
    print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")

def ranking(hacker):
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}🏆 RANKING DE HACKERS")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
    oponentes = [
        ("Shadow", 8, 12), ("Neon", 7, 10), ("Vortex", 6, 8),
        ("Ghost", 5, 7), ("Phoenix", 4, 5), ("Cipher", 3, 4),
        ("Nova", 9, 15), ("Crystal", 11, 18), ("Zen", 12, 20),
        ("Omega", 15, 25), ("Dark", 13, 22), ("Light", 10, 16)
    ]
    
    print(f"{Fore.WHITE}Posición │ Hacker │ Nivel │ Misiones{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    print(f"{Fore.GREEN}🏆 #1  │ {hacker.nombre} │ {hacker.nivel}     │ {hacker.misiones_completadas}{Style.RESET_ALL}")
    
    for i, (nombre, nivel, misiones) in enumerate(oponentes, 2):
        if random.random() > 0.2:
            print(f"#{i}  │ {nombre} │ {nivel}     │ {misiones}")
    
    print(f"\n{Fore.CYAN}💡 Completa misiones para subir.{Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

def cambiar_tema(hacker):
    temas_disponibles = ["matrix", "cyberpunk", "classic", "dark"]
    
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"🎨 CAMBIAR TEMA")
    print(f"{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Tema actual: {hacker.tema_actual}{Style.RESET_ALL}")
    
    for i, tema in enumerate(temas_disponibles, 1):
        check = "✅" if hacker.tema_actual == tema else "  "
        print(f"[{i}] {check} {tema}")
    print("[0] Cancelar")
    
    try:
        opcion = int(input("\n➡️  ").strip())
        if opcion == 0:
            return
        elif 1 <= opcion <= len(temas_disponibles):
            hacker.tema_actual = temas_disponibles[opcion-1]
            print(f"{Fore.GREEN}✅ Tema cambiado a: {hacker.tema_actual}{Style.RESET_ALL}")
            time.sleep(1)
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)
    except:
        print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
        time.sleep(1)

def guia_usuario():
    print(f"\n{Fore.CYAN}{'═'*60}")
    print(f"{Fore.YELLOW}📖 GUÍA DE USUARIO")
    print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
    
    print(f"""
{Fore.WHITE}🎯 ¿QUÉ ES?
Un juego de hacking en terminal. Hackea servidores, evita firewalls
y descifra contraseñas usando pistas.

{Fore.CYAN}🕹️  CONTROLES{Fore.WHITE}
1 - Hackear servidor
2 - Misión diaria (DOBLE recompensa)
3 - Entrenar
4 - Tienda
5 - Estadísticas
6 - Ranking
7 - Configuración (temas)
8 - Guardar partida
9 - Guía de usuario
0 - Salir

{Fore.YELLOW}💡 CONSEJOS{Fore.WHITE}
• Las pistas son CLAVE para descifrar contraseñas
• Compra herramientas en la tienda
• Mantén la racha para bonificaciones
• Misiones diarias = DOBLE recompensa
• Los logros dan créditos extra

{Fore.GREEN}⚡ TECNOLOGÍAS{Fore.WHITE}
• Python 3.8+
• Colorama (colores)
• JSON (guardado)

{Fore.CYAN}🔗 ENLACES{Fore.WHITE}
• GitHub: {GITHUB_URL}
• Issues: {GITHUB_URL}/issues

{Fore.MAGENTA}🙏 ¡GRACIAS POR JUGAR!{Style.RESET_ALL}
""")
    input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

# ============================================
# MENÚ PRINCIPAL
# ============================================

def menu_principal(hacker):
    while True:
        mostrar_header()
        print(hacker)
        
        print(f"\n{Fore.CYAN}📡 OPCIONES:{Style.RESET_ALL}")
        print("[1] 🌐 Hackear servidor")
        print("[2] 📅 Misión diaria (¡DOBLE!)")
        print("[3] 🛠️  Entrenar")
        print("[4] 🛒 Tienda")
        print("[5] 📊 Estadísticas")
        print("[6] 🏆 Ranking")
        print("[7] 🎨 Cambiar tema")
        print("[8] 💾 Guardar partida")
        print("[9] 📖 Guía")
        print("[0] 🚪 Salir")
        
        opcion = input("➡️  ").strip()
        
        if opcion == "1":
            print(f"\n{Fore.CYAN}🌐 SERVIDORES:{Style.RESET_ALL}")
            disponibles = [s for s in SERVIDORES if s['dificultad'] <= hacker.nivel + 1]
            
            for i, s in enumerate(disponibles, 1):
                hackeado = "✅" if s['nombre'] in hacker.servidores_hackeados else "❌"
                print(f"[{i}] {hackeado} {s['nombre']} (★{s['dificultad']})")
                print(f"    {Fore.WHITE}💡 {s['pista']}{Style.RESET_ALL}")
            
            print(f"\n{Fore.CYAN}💡 Nivel máx: {hacker.nivel + 1}{Style.RESET_ALL}")
            
            try:
                idx = int(input("➡️  Elige: ")) - 1
                if 0 <= idx < len(disponibles):
                    mision_hackeo(hacker, disponibles[idx])
                else:
                    print(f"{Fore.RED}❌ Inválido{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}❌ Inválido{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif opcion == "2":
            mision_diaria(hacker)
        
        elif opcion == "3":
            print(f"\n{Fore.CYAN}🛠️  ENTRENAMIENTO{Style.RESET_ALL}")
            print("[1] Firewall")
            print("[2] Criptografía")
            print("[3] SQL Injection")
            print("[4] Puzzles")
            
            try:
                sub = input("➡️  ").strip()
                dif = random.randint(1, 3)
                exito = False
                
                if sub == "1":
                    exito = MiniJuegos.firewall_memoria(dif, 3)
                elif sub == "2":
                    exito = MiniJuegos.descifrar_cesar(dif)
                elif sub == "3":
                    exito = MiniJuegos.inyeccion_sql(dif)
                elif sub == "4":
                    exito = MiniJuegos.puzzle_logico(dif)
                else:
                    print(f"{Fore.RED}❌ Inválido{Style.RESET_ALL}")
                    time.sleep(1)
                    continue
                
                if exito:
                    exp = dif * 3 + random.randint(1, 3)
                    hacker.ganar_exp(exp)
                    print(f"{Fore.GREEN}📈 +{exp} EXP{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}💪 Sigue practicando{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}❌ Inválido{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif opcion == "4":
            tienda(hacker)
        
        elif opcion == "5":
            estadisticas(hacker)
            input(f"\n{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif opcion == "6":
            ranking(hacker)
        
        elif opcion == "7":
            cambiar_tema(hacker)
        
        elif opcion == "8":
            if hacker.guardar():
                print(f"{Fore.GREEN}✅ Partida guardada{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Error{Style.RESET_ALL}")
            time.sleep(1)
        
        elif opcion == "9":
            guia_usuario()
        
        elif opcion == "0":
            if hacker.guardar():
                print(f"{Fore.GREEN}✅ Guardado{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}👋 ¡Hasta luego, {hacker.nombre}!{Style.RESET_ALL}")
            return False
        
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)

# ============================================
# MAIN
# ============================================

def main():
    try:
        mostrar_header()
        
        print(f"\n{Fore.CYAN}👤 Bienvenido al mundo del hacking.{Style.RESET_ALL}")
        
        opcion = input(f"{Fore.CYAN}¿Cargar partida? (s/n): {Style.RESET_ALL}").strip().lower()
        
        if opcion == 's':
            hacker = Hacker()
            if hacker.cargar():
                print(f"{Fore.GREEN}✅ ¡Bienvenido de vuelta, {hacker.nombre}!{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}⚠️ No hay partida.{Style.RESET_ALL}")
                nombre = input(f"{Fore.CYAN}Nombre: {Style.RESET_ALL}").strip() or "Zero_Cool"
                hacker = Hacker(nombre)
        else:
            nombre = input(f"{Fore.CYAN}Nombre de Hacker: {Style.RESET_ALL}").strip() or "Zero_Cool"
            hacker = Hacker(nombre)
        
        print(f"\n{Fore.GREEN}✅ Conexión establecida. ¡Bienvenido, {hacker.nombre}!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💡 Escribe '9' para la guía.{Style.RESET_ALL}")
        time.sleep(2)
        
        menu_principal(hacker)
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Sesión terminada.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
        input(f"{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()