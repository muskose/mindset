class Tasit:
    def calistir(self):
        self.calisiyor = True
        print("Araç çalışıyor")


class EkektrikliAraba(Tasit):
    def calistir(self):
        print("Şarj doluysa çalış")
        #super().calistir()
        print("EkektrikliAraba çalıştı mı :", False)


class BenzinliAraba(Tasit):
    def calistir(self):
        print("Depoda benzin varsa çalış")
        super().calistir()
        print("BenzinliAraba çalıştı mı :", self.calisiyor)


EkektrikliAraba().calistir()
BenzinliAraba().calistir()
