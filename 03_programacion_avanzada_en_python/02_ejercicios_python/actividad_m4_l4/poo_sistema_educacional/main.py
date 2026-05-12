from datetime import date

# --- CLASE BASE ---
class Persona:
    def __init__(self, rut: str, nombre: str, email: str):
        self._rut = rut          # Atributo protegido (#)
        self.__nombre = nombre   # Atributo privado (-)
        self.__email = email     # Atributo privado (-)

    def get_nombre(self):
        return self.__nombre

    def set_email(self, nuevo_email: str):
        self.__email = nuevo_email

    # Método base para aplicar POLIMORFISMO
    def mostrar_datos(self):
        return f"Persona Genérica: {self.__nombre}, RUT: {self._rut}"

# --- CLASES DERIVADAS (HERENCIA) ---
class Alumno(Persona):
    def __init__(self, rut: str, nombre: str, email: str, matricula: str, nivel: int):
        super().__init__(rut, nombre, email)
        self.__matricula = matricula
        self.__nivel = nivel

    def get_matricula(self):
        return self.__matricula

    def inscribir_asignatura(self, asignatura):
        print(f"El alumno {self.get_nombre()} inscribió: {asignatura.get_detalles()}")
        return True

    # SOBRESCRITURA DE MÉTODO (POLIMORFISMO)
    def mostrar_datos(self):
        return f"Rol Alumno: {self.get_nombre()} | Matrícula: {self.__matricula}"

class Profesor(Persona):
    def __init__(self, rut: str, nombre: str, email: str, especialidad: str, departamento_id: int):
        super().__init__(rut, nombre, email)
        self.__especialidad = especialidad
        self.__departamento_id = departamento_id

    def asignar_asignatura(self, asignatura):
        print(f"El profesor {self.get_nombre()} ha sido asignado a dictar: {asignatura.get_detalles()}")

    # SOBRESCRITURA DE MÉTODO (POLIMORFISMO)
    def mostrar_datos(self):
        return f"Rol Profesor: {self.get_nombre()} | Especialidad: {self.__especialidad}"

# --- ENTIDADES ACADÉMICAS ---
class Asignatura:
    def __init__(self, codigo: str, nombre: str, creditos: int):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos

    def get_detalles(self):
        return f"[{self.__codigo}] {self.__nombre}"

class Curso:
    def __init__(self, id_curso: int, nombre_seccion: str):
        self.__id_curso = id_curso
        self.__nombre_seccion = nombre_seccion
        self.__alumnos = []

    # SIMULACIÓN DE SOBRECARGA DE MÉTODOS
    # Dependiendo de si se envía o no el parámetro 'estado_beca', el método actúa diferente.
    def agregar_alumno(self, alumno: Alumno, estado_beca: bool = None):
        self.__alumnos.append(alumno)
        if estado_beca is None:
            print(f"-> Registro estándar: Alumno {alumno.get_nombre()} ingresado a la sección {self.__nombre_seccion}.")
        else:
            txt_beca = "Beca Activa" if estado_beca else "Sin Beca"
            print(f"-> Registro especial: Alumno {alumno.get_nombre()} ingresado a la sección {self.__nombre_seccion} ({txt_beca}).")

class Calificacion:
    def __init__(self, valor_nota: float, fecha: date):
        self.__valor_nota = valor_nota
        self.__fecha = fecha

    def get_nota(self):
        return self.__valor_nota


# ==========================================
# EJECUCIÓN E INTERACCIÓN ENTRE OBJETOS
# ==========================================
if __name__ == "__main__":
    # 1. Instanciación de Objetos
    alu1 = Alumno("15.555.555-5", "Mauricio Monsálvez", "mauricio@mail.cl", "MAT-01", 1)
    prof1 = Profesor("12.222.222-2", "Alan Turing", "alan@mail.cl", "Ciberseguridad", 10)
    asig1 = Asignatura("CS101", "Seguridad Perimetral", 4)
    curso1 = Curso(100, "Sección A-Vespertino")

    print("--- 1. POLIMORFISMO EN ACCIÓN ---")
    # Se trata a objetos distintos (Alumno y Profesor) de la misma forma,
    # pero cada uno responde con su propia implementación de mostrar_datos().
    lista_usuarios = [alu1, prof1]
    for usuario in lista_usuarios:
        print(usuario.mostrar_datos())

    print("\n--- 2. INTERACCIÓN ENTRE OBJETOS ---")
    # Objetos llamando a métodos de otros objetos o recibiéndolos como parámetros
    prof1.asignar_asignatura(asig1)
    alu1.inscribir_asignatura(asig1)

    print("\n--- 3. SOBRECARGA DE MÉTODOS SIMULADA ---")
    # Misma función llamada con distinta cantidad de parámetros
    curso1.agregar_alumno(alu1)              # Llamada normal
    curso1.agregar_alumno(alu1, estado_beca=True) # Llamada sobrecargada