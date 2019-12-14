class Otomobil:
    konum = 0

    def git(self, gidilecek_mesafe):
        self.konum = self.konum

        for mesafe in gidilecek_mesafe:
            self.konum += mesafe

    def km_bilgisi(self):
        print("Araç {} km yol almıştır".format(self.konum))


araba = Otomobil()
araba.git([10.23, 45, 111, 75.4])
araba.km_bilgisi()

