import inspect

class Cat():
    """
    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
    """
    def __init__(self, name, gender, age, lives):
        self.name = name
        self.age = age
        self.gender = gender
        self.lives = lives

    def say_meow(self):
        return "Мяу! (Перевод с кошачьего: 'Я хозяин этой квартиры. Несите жрать, кожаные!')"

    def drop_the_vase(self):
        return "-1 ваза, +1 недовольный человечишка :3"

def introspection_info(obj):
    dict = {"type": type(obj), "attrubutes": dir(obj), "methods": [name for name, member in inspect.getmembers(obj, predicate=inspect.ismethod)], "module": obj.__class__.__module__, "isCat": isinstance(obj, Cat)}
    return dict
def main():
    cat = Cat("Кусимир", "М", 3, 9)
    print(introspection_info(cat))


if __name__ == "__main__":
    main()