import abc


class House(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        """Abstract class"""


class PanelHouse(House):
    def __init__(self):
        print("Panel house was builded")


class WoodHouse(House):

    def __init__(self):
        print("Wood house was builded")


class Developer(abc.ABC):

    @abc.abstractmethod
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abc.abstractmethod
    def Create(self):
        return


class PanelDeveloper(Developer):

    def __init__(self, name):
        self.__name = name

    def Create(self):
        return PanelHouse()


class WoodDeveloper(Developer):

    def __init__(self, name):
        self.__name = name

    def Create(self):
        return WoodHouse()


dev = PanelDeveloper("КирпичСтрой")
panelHouse = dev.Create()
dev = WoodDeveloper("Древострой")
woodHouse = dev.Create()
