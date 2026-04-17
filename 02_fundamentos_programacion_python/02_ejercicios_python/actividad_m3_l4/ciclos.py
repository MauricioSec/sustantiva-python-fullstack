# ciclos.py

# ==========================================
# 1. Uso básico de while
# ==========================================
# Este ciclo imprime una secuencia numérica.
# Su finalización está controlada por la condición lógica: se detiene cuando el contador supera el valor 5.
contador_secuencia = 1
while contador_secuencia <= 5:
    print(contador_secuencia)
    contador_secuencia += 1

# ==========================================
# 2. Uso básico de for
# ==========================================
# Este ciclo itera sobre los elementos de una lista predefinida.
# Su finalización está controlada por el agotamiento de los elementos (termina al leer el último dato).
lista_frutas = ["manzana", "plátano", "naranja"]
for fruta_actual in lista_frutas:
    print(fruta_actual)

# ==========================================
# 3. Condición en un ciclo
# ==========================================
# Este ciclo evalúa la paridad matemática de una secuencia del 1 al 10.
# Su finalización es automática cuando la función range() alcanza su límite (11 excluido).
for numero_evaluado in range(1, 11):
    if numero_evaluado % 2 == 0:
        print(f"{numero_evaluado}: Par")
    else:
        print(f"{numero_evaluado}: Impar")

# ==========================================
# 4. Ciclo infinito controlado con break
# ==========================================
# Este ciclo solicita entrada iterativa del usuario.
# Carece de finalización natural por usar 'while True'; su término es forzado explícitamente por la sentencia 'break' al detectar el valor 0.
while True:
    numero_ingresado = int(input("Ingresa un número (0 para salir): "))
    if numero_ingresado == 0:
        break
    print(f"Ingresaste: {numero_ingresado}")

# ==========================================
# 5. Ciclo anidado
# ==========================================
# Este bloque genera tablas de multiplicar combinando dos secuencias.
# La finalización total ocurre cuando el ciclo externo ('multiplicando_base') agota su rango (del 1 al 3).
for multiplicando_base in range(1, 4):
    print(f"--- Tabla del {multiplicando_base} ---")
    for multiplicador_interno in range(1, 11):
        producto_calculado = multiplicando_base * multiplicador_interno
        print(f"{multiplicando_base} x {multiplicador_interno} = {producto_calculado}")

# ==========================================
# 6. Uso de continue
# ==========================================
# Este ciclo filtra datos de una lista omitiendo un valor específico ("Juan").
# Su finalización está dictada por el recorrido total de los elementos de la lista.
lista_nombres = ["Pedro", "Juan", "Diego", "Ana"]
for nombre_persona in lista_nombres:
    if nombre_persona == "Juan":
        continue
    print(nombre_persona)