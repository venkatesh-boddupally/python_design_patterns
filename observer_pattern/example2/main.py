class SubjectOne(object):

    def __init__(self, name):
        self._name = name

    def update(self, message):
        print('{0} got message {1}'.format(self._name, message))


class SubjectTwo(object):

    def __init__(self, name):
        self._name = name

    def receive(self, message):
        print('{0} got message {1}'.format(self._name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers = dict()

    def register(self, subscrib, callback=None):
        if callback is None:
            callback = getattr(subscrib, 'update')
        self.subscribers[subscrib] = callback

    def unregister(self, subscrib):
        del self.subscribers[subscrib]

    def notify(self, message):
        for subs, callback in self.subscribers.items():
            callback(message)


pub = Publisher()

john = SubjectOne('John')
snow = SubjectTwo('snow')

pub.register(john, john.update)
pub.register(snow, snow.receive)

pub.notify('Today is Holiday')

print('--------------------------uniregistered john object------------------')
pub.unregister(john)

pub.notify('Its lunch time')
