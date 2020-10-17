class Person:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting..')
        del self.__name


p = Person()
p.name = 'Mehmet'
print(p.name)
del p.name