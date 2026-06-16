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
        "pista": "🐱 La mascota favorita del CEO es un gato llamado... (pista: empieza por M)",
        "password": "michifu"
    },
    {
        "nombre": "DarkNet Vault",
        "dificultad": 2,
        "recompensa": 250,
        "pista": "👿 El número de la bestia pero sin el 6 final",
        "password": "666"
    },
    {
        "nombre": "CyberDyne Systems",
        "dificultad": 3,
        "recompensa": 400,
        "pista": "🎬 ¿En qué año se estrenó Blade Runner? (pista: 20XX)",
        "password": "2019"
    },
    {
        "nombre": "NeoTokyo Grid",
        "dificultad": 4,
        "recompensa": 600,
        "pista": "🇯🇵 Código postal del distrito de Shibuya en Tokio (7 dígitos)",
        "password": "1500042"
    },
    {
        "nombre": "A.I. Core",
        "dificultad": 5,
        "recompensa": 1000,
        "pista": "🔢 Secuencia Fibonacci: 1,1,2,3,5,8,13... ¿Cuál es el número en la posición 13?",
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
                nuevas = ["Descifrador", "Firewall Bypass", "Crypto Key"]
                idx = (self.nivel // 2 - 1) % len(nuevas)
                nueva = nuevas[idx]
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
{Fore.CYAN}║ {Fore.WHITE}🔥 Racha: {self.racha}
{Fore.CYAN}╚═══════════════════════════════════════════╝{Style.RESET_ALL}
"""

# ========== MINI-JUEGO FIREWALL ==========
def firewall():
    print(f"\n{Fore.YELLOW}{'='*50}")
    print(f"🔥 ¡FIREWALL DETECTADO! Memoriza la secuencia:")
    print(f"{'='*50}{Style.RESET_ALL}")
    
    secuencia = [str(random.randint(1, 9)) for _ in range(4)]
    print(f"\n{Fore.CYAN}🧠 Secuencia a memorizar:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}  {' '.join(secuencia)}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}⏳ Tienes 2 segundos...{Style.RESET_ALL}")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Fore.CYAN}⌨️  Repite la secuencia (números separados por espacio):{Style.RESET_ALL}")
    respuesta = input("➡️  ").strip().split()
    
    if respuesta == secuencia:
        print(f"{Fore.GREEN}✅ ¡Firewall evadido con éxito!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}❌ ¡Has sido detectado por el firewall!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 La secuencia era: {' '.join(secuencia)}{Style.RESET_ALL}")
        return False

# ========== MISIÓN ==========
def mision(hacker, servidor):
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.GREEN}🎯 MISIÓN: HACKEAR {servidor['nombre'].upper()}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}⭐ Dificultad: {servidor['dificultad']} ★")
    print(f"💰 Recompensa: {servidor['recompensa']} créditos")
    print(f"🔍 PISTA: {Fore.WHITE}{servidor['pista']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    # Firewall
    if not firewall():
        hacker.racha = 0
        print(f"\n{Fore.RED}💀 Misión fallida. Has sido detectado.{Style.RESET_ALL}")
        return False
    
    # Contraseña
    print(f"\n{Fore.CYAN}🔐 FASE 2: DESCIFRAR CONTRASEÑA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💡 Recuerda la pista: {servidor['pista']}{Style.RESET_ALL}")
    
    intentos = 3
    while intentos > 0:
        print(f"\n{Fore.CYAN}🔐 Intentos restantes: {intentos}{Style.RESET_ALL}")
        password = input("➡️  Contraseña: ").strip().lower()
        
        if password == servidor['password']:
            print(f"{Fore.GREEN}✅ ¡Contraseña correcta! Acceso concedido.{Style.RESET_ALL}")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"{Fore.RED}❌ Contraseña incorrecta.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💡 Pista: {servidor['pista']}{Style.RESET_ALL}")
    
    if intentos == 0:
        print(f"\n{Fore.RED}💀 Has agotado los intentos. Misión fallida.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🔑 La contraseña era: {servidor['password']}{Style.RESET_ALL}")
        hacker.racha = 0
        return False
    
    # Completada
    print(f"\n{Fore.GREEN}{'='*50}")
    print(f"🎉 ¡MISIÓN COMPLETADA CON ÉXITO! 🎉")
    print(f"{'='*50}{Style.RESET_ALL}")
    
    hacker.creditos += servidor['recompensa']
    hacker.misiones += 1
    hacker.racha += 1
    
    exp_ganada = servidor['dificultad'] * 5
    hacker.ganar_exp(exp_ganada)
    
    print(f"{Fore.GREEN}💰 +{servidor['recompensa']} créditos")
    print(f"{Fore.GREEN}📈 +{exp_ganada} EXP")
    if hacker.racha >= 3:
        print(f"{Fore.MAGENTA}🔥 ¡Racha de {hacker.racha} misiones!{Style.RESET_ALL}")
    
    return True

# ========== TIENDA ==========
def tienda(hacker):
    print(f"\n{Fore.YELLOW}{'='*50}")
    print(f"🛒 TIENDA DE HERRAMIENTAS")
    print(f"{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}💰 Créditos disponibles: {hacker.creditos}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🛠️  Tus herramientas: {', '.join(hacker.herramientas)}{Style.RESET_ALL}")
    print(f"{'='*50}")
    
    items = [
        {"nombre": "Escáner Avanzado", "precio": 100, "desc": "+2 intentos en contraseñas"},
        {"nombre": "Firewall Bypass", "precio": 200, "desc": "Reduce dificultad de firewalls"},
        {"nombre": "Crypto Key", "precio": 300, "desc": "Revela pistas adicionales"}
    ]
    
    for i, item in enumerate(items, 1):
        estado = "✅" if item['nombre'] in hacker.herramientas else "❌"
        print(f"[{i}] {estado} {item['nombre']} - {item['precio']} créditos")
        print(f"    {Fore.WHITE}📝 {item['desc']}{Style.RESET_ALL}")
    print("[0] Salir de la tienda")
    
    try:
        opcion = int(input("➡️  "))
        if opcion == 0:
            return
        if 1 <= opcion <= len(items):
            item = items[opcion-1]
            if item['nombre'] in hacker.herramientas:
                print(f"{Fore.YELLOW}⚠️ Ya tienes esta herramienta.{Style.RESET_ALL}")
            elif hacker.creditos >= item['precio']:
                hacker.creditos -= item['precio']
                hacker.herramientas.append(item['nombre'])
                print(f"{Fore.GREEN}✅ ¡{item['nombre']} adquirido!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Créditos insuficientes. Necesitas {item['precio'] - hacker.creditos} más.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
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
{Fore.GREEN}║     {Fore.WHITE}by DlopedDtorred{Fore.GREEN}                         ║
{Fore.GREEN}╚═══════════════════════════════════════════╝{Style.RESET_ALL}
""")

# ========== MAIN ==========
def main():
    header()
    nombre = input(f"{Fore.CYAN}👤 Introduce tu nombre de Hacker: {Style.RESET_ALL}").strip() or "Zero_Cool"
    hacker = Hacker(nombre)
    print(f"\n{Fore.GREEN}✅ Conexión establecida. ¡Bienvenido, {nombre}!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}💡 Tip: Presta atención a las PISTAS, te ayudarán a descifrar las contraseñas.{Style.RESET_ALL}")
    time.sleep(2)
    
    while True:
        header()
        print(hacker)
        print(f"\n{Fore.CYAN}📡 OPCIONES:{Style.RESET_ALL}")
        print("[1] 🌐 Aceptar misión (hackear servidor)")
        print("[2] 🛠️  Entrenar (practicar firewall)")
        print("[3] 🛒 Visitar tienda")
        print("[4] 📊 Ver estadísticas")
        print("[5] 🚪 Salir")
        
        opcion = input("➡️  ").strip()
        
        if opcion == "1":
            print(f"\n{Fore.CYAN}🌐 SERVIDORES DISPONIBLES:{Style.RESET_ALL}")
            for i, s in enumerate(SERVIDORES, 1):
                print(f"[{i}] {Fore.YELLOW}{s['nombre']}{Style.RESET_ALL} (★{s['dificultad']})")
            print(f"{Fore.CYAN}💡 Las pistas de cada servidor te ayudarán a encontrar la contraseña{Style.RESET_ALL}")
            
            try:
                idx = int(input("➡️  Elige un servidor: ")) - 1
                if 0 <= idx < len(SERVIDORES):
                    mision(hacker, SERVIDORES[idx])
                input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
                time.sleep(1)
        
        elif opcion == "2":
            print(f"\n{Fore.CYAN}🛠️  ENTRENAMIENTO DE FIREWALL{Style.RESET_ALL}")
            if firewall():
                hacker.ganar_exp(5)
                print(f"{Fore.GREEN}📈 +5 EXP ganada{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        
        elif opcion == "3":
            tienda(hacker)
        
        elif opcion == "4":
            print(f"\n{Fore.CYAN}{'='*50}")
            print(f"{Fore.YELLOW}📊 ESTADÍSTICAS DE {hacker.nombre.upper()}")
            print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}👤 Hacker: {hacker.nombre}")
            print(f"📈 Nivel: {hacker.nivel}")
            print(f"📊 EXP: {hacker.exp}/{hacker.exp_necesaria}")
            print(f"💰 Créditos: {hacker.creditos}")
            print(f"🎯 Misiones completadas: {hacker.misiones}")
            print(f"🔥 Racha actual: {hacker.racha}")
            print(f"🛠️  Herramientas: {', '.join(hacker.herramientas)}")
            print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}⏎ Presiona Enter para continuar...{Style.RESET_ALL}")
        
        elif opcion == "5":
            print(f"\n{Fore.GREEN}👋 ¡Hasta la próxima, {hacker.nombre}! Desconectando...{Style.RESET_ALL}")
            break
        
        else:
            print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Sesión terminada por el usuario.{Style.RESET_ALL}")