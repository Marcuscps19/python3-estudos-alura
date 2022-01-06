from movie import Movie
from serie import Serie

vingadores = Movie('Vingadores Guerra Infinita', 2018, 160)

dexter = Serie('Dexter True Blood', 2021, 1)
dexter.add_like()

movies_and_series = [vingadores, dexter]

for program in movies_and_series:
    print(program)

lista = [1, 2, 4, 5]
