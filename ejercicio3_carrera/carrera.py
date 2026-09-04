"""
Ejercicio 3 - Carrera con señal de salida
"""
import threading
import time
import random

salida = threading.Event()

def corredor(nombre, tiempo):
    print(f"  {nombre} está esperando la señal...")
    salida.wait()
    print(f"  {nombre} ¡arranca!")
    time.sleep(tiempo)
    print(f"  {nombre} terminó en {tiempo}s")

if __name__ == "__main__":
    tiempos = [3, 1, 4, 2, 5]
    hilos = []

    for i, t in enumerate(tiempos, 1):
        h = threading.Thread(target=corredor, args=(f"Corredor-{i}", t))
        hilos.append(h)
        h.start()

    print("\nÁrbitro: preparados...")
    time.sleep(3)
    print("Árbitro: ¡YA!\n")
    salida.set()

    for h in hilos:
        h.join()

    print("\n¡Todos los corredores han terminado!")

