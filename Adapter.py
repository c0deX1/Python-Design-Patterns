import abc


class Duck(abc.ABC):
    def quack(self):
        """Quack (must be overrided)"""

    def fly(self):
        """Fly (must be overrided)"""


class MallardDuck(Duck):
    def quack(self):
        print("Quack!")

    def fly(self):
        print("I'm flying")


class Turkey(abc.ABC):
    def gobble(self):
        """must be overrided"""

    def fly(self):
        """must be overrided"""


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble!")

    def fly(self):
        print("I'm flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.__turkey = turkey

    @property
    def turkey(self):
        return self.__turkey

    @turkey.setter  # Fuc incapsulation
    def turkey(self, turkey):
        self.__turkey = turkey

    def quack(self):
        self.__turkey.gobble()

    def fly(self):
        for i in range(0, 5):
            self.__turkey.fly()


def testduck(duck):
    duck.quack()
    duck.fly()


duck = MallardDuck()

turkey = WildTurkey()
turkeyAdapter = TurkeyAdapter(turkey)
print("The turkey says...")
print()
turkey.gobble()
turkey.fly()
print("The duck says...")
testduck(duck)
print()
print("The Franky says...")
testduck(turkeyAdapter)
