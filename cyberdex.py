#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKER SIMULATOR 2077 - Ultimate Edition
========================================
Un simulador de hacking en terminal donde encarnas a un hacker ético.
Version: 4.0.0
Autor: DlopedDtorred
Licencia: MIT

Características:
- 10 servidores con diferentes dificultades
- Sistema de niveles y experiencia
- Tienda con herramientas
- Sistema de logros (15+)
- Misiones diarias
- Ranking de hackers
- Inventario
- Sistema de rachas
"""

import random
import os
import time
import sys
import json
from datetime import datetime, timedelta
from colorama import init, Fore, Back, Style

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

# Inicializar colorama (conversión para terminales sin soporte)
init(autoreset=True, convert=True)

# Limpiar pantalla al inicio
os.system('cls' if os.name == 'nt' else 'clear')

# Versión del juego
VERSION = "4.0.0"
AUTOR = "DlopedDtorred"

# ============================================
# BASE DE DATOS DE SERVIDORES (10 niveles)
# ============================================

SERVIDORES = [
    # Nivel 1-2: Fáciles
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
    # Nivel 3-4: Intermedios
    {
        "id": "SRV-003",
        "nombre": "CyberDyne Systems",
        "dificultad": 3,
        "recompensa": 400,
        "pista": "🎬 ¿Año de Blade Runner? (20XX)",
        "password": "2019",
        "descripcion": "Sistemas de inteligencia artificial"
    },
    {
        "id": "SRV-004",
        "nombre": "NeoTokyo Grid",
        "dificultad": 4,
        "recompensa": 600,
        "pista": "🇯🇵 Código postal de Shibuya (7 dígitos)",
        "password": "1500042",
        "descripcion": "Red de datos de la ciudad digital"
    },
    # Nivel 5-6: Avanzados
    {
        "id": "SRV-005",
        "nombre": "A.I. Core",
        "dificultad": 5,
        "recompensa": 1000,
        "pista": "🔢 Fibonacci posición 13",
        "password": "233",
        "descripcion": "Núcleo de inteligencia artificial"
    },
    {
        "id": "SRV-006",
        "nombre": "Quantum Nexus",
        "dificultad": 6,
        "recompensa": 1500,
        "pista": "⚛️ Constante de Planck (3 primeros dígitos)",
        "password": "662",
        "descripcion": "Servidor cuántico experimental"
    },
    # Nivel 7-8: Expertos
    {
        "id": "SRV-007",
        "nombre": "NanoTech Labs",
        "dificultad": 7,
        "recompensa": 2000,
        "pista": "🔬 Número atómico del carbono",
        "password": "6",
        "descripcion": "Laboratorio de nanotecnología"
    },
    {
        "id": "SRV-008",
        "nombre": "Matrix Archive",
        "dificultad": 8,
        "recompensa": 3000,
        "pista": "🎬 Número de habitación de Neo en The Matrix",
        "password": "303",
        "descripcion": "Archivo de la resistencia humana"
    },
    # Nivel 9-10: Legendarios
    {
        "id": "SRV-009",
        "nombre": "ChronoCore",
        "dificultad": 9,
        "recompensa": 5000,
        "pista": "⏳ Año del descubrimiento del ADN (19XX)",
        "password": "1953",
        "descripcion": "Base de datos del flujo temporal"
    },
    {
        "id": "SRV-010",
        "nombre": "Omega Station",
        "dificultad": 10,
        "recompensa": 10000,
        "pista": "☯️ 666 × 7 (número de la bestia por la suerte)",
        "password": "4662",
        "descripcion": "El servidor definitivo. ¿Estás listo?"
    }
]

# ============================================
# SISTEMA DE LOGROS
# ============================================

LOGROS = {
    "primer_hackeo": {"nombre": "🚀 Primer Hackeo", "desc": "Completa tu primera misión"},
    "cinco_misiones": {"nombre": "💪 Cinco Misiones", "desc": "Completa 5 misiones"},
    "diez_misiones": {"nombre": "🏆 Diez Misiones", "desc": "Completa 10 misiones"},
    "veinticinco_misiones": {"nombre": "👑 Leyenda", "desc": "Completa 25 misiones"},
    "nivel_5": {"nombre": "⚡ Nivel 5", "desc": "Alcanza el nivel 5"},
    "nivel_10": {"nombre": "🌟 Nivel 10", "desc": "Alcanza el nivel 10"},
    "millonario": {"nombre": "💰 Millonario", "desc": "Acumula 1000 créditos"},
    "billonario": {"nombre": "💎 Billonario", "desc": "Acumula 5000 créditos"},
    "perfecto": {"nombre": "🎯 Perfecto", "desc": "Completa 5 misiones sin fallar"},
    "racha_5": {"nombre": "🔥 Racha 5", "desc": "5 misiones seguidas"},
    "racha_10": {"nombre": "🔥🔥 Racha 10", "desc": "10 misiones seguidas"},
    "coleccionista": {"nombre": "🛠️ Coleccionista", "desc": "Todas las herramientas"},
    "omega": {"nombre": "☯️ Omega", "desc": "Completa Omega Station"},
}

# ============================================
# CLASE HACKER (JUGADOR)
# ============================================

class Hacker:
    """Clase principal del jugador. Almacena todas las estadísticas y progreso."""
    
    def __init__(self, nombre):
        # Datos básicos
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0
        self.exp_necesaria = 10
        
        # Recursos
        self.creditos = 50
        self.herramientas = ["🔧 Escáner básico"]
        self.inventario = {}
        
        # Estadísticas
        self.misiones_completadas = 0
        self.fallos = 0
        self.racha_actual = 0
        self.mejor_racha = 0
        self.servidores_hackeados = []
        self.logros_desbloqueados = []
        
        # Misiones diarias
        self.ultima_mision_diaria = None
        self.mision_diaria_completada = False
        
        # Tiempo de juego
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tiempo_jugado = 0
        
        # Estado
        self.ultima_mision = None
        
    # ===== MÉTODOS DE PROGRESIÓN =====
    
    def ganar_exp(self, cantidad):
        """Gana experiencia y sube de nivel si es necesario."""
        self.exp += cantidad
        while self.exp >= self.exp_necesaria:
            self.subir_nivel()
    
    def subir_nivel(self):
        """Sube de nivel y da recompensas."""
        self.nivel += 1
        self.exp = 0
        self.exp_necesaria = self.nivel * 15
        
        # Mostrar mensaje
        print(f"\n{Fore.MAGENTA}{'═'*50}")
        print(f"🌟 ¡SUBES AL NIVEL {self.nivel}! 🌟")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        # Recompensas por nivel
        if self.nivel % 2 == 0:
            self._dar_herramienta()
        
        if self.nivel % 3 == 0:
            bonus = self.nivel * 50
            self.creditos += bonus
            print(f"{Fore.GREEN}💰 Bonus de nivel: +{bonus} créditos{Style.RESET_ALL}")
        
        if self.nivel % 5 == 0:
            print(f"{Fore.YELLOW}🎁 ¡Recompensa especial por nivel {self.nivel}!{Style.RESET_ALL}")
            self.creditos += 200
    
    def _dar_herramienta(self):
        """Da una nueva herramienta según el nivel."""
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
        
        # Calcular índice según nivel
        idx = (self.nivel // 2 - 1) % len(herramientas)
        nueva = herramientas[idx]
        
        if nueva not in self.herramientas:
            self.herramientas.append(nueva)
            print(f"{Fore.CYAN}🔧 ¡Nueva herramienta: {nueva}!{Style.RESET_ALL}")
    
    # ===== MÉTODOS DE LOGROS =====
    
    def verificar_logros(self):
        """Verifica y desbloquea logros automáticamente."""
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
        
        # Nivel
        if self.nivel >= 5 and "nivel_5" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_5")
        if self.nivel >= 10 and "nivel_10" not in self.logros_desbloqueados:
            nuevos_logros.append("nivel_10")
        
        # Créditos
        if self.creditos >= 1000 and "millonario" not in self.logros_desbloqueados:
            nuevos_logros.append("millonario")
        if self.creditos >= 5000 and "billonario" not in self.logros_desbloqueados:
            nuevos_logros.append("billonario")
        
        # Rachas
        if self.mejor_racha >= 5 and "racha_5" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_5")
        if self.mejor_racha >= 10 and "racha_10" not in self.logros_desbloqueados:
            nuevos_logros.append("racha_10")
        
        # Perfecto (5 misiones sin fallos)
        if self.misiones_completadas >= 5 and self.fallos == 0 and "perfecto" not in self.logros_desbloqueados:
            nuevos_logros.append("perfecto")
        
        # Coleccionista (todas las herramientas)
        if len(self.herramientas) >= 8 and "coleccionista" not in self.logros_desbloqueados:
            nuevos_logros.append("coleccionista")
        
        # Omega
        if "Omega Station" in self.servidores_hackeados and "omega" not in self.logros_desbloqueados:
            nuevos_logros.append("omega")
        
        # Desbloquear logros
        for logro_id in nuevos_logros:
            self.logros_desbloqueados.append(logro_id)
            logro = LOGROS[logro_id]
            print(f"{Fore.YELLOW}🏆 ¡LOGRO DESBLOQUEADO: {logro['nombre']}!{Style.RESET_ALL}")
            print(f"{Fore.WHITE}   📝 {logro['desc']}{Style.RESET_ALL}")
    
    # ===== MÉTODOS DE MOSTRAR =====
    
    def calcular_rango(self):
        """Calcula el rango del hacker según su nivel."""
        if self.nivel >= 10:
            return "👑 LEGENDARY HACKER"
        elif self.nivel >= 8:
            return "⚡ ELITE HACKER"
        elif self.nivel >= 6:
            return "🔥 SENIOR HACKER"
        elif self.nivel >= 4:
            return "💻 JUNIOR HACKER"
        elif self.nivel >= 2:
            return "🔰 APRENDIZ"
        else:
            return "🐣 NOVATO"
    
    def __str__(self):
        """Representación visual del hacker."""
        # Barra de experiencia
        if self.exp_necesaria > 0:
            porcentaje = self.exp / self.exp_necesaria
            barra = "█" * int(porcentaje * 15)
            vacio = "░" * (15 - len(barra))
        else:
            barra = ""
            vacio = "░" * 15
        
        # Construir el string
        return f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════╗
{Fore.CYAN}║ {Fore.WHITE}👤 {self.nombre} {Fore.CYAN}│ {Fore.YELLOW}Nv.{self.nivel} {Fore.CYAN}│ {Fore.GREEN}💰 {self.creditos} créditos
{Fore.CYAN}║ {Fore.WHITE}📊 EXP [{barra}{vacio}] {self.exp}/{self.exp_necesaria}
{Fore.CYAN}║ {Fore.WHITE}🏆 {self.calcular_rango()}
{Fore.CYAN}║ {Fore.WHITE}🛠️  {', '.join(self.herramientas)}
{Fore.CYAN}║ {Fore.WHITE}📈 Rachas: {self.racha_actual} actual │ {self.mejor_racha} máxima
{Fore.CYAN}║ {Fore.WHITE}🎯 Misiones: {self.misiones_completadas} │ ❌ Fallos: {self.fallos}
{Fore.CYAN}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

# ============================================
# MINI-JUEGOS
# ============================================

class MiniJuegos:
    """Colección de mini-juegos para las misiones."""
    
    @staticmethod
    def firewall_memoria(dificultad, intentos_max):
        """
        Mini-juego de firewall: memorizar y repetir una secuencia.
        
        Args:
            dificultad (int): Nivel de dificultad (afecta longitud)
            intentos_max (int): Número máximo de intentos
        
        Returns:
            bool: True si se supera, False si falla
        """
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔥 ¡FIREWALL DETECTADO! Memoriza la secuencia:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🛡️  Tienes {intentos_max} intentos{Style.RESET_ALL}")
        
        # Longitud según dificultad
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
        """
        Mini-juego: Descifrar mensaje con cifrado César.
        
        Args:
            dificultad (int): Nivel de dificultad
        
        Returns:
            bool: True si se descifra, False si falla
        """
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🔐 ¡CÓDIGO ENCRIPTADO! Descifra el mensaje:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        palabras = ["HACKER", "SISTEMA", "SEGURO", "DATOS", "RED", "CYBER", 
                   "NEXUS", "QUANTUM", "MATRIX", "OMEGA"]
        palabra = random.choice(palabras)
        
        # Desplazamiento según dificultad
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
        """
        Mini-juego: Inyección SQL.
        
        Args:
            dificultad (int): Nivel de dificultad
        
        Returns:
            bool: True si se logra, False si falla
        """
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
        """
        Mini-juego: Puzzle lógico de secuencias.
        
        Args:
            dificultad (int): Nivel de dificultad
        
        Returns:
            bool: True si se resuelve, False si falla
        """
        print(f"\n{Fore.YELLOW}{'═'*50}")
        print(f"🧩 ¡PUZZLE LÓGICO! Encuentra el número que falta:")
        print(f"{'═'*50}{Style.RESET_ALL}")
        
        # Tipos de puzzles
        tipos = ["suma", "multiplica", "fibonacci", "cuadrados"]
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
        
        else:  # cuadrados
            secuencia = [1, 4, 9, 16, 25]
            respuesta = 36
            pista = "Números al cuadrado: 1², 2², 3²..."
        
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
# FUNCIONES DEL JUEGO
# ============================================

def mostrar_header():
    """Muestra el encabezado del juego."""
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
{Fore.GREEN}║     {Fore.WHITE}by {AUTOR}{Fore.GREEN}                                              ║
{Fore.GREEN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(header)

def mision_hackeo(hacker, servidor):
    """
    Ejecuta una misión de hackeo.
    
    Args:
        hacker (Hacker): El jugador
        servidor (dict): Datos del servidor
    
    Returns:
        bool: True si se completa, False si falla
    """
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
        
        # Si tiene Crypto Key, puede pedir ayuda
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
    
    # Calcular recompensa
    recompensa_base = servidor['recompensa']
    bonus_racha = min(hacker.racha_actual * 25, 200)
    recompensa_total = recompensa_base + bonus_racha
    
    # Bonus por nivel
    if hacker.nivel >= 5:
        recompensa_total = int(recompensa_total * 1.2)
    
    # Aplicar recompensas
    hacker.creditos += recompensa_total
    hacker.misiones_completadas += 1
    hacker.racha_actual += 1
    
    if hacker.racha_actual > hacker.mejor_racha:
        hacker.mejor_racha = hacker.racha_actual
    
    hacker.servidores_hackeados.append(servidor['nombre'])
    hacker.ultima_mision = servidor['nombre']
    
    exp_ganada = servidor['dificultad'] * 5 + hacker.racha_actual * 2
    hacker.ganar_exp(exp_ganada)
    
    # Mostrar recompensas
    print(f"{Fore.GREEN}💰 Recompensa total: +{recompensa_total} créditos")
    print(f"{Fore.GREEN}📈 +{exp_ganada} EXP")
    if bonus_racha > 0:
        print(f"{Fore.GREEN}🔥 Bonus de racha: +{bonus_racha} créditos")
    if hacker.racha_actual >= 3:
        print(f"{Fore.MAGENTA}🔥 ¡Racha de {hacker.racha_actual} misiones!{Style.RESET_ALL}")
    
    # Verificar logros
    hacker.verificar_logros()
    
    return True

def tienda(hacker):
    """Muestra la tienda de herramientas."""
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
    ]
    
    for i, item in enumerate(items, 1):
        estado = "✅" if item['nombre'] in hacker.herramientas else "❌"
        print(f"[{i}] {estado} {item['nombre']}")
        print(f"    {Fore.WHITE}💰 {item['precio']} créditos │ 📝 {item['desc']}{Style.RESET_ALL}")
    
    print("[7] 💰 Comprar EXP (100 créditos = 10 EXP)")
    print("[0] 🚪 Salir de la tienda")
    
    try:
        opcion = int(input("\n➡️  ").strip())
        
        if opcion == 0:
            return
        
        elif opcion == 7:
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
    """Muestra estadísticas detalladas del hacker."""
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

def mision_diaria(hacker):
    """Genera y ejecuta una misión diaria."""
    print(f"\n{Fore.YELLOW}{'═'*50}")
    print(f"📅 MISIÓN DIARIA")
    print(f"{'═'*50}{Style.RESET_ALL}")
    
    # Verificar si ya se completó hoy
    if hacker.mision_diaria_completada:
        print(f"{Fore.YELLOW}⚠️ Ya completaste tu misión diaria de hoy.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}⏳ Vuelve mañana para una nueva misión.{Style.RESET_ALL}")
        input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        return
    
    # Seleccionar servidor aleatorio (dificultad 1-5)
    disponibles = [s for s in SERVIDORES if s['dificultad'] <= 5]
    servidor = random.choice(disponibles)
    
    print(f"{Fore.YELLOW}🌟 Misión especial de hoy:{Style.RESET_ALL}")
    print(f"🎯 HACKEAR: {servidor['nombre']}")
    print(f"⭐ Dificultad: {servidor['dificultad']} ★")
    print(f"💰 Recompensa: {servidor['recompensa'] * 2} créditos (¡DOBLE!){Style.RESET_ALL}")
    
    # Ejecutar misión con recompensa doble
    print(f"\n{Fore.CYAN}💡 La recompensa es el DOBLE por ser misión diaria.{Style.RESET_ALL}")
    
    # Hackear normalmente pero con recompensa doble
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
    
    # Completada
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

def ranking(hacker):
    """Muestra el ranking de hackers (simulado)."""
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}🏆 RANKING DE HACKERS")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    # Generar oponentes ficticios
    nombres_ficticios = [
        ("Shadow", 8), ("Neon", 7), ("Vortex", 6), 
        ("Ghost", 5), ("Phoenix", 4), ("Cipher", 3)
    ]
    
    print(f"{Fore.WHITE}Posición │ Hackers │ Nivel │ Misiones{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
    
    # Posición 1: El jugador (si tiene misiones)
    if hacker.misiones_completadas > 0:
        print(f"{Fore.GREEN}🏆 #1  │ {hacker.nombre} │ {hacker.nivel}     │ {hacker.misiones_completadas}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}#1  │ (vacío) │ 0     │ 0{Style.RESET_ALL}")
    
    # Oponentes
    for i, (nombre, nivel) in enumerate(nombres_ficticios, 2):
        misiones = random.randint(1, nivel * 3)
        print(f"#{i}  │ {nombre} │ {nivel}     │ {misiones}")
    
    print(f"\n{Fore.CYAN}💡 Para subir en el ranking, completa más misiones.{Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")

# ============================================
# MENÚ PRINCIPAL
# ============================================

def menu_principal(hacker):
    """Bucle principal del juego."""
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
        print("[7] 🚪 Salir")
        
        opcion = input("➡️  ").strip()
        
        if opcion == "1":
            # Hackear servidor
            print(f"\n{Fore.CYAN}🌐 SERVIDORES DISPONIBLES:{Style.RESET_ALL}")
            
            # Mostrar servidores disponibles según nivel
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
            print(f"\n{Fore.GREEN}👋 ¡Hasta la próxima, {hacker.nombre}! Desconectando...{Style.RESET_ALL}")
            return False
        
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    """Función principal del juego."""
    try:
        mostrar_header()
        
        # Pedir nombre
        print(f"\n{Fore.CYAN}👤 Bienvenido al mundo del hacking digital.{Style.RESET_ALL}")
        nombre = input(f"{Fore.CYAN}¿Cómo te llamas, hacker? {Style.RESET_ALL}").strip() or "Zero_Cool"
        
        # Crear hacker
        hacker = Hacker(nombre)
        
        print(f"\n{Fore.GREEN}✅ Conexión establecida. ¡Bienvenido, {nombre}!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💡 Completa misiones, sube de nivel y conviértete en el mejor hacker.{Style.RESET_ALL}")
        time.sleep(2)
        
        # Iniciar juego
        menu_principal(hacker)
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Sesión terminada por el usuario.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error inesperado: {e}{Style.RESET_ALL}")
        input(f"{Fore.CYAN}⏎ Presiona Enter para salir...{Style.RESET_ALL}")

# ============================================
# EJECUCIÓN DEL JUEGO
# ============================================

if __name__ == "__main__":
    main()