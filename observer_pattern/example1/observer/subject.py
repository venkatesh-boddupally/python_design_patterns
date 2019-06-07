import abc

from observer_pattern.example1.observer.observer import Observer


class Subject(metaclass=abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, Observer):
            raise TypeError('observer not defined')
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for obs in self._observers:
            if value is None:
                obs.update()
            else:
                obs.update(value)
