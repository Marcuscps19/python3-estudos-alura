from movie import Movie
from serie import Serie
from playlist import Playlist

avengers = Movie('Vingadores Guerra Infinita', 2018, 160)
resurrection = Movie('Resurreição', 2016, 107)
dexter = Serie('Dexter True Blood', 2021, 1)
csi = Serie('CSI Miami', 2008, 12)
cobra_kai = Serie('Cobra Kai', 2019, 3)


dexter.add_like()

movies_and_series = [avengers, resurrection, dexter, csi, cobra_kai]
playlist = Playlist('Top 5 filmes e series', movies_and_series)

for program in playlist:
    print(program)

print(avengers in playlist)
print(playlist[1])

print(f'Tamanho playlist: {len(playlist)}')
