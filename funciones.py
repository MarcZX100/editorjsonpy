import json

ids = []


def tutorial():
    print("Bienvenido a lo que sea esto (tener en cuenta que esto solo aparece cuando el archivo json no existe)")
    print("Se recomienda configurar primero los parámetros y luego no tocarlos para que no hayan errores")
    print("Se explica algo mas y ya")

def cargarJSON(rutaArchivo):
    try:
        with open(rutaArchivo, "r") as archivo:
            contenido = json.loads(archivo.read())
    except FileNotFoundError:
        with open(rutaArchivo, "w") as archivo:
            tutorial()
            archivo.write('{"main":[],"config":{"parametros":[]}}')
            contenido = json.loads('{"main":[],"config":{"parametros":[]}}')
    for usuario in contenido["main"]:
        ids.append(usuario["id"])
    return contenido

def guardarJSON(rutaArchivo, contenido, usuariosEliminar):
    for id in usuariosEliminar:
        eliminarUsuario(contenido["main"], id)
    with open(rutaArchivo, "w") as archivo:
        archivo.write(json.dumps(contenido))
    

def crearUsuario(contenido: list, nombre: str, edad: int):
    id = 1
    while id in ids:
        id += 1
    ids.append(id)
    contenido["main"].append({'id': id, 'nombre': nombre, 'edad': edad})


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
    return input(" > ")

# Obligatorio / nombre parametro / mensaje para pedirtelo / tipo valor
lista = [
    [True, "nombre", "Introduce el nombre de tu usuario", str],
    [False, "edad", "Introduce el nombre de tu usuario", int]
]

def crearParametro(listaParametros: list, parametro: str, pregunta:str, obligatorio: bool, tipo: type):
    listaParametros.append(obligatorio, parametro, pregunta, tipo)