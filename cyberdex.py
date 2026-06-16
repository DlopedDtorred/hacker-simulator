import random
import os
import time
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# ========== CONFIGURACIÓN ==========
VERSION = "3.0.0"
SERVIDORES = [
    {
        "nombre": "MegaCorp Alpha",
        "dificultad": 1,
        "recompensa": 150,
        "pista": "La mascota del CEO es un gato llamado",
        "password": "michifu"
    },
    {
        "nombre": "DarkNet Vault",
        "dificultad": 2,
        "recompensa": 250,
        "pista": "El número de la bestia sin el 6 final",
        "password": "666"
    },
    {
        "nombre": "CyberDyne Systems",
        "dificultad": 3,
        "recompensa": 400,
        "pista": "Año de Blade Runner (película de culto)",
        "password": "2019"
    },
    {
        "nombre": "NeoTokyo Grid",
        "dificultad": 4,
        "recompensa": 600,
        "pista": "Código postal de Shibuya",
        "password": "1500042"
    },
    {
        "nombre": "A.I. Core",
        "dificultad": 5,
        "recompensa": 1000,
        "pista": "Fibonacci posición 13",
        "password": "233"
    }
]

# ========== CLASE HACKER ==========
class Hacker:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0
        self.exp_necesaria = 10
        self.creditos = 50
        self.herramientas = ["Escáner básico"]
        self.misiones = 0
        self.racha = 0
        
    def ganar_exp(self, cantidad):
        self.exp += cantidad
        while self.exp >= self.exp_necesaria:
            self.nivel += 1
            self.exp = 0
            self.exp_necesaria = self.nivel * 15
            print(f"\n{Fore.MAGENTA}🌟 ¡SUBES A NIVEL {self.nivel}! 🌟{Style.RESET_ALL}")
            if self.nivel % 2 == 0:
                nueva = ["Descifrador", "Firewall Bypass", "Crypto Key"][self.nivel//2 - 1]
                if nueva not in self.herramientas:
                    self.herramientas.append(nueva)
                    print(f"{Fore.CYAN}🔧 ¡Nueva herramienta: {nueva}!{Style.RESET_ALL}")
    
    def __str__(self):
        barra = "█" * int((self.exp / self.exp_necesaria) * 10) if self.exp_necesaria > 0 else ""
        vacio = "░" * (10 - len(barra))
        return f"""
{Fore.CYAN}╔═══════════════════════════════════════════╗
{Fore.CYAN}║ {Fore.WHITE}👤 {self.nombre} {Fore.CYAN}│ {Fore.YELLOW}Nv.{self.nivel} {Fore.CYAN}│ {Fore.GREEN}💰 {self.creditos} créditos
{Fore.CYAN}║ {Fore.WHITE}📊 [{barra}{vacio}] {self.exp}/{self.exp_necesaria}
{Fore.CYAN}║ {Fore.WHITE}🛠️  {', '.join(self.herramientas)}
{Fore.CYAN}╚═══════════════════════════════════════════╝{Style.RESET_ALL}
"""

# ========== MINI-JUEGO FIREWALL ==========
def firewall():
    print(f"\n{Fore.YELLOW}🔥 ¡FIREWALL! Memoriza la secuencia:{Style.RESET_ALL}")
    secuencia = [str(random.randint(1, 9)) for _ in range(4)]
    print(f"{Fore.WHITE}{' '.join(secuencia)}{Style.RESET_ALL}")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    respuesta = input("➡️  Repite la secuencia: ").strip().split()
    if respuesta == secuencia:
        print(f"{Fore.GREEN}✅ ¡Firewall evadido!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}❌ Fallaste.{Style.RESET_ALL}")
        return False

# ========== MISIÓN ==========
def mision(hacker, servidor):
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.GREEN}🎯 HACKEANDO: {servidor['nombre']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}⭐ Dificultad: {servidor['dificultad']} ★")
    print(f"💰 Recompensa: {servidor['recompensa']} créditos")
    print(f"🔍 Pista: {servidor['pista']}{Style.RESET_ALL}")
    
    # Firewall
    if not firewall():
        hacker.racha = 0
        return False
    
    # Contraseña
    intentos = 3
    while intentos > 0:
        print(f"\n{Fore.CYAN}🔐 Intentos: {intentos}{Style.RESET_ALL}")
        password = input("➡️  Contraseña: ").strip()
        if password == servidor['password']:
            print(f"{Fore.GREEN}✅ ¡Acceso concedido!{Style.RESET_ALL}")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"{Fore.RED}❌ Incorrecto.{Style.RESET_ALL}")
    
    if intentos == 0:
        print(f"{Fore.RED}💀 Contraseña: {servidor['password']}{Style.RESET_ALL}")
        hacker.racha = 0
        return False
    
    # Completada
    print(f"\n{Fore.GREEN}🎉 ¡MISIÓN COMPLETADA!{Style.RESET_ALL}")
    hacker.creditos += servidor['recompensa']
    hacker.misiones += 1
    hacker.racha += 1
    hacker.ganar_exp(servidor['dificultad'] * 5)
    return True

