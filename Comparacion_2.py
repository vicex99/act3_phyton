def menu(argument):
    switch = {
        1: isSubcadena,
        2: ordenAlfa
    }
    try:
        ver = switch.get(int(argument), lambda: "Invalid number")
        print("resultado: " + ver())

    except:
        print("Invalid letter")


def isSubcadena():
    print("Comparando alfabeticamente")
    strPrimera = input("inserte primera cadena\n")
    strSegunda = input("inserte segunda cadena\n")
    if strPrimera.find(strSegunda) != -1:
        return "siiiiiiiii estaaa"
    else:
        return "nooooooooo estaaa"


def ordenAlfa():
    strPrimera = input("inserte primera cadena\n")
    strSegunda = input("inserte segunda cadena\n")
    palabras = [strPrimera, strSegunda]
    palabras.sort()
    return "\n" + palabras[1]


menu(input("""
    elije opcion:
        1 - mira si uno es sub cadena o no
        2 - enseña cual es la anterior alfabeticamente
    """))
