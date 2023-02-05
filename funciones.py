import json


ids = []
global usuariosCopia

def cargarJSON(rutaArchivo):
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

def guardarJSON(rutaArchivo, contenido, usuariosEliminar):
    for id in usuariosEliminar:
        eliminarUsuario(contenido["usuarios"], id)
    with open(rutaArchivo, "w") as archivo:
        archivo.write(json.dumps(contenido))
    usuariosEliminar = []
    

def crearUsuario(contenido: list, nombre: str, edad: int):
    id = 1
    while id in ids:
        id += 1
    ids.append(id)
    contenido["usuarios"].append({'id': id, 'nombre': nombre, 'edad': edad})


def eliminarUsuario(listaUsuarios: list, id: int):
    result = next((usuario for usuario in listaUsuarios if usuario["id"] == id), None)
    if result:
        listaUsuarios.remove(result)
        ids.remove(id)


def verUsuarios(usuarios, usuariosEliminar, usuariosCopia):
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