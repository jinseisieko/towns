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
moving = False
last_position_mouse = None

while running:
    position_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2 or event.button == 3:
                moving = True

            if event.button == 1:
                chunks.set_selected(*map_.get_mouse_position(position_mouse))
                map_.update_map()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2 or event.button == 3:
                moving = False

    if pygame.key.get_pressed()[pygame.K_DELETE]:
        running = False
        quit()

    if moving:
        if last_position_mouse is None:
            last_position_mouse = position_mouse
        else:
            map_.move(last_position_mouse[0] - position_mouse[0], last_position_mouse[1] - position_mouse[1])
            last_position_mouse = position_mouse
    else:
        last_position_mouse = None

    map_.draw(screen)
    pygame.display.flip()
    clock.tick(TICKS)
