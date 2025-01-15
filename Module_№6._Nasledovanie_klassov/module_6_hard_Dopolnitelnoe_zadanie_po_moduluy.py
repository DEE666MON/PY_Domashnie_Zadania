import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_color(color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        elif len(sides) > 1 and len(sides) < self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides) * self.sides_count
        self.filled = False

    def __is_valid_color(self, args):
        flag_proverka = False
        for i in args:
            flag_proverka = False
            if not isinstance(i, int):
                return False
            if i >= 0 and i <= 255:
                flag_proverka = True
            else:
                return False
        return flag_proverka

    def get_color(self):
        return self.__color

    def set_color(self, *new_color):
        if not self.__is_valid_color(new_color):
            return None
        self.__color = list(new_color)

    def __is_valid_sides(self, args):
        flag_proverka = False
        for i in args:
            flag_proverka = False
            if not isinstance(i, int):
                return False
            if (len(args) == 1 or len(args) == self.sides_count) and i > 0:
                flag_proverka = True
            else:
                return False
        return flag_proverka

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if not self.__is_valid_sides(new_sides):
            return None
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        elif self.sides_count == 12:
            self.__sides = list(new_sides) * self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) > 1:
            self.set_sides(1)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return float(3.14 * self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = float((1 / 2) * sum(self.get_sides()))
        return float(math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        for i in self.get_sides():
            return i ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6, 9)

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
