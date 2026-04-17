# estructuras.py

# ==========================================
# 1. Crear estructuras
# ==========================================
# Lista: Colección ordenada y mutable.
lista_drones = ["DJI Air 3S", "Mavic 3 Enterprise", "Phantom 4 RTK"]
print(f"Lista: {lista_drones}")

# Tupla: Colección ordenada e inmutable (no se puede modificar tras crearse).
tupla_coordenadas = (-39.81, -73.24, 15.5)
print(f"Tupla: {tupla_coordenadas}")

# Conjunto (Set): Colección desordenada de elementos únicos. No admite duplicados.
set_puertos = {"Valdivia", "Corral", "Niebla"}
print(f"Set: {set_puertos}")

# Diccionario: Colección mutable de pares clave-valor.
diccionario_inspeccion = {"id_vuelo": "V-001", "estado": "completado", "bateria_restante": 45}
print(f"Diccionario: {diccionario_inspeccion}")


# ==========================================
# 2. Acceder a elementos
# ==========================================
# Imprimir el segundo elemento de la lista (índice 1)
print(f"\nSegundo elemento de la lista: {lista_drones[1]}")

# Imprimir una clave y su valor desde el diccionario
print(f"Clave 'estado' del diccionario: {diccionario_inspeccion['estado']}")

# EXPLICACIÓN SET:
# No es posible acceder a un set por índice (ej. set_puertos[0]) porque los sets 
# son estructuras desordenadas en la memoria. Python no asigna posiciones 
# numéricas fijas a sus elementos, priorizando la unicidad y la velocidad de búsqueda.


# ==========================================
# 3. Contar e iterar
# ==========================================
print("\n--- Conteo de elementos ---")
print(f"Cantidad en lista: {len(lista_drones)}")
print(f"Cantidad en tupla: {len(tupla_coordenadas)}")
print(f"Cantidad en set: {len(set_puertos)}")
print(f"Cantidad en diccionario: {len(diccionario_inspeccion)}")

print("\n--- Iteración de Lista ---")
for dron in lista_drones:
    print(dron)

print("\n--- Iteración de Tupla ---")
for coordenada in tupla_coordenadas:
    print(coordenada)

print("\n--- Iteración de Set ---")
for puerto in set_puertos:
    print(puerto)

print("\n--- Iteración de Diccionario ---")
for clave, valor in diccionario_inspeccion.items():
    print(f"{clave}: {valor}")


# ==========================================
# 4. Modificar estructuras
# ==========================================
# Agregar elementos
lista_drones.append("Matrice 300 RTK")
set_puertos.add("Mehuín")

# Borrar elemento de la lista
lista_drones.remove("Mavic 3 Enterprise")

# Agregar nueva clave al diccionario
diccionario_inspeccion["piloto"] = "Mauricio"

# Intentar modificar la tupla
# tupla_coordenadas[0] = -40.00
# EXPLICACIÓN TUPLA:
# Si se descomenta la línea anterior, Python arrojará un error 'TypeError: 
# 'tuple' object does not support item assignment'. Esto ocurre porque las tuplas 
# son estrictamente inmutables por diseño para proteger la integridad de los datos.