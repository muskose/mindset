class Anne:
    def print_Anne(self):
        print("Anne sınıfının özellikleri")

    def yemek_pisir(self):
        print("Çok güzel yemekler yaparım")

class Baba:
    def print_Baba(self):
        print("Baba sınıfının özellikleri")

    def yemek_pisir(self):
        print("İki yumurta kıralım, ekmek de var")


class Cocuk(Anne, Baba):
    pass


cocuk = Cocuk()
cocuk.print_Anne()
cocuk.print_Baba()
cocuk.yemek_pisir()
