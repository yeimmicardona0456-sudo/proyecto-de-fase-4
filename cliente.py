from excepciones import ErrorCliente

class Cliente:
    def __init__(self, nombre, documento, telefono, correo):
        if nombre == "":
            raise ErrorCliente("Nombre vacío")

        if not documento.isdigit():
            raise ErrorCliente("Documento inválido")

        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono
        self.__correo = correo

    def mostrar(self):
        return f"{self.__nombre} - {self.__documento}"