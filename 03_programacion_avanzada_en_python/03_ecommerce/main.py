import os
from datetime import datetime

# ==========================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================
class ProductoNoEncontradoError(Exception):
    pass

class CantidadInvalidaError(Exception):
    pass

# ==========================================
# MODELO DE DOMINIO (CLASES)
# ==========================================
class Producto:
    def __init__(self, id_prod: str, nombre: str, categoria: str, precio: float):
        self.id_prod = id_prod
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"[{self.id_prod}] {self.nombre} | {self.categoria} | ${self.precio:.2f}"

class Catalogo:
    def __init__(self, archivo="catalogo.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def eliminar_producto(self, id_prod: str):
        producto = self.buscar_por_id(id_prod)
        if producto:
            self.productos.remove(producto)
            return True
        raise ProductoNoEncontradoError(f"El producto con ID {id_prod} no existe.")

    def actualizar_producto(self, id_prod: str, nombre: str, categoria: str, precio: float):
        producto = self.buscar_por_id(id_prod)
        if producto:
            if nombre: producto.nombre = nombre
            if categoria: producto.categoria = categoria
            if precio > 0: producto.precio = precio
            return True
        raise ProductoNoEncontradoError(f"El producto con ID {id_prod} no existe.")

    def buscar_por_id(self, id_prod: str):
        for p in self.productos:
            if p.id_prod == id_prod:
                return p
        return None

    def buscar_por_termino(self, termino: str):
        termino = termino.lower()
        return [p for p in self.productos if termino in p.nombre.lower() or termino in p.categoria.lower()]

    def listar_productos(self):
        return self.productos

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos:
                    f.write(f"{p.id_prod},{p.nombre},{p.categoria},{p.precio}\n")
            print("Catalogo guardado exitosamente.")
        except IOError as e:
            print(f"Error de E/S al guardar el catálogo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        self.agregar_producto(Producto(datos[0], datos[1], datos[2], float(datos[3])))
        except IOError as e:
            print(f"Error al leer el catálogo: {e}")
        except ValueError:
            print("Error: Datos corruptos en el archivo del catálogo.")

class Carrito:
    def __init__(self):
        self.items = [] # Composición: Lista de diccionarios {'producto': Producto, 'cantidad': int}

    def agregar_item(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser un número entero mayor a cero.")
        
        for item in self.items:
            if item['producto'].id_prod == producto.id_prod:
                item['cantidad'] += cantidad
                return
        self.items.append({'producto': producto, 'cantidad': cantidad})

    def calcular_total(self):
        return sum(item['producto'].precio * item['cantidad'] for item in self.items)

    def vaciar(self):
        self.items.clear()

# ==========================================
# JERARQUÍA DE USUARIOS (HERENCIA)
# ==========================================
class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Admin(Usuario):
    def __init__(self, nombre: str):
        super().__init__(nombre)

class Cliente(Usuario):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.carrito = Carrito() # Composición

# ==========================================
# CONTROLADOR PRINCIPAL
# ==========================================
class Tienda:
    def __init__(self):
        self.catalogo = Catalogo()

    def ejecutar(self):
        while True:
            print("\n=== BIENVENIDO AL ECOMMERCE CLI ===")
            print("1. Ingresar como ADMIN")
            print("2. Ingresar como CLIENTE")
            print("3. Salir")
            opcion = input("Seleccione su rol: ")

            if opcion == '1':
                self.menu_admin()
            elif opcion == '2':
                self.menu_cliente()
            elif opcion == '3':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

    def menu_admin(self):
        admin = Admin("Administrador")
        while True:
            print(f"\n--- MENÚ ADMIN ({admin.nombre}) ---")
            print("1. Listar productos")
            print("2. Crear producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Guardar catálogo")
            print("6. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                productos = self.catalogo.listar_productos()
                if not productos: print("El catálogo está vacío.")
                else:
                    for p in productos: print(p)

            elif opcion == '2':
                id_prod = input("ID: ")
                if self.catalogo.buscar_por_id(id_prod):
                    print("Error: El ID ya existe.")
                    continue
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                try:
                    precio = float(input("Precio: "))
                    self.catalogo.agregar_producto(Producto(id_prod, nombre, categoria, precio))
                    print("Producto creado.")
                except ValueError:
                    print("Error: El precio debe ser un número válido.")

            elif opcion == '3':
                id_prod = input("Ingrese ID del producto a actualizar: ")
                try:
                    nombre = input("Nuevo nombre (Enter para omitir): ")
                    categoria = input("Nueva categoría (Enter para omitir): ")
                    precio_str = input("Nuevo precio (Enter para omitir): ")
                    precio = float(precio_str) if precio_str else 0.0
                    self.catalogo.actualizar_producto(id_prod, nombre, categoria, precio)
                    print("Producto actualizado.")
                except ProductoNoEncontradoError as e:
                    print(e)
                except ValueError:
                    print("Error de tipado. Actualización abortada.")

            elif opcion == '4':
                id_prod = input("Ingrese ID del producto a eliminar: ")
                try:
                    self.catalogo.eliminar_producto(id_prod)
                    print("Producto eliminado.")
                except ProductoNoEncontradoError as e:
                    print(e)

            elif opcion == '5':
                self.catalogo.guardar_en_archivo()

            elif opcion == '6':
                break

    def menu_cliente(self):
        cliente = Cliente("Usuario Invitado")
        while True:
            print(f"\n--- MENÚ CLIENTE ({cliente.nombre}) ---")
            print("1. Ver catálogo")
            print("2. Buscar producto")
            print("3. Agregar producto al carrito")
            print("4. Ver carrito y total")
            print("5. Confirmar compra")
            print("6. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                productos = self.catalogo.listar_productos()
                if not productos: print("El catálogo está vacío.")
                else:
                    for p in productos: print(p)

            elif opcion == '2':
                termino = input("Ingrese nombre o categoría a buscar: ")
                resultados = self.catalogo.buscar_por_termino(termino)
                if resultados:
                    for p in resultados: print(p)
                else:
                    print("No se encontraron productos.")

            elif opcion == '3':
                id_prod = input("ID del producto: ")
                producto = self.catalogo.buscar_por_id(id_prod)
                
                if not producto:
                    print(f"Error: Producto con ID {id_prod} no encontrado.")
                    continue
                
                try:
                    cantidad = int(input("Cantidad: "))
                    cliente.carrito.agregar_item(producto, cantidad)
                    print("Producto agregado al carrito.")
                except ValueError:
                    print("Error: La cantidad debe ser numérica.")
                except CantidadInvalidaError as e:
                    print(f"Error de validación: {e}")

            elif opcion == '4':
                items = cliente.carrito.items
                if not items:
                    print("El carrito está vacío.")
                else:
                    for item in items:
                        subtotal = item['producto'].precio * item['cantidad']
                        print(f"{item['producto'].nombre} x{item['cantidad']} | P.U: ${item['producto'].precio:.2f} | Subtotal: ${subtotal:.2f}")
                    print(f"TOTAL A PAGAR: ${cliente.carrito.calcular_total():.2f}")

            elif opcion == '5':
                if not cliente.carrito.items:
                    print("No puede confirmar una compra con el carrito vacío.")
                    continue
                
                total = cliente.carrito.calcular_total()
                fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                resumen = f"[{fecha_hora}] Compra por ${total:.2f} | Items: {len(cliente.carrito.items)}\n"
                
                try:
                    with open("ordenes.txt", "a", encoding="utf-8") as f:
                        f.write(resumen)
                    print(f"Compra confirmada con éxito. Total cobrado: ${total:.2f}")
                    cliente.carrito.vaciar()
                except IOError as e:
                    print(f"Error crítico al registrar la orden: {e}")

            elif opcion == '6':
                break

if __name__ == "__main__":
    app = Tienda()
    app.ejecutar()