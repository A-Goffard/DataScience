class LogSistema:
    def __init__(self, id, fecha, usuario_id, accion, descripcion, nivel="INFO"):
        self.id = id
        self.fecha = fecha
        self.usuario_id = usuario_id
        self.accion = accion
        self.descripcion = descripcion
        self.nivel = nivel

    def __str__(self):
        return (
            f"[{self.nivel}] {self.fecha} - Usuario: {self.usuario_id} - Acción: {self.accion} - {self.descripcion}"
        )