class Calculator:
    def topla(self, sayi1, sayi2):
        return sayi1 + sayi2

    def cikar(self, sayi1, sayi2):
        return sayi1 - sayi2

    def bol(self, sayi1, sayi2):
        return sayi1 / sayi2

    def carp(self, sayi1, sayi2):
        return sayi1 * sayi2


class Functional(Calculator):
    def karekok(self, kok, kuvvet):
        return pow(kok, kuvvet)


