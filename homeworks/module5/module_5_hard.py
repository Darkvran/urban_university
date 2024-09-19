from UrTube.UrTube import UrTube
from UrTube.User import User
from UrTube.Video import Video

video1 = Video("Пытаемся понять C++", 10, 0, True)
video2 = Video('Пишем бота для фарма в World of Warcraft на PyAutoGUI', 600, 0, False)
video3 = Video('Техническое собеседование на Senior python-разработчика', 12000, 0, False)
video4 = Video('Учим нейросеть отличать картофель от кота', 7000, 0, False)

user1 = {'name': 'Vlad', 'password': '123123123', 'age': 21}
user2 = {'name': 'Denis', 'password': 'SuperMegaCoolPassword666', 'age': 25}
user3 = {'name': 'Vlad', 'password': '536g@#dfgdfg34rwer6!3w%^$34634', 'age': 15}
user4 = {'name': 'Dasha', 'password': 'password', 'age': 14}

ur = UrTube()



# Добавление видео
ur.add(video1, video2, video3, video4)

# Проверка поиска
print(ur.get_videos('Жоска'))
print(ur.get_videos('Индус объясняет'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Пытаемся понять C++')
ur.register(user4['name'], user4['password'], user4['age'])
ur.watch_video('Пытаемся понять C++')
ur.register(user2['name'], user2['password'], user2['age'])
ur.watch_video('Пытаемся понять C++')

# Проверка входа в другой аккаунт
ur.register(user2['name'], user2['password'], user2['age'])
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



