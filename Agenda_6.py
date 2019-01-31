agenda = {}
fin = "false"


def addNewContact():
    name = input("inserta un nombre\n")
    tlf = input("inserta un telefono\n")

    if ~agenda.hasKey('name'):
        agenda[name] = tlf
    else:
        print("el contacto ya existe\n")
        checkIfUpdate(name, tlf)


def checkIfUpdate(name, tlf):
    if input("quieres modificarlo (SI o NO)\n ").upper() == "SI":
        agenda[name] = tlf
    else:
        print("contacto no modificado")


def seeAgenda():
    for contacto in agenda:
        print(contacto)


def endProgram():
   fin = "true"


def menu(opcion):
    switch = {
        1: seeAgenda,
        2: addNewContact,
        3: endProgram
    }
    ver = switch.get(int(opcion), lambda: "option not defined")
    ver()


while fin == "False":
    menu(input("""
        elije opcion:
            1 - ver contactos
            2 - insertar contacto
            3 - terminar
        """))
