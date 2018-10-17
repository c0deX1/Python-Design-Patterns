import abc
import json

from collections import namedtuple

from zope import interface


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return self.name + " " + str(self.age)


class Student(Person):
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.__university = university

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, university):
        self.__university = university

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.university

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


John = Student("John", 19, "NSTU")
JohnSTR = John.toJSON()
#x = json.loads(JohnSTR, object_hook=lambda d: namedtuple('Student', d.keys())(*d.values()))
print(type(John))
