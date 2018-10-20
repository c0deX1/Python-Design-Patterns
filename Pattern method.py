import abc


class CaffeineBeverage(abc.ABC):
    @abc.abstractmethod
    def brew(self):
        """Abstract method for brew"""

    @abc.abstractmethod
    def addCondiments(self):
        """Abstract method for adding condiments"""

    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter")

    def addCondiments(self):
        print("Adding sugar and milk")


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding lemon")


tea = Tea()
tea.prepareRecipe()
print()
coffee = Coffee()
coffee.prepareRecipe()
