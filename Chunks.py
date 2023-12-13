from Buldings import CityHall
from Consts import *


class Chunks:
    def __init__(self):
        super().__init__()
        self.chunks = [[None for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.selected_x, self.selected_y = 0, 0

        self.build(CityHall(self), MAP_WIDTH//2, MAP_HEIGHT//2)

    def set_selected(self, x, y):
        self.selected_x = x
        self.selected_y = y

    def none_selected(self):
        self.selected_x = None
        self.selected_y = None

    def is_selected(self):
        return not (self.selected_x is None or self.selected_y is None)

    def build(self, building, x, y):
        if self.chunks[y][x] is None:
            self.chunks[y][x] = building
            building.x = x
            building.y = y

    def destroy(self, x, y):
        self.chunks[y][x] = None
