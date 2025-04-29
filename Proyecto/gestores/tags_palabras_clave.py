from dominios.tags_palabras_clave import Tag

class TagsPalabrasClave:
    
    def __init__(self):
        self.lista_tags = []

    def agregar(self, tag: Tag):
        self.lista_tags.append(tag)
        return f"Tag '{tag.palabra_clave}' agregado exitosamente."

    def editar(self, id_tag, **kwargs):
        for tag in self.lista_tags:
            if tag.id == id_tag:
                for key, value in kwargs.items():
                    if hasattr(tag, key):
                        setattr(tag, key, value)
                return f"Tag '{tag.palabra_clave}' editado exitosamente."
        return f"No se encontró el tag con ID '{id_tag}'."

    def eliminar(self, id_tag):
        for tag in self.lista_tags:
            if tag.id == id_tag:
                self.lista_tags.remove(tag)
                return f"Tag '{tag.palabra_clave}' eliminado."
        return f"No se encontró el tag con ID '{id_tag}'."
