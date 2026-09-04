"""
Ejercicio 5 - Monitor de tareas con parada controlada
"""
import threading
import time

parar = threading.Event()

def trabajador(nombre):
    contador = 0
    while not parar.is_set():
        contador += 1
        print(f"  {nombre} - tarea #{contador}")
        time.sleep(1)
    print(f"  {nombre} se detiene. Total de tareas: {contador}")
    return contador

if __name__ == "__main__":
    resultados = {}

    def hilo_trabajador(nombre):
        resultados[nombre] = 0
        contador = 0
        while not parar.is_set():
            contador += 1
            print(f"  {nombre} - tarea #{contador}")
            time.sleep(1)
        resultados[nombre] = contador
        print(f"  {nombre} se detiene. Total: {contador} tareas")

    hilos = []
    for i in range(1, 4):
        h = threading.Thread(target=hilo_trabajador, args=(f"Trabajador-{i}",))
        hilos.append(h)
        h.start()

    print("Trabajadores activos durante 10 segundos...\n")
    time.sleep(10)

    print("\nActivando señal de parada...")
    parar.set()

    for h in hilos:
        h.join()

    print("\n== RESUMEN FINAL ==")
    for nombre, total in resultados.items():
        print(f"  {nombre}: {total} tareas realizadas")
