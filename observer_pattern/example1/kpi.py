from observer_pattern.example1.observer.subject import Subject


class Kpi(Subject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_t, closed_t, new_t):
        self._open_tickets = open_t
        self._closed_tickets = closed_t
        self._new_tickets = new_t
        self.notify()
