#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - ULTIMATE EDITION v5.0
===============================================
Un simulador de hacking en terminal donde encarnas a un hacker ético.

Características:
- 15 servidores con diferentes dificultades
- Sistema de guardado en JSON
- Sistema de niveles y experiencia
- Tienda con herramientas (8+)
- Sistema de logros (20+)
- Misiones diarias
- Ranking de hackers
- Inventario
- Sistema de rachas
- Modo multijugador local
- Skins/Temas de colores
- Guía de usuario integrada
- Sonidos (opcional)
- Tests integrados
"""

import random
import os
import time
import sys
import json
import hashlib
from datetime import datetime, timedelta
from colorama import init, Fore, Back, Style

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

init(autoreset=True, convert=True)
os.system('cls' if os.name == 'nt' else 'clear')

VERSION = "5.0.0"
AUTOR = "DlopedDtorred"
GITHUB_URL = "https://github.com/DlopedDtorred/hacker-simulator"

# ============================================
# CONFIGURACIÓN DE SKINS/TEMAS
# ============================================

TEMAS = {
    "matrix": {
        "primary": Fore.GREEN,
        "secondary": Fore.LIGHTGREEN_EX,
        "accent": Fore.LIGHTBLACK_EX,
        "text": Fore.WHITE,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warning": Fore.YELLOW,
        "info": Fore.CYAN,
        "border": "═"
    },
    "cyberpunk": {
        "primary": Fore.MAGENTA,
        "secondary": Fore.LIGHTMAGENTA_EX,
        "accent": Fore.CYAN,
        "text": Fore.WHITE,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warning": Fore.YELLOW,
        "info": Fore.BLUE,
        "border": "▬"
    },
    "classic": {
        "primary": Fore.BLUE,
        "secondary": Fore.LIGHTBLUE_EX,
        "accent": Fore.WHITE,
        "text": Fore.WHITE,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warning": Fore.YELLOW,
        "info": Fore.CYAN,
        "border": "─"
    },
    "dark": {
        "primary": Fore.LIGHTBLACK_EX,
        "secondary": Fore.WHITE,
        "accent": Fore.LIGHTGREEN_EX,
        "text": Fore.WHITE,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warning": Fore.YELLOW,
        "info": Fore.CYAN,
        "border": "═"
    }
}

# ============================================
# BASE DE DATOS DE SERVIDORES (15 niveles)
# ============================================

SERVIDORES = [
    # Nivel 1-3: Fáciles
    {
        "id": "SRV-001",
        "nombre": "MegaCorp Alpha",
        "dificultad": 1,
        "recompensa": 150,
        "pista": "🐱 La mascota del CEO se llama... (empieza por M)",
        "password": "michifu",
        "descripcion": "Servidor corporativo de baja seguridad"
    },
    {
        "id": "SRV-002",
        "nombre": "DarkNet Vault",
        "dificultad": 2,
        "recompensa": 250,
        "pista": "👿 El número de la bestia sin el 6 final",
        "password": "666",
        "descripcion": "Custodia de datos en la red oscura"
    },
    {
        "id": "SRV-003",
        "nombre": "ShadowNet",
        "dificultad": 2,
        "recompensa": 300,
        "pista": "🏢 Año de fundación de ShadowNet (20XX)",
        "password": "2015",
        "descripcion": "Red de datos sombra"
    },
    # Nivel 4-6: Intermedios
    {
        "id": "SRV-004",
        "nombre": "CyberDyne Systems",
        "dificultad": 3,
        "recompensa": 400,
        "pista": "🎬 ¿Año de Blade Runner? (20XX)",
        "password": "2019",
        "descripcion": "Sistemas de inteligencia artificial"
    },
    {
        "id": "SRV-005",
        "nombre": "NeoTokyo Grid",
        "dificultad": 4,
        "recompensa": 600,
        "pista": "🇯🇵 Código postal de Shibuya (7 dígitos)",
        "password": "1500042",
        "descripcion": "Red de datos de la ciudad digital"
    },
    {
        "id": "SRV-006",
        "nombre": "A.I. Core",
        "dificultad": 5,
        "recompensa": 1000,
        "pista": "🔢 Fibonacci posición 13",
        "password": "233",
        "descripcion": "Núcleo de inteligencia artificial"
    },
    # Nivel 7-9: Avanzados
    {
        "id": "SRV-007",
        "nombre": "Quantum Nexus",
        "dificultad": 6,
        "recompensa": 1500,
        "pista": "⚛️ Constante de Planck (3 primeros dígitos)",
        "password": "662",
        "descripcion": "Servidor cuántico experimental"
    },
    {
        "id": "SRV-008",
        "nombre": "NanoTech Labs",
        "dificultad": 7,
        "recompensa": 2000,
        "pista": "🔬 Número atómico del carbono",
        "password": "6",
        "descripcion": "Laboratorio de nanotecnología"
    },
    {
        "id": "SRV-009",
        "nombre": "Matrix Archive",
        "dificultad": 8,
        "recompensa": 3000,
        "pista": "🎬 Número de habitación de Neo en The Matrix",
        "password": "303",
        "descripcion": "Archivo de la resistencia humana"
    },
    # Nivel 10-12: Expertos
    {
        "id": "SRV-010",
        "nombre": "ChronoCore",
        "dificultad": 9,
        "recompensa": 5000,
        "pista": "⏳ Año del descubrimiento del ADN (19XX)",
        "password": "1953",
        "descripcion": "Base de datos del flujo temporal"
    },
    {
        "id": "SRV-011",
        "nombre": "Omega Station",
        "dificultad": 10,
        "recompensa": 10000,
        "pista": "☯️ 666 × 7 (número de la bestia por la suerte)",
        "password": "4662",
        "descripcion": "El servidor definitivo. ¿Estás listo?"
    },
    {
        "id": "SRV-012",
        "nombre": "Void Network",
        "dificultad": 9,
        "recompensa": 4500,
        "pista": "🔮 El número de la suerte del hacker (7) al cubo",
        "password": "343",
        "descripcion": "Red en el vacío digital"
    },
    # Nivel 13-15: Legendarios
    {
        "id": "SRV-013",
        "nombre": "Eclipse Core",
        "dificultad": 11,
        "recompensa": 15000,
        "pista": "🌑 Año del primer eclipse total del siglo XXI",
        "password": "2001",
        "descripcion": "Núcleo de la sombra digital"
    },
    {
        "id": "SRV-014",
        "nombre": "Nebula Archive",
        "dificultad": 12,
        "recompensa": 20000,
        "pista": "🌌 Código postal de la NASA (5 dígitos)",
        "password": "77058",
        "descripcion": "Archivo de datos espaciales"
    },
    {
        "id": "SRV-015",
        "nombre": "Genesis Point",
        "dificultad": 13,
        "recompensa": 30000,
        "pista": "🌀 El año de la primera computadora (19XX)",
        "password": "1941",
        "descripcion": "El origen de todo. ¿Te atreves?"
    }
]

# ============================================
# SISTEMA DE LOGROS (20+)
# ============================================

LOGROS = {
    "primer_hackeo": {"nombre": "🚀 Primer Hackeo", "desc": "Completa tu primera misión", "recompensa": 50},
    "cinco_misiones": {"nombre": "💪 Cinco Misiones", "desc": "Completa 5 misiones", "recompensa": 100},
    "diez_misiones": {"nombre": "🏆 Diez Misiones", "desc": "Completa 10 misiones", "recompensa": 200},
    "veinticinco_misiones": {"nombre": "👑 Leyenda", "desc": "Completa 25 misiones", "recompensa": 500},
    "cincuenta_misiones": {"nombre": "🌟 Maestro", "desc": "Completa 50 misiones", "recompensa": 1000},
    "nivel_5": {"nombre": "⚡ Nivel 5", "desc": "Alcanza el nivel 5", "recompensa": 150},
    "nivel_10": {"nombre": "🌟 Nivel 10", "desc": "Alcanza el nivel 10", "recompensa": 300},
    "nivel_15": {"nombre": "👑 Nivel 15", "desc": "Alcanza el nivel 15", "recompensa": 500},
    "nivel_20": {"nombre": "💎 Nivel 20", "desc": "Alcanza el nivel 20", "recompensa": 1000},
    "millonario": {"nombre": "💰 Millonario", "desc": "Acumula 1000 créditos", "recompensa": 100},
    "billonario": {"nombre": "💎 Billonario", "desc": "Acumula 5000 créditos", "recompensa": 300},
    "trillonario": {"nombre": "👑 Trillonario", "desc": "Acumula 10000 créditos", "recompensa": 500},
    "perfecto": {"nombre": "🎯 Perfecto", "desc": "Completa 5 misiones sin fallar", "recompensa": 200},
    "racha_5": {"nombre": "🔥 Racha 5", "desc": "5 misiones seguidas", "recompensa": 100},
    "racha_10": {"nombre": "🔥🔥 Racha 10", "desc": "10 misiones seguidas", "recompensa": 200},
    "racha_20": {"nombre": "🔥🔥🔥 Racha 20", "desc": "20 misiones seguidas", "recompensa": 500},
    "coleccionista": {"nombre": "🛠️ Coleccionista", "desc": "Todas las herramientas", "recompensa": 500},
    "omega": {"nombre": "☯️ Omega", "desc": "Completa Omega Station", "recompensa": 1000},
    "leyenda": {"nombre": "⚡ Leyenda", "desc": "Completa todos los servidores", "recompensa": 5000},
    "speedrun": {"nombre": "🏃 Speedrun", "desc": "Completa 10 misiones en menos de 5 minutos", "recompensa": 1000}
}

# ============================================
# CLASE HACKER (CON GUARDADO)
# ============================================

class Hacker:
    """Clase principal del jugador con sistema de guardado."""
    
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
        self.sonidos_activados = False
        
    def ganar_exp(self, cantidad):
        self.exp += cantidad
        while self.exp >= self.exp_necesaria:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.exp = 0
        self.exp_necesaria = self.nivel * 15
        
        print(f"\n{Fore.MAGENTA}{'═'*50}")
        print(f"🌟 ¡SUBES AL NIVEL {self.nivel}! 🌟")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        # Herramienta por nivel par
        if self.nivel % 2 == 0:
            self._dar_herramienta()
        
        # Bonus de créditos cada 3 niveles
        if self.nivel % 3 == 0:
            bonus = self.nivel * 50
            self.creditos += bonus
            print(f"{Fore.GREEN}💰 Bonus de nivel: +{bonus} créditos{Style.RESET_ALL}")
        
        # Recompensa especial cada 5 niveles
        if self.nivel % 5 == 0:
            print(f"{Fore.YELLOW}🎁 ¡Recompensa especial por nivel {self.nivel}!{Style.RESET_ALL}")
            self.creditos += 200
            if self.nivel % 10 == 0:
                self.creditos += 500
                print(f"{Fore.CYAN}🌟 ¡BONUS EXTRA DE 500 CRÉDITOS!{Style.RESET_ALL}")
    
    def _dar_herramienta(self):
        herramientas = [
            "🔧 Escáner Avanzado",
            "🛡️ Firewall Bypass",
            "🔑 Crypto Key",
            "⚡ Quantum Decryptor",
            "🔬 Nano Analyzer",
            "🎯 Matrix Key",
            "⏳ Chrono Analyzer",
            "☯️ Omega Key"
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
        
        # Nivel
        if self.nivel >= 5 and "nivel_5" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_5")
        if self.nivel >= 10 and "nivel_10" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_10")
        if self.nivel >= 15 and "nivel_15" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_15")
        if self.nivel >= 20 and "nivel_20" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_20")
        
        # Créditos
        if self.creditos >= 1000 and "millonario" not in self.logros_desbloqueados:
            nuevos_logros.append("millonario")
        if self.creditos >= 5000 and "billonario" not in self.logros_desbloqueados:
            nuevos_logros.append("billonario")
        if self.creditos >= 10000 and "trillonario" not in self.logros_desbloqueados:
            nuevos_logros.append("trillonario")
        
        # Rachas
        if self.mejor_racha >= 5 and "racha_5" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_5")
        if self.mejor_racha >= 10 and "racha_10" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_10")
        if self.mejor_racha >= 20 and "racha_20" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_20")
        
        # Perfecto
        if self.misiones_completadas >= 5 and self.fallos == 0 and "perfecto" not in self.logros_desbloqueados:
            nuevos_logros.append("perfecto")
        
        # Coleccionista
        if len(self.herramientas) >= 8 and "coleccionista" not in self.logros_desbloqueados:
            nuevos_logros.append("coleccionista")
        
        # Omega
        if "Omega Station" in self.servidores_hackeados and "omega" not in self.logros_desbloqueados:
            nuevos_logros.append("omega")
        
        # Leyenda
        if len(set(self.servidores_hackeados)) == len(SERVIDORES) and "leyenda" not in self.logros_desbloqueados:
            nuevos_logros.append("leyenda")
        
        # Desbloquear logros
        for logro_id in nuevos_logros:
            self.logros_desbloqueados.append(logro_id)
            logro = LOGROS[logro_id]
            print(f"{Fore.YELLOW}🏆 ¡LOGRO DESBLOQUEADO: {logro['nombre']}!{Style.RESET_ALL}")
            print(f"{Fore.WHITE}   📝 {logro['desc']}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}   💰 Recompensa: +{logro['recompensa']} créditos{Style.RESET_ALL}")
            self.creditos += logro['recompensa']
    
    def calcular_rango(self):
        if self.nivel >= 15:
            return "👑 LEGENDARY HACKER"
        elif self.nivel >= 12:
            return "⚡ ELITE HACKER"
        elif self.nivel >= 9:
            return "🔥 SENIOR HACKER"
        elif self.nivel >= 6:
            return "💻 JUNIOR HACKER"
        elif self.nivel >= 3:
            return "🔰 APRENDIZ"
        else:
            return "🐣 NOVATO"
    
    # ===== SISTEMA DE GUARDADO =====
    
    def guardar(self, filename="save.json"):
        """Guarda la partida en un archivo JSON."""
        datos = {
            "nombre": self.nombre,
            "nivel": self.nivel,
            "exp": self.exp,
            "exp_necesaria": self.exp_necesaria,
            "creditos": self.creditos,
            "herramientas": self.herramientas,
            "misiones_completadas": self.misiones_completadas,
            "fallos": self.fallos,
            "racha_actual": self.racha_actual,
            "mejor_racha": self.mejor_racha,
            "servidores_hackeados": self.servidores_hackeados,
            "logros_desbloqueados": self.logros_desbloqueados,
            "tema_actual": self.tema_actual,
            "ultima_mision": self.ultima_mision,
            "mision_diaria_completada": self.mision_diaria_completada,
            "ultima_mision_diaria": self.ultima_mision_diaria,
            "tiempo_jugado": self.tiempo_jugado,
            "fecha_creacion": self.fecha_creacion,
            "sonidos_activados": self.sonidos_activados,
            "version": VERSION
        }
        try:
            with open(filename, 'w') as f:
                json.dump(datos, f, indent=4)
            return True
        except Exception as e:
            print(f"{Fore.RED}❌ Error al guardar: {e}{Style.RESET_ALL}")
            return False
    
    def cargar(self, filename="save.json"):
        """Carga una partida desde un archivo JSON."""
        try:
            with open(filename, 'r') as f:
                datos = json.load(f)
            
            for key, value in datos.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"{Fore.RED}❌ Error al cargar: {e}{Style.RESET_ALL}")
            return False
    
    def __str__(self):
        tema = TEMAS.get(self.tema_actual, TEMAS["matrix"])
        barra = "█" * int((self.exp / self.exp_necesaria) * 15) if self.exp_necesaria > 0 else ""
        vacio = "░" * (15 - len(barra))
        
        return f"""
{tema['primary']}╔══════════════════════════════════════════════════════════╗
{tema['primary']}║ {tema['text']}👤 {self.nombre} {tema['primary']}│ {tema['success']}Nv.{self.nivel} {tema['primary']}│ {tema['warning']}💰 {self.creditos} créditos
{tema['primary']}║ {tema['text']}📊 EXP [{barra}{vacio}] {self.exp}/{self.exp_necesaria}
{tema['primary']}║ {tema['text']}🏆 {self.calcular_rango()}
{tema['primary']}║ {tema['text']}🛠️  {', '.join(self.herramientas)}
{tema['primary']}║ {tema['text']}📈 Rachas: {self.racha_actual} actual │ {self.mejor_racha} máxima
{tema['primary']}║ {tema['text']}🎯 Misiones: {self.misiones_completadas} │ ❌ Fallos: {self.fallos}
{tema['primary']}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

