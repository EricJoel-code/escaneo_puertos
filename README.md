# Escáner de Puertos en Python

Este proyecto es una aplicación de escaneo de puertos implementada en Python con una interfaz gráfica utilizando `tkinter`. La aplicación permite escanear una dirección IP en un rango de puertos especificado y muestra cuáles están abiertos y cerrados.

## Características

- Escaneo de puertos para una dirección IP específica.
- Especificación de rango de puertos a escanear.
- Resultados de escaneo con puertos abiertos y cerrados.
- Interfaz gráfica amigable con `tkinter`.
- Opción para realizar un nuevo escaneo sin reiniciar la aplicación.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- `tkinter` (viene preinstalado con Python)
- `threading` (parte del paquete estándar de Python)

### Ejecuta la aplicación
python main.py

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/EricJoel-code/escaneo_puertos.git

### Uso

- Introducir Dirección IP: Escribe la dirección IP que deseas escanear en el campo correspondiente.
- Especificar Rango de Puertos: Ingresa el puerto inicial y el puerto final que deseas escanear.
- Iniciar Escaneo: Haz clic en el botón "Iniciar Escaneo" para comenzar. La aplicación mostrará los puertos abiertos y cerrados en el área de resultados.
- Nuevo Escaneo: Una vez que el escaneo se complete, puedes hacer clic en el botón "Nuevo Escaneo" para limpiar los campos y realizar otro escaneo.

### Ejemplo de IPs para Escanear
Algunos ejemplos de direcciones IP que puedes usar para probar el escáner:

- 127.0.0.1 (localhost)
- 192.168.1.1 (dirección común de routers en redes domésticas)
- 8.8.8.8 (DNS de Google)

### Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias para nuevas funcionalidades, no dudes en crear un issue o hacer un pull request.
