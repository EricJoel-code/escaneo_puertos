
from app.app import PortScannerApp
#Este bloque se asegura de que el código dentro de él solo se ejecute si el script se ejecuta directamente (no cuando se importa como un módulo en otro script).
if __name__ == "__main__":
    app = PortScannerApp()
    app.mainloop()
