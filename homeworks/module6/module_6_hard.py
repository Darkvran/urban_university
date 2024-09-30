from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: list[int], sides: list[int], filled: bool = True):
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1 for i in range(0, self.sides_count)]
        self.__color = color
        self.is_filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for side in args:
            if side < 0 or (not isinstance(side, int)) or len(args) != len(self.__sides):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *args):
        if len(args) == self.sides_count:
            self.__sides = args


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list[int], sides: list[int], filled: bool = True):
        super().__init__(color, sides, filled)
        self.radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * (self.radius) ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list[int], sides: list[int], filled: bool = True):
        super().__init__(color, sides, filled)
        self.p = len(self) / 2  # half-perimeter

    def get_square(self):
        return sqrt(self.p * (self.p - self.__sides[0]) * (self.p - self.__sides[1]) * (self.p - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list[int], sides: list[int], filled: bool = True):
        super().__init__(color, sides, filled)
        self.__sides = [sides[0] for i in range(0, 12)]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle([200, 200, 100], [10])  # (Цвет, стороны)
cube1 = Cube([222, 35, 130], [6])

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
