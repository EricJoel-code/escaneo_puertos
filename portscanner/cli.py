import argparse
#from portscanner.scanner import scan_ports
from portscanner.scanner import scan_ports


def main():
    # Crear el parser 
    parser = argparse.ArgumentParser(description="Escaneador de puertos simple")
    
    # Argumentos obligatorios
    parser.add_argument("-i","--ip", type=str, required=True, help="Direccion IP a escanear")
    
    parser.add_argument("-s","--start", type=int, required=True, help="Puerto inicial del rango a escanear")
    
    parser.add_argument("-e","--end", type=int, required=True, help="Puerto final del rango a escanear")
    
    
    # Leer los argumentos de la línea de comandos
    
    args = parser.parse_args()
    
    ip = args.ip
    start_port = args.start
    end_port = args.end
    
    print(f"[+] Escaneando {ip} ({start_port}-{end_port})...\n")

    # Llamar a la lógica reutilizada
    open_ports, closed_ports = scan_ports(ip, start_port, end_port)

    # Mostrar resultados
    print("[+] Puertos abiertos:")
    for port in open_ports:
        print(f"    [OPEN] {port}")

    print("\n[-] Puertos cerrados:")
    for port in closed_ports:
        print(f"    [CLOSED] {port}")

    print("\n[OK] Escaneo finalizado.")


if __name__ == "__main__":
    main()