from abc import ABC,abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass




class Dog(Animal):
    def make_sound(self):
        print("Bawwww")


class Cat(Animal):
    def make_sound(self):
        print("Myaaaau")


class Lion(Animal):
    def make_sound(self):
        print("Roar!!")


a=Cat()
a.make_sound()