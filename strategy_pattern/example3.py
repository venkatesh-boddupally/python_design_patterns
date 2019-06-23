from abc import ABCMeta, abstractmethod


class QuackStrategy(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass


class LoudStrategy(QuackStrategy):
    def quack(self):
        print('quack! quack!')


class GentleStrategy(QuackStrategy):
    def quack(self):
        print('quck')


class LightStrategy(metaclass=ABCMeta):
    def lights_on(self):
        pass


class On10SecLights(LightStrategy):
    def lights_on(self):
        print('lights on for 10 secs')


class Duck(object):
    def __init__(self, quack_strategy, lights_strategy):
        self._quack_strategy = quack_strategy
        self._lights_strategy = lights_strategy

    def quack(self):
        self._quack_strategy.quack()

    def lights_on(self):
        self._lights_strategy.lights_on()


loud_strategy = LoudStrategy()
gentle_quack = GentleStrategy()
ten_seconds = On10SecLights()


class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(loud_strategy, None)

    def go_home(self):
        print("Going to the river")


class ToyDuck(Duck):
    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_seconds)


class CityDuck(Duck):
    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)

    def go_home(self):
        print("Going to the Central Park pond")


class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(loud_strategy, ten_seconds)


robo = RobotDuck()

robo.quack()  # QUACK! QUACK!!
robo.lights_on()
