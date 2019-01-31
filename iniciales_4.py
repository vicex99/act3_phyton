def separar(lamdaNombres):
    strNombres = []
    for nom in lamdaNombres:
        strNombres.append(nom[1] + " " + nom[2] + ". " + nom[0])
    return strNombres


list = separar((("Martinez", "Alonso", "A"), ("Aloz", "Pedro", "P"), ("Gua", "Rabbit", "R")))

for nom in list:
    print(nom)

