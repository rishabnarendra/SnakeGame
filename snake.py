import pygame
import math
import random

def main():
    width = 500
    height = 500
    game = pygame.display.set_mode((width, height))
    rows = 20
    snake = snake((255, 0, 0),(10, 10))

    endGame = true
    clock = pygame.time.Clock()
    while(endGame):
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(game)
