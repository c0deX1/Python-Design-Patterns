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


class Observer(abs.ABC):
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
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    def registerObserver(self, observer, None):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        """"""

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.__pressure = pressure
        self.__humidity = humidity
        self.__temperature = temperature
        self.measurementsChanged()

class CurrentConditionDisplay(Observer)

    def __init__(self, weatherData):
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0

        self.__weatherData = weatherData
        weatherData.registerObserver(self)

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

    def update(self, temp, humidity, pressure):
        self.__pressure = pressure
        self.__temperature = temp
        self.__humidity = humidity

    def display(self): #not implemented, should create interface or abc class
        print("Current conditions: " + str(self.temperature) + " C degrees, " + str(self.humidity) + "% humidity and " + str(self.pressure) + " bar pressure")