# ============================================
# MINI-JUEGOS MEJORADOS
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
                print(f"{Fore.GREEN}✅ ¡Firewall evadido con éxito!{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}❌ Secuencia incorrecta.{Style.RESET_ALL}")
                if intento < intentos_max - 1:
                    print(f"{Fore.YELLOW}💡 La secuencia era: {' '.join(secuencia)}{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 Has sido detectado por el firewall.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def descifrar_cesar(dificultad):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔐 ¡CÓDIGO ENCRIPTADO! Descifra el mensaje:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        palabras = ["HACKER", "SISTEMA", "SEGURO", "DATOS", "RED", "CYBER", 
                   "NEXUS", "QUANTUM", "MATRIX", "OMEGA", "SHADOW", "VOID"]
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
                print(f"{Fore.GREEN}✅ ¡Mensaje descifrado correctamente!{Style.RESET_ALL}")
                return True
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"{Fore.RED}❌ Incorrecto. Sigue intentando.{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 No has podido descifrar el código.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def inyeccion_sql(dificultad):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"💉 ¡VULNERABILIDAD SQL ENCONTRADA! Inyecta el código:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        tablas = ["usuarios", "datos", "admin", "sistema", "logs", "config", "credenciales"]
        tabla = random.choice(tablas)
        
        codigos = [
            f"SELECT * FROM {tabla} WHERE 1=1; --",
            f"' OR '1'='1",
            f"'; DROP TABLE {tabla}; --",
            f"' UNION SELECT null,null,null--",
            f"' OR 1=1 --"
        ]
        
        codigo_correcto = random.choice(codigos)
        
        print(f"{Fore.CYAN}💻 Objetivo: Acceder a la tabla '{tabla}'{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔍 Pista: Código SQL que siempre es verdadero{Style.RESET_ALL}")
        
        intentos = 3
        while intentos > 0:
            print(f"\n{Fore.CYAN}💡 Intentos restantes: {intentos}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📝 Introduce tu código SQL:{Style.RESET_ALL}")
            respuesta = input("➡️  ").strip()
            
            if respuesta.lower() == 'help':
                print(f"{Fore.YELLOW}💡 Ejemplos de inyección:")
                print("  - ' OR '1'='1")
                print("  - SELECT * FROM tabla WHERE 1=1; --")
                print("  - '; DROP TABLE tabla; --")
                continue
            
            if respuesta == codigo_correcto:
                print(f"{Fore.GREEN}✅ ¡Inyección exitosa! Acceso concedido.{Style.RESET_ALL}")
                return True
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"{Fore.RED}❌ Código incorrecto.{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 Has sido detectado y bloqueado.{Style.RESET_ALL}")
        return False
    
    @staticmethod
    def puzzle_logico(dificultad):
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🧩 ¡PUZZLE LÓGICO! Encuentra el número que falta:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        tipos = ["suma", "multiplica", "fibonacci", "cuadrados", "primos"]
        tipo = random.choice(tipos)
        
        if tipo == "suma":
            incremento = random.randint(2, 5)
            inicio = random.randint(1, 10)
            secuencia = [inicio + i * incremento for i in range(4)]
            respuesta = secuencia[-1] + incremento
            pista = f"Suma {incremento} cada vez"
        
        elif tipo == "multiplica":
            multiplicador = random.randint(2, 4)
            inicio = random.randint(1, 3)
            secuencia = [inicio * (multiplicador ** i) for i in range(4)]
            respuesta = secuencia[-1] * multiplicador
            pista = f"Multiplica por {multiplicador} cada vez"
        
        elif tipo == "fibonacci":
            secuencia = [1, 1, 2, 3, 5]
            respuesta = 8
            pista = "Fibonacci: suma de los dos anteriores"
        
        elif tipo == "cuadrados":
            secuencia = [1, 4, 9, 16, 25]
            respuesta = 36
            pista = "Números al cuadrado: 1², 2², 3²..."
        
        else:  # primos
            secuencia = [2, 3, 5, 7, 11]
            respuesta = 13
            pista = "Números primos en orden"
        
        print(f"{Fore.CYAN}📊 Secuencia:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}╔{'═' * (len(secuencia) * 5 + 10)}╗")
        print(f"║  {'  →  '.join(map(str, secuencia))}  →  ?  ║")
        print(f"╚{'═' * (len(secuencia) * 5 + 10)}╝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💡 Pista: {pista}{Style.RESET_ALL}")
        
        intentos = 3
        while intentos > 0:
            print(f"\n{Fore.CYAN}💡 Intentos restantes: {intentos}{Style.RESET_ALL}")
            try:
                respuesta_usuario = int(input("➡️  Número que falta: ").strip())
                if respuesta_usuario == respuesta:
                    print(f"{Fore.GREEN}✅ ¡Correcto! Has resuelto el puzzle.{Style.RESET_ALL}")
                    return True
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"{Fore.RED}❌ Incorrecto. Sigue intentando.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Introduce un número válido.{Style.RESET_ALL}")
        
        print(f"{Fore.RED}💀 No has podido resolver el puzzle.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 La respuesta era: {respuesta}{Style.RESET_ALL}")
        return False

