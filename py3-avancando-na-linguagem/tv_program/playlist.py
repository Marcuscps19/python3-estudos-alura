class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    @property
    def listing(self):
        return self._programs

    @property
    def length(self):
        return len(self._programs)
