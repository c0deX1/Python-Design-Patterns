import abc


class Command(abc.ABC):
    def execute(self):
        """Execute method, must be overrided"""


class Light:
    def __init__(self):
        self.__light = False

    @property
    def light(self):
        return self.__light

    @light.setter  # Fuc incapsulation
    def light(self, light):
        self.__light = light

    def on(self):
        self.__light = True

    def off(self):
        self.__light = False


class LightOnCommand(Command):
    def __init__(self, light):
        self.__Light = light

    def execute(self):
        if not self.__Light.light:
            self.__Light.on()
            print("Light is on")
        else:
            print("Light already is on")


class LightOffCommand(Command):
    def __init__(self, light):
        self.__Light = light

    def execute(self):
        if self.__Light.light:
            self.__Light.off()
            print("Light is off")
        else:
            print("Light already is off")


class SimpleRemoteControl:
    def __init__(self):
        self.__slot = Command()

    @property
    def slot(self):
        return self.__slot

    @slot.setter  # Fuc incapsulation
    def slot(self, slot):
        self.__slot = slot

    def setCommand(self, command):
        self.__slot = command

    def buttonWasPressed(self):
        self.__slot.execute()


remote = SimpleRemoteControl()
light = Light()
lightOn = LightOnCommand(light)
lightOff = LightOffCommand(light)

remote.setCommand(lightOn)
remote.buttonWasPressed()
remote.buttonWasPressed()

remote.setCommand(lightOff)
remote.buttonWasPressed()
remote.buttonWasPressed()
