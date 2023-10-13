from typing import final

pi: final = 3.14

pi = 3.5 # trying to reassign variable but get a warning because the variable is final


@final # annotation for final class
class Animal:
    pass


class Dog(Animal): # trying to inherit class but get a warning because the class is final
    pass


class Employee:

    @final
    def work(self):
        print('Working')


class Driver(Employee):

    def work(self): # trying to override method but get a warning because this method is final
        print('Driving')


class Person:

    def __init__(self, age: int):
        self.__age = age

    @property # getter
    def person_age(self):
        return self.__age

    @person_age.setter # setter
    def person_age(self, value):
        raise RuntimeError(f' age is constant, can not be changed') # create error in setters


person1 = Person(10)

print(person1.person_age)

# person1.person_age = 100

print(person1.person_age)

print(person1.__age)