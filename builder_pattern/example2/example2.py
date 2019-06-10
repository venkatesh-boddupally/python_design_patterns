from abc import ABCMeta, abstractmethod


class HousePlan(metaclass=ABCMeta):
    @abstractmethod
    def set_basement(self, basement):
        pass

    @abstractmethod
    def set_structure(self, structure):
        pass

    @abstractmethod
    def set_roof(self, roof):
        pass

    @abstractmethod
    def set_interior(self, interior):
        pass


class House(HousePlan):

    def __init__(self):
        self.basement = None
        self.structure = None
        self.roof = None
        self.interior = None
        self.name = None

    def set_name(self, name):
        self.name = name

    def set_basement(self, basement):
        self.basement = basement

    def set_structure(self, structure):
        self.structure = structure

    def set_interior(self, interior):
        self.interior = interior

    def set_roof(self, roof):
        self.roof = roof


class HouseBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_basement(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    @abstractmethod
    def build_name(self):
        pass


class IglooHouse(HouseBuilder):
    def __init__(self):
        self._house = House()

    def build_basement(self):
        self._house.set_basement('igloo basement')

    def build_structure(self):
        self._house.set_structure('igloo structure')

    def build_interior(self):
        self._house.set_interior('igloo interior')

    def build_roof(self):
        self._house.set_roof('igloo roof')

    def get_house(self):
        return self._house

    def build_name(self):
        self._house.set_name('igloo')


class BrickHouse(HouseBuilder):
    def __init__(self):
        self._house = House()

    def build_basement(self):
        self._house.set_basement('brick basement')

    def build_structure(self):
        self._house.set_structure('brick structure')

    def build_interior(self):
        self._house.set_interior('brick interior')

    def build_roof(self):
        self._house.set_roof('brick roof')

    def get_house(self):
        return self._house

    def build_name(self):
        self._house.set_name('brick')


class CivilEngineer(object):
    def __init__(self, house_builder):
        self._house_builder = house_builder

    def build_house(self):
        self._house_builder.build_basement()
        self._house_builder.build_structure()
        self._house_builder.build_roof()
        self._house_builder.build_interior()

    def get_house(self):
        self._house_builder.get_house()


igloo_house = IglooHouse()
engineer = CivilEngineer(IglooHouse())
engineer.build_house()
print(engineer.get_house())


