import pygame

import pygame.display as display
from pygame.constants import *
from lifeforms import Lifeforms
from random import randint
from time import sleep

def main():
    pygame.init()
    display.set_caption('Game of Life')
    width, height = 800, 800

    L = Lifeforms()

    screen = display.set_mode((width, height))
    running = True
    sim=False
    clock = pygame.time.Clock()
    while running:
        # clock.tick(5)

        screen.fill(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x , y = pos
                L.add(x, y)
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    sim ^= True
                    # L.simulate()
                if event.key == K_r:
                    L = Lifeforms()
                if event.key == K_ESCAPE:
                    pygame.quit()
        if sim:
            L.simulate()
        L.display(screen)

        display.update()


main()