"""
Ejercicio 1 - Descarga simultánea de archivos
"""
import threading
import time

archivos = [
    ("documento.pdf", 3),
    ("imagen.png",    1),
    ("video.mp4",     5),
    ("musica.mp3",    2),
    ("datos.csv",     4),
]

def descargar(nombre, duracion):
    print(f"  [INICIO]  Descargando {nombre}...")
    time.sleep(duracion)
    print(f"  [FIN]     {nombre} descargado en {duracion}s")

def secuencial():
    print("\n== VERSIÓN SECUENCIAL ==")
    inicio = time.time()
    for nombre, duracion in archivos:
        descargar(nombre, duracion)
    total = time.time() - inicio
    print(f"Tiempo secuencial: {total:.2f}s")
    return total

def con_hilos():
    print("\n== VERSIÓN CON HILOS ==")
    inicio = time.time()
    hilos = []
    for nombre, duracion in archivos:
        h = threading.Thread(target=descargar, args=(nombre, duracion))
        hilos.append(h)
        h.start()
    for h in hilos:
        h.join()
    total = time.time() - inicio
    print(f"Tiempo con hilos: {total:.2f}s")
    return total

if __name__ == "__main__":
    t1 = secuencial()
    t2 = con_hilos()
    print(f"\nAhorro: {t1 - t2:.2f}s más rápido con hilos")
