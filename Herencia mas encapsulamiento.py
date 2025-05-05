# Clase base Persona
class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre         # Atributo privado
        self.edad = edad               # Usará el setter para validar
        self.__documento = documento   # Atributo privado

    # Getter para 'nombre'
    @property
    def nombre(self):
        return self.__nombre

    # Getter para 'edad'
    @property
    def edad(self):
        return self.__edad

    # Setter para 'edad' con validación
    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self.__edad = valor
        else:
            raise ValueError("La edad no puede ser negativa")

    # Getter para 'documento'
    @property
    def documento(self):
        return self.__documento


# Clase hija Paciente, hereda de Persona
class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)  # Llama al constructor de Persona
        self.__diagnostico = diagnostico           # Diagnóstico actual del paciente
        self.__historial = []                      # Lista vacía para entradas al historial

    # Método para agregar una entrada al historial
    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    # Método para ver el historial médico
    def ver_historial(self):
        return self.__historial

    # Método para ver el diagnóstico actual
    def ver_diagnostico(self):
        return self.__diagnostico

    # Método protegido (usado solo por Doctor) para modificar el diagnóstico
    def _modificar_diagnostico(self, nuevo):
        self.__diagnostico = nuevo


# Clase hija Doctor, hereda de Persona
class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)  # Llama al constructor de Persona
        self.__especialidad = especialidad         # Especialidad médica del doctor

    # Método para ver la especialidad del doctor
    def ver_especialidad(self):
        return self.__especialidad

    # Método para modificar el diagnóstico de un paciente (solo si es instancia de Paciente)
    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._modificar_diagnostico(nuevo_diagnostico)
        else:
            raise TypeError("El objeto no es un paciente")


paciente1 = Paciente("Ana Gómez", 30, "12345678A", "Gripe")
paciente1.agregar_historial("Consulta inicial por fiebre y tos.")
paciente1.agregar_historial("Recetado paracetamol y reposo.")

# Crear un doctor
doctor1 = Doctor("Dr. Luis Fernández", 45, "87654321B", "Medicina Interna")

# Mostrar información del paciente
print("Paciente:", paciente1.nombre)
print("Edad:", paciente1.edad)
print("Documento:", paciente1.documento)
print("Diagnóstico actual:", paciente1.ver_diagnostico())
print("Historial médico:")
for entrada in paciente1.ver_historial():
    print("-", entrada)

# Mostrar información del doctor
print("\nDoctor:", doctor1.nombre)
print("Especialidad:", doctor1.ver_especialidad())

# Modificar diagnóstico del paciente
print("\nModificando diagnóstico del paciente...\n")
doctor1.modificar_diagnostico(paciente1, "Neumonía")

# Ver diagnóstico actualizado
print("Nuevo diagnóstico del paciente:", paciente1.ver_diagnostico())