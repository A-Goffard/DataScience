import reflex as rx
from ListaCoches import ListaCoches
from coche import Coche

lista_coches = ListaCoches()

def add_car(matricula, marca, modelo, color, tamanio):
    coche = Coche(matricula, marca, modelo, color, tamanio)
    lista_coches.anadir_coche(coche)

def delete_car(matricula):
    lista_coches.eliminar_coche(matricula)

def show_cars():
    lista_coches.mostrar_coches()

def clear_messages():
    lista_coches.limpiar_mensajes()

def app():
    return rx.vstack(
        rx.heading("Gestión de Coches"),
        rx.input(placeholder="Matrícula", id="matricula"),
        rx.input(placeholder="Marca", id="marca"),
        rx.input(placeholder="Modelo", id="modelo"),
        rx.input(placeholder="Color", id="color"),
        rx.input(placeholder="Tamaño", id="tamanio"),
        rx.button("Añadir Coche", on_click=lambda: add_car(
            rx.get_value("matricula"),
            rx.get_value("marca"),
            rx.get_value("modelo"),
            rx.get_value("color"),
            rx.get_value("tamanio"),
        )),
        rx.input(placeholder="Matrícula para eliminar", id="delete_matricula"),
        rx.button("Eliminar Coche", on_click=lambda: delete_car(rx.get_value("delete_matricula"))),
        rx.button("Mostrar Coches", on_click=show_cars),
        rx.button("Limpiar Mensajes", on_click=clear_messages),
        rx.text_area(value="\n".join(lista_coches.obtener_mensajes()), readonly=True),
    )

app = rx.App(app)
