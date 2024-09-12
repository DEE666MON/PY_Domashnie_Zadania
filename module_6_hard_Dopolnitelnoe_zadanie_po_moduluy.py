import math


class Figure:
    sides_count = 0
    def __init__(self):
        self.__sides = []
        self.__color = [0, 0, 0]
        self.filled = False

    def __is_valid_color(self, *args):
        flag_proverka = False
        for i in args:
            flag_proverka = False
            if i >= 0 and i <= 255:
                flag_proverka = True
            else:
                return False
        return flag_proverka

    def get_color(self):
        return self.__color

    def set_color(self, red, green, blue):
        if self.__is_valid_color(red, green, blue):
            self.__color[0] = red
            self.__color[1] = green
            self.__color[2] = blue

    def __is_valid_sides(self, args):
        flag_proverka = False
        for i in args:
            flag_proverka = False
            if len(args) == self.sides_count and i > 0:
                flag_proverka = True
            else:
                return False
        return flag_proverka

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(self.__sides) != 0:
            self.__sides = []
        if self.__is_valid_sides(new_sides):
            for i in new_sides:
                if len(new_sides) == Circle.sides_count:
                    self.__sides.append(i)
                elif len(new_sides) == Circle.sides_count or len(new_sides) == Triangle.sides_count:
                    for j in range(Triangle.sides_count):
                        self.__sides.append(i)
                elif len(new_sides) == Circle.sides_count or len(new_sides) == Cube.sides_count:
                    for j in range(Cube.sides_count):
                        self.__sides.append(i)


    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        self.set_color(color[0], color[1], color[2])
        self.set_sides(sides)
        self.__radius = sides / 3.14 / 2

    def get_square(self):
        return float(self.__radius * (3.14 * 3.14))


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        self.set_color(color[0], color[1], color[2])
        self.set_sides(sides)

    def get_square(self):
        p = float((1 / 2) * sum(self.__sides))
        return float(math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])))


class Cube(Figure):
    sides_count = 12
    
    def __init__(self, color, sides):
        self.set_color(color[0], color[1], color[2])
        self.set_sides(sides)

    def get_volume(self):
        for i in self.get_sides():
            return i ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

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
