import time


class Video:
    time_now = 0

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class UrTube:
    videos: list[Video] = []
    users: list[User] = []
    current_user = None

    def register(self, nickname: str, password: str, age: int):
        newUser = User(nickname, password, age)
        for i in self.users:
            if nickname == i.nickname:
                print(f"Пользователь {nickname} уже существует")
                return None
        self.users.append(newUser)
        self.log_in(nickname, password)

    def log_in(self, nickname: str, password: str):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                break

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word: str):
        videoTrue = []
        search_word = search_word.lower()
        for i in self.videos:
            if search_word in i.title.lower():
                videoTrue.append(i.title)
        return videoTrue

    def watch_video(self, search_video: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return None
        for i in self.videos:
            if search_video == i.title:
                if i.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break
                else:
                    for j in range(i.duration):
                        i.time_now += 1
                        print(i.time_now, end=' ')
                        time.sleep(0.01)
                    i.time_now = 0
                    print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
