from .User import User
from .Video import Video
from time import sleep


class UrTube:

    def __init__(self, users: list[User] = [], videos: list[Video] = [], current_user: User = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname: str, password: str):
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname and self.users[i].password == hash(password):
                self.current_user = self.users[i]
        print(f'Неверный логин или пароль')
        return Exception('Login error: invalid login or password')

    def register(self, nickname: str, password: str, age: int):
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return Exception('Register error: Existing user')
        new_user = User(nickname, password, age)
        print(new_user)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for argument in args:
            if isinstance(argument, Video):
                self.videos.append(argument)

    def get_videos(self, keyword: str):
        finded_videos = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                finded_videos.append(video.title)
        return finded_videos

    def watch_video(self, searching_video_title: str):
        if self.current_user != None:
            for video in self.videos:
                if video.title == searching_video_title:
                    if video.adult_mode and self.current_user.age >= 18 or video.adult_mode == False:
                        while video.time_now != video.duration:
                            video.time_now += 1
                            sleep(1)
                            print(video.time_now)
                        print('Конец видео')
                    else:
                        print('Вам рано такое смотреть, в видео много нецензурной лексики')
                        return Exception('Access denied: Underage user')
                    video.time_now = 0
        else:
            print('Перед просмотром видео следует пройти авторизацию')
            return Exception('Access denied: Token was expected, but was not received')



