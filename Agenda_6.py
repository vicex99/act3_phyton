agenda = {"yo": "12345"}
gfin = False


def addNewContact():
    print(agenda)
    name = input("inserta un nombre\n")
    tlf = input("inserta un telefono\n")

    if agenda.get(name) is not None:
        print("el contacto ya existe\n")
        checkIfUpdate(name, tlf)
    else:
        agenda[name] = tlf
        print("contacto " + agenda[name] + " añadido")


def checkIfUpdate(name, tlf):
    if input("quieres modificarlo (SI o NO)\n ").upper() == "SI":
        agenda[name] = tlf
    else:
        print("contacto no modificado")
    return False


def seeAgenda():
    for contacto in agenda:
        print(contacto + " - " + agenda[contacto])
    return False


def endProgram():
    return True


def menu(opcion):
    switch = {
        1: seeAgenda,
        2: addNewContact,
        3: endProgram
    }
    ver = switch.get(int(opcion), lambda: "option not defined")
    return ver()


while not gfin:
    gfin = menu(input("""
        elije opcion:
            1 - ver contactos
            2 - insertar contacto
            3 - terminar
        """))
