🔍 Escáner de Puertos en Python

Este proyecto es una herramienta de escaneo de puertos TCP desarrollada en Python. Permite identificar qué puertos se encuentran abiertos o cerrados en una dirección IP específica, utilizando sockets y técnicas básicas de concurrencia.

El sistema cuenta con dos formas de uso:

🖥️ Interfaz gráfica (GUI) desarrollada con tkinter

⌨️ Interfaz por línea de comandos (CLI) para uso técnico y automatización

🚀 Características

Escaneo de puertos TCP para una IP específica

Definición de rango de puertos (inicio y fin)

Identificación de puertos abiertos y cerrados

Interfaz gráfica amigable con tkinter

Interfaz CLI profesional mediante argumentos

Escaneo en segundo plano sin bloquear la interfaz

Código modular y reutilizable

Preparado para mejoras avanzadas (multithreading)

🧱 Estructura del Proyecto
port_scanner/
│
├── scanner/
│   ├── __init__.py
│   └── scanner.py        # Lógica principal de escaneo
│
├── cli/
│   ├── __init__.py
│   └── cli_app.py        # Escáner por línea de comandos
│
├── app/
│   └── app.py            # Interfaz gráfica (tkinter)
│
├── main.py               # Archivo Principal
└── README.md

📋 Requisitos

Python 3.9 o superior

Librerías estándar de Python:

socket

threading

tkinter

argparse

No se requieren dependencias externas.

🖥️ Uso — Interfaz Gráfica (GUI)

Desde la carpeta raíz del proyecto:

python gui/app.py

Pasos:

Ingresa la dirección IP objetivo

Define el puerto inicial y final

Haz clic en Iniciar Escaneo

Visualiza los puertos abiertos y cerrados

Usa Nuevo Escaneo para reiniciar

⌨️ Uso — Línea de Comandos (CLI)

Ejecuta el escáner desde la raíz del proyecto:

python -m cli.cli_app -i 127.0.0.1 -s 1 -e 100

Parámetros disponibles:
Parámetro	Descripción
-i	Dirección IP objetivo
-s	Puerto inicial
-e	Puerto final
-h	Mostrar ayuda
Ejemplo con salida a archivo:
python -m cli.cli_app -i 127.0.0.1 -s 1 -e 100 > resultados.txt

🧪 Ejemplos de IP para pruebas

127.0.0.1 — localhost

192.168.1.1 — router doméstico

8.8.8.8 — DNS público de Google

⚠️ Aviso Legal

Este proyecto es solo para fines educativos.
No escanees sistemas sin autorización explícita.

🤝 Contribuciones

Las contribuciones son bienvenidas.
Puedes:

Reportar errores

Proponer mejoras

Enviar pull requests

🛣️ Roadmap

 Escaneo secuencial de puertos

 Interfaz gráfica (GUI)

 Interfaz CLI

 Escaneo multithreading

 Exportación a CSV / HTML

 Detección de servicios comunes

 Medición de tiempos de respuesta