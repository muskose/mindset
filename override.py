class Memeliler:
    eseyli_ureme = True
    vucudu_killarla_kapli = True
    yavrularini_sutle_besleme = True

    def __init__(self, name):
        self.name = name
        print(self.name)

    def beslen(self):
        print("Kırlarda otla")

    def bagir(self):
        print("Asafdfafasfa")

    def kos(self):
        print("Run run run...")


class Kedi(Memeliler):
    def beslen(self):
        print("Wiskas mamaya bayılırım")

    def bagir(self):
        print("Miyav")


class Yunus(Memeliler):
    vucudu_killarla_kapli = False

    def beslen(self):
        print("Küçük balıklara bayılırım")

    def kos(self):
        print("Çok güzel yüzerim...")


class Kopek(Memeliler):
    def beslen(self):
        print("Kemikler çok lezzetli")

    def bagir(self):
        print("Hav" * 3)

    def isir(self):
        print("Hırrrr")

    def bekcilik_yap(self):
        print("Kimse giremez!")

class Pitbul(Kopek):
    pass

class Fino(Kopek):
    def bekcilik_yap(self):
        print("Beni kim beklesin")

    def isir(self):
        print("Bu dişlerle mi?")


kedi = Kedi("Tekir")
print(kedi.vucudu_killarla_kapli)
kedi.bagir()
kedi.beslen()
kedi.kos()

print("")

yunus = Yunus("Clipper")
print(yunus.vucudu_killarla_kapli)
yunus.bagir()
yunus.beslen()
yunus.kos()

print("")

kurt = Kopek("Atıl Kurt")
kurt.kos()
kurt.isir()
kurt.bekcilik_yap()
kurt.beslen()
kurt.bagir()

print("")

balta = Pitbul("Balta")
balta.isir()
balta.bekcilik_yap()

print("")

topac = Fino("Topaç")
topac.bekcilik_yap()
topac.isir()
topac.kos()
