class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(kwargs.get('name'))
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.args = args
        for key, values in kwargs.items():
            setattr(self, key, values)

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


h1 = House(name='ЖК Эльбрус', number_of_floors=10)
print(House.houses_history)
h2 = House(name='ЖК Акация', number_of_floors=20)
print(House.houses_history)
h3 = House(name='ЖК Матрёшки', number_of_floors=20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

