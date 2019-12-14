class A:
    def a(self):
        print(1)


class B(A):
    def a(self):
        print(2)


class C(B):
    def c(self):
        print(3)


c = C()
c.a()