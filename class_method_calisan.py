class Sirket:
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adli kisi personele eklendi'.format(self.isim))

    def personele_kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def personel_kabiliyetlerini_goruntule(self):
        print('{} adli kisinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

    @classmethod
    def personel_sayisini_goruntule(cls):
        print(len(cls.personel))

    @classmethod
    def personeli_goruntule(cls):
        print('Personel listesi:')
        for kisi in cls.personel:
            print(kisi)

class Bordro:
    pass