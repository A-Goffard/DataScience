from dominios.tags_palabras_clave import Tag

class Tags:
    def __init__(self):
        self.lista_tags = []

    def agregar_tag(self, tag: Tag):
        self.lista_tags.append(tag)
        return f"Tag '{tag.palabra_clave}' agregado exitosamente."

    def modificar_tag(self, id_tag, **kwargs):
        for tag in self.lista_tags:
            if tag.id == id_tag:
                for key, value in kwargs.items():
                    if hasattr(tag, key):
                        setattr(tag, key, value)
                return f"Tag '{tag.palabra_clave}' modificado exitosamente."
        return f"No se encontró el tag con ID '{id_tag}'."

    def buscar_tag(self, id_tag):
        for tag in self.lista_tags:
            if tag.id == id_tag:
                return tag
        return None

    def eliminar_tag(self, id_tag):
        for tag in self.lista_tags:
            if tag.id == id_tag:
                self.lista_tags.remove(tag)
                return f"Tag '{tag.palabra_clave}' eliminado."
        return f"No se encontró el tag con ID '{id_tag}'."
