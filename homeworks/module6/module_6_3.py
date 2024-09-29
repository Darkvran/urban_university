class Horse:
    sound = 'Frrr'

    def __init__(self, x_distance=0):
        self.x_distance = x_distance

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance=0):
        self.y_distance = y_distance

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def __init__(self, x_distance=0, y_distance=0):
        super().__init__(y_distance)
        Horse.__init__(self, x_distance)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
