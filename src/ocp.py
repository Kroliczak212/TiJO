from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def draw(self):
        pass

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for _ in range(self.a):
            print("o " * self.a)
        print()

class Triangle(Figure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for side in range(1, self.h + 1):
            print("o " * side)
        print()

class FigureDrawer:
    def draw(self, figure: Figure):
        figure.draw()

# Użycie
a = 5
h = 5

square = Square(a)
triangle = Triangle(h)

drawer = FigureDrawer()
drawer.draw(square)
drawer.draw(triangle)
