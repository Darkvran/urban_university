class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name, self.weight, self.category}'

class Shop:

    def __init__(self, filename: str = 'products.txt'):
        self.__file_name = filename

    def get_products(self):
        file = open(self.__file_name, 'r')
        string = file.read()
        file.close()
        return string

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in self.get_products():
                print(f'Продукт {product} уже есть в магазине')
                continue
            file.write(f'{product}\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
