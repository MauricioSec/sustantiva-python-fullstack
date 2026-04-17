# ecommerce_m3.py

# ==========================================
# 1. Catálogo inicial de productos
# Estructura: Diccionario con ID como clave única
# ==========================================
catalogo_productos = {
    101: {"nombre": "Drone DJI Air 3S", "precio": 1099.0, "categoria": "tecnología"}, # [cite: 90-97]
    102: {"nombre": "Antena Starlink Mini", "precio": 599.0, "categoria": "tecnología"},
    103: {"nombre": "Generador Perkins 20kW", "precio": 11500.0, "categoria": "maquinaria"},
    104: {"nombre": "Laptop HP EliteBook", "precio": 1450.0, "categoria": "tecnología"},
    105: {"nombre": "Motor Fuera de Borda", "precio": 3800.0, "categoria": "maquinaria"}
}

# Estructura en memoria para el carrito de compras
carrito_compras = [] # [cite: 112, 141]

# ==========================================
# 2. Funciones del sistema
# ==========================================

def mostrar_menu():
    """Imprime las opciones del menú y retorna la selección del usuario."""
    print("\n--- Bienvenido/a a tu Ecommerce (Precios en USD) ---") # [cite: 100, 154]
    print("1) Ver catálogo de productos") # [cite: 101]
    print("2) Buscar producto por nombre o categoría") # [cite: 102]
    print("3) Agregar producto al carrito") # [cite: 103]
    print("4) Ver carrito y total") # [cite: 104]
    print("5) Vaciar carrito") # [cite: 105]
    print("0) Salir") # [cite: 106]
    return input("Elige una opción: ").strip() # 

def listar_productos(catalogo):
    """Itera y muestra todos los productos con moneda explícita."""
    print("\n--- Catálogo de Productos ---")
    for id_prod, datos in catalogo.items():
        print(f"ID: {id_prod} | {datos['nombre']} | Categoría: {datos['categoria']} | Precio: USD {datos['precio']}") # [cite: 83, 155]

def buscar_productos(catalogo, termino_busqueda):
    """
    Busca coincidencias parciales por nombre o categoría.
    Recibe el catálogo y el término, y retorna una lista de resultados.
    """
    resultados = [] # [cite: 159]
    termino = termino_busqueda.lower()
    
    for id_prod, datos in catalogo.items():
        if termino in datos['nombre'].lower() or termino in datos['categoria'].lower():
            resultados.append((id_prod, datos))
            
    return resultados # [cite: 130, 131, 156]

def agregar_al_carrito(catalogo, carrito):
    """Maneja la lógica de validación e inserción al carrito."""
    try:
        id_ingresado = int(input("\nIngresa el ID del producto: ")) # [cite: 118]
        
        # Validación de existencia del producto
        if id_ingresado not in catalogo:
            print("Error: El ID ingresado no existe en el catálogo.") # [cite: 120]
            return

        cantidad_ingresada = int(input("Ingresa la cantidad: ")) # [cite: 119]
        
        # Validación de cantidad positiva
        if cantidad_ingresada <= 0:
            print("Error: La cantidad debe ser mayor a 0.") # [cite: 145]
            return
            
        producto = catalogo[id_ingresado]
        subtotal = producto['precio'] * cantidad_ingresada
        
        item_carrito = {
            "id": id_ingresado,
            "nombre": producto['nombre'],
            "cantidad": cantidad_ingresada,
            "precio_unitario": producto['precio'],
            "subtotal": subtotal
        }
        
        carrito.append(item_carrito) # [cite: 121]
        print(f"Éxito: {cantidad_ingresada}x '{producto['nombre']}' agregado(s) al carrito.")
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar números enteros.")

def mostrar_carrito_y_total(carrito):
    """Muestra los ítems del carrito y el total acumulado en USD."""
    if not carrito:
        print("\nEl carrito está actualmente vacío.") # [cite: 146]
        return
        
    print("\n--- Tu Carrito de Compras ---")
    total_pagar = 0.0
    
    for item in carrito:
        # Visualización de detalles con moneda USD
        print(f"ID: {item['id']} | {item['nombre']} | Cant: {item['cantidad']} | P.Unit: USD {item['precio_unitario']} | Subtotal: USD {item['subtotal']}") # [cite: 122-125]
        total_pagar += item['subtotal']
        
    print("-" * 35)
    print(f"TOTAL A PAGAR: USD {total_pagar}") # [cite: 126, 158]

# ==========================================
# 3. Ciclo Principal del Programa
# ==========================================
if __name__ == "__main__":
    while True: # [cite: 107, 148]
        opcion = mostrar_menu()
        
        if opcion == "1":
            listar_productos(catalogo_productos)
            
        elif opcion == "2":
            termino = input("\nIngresa el nombre o categoría a buscar: ")
            resultados_busqueda = buscar_productos(catalogo_productos, termino)
            
            if resultados_busqueda:
                print("\n--- Resultados de Búsqueda ---")
                for id_prod, datos in resultados_busqueda:
                    print(f"ID: {id_prod} | {datos['nombre']} | {datos['categoria']} | USD {datos['precio']}")
            else:
                print("\nNo se encontraron productos coincidentes.")
                
        elif opcion == "3":
            agregar_al_carrito(catalogo_productos, carrito_compras) # [cite: 157]
            
        elif opcion == "4":
            mostrar_carrito_y_total(carrito_compras)
            
        elif opcion == "5":
            carrito_compras.clear() # [cite: 127]
            print("\nConfirmación: El carrito ha sido vaciado.") # [cite: 128]
            
        elif opcion == "0":
            print("\nCerrando sistema... ¡Hasta pronto!")
            break # [cite: 106]
            
        else:
            print("\nError: Opción no válida.") #