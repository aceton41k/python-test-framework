from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def power(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def power(self) -> int:
        return int(math.pow(self.radius, 2))


# Использование абстракции
my_circle = Circle(5)
print(my_circle.power())
