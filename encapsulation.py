class Employee:
    __version = 'v3.11.2'

    def __init__(self, name, salary):
        self._name = name
        self.__salary = salary


em = Employee('Ali Veli', 3500)
print(em._name)
print(em._Employee__version)
print(em._Employee__salary)
