#socket es una biblioteca que se utiliza para crear conexiones de red 
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time 

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
    # Se registra el tiempo de inicio del escaneo para calcular la duración total al finalizar.
    start_time = time.time()
    
    #Lista para almacenar los puertos abiertos y cerrados
    open_ports = []
    closed_ports = []

    ports = range(start_port, end_port + 1)
    #Utiliza un ThreadPoolExecutor para escanear los puertos en paralelo, lo que mejora el rendimiento.
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {
            executor.submit(scan_port, ip, port): port for port in ports
        }
        
        for future in as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    open_ports.append(port)
                else:
                    closed_ports.append(port)
            except Exception:
                closed_ports.append(port)
                
    # Se registra el tiempo de finalización del escaneo y se calcula el tiempo transcurrido, que se devuelve junto con las listas de puertos abiertos y cerrados.           
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 4)
                
    return sorted(open_ports), sorted(closed_ports), elapsed_time