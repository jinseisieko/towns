from Consts import *


class Chunks:
    def __init__(self):
        super().__init__()
        self.chunks = [[None for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    def build(self, building, x, y):
        if self.chunks[y][x] is None:
            return
        self.chunks[y][x] = building

    def destroy(self, x, y):
        self.chunks[y][x] = None
