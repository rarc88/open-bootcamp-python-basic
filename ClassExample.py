from abc import ABC, abstractmethod


class Math:
    result = None

    def __init__(self):
        print('Constructor')

    def __del__(self):
        print('Deconstructor')

    def addition(self, x, y):
        result = x + y
        return self.result


m = Math()

print(m.addition(1, 1))

# Clases estaticas


class Static:
    number = 1

    def increment():
        Static.number += 1


Static.increment()
print(Static.number)
Static.increment()
Static.increment()
print(Static.number)

# Herencia


class Person:
    _firstName = None
    _lastName = None

    def __init__(self):
        print('Constructor Person')

    def setFirstName(self, firstName):
        self._firstName = firstName

    def setLastName(self, lastName):
        self._lastName = lastName


class Person2(Person):
    _phone = None

    def __init__(self):
        super().__init__()
        print('Constructor Person2')

    def setPhone(self, phone):
        self._phone = phone

    def getInfo(self):
        print(f'Name: {self._firstName} {self._lastName}, phone: {self._phone}')


p2 = Person2()
p2.setFirstName('Roberto')
p2.setLastName('Ruiz')
p2.getInfo()

# Clases abstractas


class Animal(ABC):
    @abstractmethod
    def sonic(self):
        pass


class Dog(Animal):
    def sonic(self):
        print('Guau')


d = Dog()
d.sonic()


class Cat(Animal):
    def sonic(self):
        print('Miau')


c = Cat()
c.sonic()
