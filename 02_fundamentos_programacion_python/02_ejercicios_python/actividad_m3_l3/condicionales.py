# condicionales.py

# 1. Decisión simple
edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 2. Decisión múltiple con elif
calificacion_usuario = float(input("Ingresa una calificación (entre 1 y 7): "))

# Se añade una validación de rango superior para evitar falsos positivos
if calificacion_usuario > 7 or calificacion_usuario < 1:
    print("Calificación fuera de rango permitido")
elif calificacion_usuario == 7:
    print("Excelente")
elif calificacion_usuario >= 6:
    print("Muy bien")
elif calificacion_usuario >= 5:
    print("Bien")
elif calificacion_usuario >= 4:
    print("Suficiente")
else:
    print("Insuficiente")

# 3. Condiciones anidadas (Se mantiene la estructura exigida por el encargo)
numero_entero = int(input("Ingresa un número entero: "))

if numero_entero >= 0:
    if numero_entero == 0:
        print("Es cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")

# 4. Condición de borde
numero_rango = float(input("Ingresa un número entre 1 y 100: "))

if numero_rango == 1 or numero_rango == 100:
    print("Estás en un límite permitido")
# Mejora PEP 8: Encadenamiento de operadores relacionales
elif 1 < numero_rango < 100:
    print("Dentro del rango")
else:
    print("Fuera del rango")