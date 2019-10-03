from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        print('Area!')

    @abstractmethod
    def perimeter(self):
        print('Perimeter!')


class Ellipse(Figure):
    def area(self):
        pass

    def perimeter(self):
        pass
    pass


class Circle(Figure):
    def area(self):
        pass

    def perimeter(self):
        pass

    pass


class Triangle(Figure):
    def area(self):
        pass

    def perimeter(self):
        pass
    pass
