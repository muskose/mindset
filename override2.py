class Araclar:
    def __init__(self, model, yil, motor_cc):
        self.model = model
        self.uretim_yili = yil
        self.motor_gucu = motor_cc

    def git(self):
        print("Git")

    def dur(self):
        print("Dur")

    def korna_cal(self):
        print("Düt düt")


class Otobus(Araclar):
    def __init__(self, yil):
        self.model = "O-302"
        self.uretim_yili = yil


class Tren(Araclar):
    def __init__(self):
        self.motor_gucu = "14000 cc"

    def korna_cal(self):
        return "çuf çuf çuf"


otobus = Otobus(1984)
print(otobus.model)
print(otobus.uretim_yili)


tren = Tren()
print(tren.korna_cal())