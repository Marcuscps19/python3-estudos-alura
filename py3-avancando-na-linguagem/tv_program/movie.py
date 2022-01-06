from program import Program


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return (f'\nNome: {self._name} - Duração: {self.duration} - '
                f'Ano: {self.year} - Likes: {self._likes}')
