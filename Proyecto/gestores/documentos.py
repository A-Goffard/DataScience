from dominios.documento import Documento

class Documentos:
    def __init__(self):
        self.lista_documentos = []

    def agregar_documento(self, documento: Documento):
        self.lista_documentos.append(documento)
        return f"Documento '{documento.titulo}' agregado exitosamente."

    def modificar_documento(self, id_documento, **kwargs):
        for documento in self.lista_documentos:
            if documento.id == id_documento:
                for key, value in kwargs.items():
                    if hasattr(documento, key):
                        setattr(documento, key, value)
                return f"Documento '{documento.titulo}' modificado exitosamente."
        return f"No se encontró el documento con ID '{id_documento}'."

    def buscar_documento(self, id_documento):
        for documento in self.lista_documentos:
            if documento.id == id_documento:
                return documento
        return None

    def eliminar_documento(self, id_documento):
        for documento in self.lista_documentos:
            if documento.id == id_documento:
                self.lista_documentos.remove(documento)
                return f"Documento '{documento.titulo}' eliminado."
        return f"No se encontró el documento con ID '{id_documento}'."
