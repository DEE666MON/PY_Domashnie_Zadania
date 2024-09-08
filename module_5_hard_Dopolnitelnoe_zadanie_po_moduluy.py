import time


class Video:
    dictVideoDuration = {}
    dictVideoAdult = {}
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.dictVideoDuration[self.title] = self.duration
        self.dictVideoAdult[self.title] = self.adult_mode

    def __str__(self):
        return self.title


class User:
    dictUserPassword = None
    dictUserAge = None

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.dictUserPassword[self.nickname] = self.password
        self.dictUserAge[self.nickname] = self.age


class UrTube:
    videos = []
    users = []
    current_user = None

    def add(self, *args):
        for i in args:
            for j in Video.dictVideoDuration.keys():
                if i.title != j:
                    self.videos.append(i.title)

    def get_videos(self, search_word):
        listTrueVideo = []
        listVideo = []
        search_word = search_word.lower()
        for i in range(len(self.videos)):
            listVideo.append(self.videos[i].lower())
        for qq in range(len(self.videos)-1):
            sumWord = ''
            for q in range(len(listVideo)):
                for w in range(len(listVideo[q])):
                    sumWord += listVideo[q][w]
                    if search_word == sumWord and len(sumWord) == len(search_word):
                        listTrueVideo.append(self.videos[qq])
                        qq += 1
                        break
                    if listVideo[q][w] == ' ' or w == len(listVideo[q])-1:
                        sumWord = ''
        return listTrueVideo

    def watch_video(self, name_video):
        for i in range(len(self.videos)):
            flagBreak = False
            if self.current_user != None:
                for key, value in User.dictUserAge.items():
                    if key == self.current_user:
                        if value >= 18:
                            if name_video == self.videos[i]:
                                for timeS in range(10):
                                    print(timeS + 1, end=' ')
                                    time.sleep(0.1)
                                print("Конец видео")
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                            flagBreak = True
                            break
            else:
                print("Войдите в аккаунт, чтобы смотреть видео")
                break
            if flagBreak:
                break

    def log_in(self, nickname, password):
        for key, value in User.dictUserPassword.items():
            if nickname == key and hash(password) == value:
                self.current_user = nickname

    def register(self, nickname, password, age):
        if User.dictUserPassword == None or User.dictUserAge == None:
            User.dictUserPassword = dict()
            User.dictUserAge = dict()
            User(nickname, password, age)
            self.users.append(nickname)
            self.current_user = nickname
        else:
            for i in self.users:
                if nickname != i:
                    User(nickname, password, age)
                    self.users.append(nickname)
                    self.current_user = nickname
                    break
                else:
                    print(f"Пользователь {nickname} уже существует")
                    break

    def log_out(self):
        self.current_user = None


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
