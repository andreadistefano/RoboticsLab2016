# -*- coding: utf-8 -*-


def sum(a, b):
    return a + b


class Person():
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._address = None

    def __str__(self):
        out = self._name + " " + self._surname
        if not (self._address is None):
            out += "\n" + self._address
        return out

    def setAddress(self, address):
        self._address = address

a, b = 2, 3
c = sum(a, b)
print(c)

p1 = Person("Andrea", "Di Stefano")
print(p1)
p1.setAddress("Piazza Duomo, L'Aquila")
print(p1)