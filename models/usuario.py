class Usuario:
    def __init__(self, id, nombre, usuario, rol):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.rol = rol

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Usuario: {self.usuario} | Rol: {self.rol}"
