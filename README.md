# 🔍 PortScanner — Escáner de Puertos TCP en Python

EHerramienta profesional de escaneo de puertos TCP desarrollada en Python.
Permite identificar puertos abiertos y cerrados en un host específico utilizando sockets y ejecución concurrente mediante multithreading.

El proyecto está estructurado como paquete instalable y puede ejecutarse como:

* 🖥️ Interfaz gráfica (GUI) desarrollada con tkinter
* ⌨️ Herramienta CLI profesional (portscan)

---

## 🚀 Características

* Escaneo de puertos TCP
* Definición de rango personalizado
* Identificación de puertos abiertos y cerrados
* Escaneo concurrente con multithreading configurable
* Configuración de número de hilos (--threads)
* Configuración de timeout por puerto (--timeout)
* Medición del tiempo total de escaneo
* CLI profesional con argumentos avanzados
* Interfaz gráfica no bloqueante
* Código modular y reutilizable
* Instalación como paquete local (pip install -e .)
* Arquitectura preparada para expansión profesional

---

## 🧱 Estructura del Proyecto

```text
port_scanner/
│
├── portscanner/
│   ├── __init__.py
│   └── scanner.py        # Lógica principal de escaneo
│   └── cli.py            # Escáner por línea de comandos
│
├── gui/
│   └── app.py            # Interfaz gráfica (tkinter)
│
├── venv/                 # Entorno virtual
│
├── setup.py
├── requirements.txt
├── main.py               # Archivo principal
└── README.md
```

---

## 🛠 Instalación (Recomendado)

1️⃣ Crear entorno virtual
```
python -m venv venv
```
Activar:

Windows:
```
venv\Scripts\activate
```
Linux / macOS:
```
source venv/bin/activate
```

2️⃣ Instalar el proyecto en modo editable
```
pip install -e .
```
Esto habilita el comando:
```
portscan
```

---

## ⌨️ Uso — CLI Profesional (Actualizado)

Ejecuta el escáner desde la raíz del proyecto:

```bash
portscan -i 127.0.0.1 -s 1 -e 100
```

### Parámetros disponibles

| Parámetro      | Descripción                                          |
| -------------- | ---------------------------------------------------- |
| -i/--i         | Dirección IP objetivo                                |
| -s/--start     | Puerto inicial                                       |
| -e/--end       | Puerto final                                         |
| -t/--threads   | Número de hilos (default: 100)                       |
| --timeout      | Tiempo de espera por puerto en segundos (default: 1) |
| -h             | Mostrar ayuda                                        |

### Ejemplo Avanzado

```bash
portscan -i 127.0.0.1 -s 1 -e 100 --threads 200 --timeout 0.5
```

### Redireccion de Salida

```bash
portscan -i 127.0.0.1 -s 1 -e 100 > resultados.txt
```

---

## 🖥️ Uso — Interfaz Gráfica (GUI)

Desde la carpeta raíz del proyecto:

```bash
python -m gui.app
```

### Pasos

1. Ingresa la dirección IP objetivo
2. Define el puerto inicial y final
3. Haz clic en **Iniciar Escaneo**
4. Visualiza los puertos abiertos y cerrados
5. Usa **Nuevo Escaneo** para reiniciar

---

## 📋 Requisitos

* Python 3.9 o superior
* Librerías estándar de Python:

  * socket
  * threading
  * tkinter
  * argparse

No se requieren dependencias externas.

---

## 🧪 Ejemplos de IP para pruebas

* 127.0.0.1 — localhost
* 192.168.1.1 — router doméstico
* 8.8.8.8 — DNS público de Google

---

## ⚠️ Aviso Legal

Este proyecto es solo para fines educativos.
No escanees sistemas sin autorización explícita.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes:

* Reportar errores
* Proponer mejoras
* Enviar pull requests

---

## 🛣️ Roadmap

* [x] Escaneo secuencial de puertos
* [x] Interfaz gráfica (GUI)
* [x] Interfaz CLI
* [x] Escaneo multithreading
* [x] Configuración de threads y timeout
* [x] Medición de tiempo de escaneo
* [ ] Exportación a CSV / HTML
* [ ] Detección de servicios comunes
* [ ] Sistema de logs
* [ ] Tests automatizados

---

## ⚙️ Configuración avanzada

El escáner permite ajustar el rendimiento mediante:

- --threads: Controla el número de hilos concurrentes.
- --timeout: Define el tiempo máximo de espera por puerto.

Esto permite adaptar la herramienta a redes rápidas o lentas.

---

## 🎯 Objetivo del Proyecto

Proyecto enfocado en aprendizaje práctico de:

* Sockets en Python
* Concurrencia con threading
* Arquitectura modular
* Empaquetado profesional
* Buenas prácticas de desarrollo

---

⭐ Si te resulta útil, ¡no olvides darle una estrella al repositorio!
