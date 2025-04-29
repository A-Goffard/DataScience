import tkinter as tk
from tkinter import messagebox

class Figura:
    def __init__(self, id, nombre,lados, color):
        self.id = id
        self.color = color
        self.nombre = nombre 
        self.lados = lados

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nueva_id):
        self._id = nueva_id

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nueva_nombre):
        self._nombre = nueva_nombre 
        
    @property
    def lados(self):
        return self._lados

    @id.setter
    def lados(self, nueva_lados):
        self._lados = nueva_lados