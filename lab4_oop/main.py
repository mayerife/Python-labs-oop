from abc import ABC, abstractmethod
from math import pi


if __name__ == "__main__":
    class Shape(ABC):
        """
        Базовый класс для всех фигур.
        """

        def __init__(self, color: str):
            """
            Конструктор класса Shape.

            Parameters:
            color (str): Цвет фигуры.
            """
            self.color = color

        @abstractmethod
        def area(self) -> float:
            """
            Метод для вычисления площади фигуры.
            """
            pass

        @abstractmethod
        def perimeter(self) -> float:
            """
            Метод для вычисления периметра фигуры.
            """
            pass

        def __str__(self) -> str:
            """
            Метод для получения строкового представления фигуры.
            """
            return f"Фигура цвета {self.color}"

        def __repr__(self) -> str:
            """
            Метод для получения формального строкового представления фигуры.
            """
            return f"{self.__class__.__name__}(color={self.color!r})"


    class Circle(Shape):
        """
        Класс для кругов.
        """

        def __init__(self, color: str, radius: float):
            """
            Конструктор класса Circle.

            Parameters:
            color (str): Цвет круга.
            radius (float): Радиус круга.
            """
            super().__init__(color)
            self.radius = radius

        def area(self) -> float:
            """
            Метод для вычисления площади круга.
            """
            return pi * self.radius ** 2

        def perimeter(self) -> float:
            """
            Метод для вычисления периметра круга.
            """
            return 2 * pi * self.radius

        def __str__(self) -> str:
            """
            Переопределение метода __str__ для круга.
            """
            return f"Круг цвета {self.color} с радиусом {self.radius}"

        def __repr__(self) -> str:
            """
            Переопределение метода __repr__ для круга.
            """
            return f"Circle(color={self.color!r}, radius={self.radius})"


    class Rectangle(Shape):
        """
        Класс для прямоугольников.
        """

        def __init__(self, color: str, width: float, height: float):
            """
            Конструктор класса Rectangle.

            Parameters:
            color (str): Цвет прямоугольника.
            width (float): Ширина прямоугольника.
            height (float): Высота прямоугольника.
            """
            super().__init__(color)
            self.width = width
            self.height = height

        def area(self) -> float:
            """
            Метод для вычисления площади прямоугольника.
            """
            return self.width * self.height

        def perimeter(self) -> float:
            """
            Метод для вычисления периметра прямоугольника.
            """
            return 2 * (self.width + self.height)

        def __str__(self) -> str:
            """
            Переопределение метода __str__ для прямоугольника.
            """
            return f"Прямоугольник цвета {self.color} с шириной {self.width} и высотой {self.height}"

        def __repr__(self) -> str:
            """
            Переопределение метода __repr__ для прямоугольника.
            """
            return f"Rectangle(color={self.color!r}, width={self.width}, height={self.height})"
    pass