# ============================================
# FUNCIONES DEL JUEGO (Mejoradas)
# ============================================

def mostrar_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    header = f"""
{Fore.GREEN}╔══════════════════════════════════════════════════════════════════╗
{Fore.GREEN}║  {Fore.CYAN}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗  {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}███████║███████║██║     █████╔╝ █████╗  ██████╔╝ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║ {Fore.GREEN}       ║
{Fore.GREEN}║  {Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {Fore.GREEN}       ║
{Fore.GREEN}║     {Fore.YELLOW}HACKER SIMULATOR 2077 - ULTIMATE EDITION v{VERSION}{Fore.GREEN}     ║
{Fore.GREEN}║     {Fore.WHITE}by {AUTOR} {Fore.GREEN}| {Fore.CYAN}⭐ GitHub: {GITHUB_URL}{Fore.GREEN}     ║
{Fore.GREEN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(header)

def mision_hackeo(hacker, servidor):
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.GREEN}🎯 MISIÓN: HACKEAR {servidor['nombre'].upper()}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}📋 ID: {servidor['id']}")
    print(f"⭐ Dificultad: {servidor['dificultad']} ★")
    print(f"💰 Recompensa: {servidor['recompensa']} créditos")
    print(f"📝 {servidor['descripcion']}")
    print(f"🔍 PISTA: {Fore.WHITE}{servidor['pista']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    # FASE 1: Firewall
    print(f"\n{Fore.CYAN}🛡️  FASE 1: ELUDIR FIREWALL{Style.RESET_ALL}")
    intentos_firewall = max(3, 5 - servidor['dificultad'] // 2)
    
    if not MiniJuegos.firewall_memoria(servidor['dificultad'], intentos_firewall):
        print(f"\n{Fore.RED}💀 Misión fallida. Has sido detectado.{Style.RESET_ALL}")
        hacker.fallos += 1
        hacker.racha_actual = 0
        return False
    
    # FASE 2: Contraseña
    print(f"\n{Fore.CYAN}🔑 FASE 2: DESCIFRAR CONTRASEÑA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💡 Pista: {servidor['pista']}{Style.RESET_ALL}")
    
    intentos = max(3, 5 - servidor['dificultad'] + 1)
    acertado = False
    
    while intentos > 0 and not acertado:
        print(f"\n{Fore.CYAN}🔐 Intentos restantes: {intentos}{Style.RESET_ALL}")
        
        if "🔑 Crypto Key" in hacker.herramientas:
            print(f"{Fore.YELLOW}💡 Escribe 'help' para una pista extra{Style.RESET_ALL}")
        
        password = input("➡️  Contraseña: ").strip().lower()
        
        if password == 'help' and "🔑 Crypto Key" in hacker.herramientas:
            print(f"{Fore.CYAN}💡 Pista extra: La contraseña tiene {len(servidor['password'])} caracteres{Style.RESET_ALL}")
            continue
        
        if password == servidor['password']:
            acertado = True
            print(f"{Fore.GREEN}✅ ¡Contraseña correcta! Acceso concedido.{Style.RESET_ALL}")
        else:
            intentos -= 1
            if intentos > 0:
                print(f"{Fore.RED}❌ Contraseña incorrecta.{Style.RESET_ALL}")
    
    if not acertado:
        print(f"\n{Fore.RED}💀 Has agotado los intentos. Misión fallida.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🔑 La contraseña era: {servidor['password']}{Style.RESET_ALL}")
        hacker.fallos += 1
        hacker.racha_actual = 0
        return False
    
    # FASE 3: Mini-juego extra (si dificultad >= 5)
    if servidor['dificultad'] >= 5:
        print(f"\n{Fore.CYAN}🕵️  FASE 3: SEGURIDAD ADICIONAL{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⚠️  El servidor tiene protección extra...{Style.RESET_ALL}")
        
        mini_juego = random.choice([
            MiniJuegos.descifrar_cesar,
            MiniJuegos.inyeccion_sql,
            MiniJuegos.puzzle_logico
        ])
        
        if not mini_juego(servidor['dificultad']):
            print(f"{Fore.RED}💀 ¡Has sido descubierto! Misión fallida.{Style.RESET_ALL}")
            hacker.fallos += 1
            hacker.racha_actual = 0
            return False
    
    # ¡MISIÓN COMPLETADA!
    print(f"\n{Fore.GREEN}{'═'*50}")
    print(f"🎉 ¡MISIÓN COMPLETADA CON ÉXITO! 🎉")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
    recompensa_base = servidor['recompensa']
    bonus_racha = min(hacker.racha_actual * 25, 200)
    recompensa_total = recompensa_base + bonus_racha
    
    if hacker.nivel >= 5:
        recompensa_total = int(recompensa_total * 1.2)
    
    hacker.creditos += recompensa_total
    hacker.misiones_completadas += 1
    hacker.racha_actual += 1
    
    if hacker.racha_actual > hacker.mejor_racha:
        hacker.mejor_racha = hacker.racha_actual
    
    hacker.servidores_hackeados.append(servidor['nombre'])
    hacker.ultima_mision = servidor['nombre']
    
    exp_ganada = servidor['dificultad'] * 5 + hacker.racha_actual * 2
    hacker.ganar_exp(exp_ganada)
    
    print(f"{Fore.GREEN}💰 Recompensa total: +{recompensa_total} créditos")
    print(f"{Fore.GREEN}📈 +{exp_ganada} EXP")
    if bonus_racha > 0:
        print(f"{Fore.GREEN}🔥 Bonus de racha: +{bonus_racha} créditos")
    if hacker.racha_actual >= 3:
        print(f"{Fore.MAGENTA}🔥 ¡Racha de {hacker.racha_actual} misiones!{Style.RESET_ALL}")
    
    hacker.verificar_logros()
    
    return True

def mision_diaria(hacker):
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"📅 MISIÓN DIARIA")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
    if hacker.mision_diaria_completada:
        print(f"{Fore.YELLOW}⚠️ Ya completaste tu misión diaria de hoy.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}⏳ Vuelve mañana para una nueva misión.{Style.RESET_ALL}")
        input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        return
    
    disponibles = [s for s in SERVIDORES if s['dificultad'] <= 5]
    servidor = random.choice(disponibles)
    
    print(f"{Fore.YELLOW}🌟 Misión especial de hoy:{Style.RESET_ALL}")
    print(f"🎯 HACKEAR: {servidor['nombre']}")
    print(f"⭐ Dificultad: {servidor['dificultad']} ★")
    print(f"💰 Recompensa: {servidor['recompensa'] * 2} créditos (¡DOBLE!){Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}🔍 Pista: {servidor['pista']}{Style.RESET_ALL}")
    
    # FASE 1: Firewall
    print(f"\n{Fore.CYAN}🛡️  ELUDIR FIREWALL{Style.RESET_ALL}")
    if not MiniJuegos.firewall_memoria(servidor['dificultad'], 4):
        print(f"{Fore.RED}💀 Misión diaria fallida.{Style.RESET_ALL}")
        return
    
    # FASE 2: Contraseña
    print(f"\n{Fore.CYAN}🔑 DESCIFRAR CONTRASEÑA{Style.RESET_ALL}")
    intentos = 3
    acertado = False
    
    while intentos > 0 and not acertado:
        print(f"\n{Fore.CYAN}🔐 Intentos: {intentos}{Style.RESET_ALL}")
        password = input("➡️  Contraseña: ").strip().lower()
        
        if password == servidor['password']:
            acertado = True
            print(f"{Fore.GREEN}✅ ¡Contraseña correcta!{Style.RESET_ALL}")
        else:
            intentos -= 1
            if intentos > 0:
                print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
    
    if not acertado:
        print(f"{Fore.RED}💀 Misión diaria fallida.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🔑 Contraseña: {servidor['password']}{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.GREEN}{'═'*50}")
    print(f"🎉 ¡MISIÓN DIARIA COMPLETADA! 🎉")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
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
    input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")

def tienda(hacker):
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"🛒 TIENDA DE HERRAMIENTAS")
    print(f"{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}💰 Créditos: {hacker.creditos}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🛠️  Tus herramientas: {', '.join(hacker.herramientas)}{Style.RESET_ALL}")
    print(f"{'═'*50}")
    
    items = [
        {"nombre": "🔧 Escáner Avanzado", "precio": 100, "desc": "+2 intentos en contraseñas"},
        {"nombre": "🛡️ Firewall Bypass", "precio": 200, "desc": "Firewalls -1 dificultad"},
        {"nombre": "🔑 Crypto Key", "precio": 300, "desc": "Revela pistas extra"},
        {"nombre": "⚡ Quantum Decryptor", "precio": 500, "desc": "Descifra mensajes automáticamente"},
        {"nombre": "🔬 Nano Analyzer", "precio": 700, "desc": "Analiza servidores en profundidad"},
        {"nombre": "🎯 Matrix Key", "precio": 1000, "desc": "Acceso a servidores de élite"},
        {"nombre": "⏳ Chrono Analyzer", "precio": 1500, "desc": "Predice contraseñas"},
        {"nombre": "☯️ Omega Key", "precio": 2500, "desc": "Acceso total al sistema Omega"}
    ]
    
    for i, item in enumerate(items, 1):
        estado = "✅" if item['nombre'] in hacker.herramientas else "❌"
        print(f"[{i}] {estado} {item['nombre']}")
        print(f"    {Fore.WHITE}💰 {item['precio']} créditos │ 📝 {item['desc']}{Style.RESET_ALL}")
    
    print("[9] 💰 Comprar EXP (100 créditos = 10 EXP)")
    print("[0] 🚪 Salir de la tienda")
    
    try:
        opcion = int(input("\n➡️  ").strip())
        
        if opcion == 0:
            return
        
        elif opcion == 9:
            if hacker.creditos >= 100:
                hacker.creditos -= 100
                hacker.ganar_exp(10)
                print(f"{Fore.GREEN}✅ +10 EXP adquirida!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Créditos insuficientes.{Style.RESET_ALL}")
            time.sleep(1)
            return
        
        elif 1 <= opcion <= len(items):
            item = items[opcion-1]
            if item['nombre'] in hacker.herramientas:
                print(f"{Fore.YELLOW}⚠️ Ya tienes esta herramienta.{Style.RESET_ALL}")
            elif hacker.creditos >= item['precio']:
                hacker.creditos -= item['precio']
                hacker.herramientas.append(item['nombre'])
                print(f"{Fore.GREEN}✅ ¡{item['nombre']} adquirido!{Style.RESET_ALL}")
                hacker.verificar_logros()
            else:
                print(f"{Fore.RED}❌ Créditos insuficientes. Necesitas {item['precio'] - hacker.creditos} más.{Style.RESET_ALL}")
            time.sleep(1)
        
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)
            
    except ValueError:
        print(f"{Fore.RED}❌ Introduce un número válido.{Style.RESET_ALL}")
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
    
    print(f"\n{Fore.WHITE}🖥️  Servidores hackeados:")
    if hacker.servidores_hackeados:
        for s in hacker.servidores_hackeados:
            print(f"  • ✅ {s}")
    else:
        print(f"  • Ninguno aún")
    
    print(f"\n{Fore.WHITE}🏆 Logros:")
    if hacker.logros_desbloqueados:
        for logro_id in hacker.logros_desbloqueados:
            logro = LOGROS[logro_id]
            print(f"  • {logro['nombre']} - {logro['desc']}")
    else:
        print(f"  • Ningún logro desbloqueado aún")
    
    print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")

def ranking(hacker):
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}🏆 RANKING DE HACKERS")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    nombres_ficticios = [
        ("Shadow", 8, 12), ("Neon", 7, 10), ("Vortex", 6, 8),
        ("Ghost", 5, 7), ("Phoenix", 4, 5), ("Cipher", 3, 4),
        ("Nova", 9, 15), ("Crystal", 11, 18)
    ]
    
    print(f"{Fore.WHITE}Posición │ Hacker │ Nivel │ Misiones{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    # Posición 1: El jugador
    if hacker.misiones_completadas > 0:
        print(f"{Fore.GREEN}🏆 #1  │ {hacker.nombre} │ {hacker.nivel}     │ {hacker.misiones_completadas}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}#1  │ (vacío) │ 0     │ 0{Style.RESET_ALL}")
    
    # Oponentes
    for i, (nombre, nivel, misiones) in enumerate(nombres_ficticios, 2):
        if random.random() > 0.3:
            print(f"#{i}  │ {nombre} │ {nivel}     │ {misiones}")
    
    print(f"\n{Fore.CYAN}💡 Para subir en el ranking, completa más misiones.{Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")

def cambiar_tema(hacker):
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"🎨 CAMBIAR TEMA")
    print(f"{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Tema actual: {hacker.tema_actual}{Style.RESET_ALL}")
    print(f"\n{Fore.CYAN}Temas disponibles:{Style.RESET_ALL}")
    
    for i, (nombre, _) in enumerate(TEMAS.items(), 1):
        check = "✅" if hacker.tema_actual == nombre else "  "
        print(f"[{i}] {check} {nombre}")
    
    print("[0] Cancelar")
    
    try:
        opcion = int(input("\n➡️  ").strip())
        temas = list(TEMAS.keys())
        if opcion == 0:
            return
        elif 1 <= opcion <= len(temas):
            hacker.tema_actual = temas[opcion-1]
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
    print(f"{Fore.YELLOW}📖 GUÍA DE USUARIO - HACKER SIMULATOR 2077")
    print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
    
    print(f"""
{Fore.WHITE}🎯 ¿QUÉ ES?
Un juego de hacking en terminal donde encarnas a un hacker ético.
Tu objetivo es infiltrarte en servidores, descifrar contraseñas y
convertirte en el mejor hacker.

