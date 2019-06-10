from builder_pattern.example1.high_computer_builder import HighComputer
from builder_pattern.example1.cheap_computer import CheapComputer
from builder_pattern.example1.director import Director

highcomputer = HighComputer()
director = Director(highcomputer)
director.build_computer()
computer = director.get_computer()
computer.display()
print('\n\n')
cheapcomputer = CheapComputer()
director = Director(cheapcomputer)
director.build_computer()
computer = director.get_computer()
computer.display()