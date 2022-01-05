class Movie:
    def __init__(self, name, year, duration):
        self.__name = name
        self.year = year
        self.duration = duration
        self.__likes = 0

    def add_like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name.title()

    @property
    def likes(self):
        return self.__likes

    @name.setter
    def name(self, name):
        self.__name = name


vingadores = Movie('Vingadores - Guerra Infinita', 2018, 160)
print(f'Nome: {vingadores.name}\nAno: {vingadores.year}\n'
      f'Tempo de duração: {vingadores.duration}\n Likes:{vingadores.likes}')


class Show:
    def __init__(self, name, year, seasons):
        self.__name = name
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    def add_like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @property
    def likes(self):
        return self.__likes

    @name.setter
    def name(self, name):
        self.__name = name


dexter = Show('Dexter - True Blood', 2021, 1)
dexter.add_like()
dexter.name = 'Cobra Kai'
print(f'\nNome: {dexter.name}\nAno: {dexter.year}\n'
      f'Tempo de duração: {dexter.seasons}\nLikes:{dexter.likes}')
