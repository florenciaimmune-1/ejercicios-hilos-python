"""
Ejercicio 2 - Contador de productos procesados
"""
import threading
import time

productos_procesados = 0
lock = threading.Lock()

def trabajador(nombre):
    global productos_procesados
    for i in range(100):
        time.sleep(0.001)
        with lock:
            productos_procesados += 1
    print(f"  {nombre} terminó de procesar 100 productos")

if __name__ == "__main__":
    hilos = []
    for i in range(1, 5):
        h = threading.Thread(target=trabajador, args=(f"Trabajador-{i}",))
        hilos.append(h)
        h.start()

    for h in hilos:
        h.join()

    print(f"\nTotal de productos procesados: {productos_procesados}")
    print(f"Esperados: 400 (4 trabajadores x 100 productos)")
