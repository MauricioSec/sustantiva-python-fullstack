def calcular_promedio(lista_notas):
    """Calcula el promedio aritmético de una lista de números."""
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)

def contar_sobre_promedio(lista_notas, promedio):
    """Cuenta cuántos elementos de la lista son estrictamente mayores al promedio."""
    contador = 0
    for nota in lista_notas:
        if nota > promedio:
            contador += 1
    return contador

def ejecutar_programa():
    """Función principal que gestiona la entrada y salida de datos."""
    try:
        # 1. Preguntar cuántos datos ingresará 
        cantidad = int(input("¿Cuántos datos ingresará? "))
        
        if cantidad <= 0:
            print("No se ingresaron datos para procesar.")
            return

        notas = []
        
        # 2. Pedir las notas una por una 
        for i in range(cantidad):
            nota = float(input(f"Dato {i + 1}: "))
            notas.append(nota)

        # 3. Procesamiento lógico
        promedio = calcular_promedio(notas)
        mayores = contar_sobre_promedio(notas, promedio)

        # 4. Entrega de salida final [cite: 102, 113]
        print(f"{mayores} datos son mayores que el promedio")

    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")

if __name__ == "__main__":
    ejecutar_programa()