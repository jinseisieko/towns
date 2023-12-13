import pygame

from Consts import *


class Map:
    def __init__(self, chunks):
        super().__init__()

        self.chunks = chunks
        self.x = MAP_WIDTH * CHUNK_SIZE // 2 - WIDTH // 2
        self.y = MAP_HEIGHT * CHUNK_SIZE // 2 - HEIGHT // 2
        self.map = pygame.Surface((MAP_WIDTH * CHUNK_SIZE, MAP_HEIGHT * CHUNK_SIZE))

    def draw(self, screen):
        screen.blit(self.map, (0, 0), (self.x, self.y, WIDTH, HEIGHT))

    def update_map(self):
        self.map.fill((255, 255, 255))
        for y, line in enumerate(self.chunks.chunks):
            for x, town in enumerate(line):
                if town is None:
                    pygame.draw.rect(self.map, 0, (x * CHUNK_SIZE, y * CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE), width=1)
