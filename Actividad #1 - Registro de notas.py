class Estudiante:
    def __init__(self, nombre, codigo):
        self.__nombre = None
        self.__codigo = None
        self.nombre = nombre  # Usamos el setter
        self.codigo = codigo  # Usamos el setter
        self.__notas = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor.isalnum():
            raise ValueError("El código debe ser alfanumérico.")
        self.__codigo = valor

    def agregar_nota(self, nota):
        if not (0.0 <= nota <= 5.0):
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        self.__notas.append(nota)

    def calcular_promedio(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)
      

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0
    
est = Estudiante("Juan Pérez", "ABC123")
est2 = Estudiante("Maria Gonzales", "FEG456")

# Agregar algunas notas
est.agregar_nota(4.5)
est.agregar_nota(3.8)
est.agregar_nota(2.9)

est2.agregar_nota(1.5)
est2.agregar_nota(1.2)
est2.agregar_nota(1.2)

# Mostrar el promedio
print(f"Promedio de {est.nombre}: {est.calcular_promedio():.2f}")

if est2.es_aprobado():
    print(f"{est2.nombre} está aprobado ")
else:
    print(f"{est2.nombre} no está aprobado ")