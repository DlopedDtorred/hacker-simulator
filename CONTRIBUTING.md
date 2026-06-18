# Guía para Colaboradores

¡Gracias por tu interés en contribuir a Hacker Simulator 2077! 🎉

## 📋 Tabla de Contenidos
- [Código de Conducta](#código-de-conducta)
- [Cómo Empezar](#cómo-empezar)
- [Áreas de Contribución](#áreas-de-contribución)
- [Proceso de PR](#proceso-de-pr)
- [Estilo de Código](#estilo-de-código)
- [Reportar Bugs](#reportar-bugs)
- [Sugerir Mejoras](#sugerir-mejoras)

## 📜 Código de Conducta

Por favor, sé respetuoso con otros colaboradores. Aceptamos a todos independientemente de su nivel de experiencia.

## 🚀 Cómo Empezar

1. **Fork del repositorio**
2. **Clona tu fork:**
```bash
git clone https://github.com/tu-usuario/hacker-simulator.git
cd hacker-simulator
Instala las dependencias:

bash
pip install colorama
Crea una rama para tu feature:

bash
git checkout -b feature/nueva-caracteristica
Haz tus cambios y haz commit:

bash
git add .
git commit -m "Añade nueva característica"
Sube tus cambios:

bash
git push origin feature/nueva-caracteristica
Abre un Pull Request

## 🎯 Áreas de Contribución
1. Servidores (Fácil)
Añadir servidores en SERVIDORES:

python
{
    "id": "SRV-XXX",
    "nombre": "Nombre del Servidor",
    "dificultad": 1-13,
    "recompensa": 100-30000,
    "pista": "Pista útil para la contraseña",
    "password": "contraseña",
    "descripcion": "Breve descripción"
}
2. Mini-juegos (Media)
Añadir en la clase MiniJuegos:

python
@staticmethod
def nuevo_juego(dificultad):
    # Lógica del juego
    return True/False
3. Herramientas (Fácil)
Añadir en tienda():

python
{"nombre": "🔧 Nueva Herramienta", "precio": 100, "desc": "Descripción"}
4. Logros (Fácil)
Añadir en LOGROS:

python
"id_logro": {"nombre": "🏆 Nombre", "desc": "Descripción", "recompensa": 100}
5. Documentación (Fácil)
Mejorar README.md

Crear guías en docs/

Traducir a otros idiomas

6. Tests (Media)
Crear tests en tests/:

python
import unittest
from cyberdex import *

class TestHacker(unittest.TestCase):
    def test_crear_hacker(self):
        h = Hacker("Test")
        self.assertEqual(h.nombre, "Test")
## 🔄 Proceso de PR
Asegúrate de que tu código funciona:

Ejecuta python cyberdex.py y prueba

Verifica que no haya errores

Actualiza la documentación:

README.md si es necesario

Añade comentarios en el código

Envía el PR:

Título descriptivo

Descripción de los cambios

Issue relacionado (si existe)

## 📝 Estilo de Código
Sigue PEP 8 para Python

Usa comentarios en inglés

Nombres descriptivos

Máximo 80 caracteres por línea

## 🐛 Reportar Bugs
Crea un issue con:

Descripción del bug

Pasos para reproducirlo

Comportamiento esperado

Captura de pantalla (si aplica)

## 💡 Sugerir Mejoras
Crea un issue con:

Descripción de la mejora

Beneficio para el proyecto

Código de ejemplo (opcional)

## 🏆 Reconocimiento
Todos los colaboradores serán listados en:

Contributors

README.md

¡Gracias por hacer que Hacker Simulator 2077 sea mejor! 🚀