import abc


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, value):
        pass
