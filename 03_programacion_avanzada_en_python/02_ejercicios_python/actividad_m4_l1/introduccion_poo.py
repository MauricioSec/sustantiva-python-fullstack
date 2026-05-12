# 1. Exploración teórica
# ¿Qué es la programación orientada a objetos?
# Es un paradigma de diseño de software que modela el código agrupando el estado (datos) y el comportamiento (lógica operativa) en unidades funcionales e independientes llamadas objetos.
#
# ¿En qué se diferencia de la programación estructurada?
# La programación estructurada diseña el código como una secuencia lineal de instrucciones de arriba hacia abajo, separando los datos de las funciones. La POO empaqueta los datos y las funciones que los manipulan dentro de una misma entidad, limitando el uso riesgoso de variables globales.
#
# Menciona un ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto.
# Un remolcador marítimo. La clase teórica sería "Embarcación". El objeto concreto es un remolcador de nave menor específico en operación. Sus atributos (estado) serían la eslora (17.48m) o el tonelaje (49.9). Sus métodos (comportamiento) serían encender_motores() o soltar_amarras().

# 2 y 4. Definición de una clase simple y Principios de POO
class Perro:
    def __init__(self, nombre, edad, raza):
        # Atributos encapsulados para proteger la integridad de los datos
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    # Método de comportamiento
    def ladrar(self):
        print("¡Guau!")

    # Método de abstracción para devolver el estado formateado
    def mostrar_info(self):
        return f"Perro: {self._nombre}, Edad: {self._edad} años, Raza: {self._raza}"

# Instanciación y ejecución
mi_perro = Perro("Rex", 4, "Pastor Alemán")
mi_perro.ladrar()
print(mi_perro.mostrar_info())

# 3. Diferenciar conceptos
# Clase, instancia y objeto:
# La clase es el plano arquitectónico estático. La instancia es el proceso técnico de asignar memoria del sistema operativo. El objeto es la entidad materializada resultante que existe en la RAM durante la ejecución.
#
# Atributo y estado:
# El atributo es la variable definida conceptualmente en la clase (ej. _edad). El estado es el valor numérico o de texto exacto que tiene ese atributo en un momento determinado de la ejecución (ej. 4).
#
# Método y comportamiento:
# El método es la función programada dentro de la estructura de la clase. El comportamiento es el efecto práctico o la alteración lógica del sistema cuando el procesador ejecuta ese método.

# 4. Principios de POO (Abstracción)
# Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo:
# La abstracción consiste en exponer solo las interfaces necesarias para interactuar con el objeto, ocultando su complejidad interna. En este script, al llamar a 'mostrar_info()', obtenemos la cadena de texto estructurada sin necesidad de saber cómo la clase almacena o concatena internamente las variables encapsuladas (_nombre, _edad, _raza).