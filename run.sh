#!/bin/bash
# Script para ejecutar el juego fácilmente

# Activar entorno virtual si existe
if [ -d ".venv" ]; then
    source .venv/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
fi

# Ejecutar el juego
python cyberdex.py

# Desactivar entorno virtual
deactivate 2>/dev/null