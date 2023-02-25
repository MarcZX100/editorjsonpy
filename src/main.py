import os

import funciones

if __name__ != "__main__":
    print("Que haces tonto")
    quit()

rutaArchivoJSON = os.path.dirname(__file__) + "\\004 - archivo.json"

def reload():
    contenido = funciones.cargarJSON(rutaArchivoJSON)
    usuarios = contenido["main"]
    usuariosCopia = contenido["main"].copy()
    usuariosEliminar = []
    config = contenido["config"]
    parametros = config["parametros"]
    return contenido, usuarios, usuariosCopia, usuariosEliminar, config, parametros

contenido, usuarios, usuariosCopia, usuariosEliminar, config, parametros = reload()

posiblesRespuestas = ["l", "list", "n", "new", "r", "remove", "s", "save", "q", "quit", "cp", "cparameter", "createparameter"]
eleccion = funciones.verComandos()

if(eleccion not in posiblesRespuestas):
    eleccion = input("ERROR! Deberías escribir algo valido: ")

while True:
    
    if(eleccion == "cp" or eleccion == "cparameter" or eleccion == "createparameter"):
        nombreParametro = input("Introduce el nombre del parámetro que deseas crear.\n > ").lower()
        while any([i[1] == nombreParametro for i in parametros]):
            nombreParametro = input("ERROR! Ya existe un parámetro con ese nombre. Introduce otro.\n > ").lower()

        inputParametro = input("Introduce el mensaje para pedir datos del parámetro que deseas crear.\nP.ej: Introduce la ciudad de nacimiento.\n > ")
        
        tiposPermitidos = ["str", "string", "int", "integer", "numero", "float", "decimal", "array", "lista", "boolean", "bool", "dict", "dictionary", "diccionario", "cualquiera", "any", ""]
        tipoParametro = input("Introduce el tipo de valor permitido para el parámetro.\n > ").lower()
        while not tipoParametro in tiposPermitidos:
            tipoParametro = input("ERROR! Ese tipo no está permitido. Selecciona uno de la siguiente lista:\nstr (string), int (numero), float (decimal), array (lista), bool (booleano), dict (diccionario) o any (cualquiera).\n > ").lower()
        
        if tipoParametro in ["str", "string"]:
            tipoParametro = "str"
        elif tipoParametro in ["int", "integer", "numero"]:
            tipoParametro = "int"
        elif tipoParametro in ["float", "decimal",]:
            tipoParametro = "float"
        elif tipoParametro in ["array", "lista"]:
            tipoParametro = "list"
        elif tipoParametro in ["bool", "boolean"]:
            tipoParametro = "bool"
        elif tipoParametro in ["dict", "dictionary", "diccionario"]:
            tipoParametro = "dict"
        else: # any
            tipoParametro = "None"
        
        respuestasPermitidas = ["sí", "si", "s", "yes", "y", "", "no", "n"]
        parametroObligatorio = input("Es obligatorio introducir este parámetro? (S/n)\n > ").lower()
        while not parametroObligatorio in respuestasPermitidas:
            parametroObligatorio = input("ERROR! Debes introducir si o no.\n > ").lower()
        
        if parametroObligatorio in ["sí", "si", "s", "yes", "y", ""]:
            parametroObligatorio = True
        else:
            parametroObligatorio = False

        funciones.crearParametro(parametros, nombreParametro, inputParametro, parametroObligatorio, tipoParametro)

    if(eleccion == "l" or eleccion == "list"):
        funciones.verUsuarios(usuarios, usuariosEliminar, usuariosCopia)
        print(parametros)

    if(eleccion == "n" or eleccion == "new"):
        listaParametros = []
        for i in parametros:
            valor = input(i[2] + (' (Opcional)' if not eval(i[0]) else '') + "\n > ")

            try:
                if valor != "":
                    tipoValor = valor.split()[0] # Para que no pete si metes dos palabras separadas
                    tipoValor = type(eval(tipoValor))
                else:
                    tipoValor = str
            except NameError:
                tipoValor = str

            if bool(i[0]):
                if not i[3] == "None":
                    while tipoValor != eval(i[3]):
                        valor = input(f"ERROR! El valor introducido es de tipo {tipoValor} pero requiere un {i[3]}.\n > ")
                        
            listaParametros.append([i[1], valor])

        funciones.crearUsuario(contenido, listaParametros)

    if(eleccion == "r" or eleccion == "remove"):
        identificador = input("Introduce un ID\n > ")
        while not identificador.isdigit() or not int(identificador) in funciones.ids:
            while not identificador.isdigit():
                identificador = input("Debes introducir un identificador.\n > ")
            while not int(identificador) in funciones.ids:
                identificador = input("ERROR! Esa ID no existe. Introduce una existente.\n > ")
        usuariosEliminar.append(int(identificador))

    if(eleccion == "s" or eleccion == "save"):
        funciones.guardarJSON(rutaArchivoJSON, contenido, usuariosEliminar)
        contenido, usuarios, usuariosCopia, usuariosEliminar, config, parametros = reload()

    if(eleccion == "q" or eleccion == "quit"):
        print("deu")
        quit()

    if(eleccion not in posiblesRespuestas):
        eleccion = input("ERROR! Deberías escribir algo valido: ")
    else:
        eleccion = funciones.verComandos()
