# 3. Excepciones personalizadas
class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad ingresada es menor que cero."""
    pass

def validar_edad(edad):
    """Valida que la edad no sea negativa."""
    if edad < 0:
        raise EdadInvalidaError("La edad ingresada no puede ser un valor negativo.")
    print(f"Edad validada correctamente: {edad} años.")

def main():
    # 4. Limpieza de recursos (Simulación de apertura)
    print("Abriendo archivo...")
    
    try:
        # 1 y 2. Captura básica y Múltiples excepciones
        num1 = float(input("Ingrese el primer número (dividendo): "))
        num2 = float(input("Ingrese el segundo número (divisor): "))
        
        resultado = num1 / num2
        print(f"Resultado de la división: {resultado}")
        
        # Prueba de la función con excepción personalizada
        edad_usuario = int(input("Ingrese su edad para validación: "))
        validar_edad(edad_usuario)

    except ZeroDivisionError:
        print("Error: Indeterminación matemática. No es posible dividir por cero.")
    except ValueError:
        print("Error: Tipo de dato incorrecto. Solo se permiten valores numéricos.")
    except EdadInvalidaError as e:
        print(f"Error de Regla de Negocio: {e}")
    finally:
        # 4. Limpieza de recursos (Garantía de ejecución)
        print("Cerrando archivo...")

if __name__ == "__main__":
    main()