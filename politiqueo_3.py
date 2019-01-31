def menu(argument):
    lamdaNombres = (("Alonso", "hombre"), ("Miriam", "mujer"),
                    ("Cristina", "mujer"), ("Fernando", "hombre"), ("Carlos", "hombre"), ("Martina", "mujer"))
    switch = {
        1: imprimirListado,
        2: imprimirListadoComplejo,
        3: imprimirListado
    }
    ver = switch.get(int(argument), lambda: "Invalid number")
    ver(lamdaNombres)


def imprimirListado(nombres):
    for participante in nombres:
        print("Participante " + participante[1] + ", " + participante[0] + ", vote por mí")


def imprimirListadoComplejo(nombres):
    cont = 1
    faltantes = len(nombres) - 1
    for participante in nombres:
        print("Participante " + participante[1] + ", " + participante[0] + " " + str(cont) + " faltando " + str(faltantes) + " participantes")
        cont += 1
        faltantes -= 1


menu(input("""
    elije opcion:
        1 - participantes
        2 - participantes complejo
    """))
