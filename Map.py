import pygame

from Consts import *
from Sprites import sprites


class Map:
    def __init__(self, chunks):
        super().__init__()

        self.chunks = chunks
        self.x = MAP_WIDTH * CHUNK_SIZE // 2 - WIDTH // 2
        self.y = MAP_HEIGHT * CHUNK_SIZE // 2 - HEIGHT // 2
        self.map = pygame.Surface((MAP_WIDTH * CHUNK_SIZE, MAP_HEIGHT * CHUNK_SIZE))

    def draw(self, screen):
        screen.blit(self.map, (0, 0), (self.x, self.y, WIDTH, HEIGHT))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, MAP_WIDTH * CHUNK_SIZE - WIDTH))
        self.y = max(0, min(self.y, MAP_HEIGHT * CHUNK_SIZE - HEIGHT))

    def get_mouse_position(self, mouse_position):
        x = self.x + mouse_position[0]
        y = self.y + mouse_position[1]
        return x // CHUNK_SIZE, y // CHUNK_SIZE

    def update_map(self):
        self.map.fill((255, 255, 255))
        if self.chunks.is_selected():
            pygame.draw.rect(self.map, (0, 255, 0, 0), (
                self.chunks.selected_x * CHUNK_SIZE, self.chunks.selected_y * CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE))
        for y, line in enumerate(self.chunks.chunks):
            for x, town in enumerate(line):
                if town is None:
                    pygame.draw.rect(self.map, 0, (x * CHUNK_SIZE, y * CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE), width=1)
                else:
                    self.map.blit(sprites[town.name], (x * CHUNK_SIZE, y * CHUNK_SIZE))
                    pygame.draw.rect(self.map, 0, (x * CHUNK_SIZE, y * CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE), width=1)
