import pygame
import math
import random
import time
import sys

#Constants
width = 640
height = 640
pixels = 32
squares = int(width / pixels)

#Colors
bg1 = (156, 210, 54)
bg2 = (137, 203, 57)

class Background:
    def draw(self, surface):
        surface.fill(bg1)
        counter = 0
        for row in range(squares):
            for col in range(squares):
                if counter % 2 == 0:
                    pygame.draw.rect(surface, bg2, (col * pixels, row * pixels, pixels, pixels))
                if col != squares - 1:
                    counter += 1
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

    background = Background()

    #Mainloop
    while True:
        background.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()        

main()