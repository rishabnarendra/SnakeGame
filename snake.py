import pygame
import math
import random

# width, height and rows for the snake game, can be changed based upon difficulty level
width = 500
height = 500
rows = 20


class snake(object):
    snakeBody = []
    turns = {}

    # intialize the snake object 
    def initialize(self, color, position):
        self.color = color
        self.head = square(position)
        self.body.append(self.head)
        self.directionX = 0
        self.directionY = 1

    # move the snake object based on the key pressed 
    def move(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()

            # dictionary of all keys and whether they were pressed or not
            keys = pygame.key.get_pressed()
            # change direction of the head of the snake 
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.directionX = -1
                    self.directionY = 0
                    self.turns[self.head.pos[:]] = self[directionX, self.directionY]

                elif keys[pygame.K_RIGHT]:
                    self.directionX = 1
                    self.directionY = 0
                    self.turns[self.head.pos[:]] = self[directionX, self.directionY]

                elif keys[pygame.K_UP]:
                    self.directionX = 0
                    self.directionY = -1
                    self.turns[self.head.pos[:]] = self[directionX, self.directionY]

                elif keys[pygame.K_DOWN]:
                    self.directionX = 0
                    self.directionY = 1
                    self.turns[self.head.pos[:]] = self[directionX, self.directionY]


            for index, square in enumerate(self.body):
                position = square.position[:]
                if position in self.turns:
                    turn = self.turns[position]
                    square.move(turn[0], turn[1])
                    if i == len(self.body) - 1:
                        self.turns.pop(position)
                # wrap around if we are out of bounds in the grid or continue moving 
                else:
                    if directionX == -1 and square.position[0] <= 0:
                        square.position = (square.rows - 1, square.position[1])
                    elif directionX == 1 and square.position[0] >= square.rows - 1:
                        square.position = (0, square.position[1])
                    elif directionY == -1 and square.position[1] <= 0:
                        square.position = (square.position[1], square.rows - 1)
                    elif directionX == 1 and square.position[0] >= square.rows - 1:
                        square.position = (square.position[0], 0)
                    else:
                        square.move(square.directionX, square.directionY)


    def draw(self, game):
        for index, square in enumerate(self.body):
            if index == 0:
                square.draw(game, true)
            else:
                square.draw(game)


def main():
    game = pygame.display.set_mode((width, height))
    snakeGame = snake((255, 0, 0),(10, 10))

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
