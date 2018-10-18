import abc


class Beverage(abc.ABC):

    def __init__(self):
        self.__cost = 0
        self.__description = "Unknown Beverage"

    @property
    def description(self):
        return self.__description

    def getDescription(self):
        return self.description

    @property
    @abc.abstractmethod
    def cost(self):
        return self.__cost


class CondimentDecorator(Beverage, abc.ABC):
    @abc.abstractmethod
    def getDescription(self):
        """Return description"""


class Espresso(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.__description = "Espresso"

    @property
    def description(self):
        return self.__description

    def getDescription(self):
        return self.description

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.__description = "House Blend Coffee"

    @property
    def description(self):
        return self.__description

    def getDescription(self):
        return self.description

    def cost(self):
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.__description = "Dark Roast Coffee"

    @property
    def description(self):
        return self.__description

    def getDescription(self):
        return self.description

    def cost(self):
        return .99


class Decaf(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.__description = "Decaf"

    def cost(self):
        return 1.05


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.__beverage = beverage

    def getDescription(self):
        return self.__beverage.getDescription() + " Mocha"

    def cost(self):
        return .20 + self.__beverage.cost()


beverage = Espresso()
print(beverage.getDescription() + " $" + str(beverage.cost()))

beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
print(beverage2.getDescription() + " $" + str(beverage2.cost()))
