class OS:
    instance = None

    def __init__(self, name):
        self.__name = name

    @staticmethod
    def getInstanse(name):
        if not OS.instance:
            OS.instance = OS(name)
        return OS.instance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Computer:
    def __init__(self):
        self.__OS = None

    def Launch(self, osName):
        self.__OS = OS.getInstanse(osName)

    @property
    def OS(self):
        return self.__OS


# comp = Computer()
# comp.Launch("Windows")
# print(str(comp.OS.name))
# comp.Launch("Linux")
# print(str(comp.OS.name))
