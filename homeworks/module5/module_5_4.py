class House:
    houses_history = []

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        return (self + value)

    def __iadd__(self, value):

        return (self + value)

    def go_to(self, new_floor):
        if new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

#Объясните пожалуйста, чем плох такой метод? (без args) Не совсем понимаю, как реализовать иначе и для чего.