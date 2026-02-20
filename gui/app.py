#maneja el escaneo de puertos en segundo plano sin bloquear la interfaz gráfica.
import threading
#crea la interfaz gráfica de usuario.
import tkinter as tk
#muestra mensajes de diálogo.
from tkinter import ttk, messagebox
#Importa la función scan_ports del módulo scanner que escanea un rango de puertos.
from portscanner.scanner import scan_ports

class PortScannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Escáner de Puertos")
        self.geometry("600x400")
        self.create_widgets()
        
        # Listas para almacenar los resultados
        self.open_ports = []
        self.closed_ports = []
        self.elapsed_time = 0 # Variable para almacenar el tiempo de escaneo

        """
        Entradas de texto para la dirección IP y los puertos inicial y final.
        Botón para iniciar el escaneo.
        Área de texto para mostrar los resultados.
        """
    def create_widgets(self):
        # Dirección IP
        tk.Label(self, text="Dirección IP:").grid(row=0, column=0, padx=10, pady=10)
        self.ip_entry = tk.Entry(self)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Puerto inicial
        tk.Label(self, text="Puerto inicial:").grid(row=1, column=0, padx=10, pady=10)
        self.start_port_entry = tk.Entry(self)
        self.start_port_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Puerto final
        tk.Label(self, text="Puerto final:").grid(row=2, column=0, padx=10, pady=10)
        self.end_port_entry = tk.Entry(self)
        self.end_port_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Botón para iniciar el escaneo
        self.scan_button = tk.Button(self, text="Iniciar Escaneo", command=self.start_scan)
        self.scan_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Botón para nuevo escaneo
        self.new_scan_button = tk.Button(self, text="Nuevo Escaneo", command=self.new_scan)
        self.new_scan_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        
        # Área de resultados
        self.results_text = tk.Text(self, state='disabled', height=15)
        self.results_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        """
        Recupera los valores de los campos de entrada.
        Actualiza el área de resultados para indicar que el escaneo ha comenzado.
        Reinicia las listas de puertos abiertos y cerrados.
        Inicia un hilo para ejecutar el escaneo sin bloquear la interfaz gráfica.
        """       
    def start_scan(self):
        ip = self.ip_entry.get()
        start_port = int(self.start_port_entry.get())
        end_port = int(self.end_port_entry.get())
        
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, f"Iniciando el escaneo de {ip} desde el puerto {start_port} hasta el puerto {end_port}\n")
        self.results_text.config(state='disabled')
        
        self.open_ports = []
        self.closed_ports = []
        
        # Crear y empezar un hilo para cada puerto en el rango
        scan_thread = threading.Thread(target=self.perform_scan, args=(ip, start_port, end_port))
        scan_thread.start()
    
        
    # Este método llama a la función scan_ports para realizar el escaneo de puertos y luego actualiza el área de resultados con los puertos abiertos, cerrados y el tiempo total del escaneo.
    def perform_scan(self, ip, start_port, end_port):
        self.open_ports, self.closed_ports, self.elapsed_time = scan_ports(ip, start_port, end_port)
        self.show_results()
        
        #Actualiza el área de resultados con los puertos abiertos y cerrados una vez completado el escaneo.
    def show_results(self):
        self.results_text.config(state='normal')
        
        self.results_text.insert(tk.END, "\nEscaneo completo.\n")
        self.results_text.insert(tk.END, f"Tiempo total: {self.elapsed_time} segundos\n")
        
        self.results_text.insert(tk.END, "\nPuertos abiertos:\n")
        if self.open_ports:
            for port in self.open_ports:
                self.results_text.insert(tk.END, f"Puerto {port}: Abierto\n")
                
        else:
            self.results_text.insert(tk.END, "Ninguno\n")
            
        self.results_text.insert(tk.END, "\nPuertos cerrados:\n")
        for port in self.closed_ports:
            self.results_text.insert(tk.END, f"Puerto {port}: Cerrado\n")
            
        self.results_text.config(state='disabled')

    #Este método limpia los campos de entrada de dirección IP, puerto inicial y puerto final, así como el área de resultados, preparándolos para un nuevo escaneo.
    def new_scan(self):
        self.ip_entry.delete(0, tk.END)
        self.start_port_entry.delete(0, tk.END)
        self.end_port_entry.delete(0, tk.END)
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(state='disabled')

"""
Crea una instancia de la aplicación PortScannerApp.
Inicia el bucle principal de la interfaz gráfica.
"""
if __name__ == "__main__":
    app = PortScannerApp()
    app.mainloop()
