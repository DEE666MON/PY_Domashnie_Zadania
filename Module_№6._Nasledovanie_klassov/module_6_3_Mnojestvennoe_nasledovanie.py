class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        if self.x_distance == 0:
            self.x_distance = dx
        else:
            self.x_distance += dx

    def voice(self):
        print(super().sound)


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        if self.y_distance == 0:
            self.y_distance = dy
        else:
            self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        super().voice()


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
