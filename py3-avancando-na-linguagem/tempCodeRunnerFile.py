class Movie:
    def __init__(self, name, year, duration):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def add_like(self):
        self.likes += 1


vingadores = Movie('Vingadores - Guerra Infinita', 2018, 160)
print(f'Nome: {vingadores.name}\nAno: {vingadores.year}\n'
      f'Tempo de duração: {vingadores.duration}\n Likes:{vingadores.likes}')


class Show:
    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def add_like(self):
        self.likes += 1


dexter = Show('Dexter - True Blood', 2021, 1)
dexter.add_like()
print(f'\nNome: {dexter.name}\nAno: {dexter.year}\n'
      f'Tempo de duração: {dexter.seasons}\nLikes:{dexter.likes}')
