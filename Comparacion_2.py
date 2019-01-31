def menu(argument):
    switch = {
        1: isSubcadena,
        2: ordenAlfa
    }
    ver = switch.get(int(argument), lambda: "Invalid number")
    ver()


def isSubcadena():
    strPrimera = input("inserte primera cadena\n")
    strSegunda = input("inserte segunda cadena\n")
    if strPrimera.find(strSegunda) != -1:
        print("siiiii")
    else:
        print("nooooooooo")


def ordenAlfa():
    strPrimera = input("inserte primera cadena\n")
    strSegunda = input("inserte segunda cadena\n")
    palabras = [strPrimera, strSegunda]
    palabras.sort()
    print("\n" + palabras[0])


menu(input("""
    elije opcion:
        1 - mira si uno es sub cadena o no
        2 - enseña cual es la anterior alfanumericamente
    """))
