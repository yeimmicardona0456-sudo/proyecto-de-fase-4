class Cliente:
    def __init__(self, nombre, documento, telefono, correo):
        if not nombre:
            raise ValueError("Nombre inválido")
        if not documento.isdigit():
            raise ValueError("Documento debe ser numérico")

        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
        self.correo = correo

    def mostrar(self):
        return f"{self.nombre} - {self.documento}"