class Otomobil:
    model_yili = 2019
    tekerlek_sayisi = 4
    hatchback_kapi_sayisi = 5
    sedan_kapi_sayisi = 4
    cabrio_kapi_sayisi = 2

    def __init__(self, model_adi, kasa_tipi):
        self.model_adi = model_adi
        self.kasa_tipi = kasa_tipi
        self.renk = ''

    def boya(self):
        return input('Renk seçeneğinizi giriniz: ')

    def sedan_uret(self):
        print("{} kapılı sedan aracınız üretilmiştir".format(self.sedan_kapi_sayisi))
        self.renk = self.boya()

    def hatchback_uret(self):
        print("{} kapılı hatchback aracınız üretilmiştir".format(self.hatchback_kapi_sayisi))
        self.renk = self.boya()

    def cabrio_uret(self):
        print("{} kapılı cabrio aracınız üretilmiştir".format(self.cabrio_kapi_sayisi))
        self.renk = self.boya()

    def uret(self):
        if self.kasa_tipi == 'sedan':
            self.sedan_uret()
            print("{} model, {} üretimi ve {} rengindeki aracınız hazır, A mağazamızdan alabilirsiniz".format(
                self.model_adi, self.model_yili, self.renk))
        if self.kasa_tipi == 'hatchback':
            self.hatchback_uret()
            print("{} model, {} üretimi ve {} rengindeki aracınız hazır, B mağazamızdan alabilirsiniz".format(
                self.model_adi, self.model_yili, self.renk))
        if self.kasa_tipi == 'cabrio':
            self.cabrio_uret()
            print("{} model, {} üretimi ve {} rengindeki aracınız hazır, C mağazamızdan alabilirsiniz".format(
                self.model_adi, self.model_yili, self.renk))


if __name__ == '__main__':
    araba = Otomobil("a4", "hatchback")
    araba.uret()
