import os
import importlib

import funciones

# Para que no use una versión vieja de las funciones
importlib.reload(funciones)

rutaArchivoJSON = os.path.dirname(__file__) + "\\004 - archivo.json"

contenido = funciones.cargarJSON(rutaArchivoJSON)
usuarios = contenido["usuarios"]
usuariosCopia = contenido["usuarios"].copy()
usuariosEliminar = []

posiblesRespuestas = ["l", "list", "n", "new", "r", "remove", "s", "save", "q", "quit"]
funciones.verComandos()
eleccion = input(" > ")
if(eleccion not in posiblesRespuestas):
    eleccion = input("Deberías escribir algo valido: ")
while True:
    if(eleccion == "l" or eleccion == "list"):
        funciones.verUsuarios(usuarios, usuariosEliminar, usuariosCopia)

    if(eleccion == "n" or eleccion == "new"):
        nombre = input("Como quieres llamar a este usuario?\n > ")
        edad = input("Cual será la edad de este usuario?\n > ")
        while not edad.isdigit():
            edad = input(f"{edad} no es un nombre entero. Introduce un nombre entero.\n > ")
        funciones.crearUsuario(contenido, nombre, int(edad))

    if(eleccion == "r" or eleccion == "remove"):
        identificador = input("Introduce un ID\n > ")
        while not identificador.isdigit() or not int(identificador) in funciones.ids:
            while not identificador.isdigit():
                identificador = input("Debes introducir un identificador.\n > ")
            while not int(identificador) in funciones.ids:
                identificador = input("Esa ID no existe. Introduce una existente.\n > ")
        usuariosEliminar.append(int(identificador))

    if(eleccion == "s" or eleccion == "save"):
        funciones.guardarJSON(rutaArchivoJSON, contenido, usuariosEliminar)
        usuariosCopia = contenido["usuarios"].copy()

    if(eleccion == "q" or eleccion == "quit"):
        print("deu")
        quit()

    if(eleccion not in posiblesRespuestas):
        eleccion = input("Deberías escribir algo valido: ")
    else:
        funciones.verComandos()
        eleccion = input(" > ")

