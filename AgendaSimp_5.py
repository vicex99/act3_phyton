def busquedaStirng(itemSearch, TuplaItems):
    for item in TuplaItems:
        if itemSearch in item:
            return "Si esta en tus contactos"
        elif itemSearch in item[0]:
            return "Si esta en tus contactos"
        else:
            return "No esta entre tus contactos"


def busquedaTupla(itemSearch, TuplaItems):
    for item in TuplaItems:
        if itemSearch == item:
            return "Si esta en tus contactos"
        else:
            return "No esta entre tus contactos"


def tipoSearch(argument):
    lista = (("Rabbit Rabbit", "000000000"), ("persona aleatoria", "675832376"), ("Mefisto infernal", "666666666"))
    switch = {
        1: conTodo,
        2: nombreCompleto,
        3: soloNombre,
        4: soloApellido,
        5: soloTlf
    }
    ver = switch.get(int(argument), lambda: "Invalid number")
    ver(lista)


def nombreCompleto(lista):
    for elem in lista:
        print(elem[0] + " --- " + elem[1])
    str = input("\nnombre\n") + " " + input("\napellido\n")
    item = (str)

    print(busquedaStirng(item, lista))


def conTodo(lista):
    for elem in lista:
        print(elem[0] + " --- " + elem[1])
    str = input("\nnombre\n") + " " + input("\napellido\n")
    item = (str, input("telefono\n"))

    print(busquedaTupla(item, lista))


def soloNombre(lista):
    for elem in lista:
        print(elem[0] + " --- " + elem[1])
    item = (input("\nnombre\n"))

    print(busquedaStirng(item, lista))


def soloApellido(lista):
    for elem in lista:
        print(elem[0] + " --- " + elem[1])
    item = (input("\napellido\n"))

    print(busquedaStirng(item, lista))


def soloTlf(lista):
    for elem in lista:
        print(elem[0] + " --- " + elem[1])
    item = (input("telefono\n"))

    print(busquedaStirng(item, lista))


tipoSearch(input("""elije
    1: conTodo,
    2: nombreCompleto,
    3: soloNombre,
    4: soloApellido,
    5: soloTlf
    """))
