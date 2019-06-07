from observer_pattern.example1.observer.observer import Observer


class Obs2(Observer):

    def __init__(self, kpi):
        self.open_tickets = -1
        self.closed_tickets = -1
        self.new_tickets = -1

        self._kpi = kpi
        kpi.attach(self)

    def update(self):
        self.open_tickets = self._kpi.open_tickets
        self.closed_tickets = self._kpi.closed_tickets
        self.new_tickets = self._kpi.new_tickets
        self.display()

    def display(self):
        print('------------observer* 2*  output-------------')
        print('open tickets', self.open_tickets)
        print('closed tickets', self.closed_tickets)
        print('new tickets', self.new_tickets)
        print('------------------------------')
