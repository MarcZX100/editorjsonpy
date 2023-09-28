import json

ids = []
fileName = "file" # Quiero hacer que puedas cambiar el nombre del archivo json

def tutorial():
    print("Bienvenido a lo que sea esto (tener en cuenta que esto solo aparece cuando el archivo json no existe)")
    print("Se recomienda configurar primero los parámetros y luego no tocarlos para que no hayan errores")
    print("Se explica algo mas y ya")

def cargarJSON(rutaArchivo: str):
    try: # Si encuentra el archivo
        with open(rutaArchivo, "r") as archivo:
            contenido = json.loads(archivo.read())
    except FileNotFoundError: # Si no encuentra el archivo crearlo
        with open(rutaArchivo, "w") as archivo:
            tutorial()
            archivo.write('{"main":[],"config":{"parametros":[]}}')
            contenido = json.loads('{"main":[],"config":{"parametros":[]}}')
    except json.decoder.JSONDecodeError: # Si el archivo está vacio editarlo
        with open(rutaArchivo, "w") as archivo:
            archivo.write('{"main":[],"config":{"parametros":[]}}')
            contenido = json.loads('{"main":[],"config":{"parametros":[]}}')
    for usuario in contenido["main"]:
        ids.append(usuario["id"])
    return contenido

def guardarJSON(rutaArchivo: str, contenido: str, usuariosEliminar: list):
    for id in usuariosEliminar:
        eliminarUsuario(contenido["main"], id)
    with open(rutaArchivo, "w") as archivo:
        archivo.write(json.dumps(contenido))
    

def crearUsuario(contenido: list, parametros: list):
    id = 1
    while id in ids:
        id += 1
    ids.append(id)
    usuario = {"id": id}
    for parametro in parametros:
        usuario[parametro[0]] = parametro[1]
    contenido["main"].append(usuario)


def eliminarUsuario(listaUsuarios: list, id: int):
    result = next((usuario for usuario in listaUsuarios if usuario["id"] == id), None)
    if result:
        listaUsuarios.remove(result)
        ids.remove(id)


def verUsuarios(usuarios: list, usuariosEliminar: list, usuariosCopia: list):
    print("\n")
    if len(usuarios) == 0:
        print("\33[41mAún no hay usuarios guardados.\33[0m")
    for usuario in usuarios:
        if usuario["id"] in usuariosEliminar:
            print("\33[41m" + str(usuario) + "\33[0m")
        elif usuario not in usuariosCopia:
            print("\33[42m" + str(usuario) + "\33[0m")
        else:
            print(usuario)
    print("\n")

def verComandos():
    print("\nPuedes usar varios comandos")
    print("cp - Para crear un nuevo parámetro")
    print("rp - Para eliminar un parámetro")
    print()
    print("l - Para ver una lista de usuarios")
    print("n - Para crear un nuevo usuario")
    print("r - Para eliminar un usuario existente")
    print("s - Para guardar la lista actual de usuarios")
    print("q - Para abandonar esta terminal")
    return input(" > ")

def crearParametro(listaParametros: list, parametro: str, pregunta:str, obligatorio: bool, tipo: type):
    listaParametros.append([str(obligatorio), parametro, pregunta, str(tipo)])
