from program import Program


class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return (f'\nNome: {self._name} - Temporadas: {self.seasons} - '
                f'Ano: {self.year} - Likes: {self._likes}')
