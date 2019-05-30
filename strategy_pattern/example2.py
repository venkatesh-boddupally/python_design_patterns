import abc


class Itransport(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def move(self):
        pass


class BusTransport(Itransport):
    def move(self):
        print('Going by Bus')


class CarTransport(Itransport):
    def move(self):
        print('Going by Car')


class TrainTransport(Itransport):
    def move(self):
        print('Going by Train')


class Journey(object):
    def __init__(self, journey_type):
        self.jounery_type = journey_type

    def start(self):
        self.jounery_type.move()


bus_transport = BusTransport()
journey = Journey(bus_transport)
journey.start()

journey = Journey(TrainTransport())
journey.start()

journey = Journey(CarTransport())
journey.start()
