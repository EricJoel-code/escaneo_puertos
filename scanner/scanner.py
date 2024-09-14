#socket es una biblioteca que se utiliza para crear conexiones de red 
import socket

def scan_port(ip, port):
    """
    Escanea un puerto específico en una dirección IP.
    
    Args:
        ip (str): La dirección IP a escanear.
        port (int): El puerto a escanear.
    """
    #Se crea un objeto de socket utilizando IPv4 (AF_INET) y TCP (SOCK_STREAM).
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Se establece un tiempo de espera de 1 segundo para la conexión.
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False
    finally:
        sock.close()

def scan_ports(ip, start_port, end_port):
    """
    Escanea un rango de puertos en una dirección IP específica.
    
    Args:
        ip (str): La dirección IP a escanear.
        start_port (int): El puerto inicial del rango.
        end_port (int): El puerto final del rango.
    """
    #Lista para almacenar los puertos abiertos y cerrados
    open_ports = []
    closed_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)
        else:
            closed_ports.append(port)

    return open_ports, closed_ports