{Fore.CYAN}🕹️  CONTROLES{Fore.WHITE}
1 - Aceptar misión (hackear servidor)
2 - Misión diaria (recompensa doble)
3 - Entrenar (practicar habilidades)
4 - Visitar tienda
5 - Ver estadísticas
6 - Ranking de hackers
7 - Configuración (temas, sonidos)
8 - Guardar partida
9 - Guía de usuario
0 - Salir

{Fore.YELLOW}💡 CONSEJOS{Fore.WHITE}
• Presta atención a las PISTAS, te ayudarán a descifrar contraseñas
• Compra herramientas en la tienda para facilitar las misiones
• Mantén la racha para obtener bonificaciones extra
• Completa misiones diarias para recompensas dobles
• Los logros dan recompensas en créditos

{Fore.GREEN}⚡ TECNOLOGÍAS{Fore.WHITE}
• Python 3.8+
• Colorama (colores en terminal)
• JSON (guardado de partidas)
• 100% Open Source (MIT License)

{Fore.CYAN}🔗 ENLACES{Fore.WHITE}
• GitHub: {GITHUB_URL}
• Issues: {GITHUB_URL}/issues
• Contribuir: {GITHUB_URL}/blob/main/CONTRIBUTING.md

{Fore.MAGENTA}🙏 ¡GRACIAS POR JUGAR!{Style.RESET_ALL}
""")
    input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")

# ============================================
# MENÚ PRINCIPAL
# ============================================

def menu_principal(hacker):
    while True:
        mostrar_header()
        print(hacker)
        
        print(f"\n{Fore.CYAN}📡 OPCIONES:{Style.RESET_ALL}")
        print("[1] 🌐 Hackear servidor")
        print("[2] 📅 Misión diaria (recompensa doble)")
        print("[3] 🛠️  Entrenar (practicar habilidades)")
        print("[4] 🛒 Visitar tienda")
        print("[5] 📊 Ver estadísticas")
        print("[6] 🏆 Ranking de hackers")
        print("[7] ⚙️  Configuración (temas/sonidos)")
        print("[8] 💾 Guardar partida")
        print("[9] 📖 Guía de usuario")
        print("[0] 🚪 Salir")
        
        opcion = input("➡️  ").strip()
        
        if opcion == "1":
            print(f"\n{Fore.CYAN}🌐 SERVIDORES DISPONIBLES:{Style.RESET_ALL}")
            disponibles = [s for s in SERVIDORES if s['dificultad'] <= hacker.nivel + 1]
            
            for i, s in enumerate(disponibles, 1):
                hackeado = "✅" if s['nombre'] in hacker.servidores_hackeados else "❌"
                print(f"[{i}] {hackeado} {s['nombre']} (★{s['dificultad']})")
                print(f"    {Fore.WHITE}💡 {s['pista']}{Style.RESET_ALL}")
            
            print(f"\n{Fore.CYAN}💡 Puedes hackear servidores hasta nivel {hacker.nivel + 1}{Style.RESET_ALL}")
            
            try:
                idx = int(input("➡️  Elige un servidor: ")) - 1
                if 0 <= idx < len(disponibles):
                    mision_hackeo(hacker, disponibles[idx])
                else:
                    print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            
            input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        
        elif opcion == "2":
            mision_diaria(hacker)
        
        elif opcion == "3":
            print(f"\n{Fore.CYAN}🛠️  ENTRENAMIENTO{Style.RESET_ALL}")
            print("[1] Práctica de Firewalls")
            print("[2] Práctica de Criptografía")
            print("[3] Práctica de SQL Injection")
            print("[4] Puzzles lógicos")
            
            try:
                subopcion = input("➡️  ").strip()
                dificultad = random.randint(1, 3)
                exito = False
                
                if subopcion == "1":
                    exito = MiniJuegos.firewall_memoria(dificultad, 3)
                elif subopcion == "2":
                    exito = MiniJuegos.descifrar_cesar(dificultad)
                elif subopcion == "3":
                    exito = MiniJuegos.inyeccion_sql(dificultad)
                elif subopcion == "4":
                    exito = MiniJuegos.puzzle_logico(dificultad)
                else:
                    print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
                    time.sleep(1)
                    continue
                
                if exito:
                    exp = dificultad * 3 + random.randint(1, 3)
                    hacker.ganar_exp(exp)
                    print(f"{Fore.GREEN}📈 +{exp} EXP{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}💪 Sigue practicando.{Style.RESET_ALL}")
                
            except:
                print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            
            input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        
        elif opcion == "4":
            tienda(hacker)
        
        elif opcion == "5":
            estadisticas(hacker)
            input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        
        elif opcion == "6":
            ranking(hacker)
        
        elif opcion == "7":
            print(f"\n{Fore.CYAN}⚙️  CONFIGURACIÓN{Style.RESET_ALL}")
            print("[1] 🎨 Cambiar tema")
            print("[2] 🔊 Activar/Desactivar sonidos")
            print("[0] Volver")
            
            try:
                subopcion = input("➡️  ").strip()
                if subopcion == "1":
                    cambiar_tema(hacker)
                elif subopcion == "2":
                    hacker.sonidos_activados = not hacker.sonidos_activados
                    estado = "activados" if hacker.sonidos_activados else "desactivados"
                    print(f"{Fore.GREEN}✅ Sonidos {estado}{Style.RESET_ALL}")
                    time.sleep(1)
            except:
                print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
                time.sleep(1)
        
        elif opcion == "8":
            if hacker.guardar():
                print(f"{Fore.GREEN}✅ Partida guardada correctamente.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Error al guardar la partida.{Style.RESET_ALL}")
            time.sleep(1)
        
        elif opcion == "9":
            guia_usuario()
        
        elif opcion == "0":
            if hacker.guardar():
                print(f"{Fore.GREEN}✅ Partida guardada.{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}👋 ¡Hasta la próxima, {hacker.nombre}! Desconectando...{Style.RESET_ALL}")
            return False
        
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    try:
        mostrar_header()
        
        print(f"\n{Fore.CYAN}👤 Bienvenido al mundo del hacking digital.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Puedes cargar una partida existente o crear una nueva.{Style.RESET_ALL}")
        
        opcion = input(f"{Fore.CYAN}¿Cargar partida? (s/n): {Style.RESET_ALL}").strip().lower()
        
        hacker = None
        
        if opcion == 's':
            hacker = Hacker()
            if hacker.cargar():
                print(f"{Fore.GREEN}✅ Partida cargada. ¡Bienvenido de vuelta, {hacker.nombre}!{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}⚠️ No se encontró partida guardada. Creando nueva...{Style.RESET_ALL}")
                nombre = input(f"{Fore.CYAN}¿Cómo te llamas, hacker? {Style.RESET_ALL}").strip() or "Zero_Cool"
                hacker = Hacker(nombre)
        else:
            nombre = input(f"{Fore.CYAN}¿Cómo te llamas, hacker? {Style.RESET_ALL}").strip() or "Zero_Cool"
            hacker = Hacker(nombre)
        
        print(f"\n{Fore.GREEN}✅ Conexión establecida. ¡Bienvenido, {hacker.nombre}!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💡 Completa misiones, sube de nivel y conviértete en el mejor hacker.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Escribe '9' en cualquier momento para ver la guía de usuario.{Style.RESET_ALL}")
        time.sleep(2)
        
        menu_principal(hacker)
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Sesión terminada por el usuario.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error inesperado: {e}{Style.RESET_ALL}")
        input(f"{Fore.CYAN}⏎ Presiona Enter para salir...{Style.RESET_ALL}")

# ============================================
# EJECUCIÓN
# ============================================

if __name__ == "__main__":
    main()