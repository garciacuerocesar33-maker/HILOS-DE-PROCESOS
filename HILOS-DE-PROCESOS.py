import threading
import time

# Variable global compartida
contador = 0
lock = threading.Lock()  # Lock para sincronización

def tarea_hilo_sincronizada(identificador, delay, iteraciones):
    global contador
    for i in range(iteraciones):
        with lock:  # Bloquea el acceso para evitar conflictos
            contador += 1
            print(f'Hilo {identificador}: Iteración {i+1}, Contador: {contador}')
        time.sleep(delay)

# Crear instancias de hilos
hilo1 = threading.Thread(target=tarea_hilo_sincronizada, args=(1, 1.0, 5))
hilo2 = threading.Thread(target=tarea_hilo_sincronizada, args=(2, 0.8, 4))
hilo3 = threading.Thread(target=tarea_hilo_sincronizada, args=(3, 1.2, 6))

# SECCIÓN 1: Iniciar todos los hilos (ejecución concurrente comienza aquí)
print("Iniciando hilos...")
hilo1.start()
hilo2.start()
hilo3.start()

# SECCIÓN 2: Esperar a que todos los hilos terminen (el programa principal espera aquí)
print("Esperando a que los hilos terminen...")
hilo1.join()
hilo2.join()
hilo3.join()

print(f'Programa principal: Tareas completadas. Contador final: {contador}')
