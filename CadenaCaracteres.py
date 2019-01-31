def menu(argument):
    switch = {
        1: Separa,
        2: Barrabaja,
        3: ClaveOculta,
        4: puntosDigitos
    }
    ver = switch.get(int(argument), lambda: "Invalid number")
    ver()


def Separa():
    palabra = input("inserte una frase\n")
    palabraSeparada = ""
    cont = 0
    while cont < len(palabra):
        letra = palabra[cont]
        palabraSeparada += letra + ","
        cont += 1
    print(palabraSeparada[:-1])


def Barrabaja():
    # usar replace -->  mensaje7.replace("L", "pizza")
    palabra = input("inserte una frase\n")
    palabra = palabra.replace(" ", "_")
    print(palabra)


def ClaveOculta():
    palabra = input("inserte una palabra\n")
    palabraSeparada = ""
    indice = 0

    while indice < len(palabra):
        letra = palabra[indice]
        if letra.isnumeric():
            palabraSeparada += "#"
        else:
            palabraSeparada += letra
        indice += 1
    print(palabraSeparada)


def puntosDigitos():
    palabra = input("inserte un numero\n")
    palabraSeparada = ""
    cont = 0

    for letra in palabra:
        cont = cont + 1
        if cont != 0 and cont % 3 == 0:
            palabraSeparada += letra + "."
        else:
            palabraSeparada += letra

    print(palabraSeparada[:-1])


menu(input("""
elije opcion:
1 - separa cada caracter por comas
2 - separa cada palabra por barra bajas
3 - cambia numeros por #
4 - pon puntos cada tres numeros
"""))
