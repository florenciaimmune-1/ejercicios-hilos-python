"""
Ejercicio 4 - Productor y consumidor de pedidos
"""
import threading
import queue
import time

cola = queue.Queue()

def productor():
    for i in range(1, 11):
        pedido = f"Pedido-{i}"
        cola.put(pedido)
        print(f"  [COCINA]    Nuevo {pedido} recibido")
        time.sleep(0.5)
    print("  [COCINA]    No hay más pedidos")

def cocinero(nombre):
    while True:
        try:
            pedido = cola.get(timeout=2)
            print(f"  [{nombre}] Preparando {pedido}...")
            time.sleep(1)
            print(f"  [{nombre}] {pedido} listo")
            cola.task_done()
        except queue.Empty:
            print(f"  [{nombre}] No hay más pedidos, me retiro")
            break

if __name__ == "__main__":
    h_productor = threading.Thread(target=productor)
    h_cocinero1 = threading.Thread(target=cocinero, args=("Cocinero-1",))
    h_cocinero2 = threading.Thread(target=cocinero, args=("Cocinero-2",))

    h_productor.start()
    h_cocinero1.start()
    h_cocinero2.start()

    cola.join()
    print("\n¡Todos los pedidos han sido preparados!")

