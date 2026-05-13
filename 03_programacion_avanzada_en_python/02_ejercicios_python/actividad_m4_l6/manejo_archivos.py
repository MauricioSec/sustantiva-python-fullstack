def main():
    nombre_archivo = "datos.txt"

    # 1. Escribir en un archivo (modo 'w')
    print("--- 1. Escribir en un archivo ---")
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_escritura:
        archivo_escritura.write("Línea 1: Registro inicial de seguridad del SOC.\n")
        archivo_escritura.write("Línea 2: Análisis de vulnerabilidades perimetrales completado.\n")
        archivo_escritura.write("Línea 3: Monitoreo de red activo.\n")
    print(f"Archivo '{nombre_archivo}' creado exitosamente.\n")

    # 2. Leer el archivo completo (modo 'r')
    print("--- 2. Leer el archivo completo ---")
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_lectura_total:
        contenido_total = archivo_lectura_total.read()
        print(contenido_total)

    # 3. Leer línea por línea
    print("--- 3. Leer línea por línea ---")
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_lineas:
        primera_linea = archivo_lineas.readline()
        print(f"Primera línea (readline): {primera_linea}", end="")
        
        print("Resto del archivo (ciclo for):")
        for linea in archivo_lineas:
            print(linea, end="")
    print("\n")

    # 4. Añadir contenido (modo 'a')
    print("--- 4. Añadir contenido ---")
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo_append:
        archivo_append.write("Línea 4: Alerta de acceso no autorizado detectada.\n")
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_verificacion:
        print("Verificación de la nueva línea agregada:")
        print(archivo_verificacion.read())

    # 5. Atributos y cierre
    print("--- 5. Atributos y cierre ---")
    # Se consulta el estado del objeto 'archivo_verificacion' fuera de su bloque 'with'
    print(f"Nombre del archivo (.name): {archivo_verificacion.name}")
    print(f"Modo de apertura previo (.mode): {archivo_verificacion.mode}")
    print(f"¿El archivo está cerrado? (.closed): {archivo_verificacion.closed}")

if __name__ == "__main__":
    main()