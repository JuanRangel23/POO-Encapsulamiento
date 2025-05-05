class Empleado:
    def __init__(self, nombre, rol, clave):
        self.__nombre = nombre
        self.__rol = rol
        self.__clave_acceso = self.__cifrar(clave)
    

    def __cifrar(self, texto):
        return texto[::-1]
    
    def __decifrar(self, clave_encriptada):
        return clave_encriptada[::-1]
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def rol(self):
        return self.__rol
    
    def verificar_clave(self, clave_ingresada):
        return self.__cifrar(clave_ingresada) == self.__clave_acceso

    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):
            self.__clave_acceso = self.__cifrar(nueva_clave)
            return True
        return False
    
emp = Empleado("Luis", "Sapovisor", "Hellokitty")
print(emp.verificar_clave("Hellokitty"))
emp.cambiar_clave("Hellokitty","kdrama")
print(emp.verificar_clave("kdrama"))