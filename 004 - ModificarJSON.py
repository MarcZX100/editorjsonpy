import os
import json

def cargarJSON(rutaArchivo):
    global usuariosCopia
    try:
        with open(rutaArchivo, "r") as archivo:
            contenido = json.loads(archivo.read())
    except FileNotFoundError:
        with open(rutaArchivo, "w") as archivo:
            archivo.write('{"usuarios":[],"bots":[]}')
            contenido = json.loads('{"usuarios":[],"bots":[]}')
    for usuario in contenido["usuarios"]:
        ids.append(usuario["id"])
    usuariosCopia = contenido["usuarios"].copy()
    return contenido

def guardarJSON(rutaArchivo):
    global usuariosCopia
    global usuariosEliminar
    for id in usuariosEliminar:
        eliminarUsuario(id)
    with open(rutaArchivo, "w") as archivo:
        archivo.write(json.dumps(contenido))
    usuariosCopia = contenido["usuarios"].copy()
    usuariosEliminar = []
    

def crearUsuario(nombre: str, edad: int):
    id = 1
    while id in ids:
        id += 1
    ids.append(id)
    usuarios.append({'id': id, 'nombre': nombre, 'edad': edad})


def eliminarUsuario(id: int):
    result = next((usuario for usuario in usuarios if usuario["id"] == id), None)
    if result:
        usuarios.remove(result)
        ids.remove(id)


def verUsuarios():
    for usuario in usuarios:
        if usuario["id"] in usuariosEliminar:
            print("\33[41m" + str(usuario) + "\33[0m")
        elif usuario not in usuariosCopia:
            print("\33[42m" + str(usuario) + "\33[0m")
        else:
            print(usuario)

def verComandos():
    print("Puedes usar varios comandos")
    print("l - Para ver una lista de usuarios")
    print("n - Para crear un nuevo usuario")
    print("r - Para eliminar un usuario existente")
    print("s - Para guardar la lista actual de usuarios")
    print("q - Para abandonar esta terminal")

rutaArchivoJSON = os.path.dirname(__file__) + "\\004 - archivo.json"
ids = []

contenido = cargarJSON(rutaArchivoJSON)
usuarios = contenido["usuarios"]
usuariosCopia = contenido["usuarios"].copy()
usuariosEliminar = []

posiblesRespuestas = ["l", "list", "n", "new", "r", "remove", "s", "save", "q", "quit"]
verComandos()
eleccion = input(" > ")
if(eleccion not in posiblesRespuestas):
    eleccion = input("Deberías escribir algo valido: ")
while True:
    if(eleccion == "l" or eleccion == "list"):
        verUsuarios()

    if(eleccion == "n" or eleccion == "new"):
        nombre = input("Como quieres llamar a este usuario?\n > ")
        edad = input("Cual será la edad de este usuario?\n > ")
        while not edad.isdigit():
            edad = input(f"{edad} no es un nombre entero. Introduce un nombre entero.\n > ")
        crearUsuario(nombre, int(edad))

    if(eleccion == "r" or eleccion == "remove"):
        identificador = input("Introduce un ID\n > ")
        while not identificador.isdigit():
            identificador = input("Debes introducir un identificador.")
        usuariosEliminar.append(int(identificador))

    if(eleccion == "s" or eleccion == "save"):
        guardarJSON(rutaArchivoJSON)

    if(eleccion == "q" or eleccion == "quit"):
        print("deu")
        quit()

    if(eleccion not in posiblesRespuestas):
        eleccion = input("Deberías escribir algo valido: ")
    else:
        verComandos()
        eleccion = input(" > ")

