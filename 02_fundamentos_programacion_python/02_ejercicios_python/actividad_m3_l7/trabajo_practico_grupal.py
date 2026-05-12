def ejercicio_1():
    """Genera secuencias de números pares o impares según la entrada."""
    print("\n--- Ejercicio 1 ---")
    while True:
        try:
            # Validación de entrada para rango 1 a 100
            num = int(input("Ingrese un número (1 al 100): "))
            
            if num <= 0 or num > 100:
                print("No es posible realizarlo. Intente nuevamente.")
                continue
            
            if num % 2 == 0:
                # Lógica para pares
                siguientes = [str(i) for i in range(num + 2, 101, 2)]
                print(f"Resultado: usted ha ingresado un numero par y los números pares siguientes son:")
                print(f"Resultado: {' '.join(siguientes)}")
                break
            else:
                # Lógica para impares
                siguientes = [str(i) for i in range(num + 2, 100, 2)]
                print(f"Resultado: usted ha ingresado un número impar y los números impares siguientes son:")
                print(f"Resultado: {' '.join(siguientes)}")
                break
                
        except ValueError:
            print("Error: Entrada no válida. Ingrese un número entero.")

def ejercicio_2():
    """Captura 5 notas y calcula media, máxima y mínima."""
    print("\n--- Ejercicio 2 ---")
    notas = []
    
    while len(notas) < 5:
        try:
            nota = float(input(f"Ingrese la nota {len(notas) + 1} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Error: La nota debe estar estrictamente entre 0 y 10.")
        except ValueError:
            print("Error: Entrada no válida. Ingrese valores numéricos.")
            
    media = sum(notas) / len(notas)
    
    print(f"\nNotas ingresadas: {notas}")
    print(f"Nota media: {media:.2f}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota menor: {min(notas)}")

def ejercicio_3():
    """Retorna los días y el nombre del mes basado en listas."""
    print("\n--- Ejercicio 3 ---")
    # Estructura de datos requerida
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    while True:
        try:
            num_mes = int(input("Ingrese el número del mes (1-12): "))
            if 1 <= num_mes <= 12:
                # Ajuste de índice (el usuario ingresa 1, Python lee índice 0)
                indice = num_mes - 1
                nombre_mes = meses[indice]
                cantidad_dias = dias[indice]
                
                print(f"El mes número {num_mes} es {nombre_mes} y tiene {cantidad_dias} días.")
                break
            else:
                print("Error: El número de mes debe estar entre 1 y 12.")
        except ValueError:
            print("Error: Entrada no válida. Ingrese un número entero.")

if __name__ == "__main__":
    # Ejecución secuencial de los ejercicios
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()