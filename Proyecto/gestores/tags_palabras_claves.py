class Tags:
    def __init__(self):
        self.lista_tags = []

    def crear(self):
        return f"Tag '{self.palabra_clave}' creado exitosamente."

    def editar(self, palabra_clave=None, categoria=None, frecuencia_uso=None):
        if palabra_clave:
            self.palabra_clave = palabra_clave
        if categoria:
            self.categoria = categoria
        if frecuencia_uso:
            self.frecuencia_uso = frecuencia_uso
        return f"Tag '{self.palabra_clave}' editado exitosamente."

    def eliminar(self):
        return f"Tag '{self.palabra_clave}' eliminado."

    def buscar(self, criterio):
        if criterio in self.palabra_clave or criterio in self.categoria:
            return f"Tag '{self.palabra_clave}' coincide con la búsqueda."
        return f"No se encontraron coincidencias en el tag '{self.palabra_clave}'."
