import abc


class Subject(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        """Abstract class for subject"""

    @abc.abstractmethod
    def registerObserver(self, observer):
        """Registration of observer"""

    @abc.abstractmethod
    def removeObserver(self, observer):
        """Remover concrete observer"""

    @abc.abstractmethod
    def notifyObservers(self):
        """Function for notification observers"""


class Observer(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        """Abstract class"""

    @abc.abstractmethod
    def update(self, temp, humidity, pressure):
        """Update information"""


class WeatherData(Subject):
    def __init__(self):
        self.__humidity = 0
        self.__temperature = 0
        self.__pressure = 0
        self.__observers = []

    @property
    def observer(self):
        return self.__observers

    @observer.setter
    def observer(self, observer):
        self.__observers = observer

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @property
    def humidity(self):
        return self.__humidity

    @humidity.setter
    def humidity(self, humidity):
        self.__humidity = humidity

    @property
    def observers(self):
        return self.__observers

    @observers.setter
    def observers(self, observers):
        self.__observers = observers

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    def registerObserver(self, observer):
        self.__observers.append(observer)
        print("New subscriber!")

    def removeObserver(self, observer):
        self.__observers.remove(observer)
        print("Subscriber " + observer.name + " deleted!")

    def notifyObservers(self):
        for obs in self.__observers:
            obs.update(self.temperature, self.humidity, self.pressure)
            print("Subscriber " + obs.name + "get message!")

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.__pressure = pressure
        self.__humidity = humidity
        self.__temperature = temperature
        self.measurementsChanged()


class CurrentConditionDisplay(Observer):

    def __init__(self, name, weatherData):
        self.__name = name
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0

        self.__weatherData = weatherData
        self.weatherData.registerObserver(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @property
    def humidity(self):
        return self.__humidity

    @humidity.setter
    def humidity(self, humidity):
        self.__humidity = humidity

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    @property
    def weatherData(self):
        return self.__weatherData

    @weatherData.setter
    def weatherData(self, weatherData):
        self.__weatherData = weatherData

    def update(self, temp, humidity, pressure):
        self.__pressure = pressure
        self.__temperature = temp
        self.__humidity = humidity
        self.display()

    def display(self):  # not implemented, should create interface or abc class
        print("Current conditions by " + self.name + " : " + str(self.temperature) + " C degrees, " + str(
            self.humidity) + "% humidity and " + str(self.pressure) + " bar pressure")


weatherData = WeatherData()
conditionDisplay1 = CurrentConditionDisplay("Observer 1", weatherData)
conditionDisplay2 = CurrentConditionDisplay("Observer 2", weatherData)

weatherData.setMeasurements(80, 65, 30.4)
weatherData.setMeasurements(82, 70, 29.2)
weatherData.setMeasurements(78, 90, 29.2)
weatherData.removeObserver(conditionDisplay1)
weatherData.removeObserver(conditionDisplay2)
