class AuditoriaPublicacion:
    def __init__(self, id, publicacion_id, generador_ia_id, fecha_generacion, usuario_id, parametros_entrada, resultado, observaciones=None):
        self.id = id
        self.publicacion_id = publicacion_id
        self.generador_ia_id = generador_ia_id
        self.fecha_generacion = fecha_generacion
        self.usuario_id = usuario_id
        self.parametros_entrada = parametros_entrada  # Puede ser un dict o JSON
        self.resultado = resultado  # Puede ser resumen, estado, etc.
        self.observaciones = observaciones

    def __str__(self):
        return (
            f"Auditoría: {self.id}, Publicación: {self.publicacion_id}, "
            f"Generador IA: {self.generador_ia_id}, Fecha: {self.fecha_generacion}, "
            f"Usuario: {self.usuario_id}, Resultado: {self.resultado}, Observaciones: {self.observaciones}"
        )