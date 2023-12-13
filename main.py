import pygame

from Chunks import Chunks
from Map import Map
from Consts import *

pygame.init()
clock = pygame.time.Clock()

chunks = Chunks()
map_ = Map(chunks)
map_.update_map()

screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()

    if pygame.key.get_pressed()[pygame.K_DELETE]:
        running = False
        quit()

    map_.draw(screen)
    pygame.display.flip()
    clock.tick(TICKS)
