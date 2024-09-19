class User:

    def __str__(self):
        return f'{self.nickname}\nВозраст: {self.age}'

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age