#!/usr/bin/env python3
"""
Generador de logo para Hacker Simulator 2077
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ Necesitas instalar Pillow: pip install Pillow")
    exit(1)

# Configuración
WIDTH = 500
HEIGHT = 500
COLOR_BG = (10, 10, 10)
COLOR_VERDE = (0, 255, 0)
COLOR_VERDE_OSCURO = (0, 100, 0)
COLOR_BLANCO = (255, 255, 255)

# Crear imagen
img = Image.new('RGB', (WIDTH, HEIGHT), COLOR_BG)
draw = ImageDraw.Draw(img)

# Fuentes
try:
    font_grande = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 60)
    font_pequena = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", 30)
except:
    try:
        font_grande = ImageFont.truetype("arial.ttf", 60)
        font_pequena = ImageFont.truetype("arial.ttf", 30)
    except:
        font_grande = ImageFont.load_default()
        font_pequena = ImageFont.load_default()

# Borde
draw.rectangle([10, 10, WIDTH-10, HEIGHT-10], outline=COLOR_VERDE, width=3)

# Icono terminal
draw.rectangle([180, 80, 320, 220], outline=COLOR_VERDE, width=3)
draw.text((210, 120), ">", fill=COLOR_VERDE, font=font_grande)
draw.text((260, 120), "_", fill=COLOR_VERDE, font=font_grande)

# Texto
draw.text((50, 250), "HACKER", fill=COLOR_VERDE, font=font_grande)
draw.text((50, 310), "SIMULATOR", fill=COLOR_VERDE_OSCURO, font=font_grande)
draw.text((180, 380), "2077", fill=COLOR_BLANCO, font=font_grande)
draw.text((150, 440), "⚡ ULTIMATE EDITION", fill=COLOR_VERDE, font=font_pequena)

# Guardar
img.save('logo.png')
print("✅ Logo creado: logo.png")