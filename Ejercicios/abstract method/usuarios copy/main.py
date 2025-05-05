import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from usuario import Usuario
from usuariosAdmin import UsuariosAdmin

if os.path.exists("usuarios.txt"):
    print("El archivo usuarios.txt existe en:", os.path.abspath("usuarios.txt"))
else:
    print("El archivo usuarios.txt no existe.")

def iniciar_sesion():
    usuario_input = entry_usuario.get()
    passwd_input = entry_contrasena.get()
    usuario = gestor.buscar(usuario_input)

    if usuario != "Usuario no encontrado":
        if usuario.passwd == passwd_input:
            messagebox.showinfo("Éxito", "✅ Estás dentro")
        else:
            nueva_pass = simpledialog.askstring("Restablecer", "Contraseña incorrecta. Introduce una nueva contraseña:")
            if nueva_pass:
                usuario.passwd = nueva_pass
                gestor.anadir(usuario)
                messagebox.showinfo("Actualización", "Contraseña restablecida correctamente.")
    else:
        if messagebox.askyesno("Registro", "Usuario no encontrado. ¿Deseas registrarte?"):
            nombre = simpledialog.askstring("Registro", "Nombre:")
            apellido = simpledialog.askstring("Registro", "Apellido:")
            anio_nac = simpledialog.askstring("Registro", "Año de nacimiento:")
            passwd = simpledialog.askstring("Registro", "Contraseña:")
            nuevo = Usuario(usuario_input, nombre, apellido, anio_nac, passwd)
            gestor.anadir({"clave": usuario_input, "usuario": nuevo})
            messagebox.showinfo("Registro", "Usuario registrado correctamente.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Login")
ventana.geometry("300x200")

# Elementos visuales
label_usuario = tk.Label(ventana, text="Usuario")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana, text="Contraseña")
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack(pady=5)

btn_login = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
btn_login.pack(pady=10)

# Inicializar gestor y ejecutar
gestor = UsuariosAdmin()
ventana.mainloop()
