class Building:
    def __init__(self, chunks):
        super().__init__()
        self.x, self.y = None, None
        self.chunks = chunks
        self.name = None


class CityHall(Building):
    def __init__(self, chunks):
        super().__init__(chunks)
        self.name = 'CityHall'
