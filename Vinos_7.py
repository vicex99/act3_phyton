class Corcho:

    def __init__(self, strBodega):
        print("creado corcho de la bodega  '" + str(strBodega) + "'")
        self.bodega = strBodega


class Botella:

    def __init__(self, corcho):
        print("Creada botella con corcho de bodega '" + corcho.bodega + "'")
        self.corcho = corcho


class Sacacorchos:

    def __init__(self):
        print("sacacorchos creado")

    def destapar(self, botella):
        if botella.corcho is not None:
            self.corcho = botella.corcho
            botella.corcho = None
            print("sacado corcho " + self.corcho.bodega + " de la botella ")
        else:
            print("la botella no tenia corcho")


def limpiar(sacacorchos):
    sacacorchos.corcho = None
    print("sacacorchos limpio")


corcho1 = Corcho("bodega vieja")
bot = Botella(corcho1)
sacacorchos = Sacacorchos()
sacacorchos.destapar(bot)
sacacorchos.destapar(bot)
limpiar(sacacorchos)





