# 4. Colaboración entre objetos (Independiente)
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

# 5. Composición (Dependiente)
class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

# 1. Clase con constructor y relaciones
class Libro:
    def __init__(self, titulo, autor_obj, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        
        # Colaboración: El autor es un objeto externo [cite: 64]
        self.autor = autor_obj
        
        # Composición: La editorial se crea dentro del libro [cite: 71]
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)

    # 2. Métodos accesadores y mutadores [cite: 55-56]
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def set_anio_publicacion(self, nuevo_anio):
        self.anio_publicacion = nuevo_anio

    # 3. Sobrecarga simulada [cite: 59-62]
    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print(texto)

    def mostrar_info(self):
        print("--- Información de la Obra ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre} ({self.autor.pais})")
        print(f"Año original: {self.anio_publicacion}")
        print(f"Editorial histórica: {self.editorial.nombre} ({self.editorial.ciudad})")

# Bloque de ejecución principal con datos de cultura general
if __name__ == "__main__":
    # Colaboración: El autor existe antes que el libro
    autor_quijote = Autor("Miguel de Cervantes Saavedra", "España")
    
    # Instanciación con Composición interna de la Editorial
    libro_famoso = Libro(
        "Don Quijote de la Mancha", 
        autor_quijote, 
        1605, 
        "Juan de la Cuesta", 
        "Madrid"
    )
    
    # 1. Mostrar información inicial
    libro_famoso.mostrar_info()
    
    # 2. Uso de métodos mutadores para corregir o actualizar datos [cite: 57]
    print("\n--- Actualización de datos mediante métodos ---")
    libro_famoso.set_titulo("El ingenioso hidalgo Don Quijote de la Mancha")
    libro_famoso.set_anio_publicacion(1615) # Año de la segunda parte
    
    print(f"Título actualizado: {libro_famoso.get_titulo()}")
    print(f"Año actualizado: {libro_famoso.get_anio_publicacion()}")
    
    # 3. Prueba de resumen (Sobrecarga simulada)
    print("\n--- Resumen de la obra ---")
    libro_famoso.resumen("La historia de un hidalgo que, tras leer demasiados libros de caballería, pierde la cordura y sale en busca de aventuras.")