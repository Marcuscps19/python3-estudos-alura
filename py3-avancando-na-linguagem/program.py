class Program:
    def __init__(self, name, year):
        self._name = name
        self.year = year
        self._likes = 0

    def add_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name.title()

    @property
    def likes(self):
        return self._likes

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'{self._name} - {self.year} - {self._likes}'
