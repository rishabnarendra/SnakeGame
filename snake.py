import pygame
import math
import random

# width, height and rows for the snake game, can be changed based upon difficulty level
width = 500
height = 500
rows = 20


def main():
    print("dsvuasdgjbas")
    game = pygame.display.set_mode((width, height))
    print("hello")
    print(10)
    # snakeGame = snake((255, 0, 0),(10, 10))

    endGame = True
    clock = pygame.time.Clock()
    while(endGame):
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(game)


# redraw game window after each iteration
def redrawWindow(game):
    game.fill((0, 0, 0))
    drawGrid(game)
    pygame.display.update()


# draw grid through which snake is moving 
def drawGrid(game):
    sizeBetweenRows = width // rows
    xAxis = 0
    yAxis = 0

    # draw lines in between to make boxes 
    for l in range(rows):
        xAxis += sizeBetweenRows
        yAxis += sizeBetweenRows
        pygame.draw.line(game, (255, 255, 255), (xAxis, 0), (xAxis, width))
        pygame.draw.line(game, (255, 255, 255), (0, yAxis), (width, yAxis))

main()
