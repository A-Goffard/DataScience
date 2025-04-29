from dominios.documento import Documento

class Documentos:
    
    def __init__(self):
        self.lista_documentos = []

    def subir(self, documento: Documento):
        self.lista_documentos.append(documento)
        return f"Documento '{documento.titulo}' subido exitosamente."

    def editar(self, id_documento, **kwargs):
        for documento in self.lista_documentos:
            if documento.id == id_documento:
                # Actualizar los atributos del documento según los argumentos proporcionados
                for key, value in kwargs.items():
                    if hasattr(documento, key):
                        setattr(documento, key, value)
                return f"Documento '{documento.titulo}' editado exitosamente."
        return f"No se encontró el documento con ID '{id_documento}'."

    def eliminar(self, id_documento):
        for documento in self.lista_documentos:
            if documento.id == id_documento:
                self.lista_documentos.remove(documento)
                return f"Documento '{documento.titulo}' eliminado."
        return f"No se encontró el documento con ID '{id_documento}'."

    def buscar(self, palabra_clave):
        resultados = [
            documento for documento in self.lista_documentos
            if palabra_clave in documento.titulo or palabra_clave in documento.descripcion or palabra_clave in documento.tematica
        ]
        if resultados:
            return [f"Documento '{doc.titulo}' coincide con la búsqueda." for doc in resultados]
        return f"No se encontraron coincidencias para la palabra clave '{palabra_clave}'."

    def asociar_a_publicacion(self, id_documento, publicacion):
        for documento in self.lista_documentos:
            if documento.id == id_documento:
                return f"Documento '{documento.titulo}' asociado a la publicación '{publicacion.titulo}'."
        return f"No se encontró el documento con ID '{id_documento}'."