# ========== TIENDA ==========
def tienda(hacker):
    print(f"\n{Fore.YELLOW}🛒 TIENDA{Style.RESET_ALL}")
    print(f"{Fore.GREEN}💰 Créditos: {hacker.creditos}{Style.RESET_ALL}")
    
    items = [
        {"nombre": "Escáner Avanzado", "precio": 100},
        {"nombre": "Firewall Bypass", "precio": 200},
        {"nombre": "Crypto Key", "precio": 300}
    ]
    
    for i, item in enumerate(items, 1):
        estado = "✅" if item['nombre'] in hacker.herramientas else "❌"
        print(f"[{i}] {estado} {item['nombre']} - {item['precio']} créditos")
    print("[0] Salir")
    
    try:
        opcion = int(input("➡️  "))
        if opcion == 0:
            return
        item = items[opcion-1]
        if item['nombre'] in hacker.herramientas:
            print(f"{Fore.YELLOW}⚠️ Ya lo tienes{Style.RESET_ALL}")
        elif hacker.creditos >= item['precio']:
            hacker.creditos -= item['precio']
            hacker.herramientas.append(item['nombre'])
            print(f"{Fore.GREEN}✅ ¡Comprado!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Sin créditos{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
    time.sleep(1)

# ========== HEADER ==========
def header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}╔═══════════════════════════════════════════╗
{Fore.GREEN}║  {Fore.CYAN}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ {Fore.GREEN}║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗{Fore.GREEN}║
{Fore.GREEN}║  {Fore.CYAN}███████║███████║██║     █████╔╝ █████╗  ██████╔╝{Fore.GREEN}║
{Fore.GREEN}║  {Fore.CYAN}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗{Fore.GREEN}║
{Fore.GREEN}║  {Fore.CYAN}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║{Fore.GREEN}║
{Fore.GREEN}║  {Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.GREEN}║
{Fore.GREEN}║     {Fore.YELLOW}HACKER SIMULATOR 2077 v{VERSION}{Fore.GREEN}     ║
{Fore.GREEN}╚═══════════════════════════════════════════╝{Style.RESET_ALL}
""")

# ========== MAIN ==========
def main():
    header()
    nombre = input(f"{Fore.CYAN}👤 Nombre de Hacker: {Style.RESET_ALL}").strip() or "Zero_Cool"
    hacker = Hacker(nombre)
    print(f"{Fore.GREEN}✅ ¡Bienvenido, {nombre}!{Style.RESET_ALL}")
    time.sleep(1)
    
    while True:
        header()
        print(hacker)
        print(f"\n{Fore.CYAN}📡 OPCIONES:{Style.RESET_ALL}")
        print("[1] 🌐 Misión")
        print("[2] 🛠️  Entrenar")
        print("[3] 🛒 Tienda")
        print("[4] 📊 Estadísticas")
        print("[5] 🚪 Salir")
        
        opcion = input("➡️  ").strip()
        
        if opcion == "1":
            print(f"\n{Fore.CYAN}🌐 SERVIDORES:{Style.RESET_ALL}")
            for i, s in enumerate(SERVIDORES, 1):
                print(f"[{i}] {s['nombre']} (★{s['dificultad']})")
            try:
                idx = int(input("➡️  ")) - 1
                if 0 <= idx < len(SERVIDORES):
                    mision(hacker, SERVIDORES[idx])
                input(f"{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
                time.sleep(1)
        
        elif opcion == "2":
            print(f"\n{Fore.CYAN}🛠️  ENTRENANDO...{Style.RESET_ALL}")
            if firewall():
                hacker.ganar_exp(5)
                print(f"{Fore.GREEN}📈 +5 EXP{Style.RESET_ALL}")
            input(f"{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif opcion == "3":
            tienda(hacker)
        
        elif opcion == "4":
            print(f"\n{Fore.CYAN}{'='*50}")
            print(f"{Fore.YELLOW}📊 ESTADÍSTICAS{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
            print(f"👤 Hacker: {hacker.nombre}")
            print(f"📈 Nivel: {hacker.nivel}")
            print(f"💰 Créditos: {hacker.creditos}")
            print(f"🎯 Misiones: {hacker.misiones}")
            print(f"🔥 Racha: {hacker.racha}")
            print(f"🛠️  Herramientas: {', '.join(hacker.herramientas)}")
            input(f"{Fore.CYAN}⏎ Enter...{Style.RESET_ALL}")
        
        elif opcion == "5":
            print(f"{Fore.GREEN}👋 ¡Hasta luego!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Sesión terminada{Style.RESET_ALL}")