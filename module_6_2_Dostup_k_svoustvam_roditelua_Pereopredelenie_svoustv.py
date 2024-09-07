class Vehicle:
    __COLOR_VARIANTS = ['white', 'blue', 'red', 'black', 'green']
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_model(self, new_model):
        self.__model = new_model

    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power

    def set_color(self, new_color):
        flag_break = False
        new_color = new_color.lower()
        for i in range(len(self.__COLOR_VARIANTS)):
            flag_break = False
            if new_color == self.__COLOR_VARIANTS[i]:
                self.__color = new_color
                flag_break = False
                break
            else:
                flag_break = True
        if flag_break:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, o, m, c, h):
        self.owner = o
        self.set_model(m)
        self.set_engine_power(h)
        self.set_color(c)


# Текущие цвета __COLOR_VARIANTS = ['white', 'blue', 'red','black', 'green']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
