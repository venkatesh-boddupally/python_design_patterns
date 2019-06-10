from abc import ABCMeta, abstractmethod
from builder_pattern.example1.computer import Computer


class Ibuilder(metaclass=ABCMeta):
    
    _computer = None
    
    def get_computer(self):
        return self._computer
    
    def new_computer(self):
        self._computer = Computer()

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass

    @abstractmethod
    def install_video_card(self):
        pass
