import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# class that represents the look of the snake and its movement 
class square(object):
    rows = 20
    w = 500
    # initialize the square object 
    def __init__(self, start, directionX = 1, directionY = 0, color = (255, 0, 0)):
        self.position = start
        self.directionX = 1
        self.directionY = 0
        self.color = color


    # Move the square object in the correct direction based on the key pressed 
    def move(self, directionX, directionY):
        self.directionX = directionX
        self.directionY = directionY
        self.position = (self.position[0] + self.directionX, self.position[1] + self.directionY)



    def draw(self, game, eyes = False):
        dis = self.w // self.rows
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(game, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(game, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(game, (0,0,0), circleMiddle2, radius)

            

class snake(object):
    snakeBody = []
    turns = {}


    # intialize the snake object 
    def __init__(self, color, position):
        self.color = color
        self.head = square(position)
        self.snakeBody.append(self.head)
        self.directionX = 0
        self.directionY = 1


    # move the snake object based on the key pressed 
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.directionX = -1
                    self.directionY = 0
                    self.turns[self.head.position[:]] = [self.directionX, self.directionY]

                elif keys[pygame.K_RIGHT]:
                    self.directionX = 1
                    self.directionY = 0
                    self.turns[self.head.position[:]] = [self.directionX, self.directionY]

                elif keys[pygame.K_UP]:
                    self.directionX = 0
                    self.directionY = -1
                    self.turns[self.head.position[:]] = [self.directionX, self.directionY]

                elif keys[pygame.K_DOWN]:
                    self.directionX = 0
                    self.directionY = 1
                    self.turns[self.head.position[:]] = [self.directionX, self.directionY]

        for i, c in enumerate(self.snakeBody):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.snakeBody)-1:
                    self.turns.pop(p)
            else:
                if c.directionX == -1 and c.position[0] <= 0:
                    c.position = (c.rows - 1, c.position[1])
                elif c.directionX == 1 and c.position[0] >= c.rows - 1:
                    c.position = (0, c.position[1])
                elif c.directionY == 1 and c.position[1] >= c.rows - 1:
                    c.position = (c.position[0], 0)
                elif c.directionY == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], c.rows-1)
                else: c.move(c.directionX, c.directionY)


    # draw the squares of the snake
    def draw(self, game):
        for i, c in enumerate(self.snakeBody):
            if i == 0:
                c.draw(game, True)
            else:
                c.draw(game)


    def addSquare(self):
        tail = self.snakeBody[-1]
        dx, dy = tail.directionX, tail.directionY

        if dx == 1 and dy == 0:
            self.snakeBody.append(square((tail.position[0]-1,tail.position[1])))
        elif dx == -1 and dy == 0:
            self.snakeBody.append(square((tail.position[0]+1,tail.position[1])))
        elif dx == 0 and dy == 1:
            self.snakeBody.append(square((tail.position[0],tail.position[1]-1)))
        elif dx == 0 and dy == -1:
            self.snakeBody.append(square((tail.position[0],tail.position[1]+1)))

        self.snakeBody[-1].directionX = dx
        self.snakeBody[-1].directionY = dy



    # reset the game if it ends
    def reset(self, postion):
        self.head = square(position)
        self.body = []
        self.snakeBody.append(self.head)
        self.turns = {}
        self.directionX = 0
        self.directionY = 1
            


# redraw game window after each iteration
def redrawWindow(game):
    global rows, width, snakeGame, snakeSnack
    game.fill((0, 0, 0))
    snakeGame.draw(game)
    snakeSnack.draw(game)
    drawGrid(width, rows, game)
    pygame.display.update()


# draw grid through which snake is moving 
def drawGrid(w, rows, game):
    sizeBetweenRows = w // rows
    xAxis = 0
    yAxis = 0

    # draw lines in between to make boxes 
    for l in range(rows):
        xAxis += sizeBetweenRows
        yAxis += sizeBetweenRows
        pygame.draw.line(game, (255, 255, 255), (xAxis, 0), (xAxis, width))
        pygame.draw.line(game, (255, 255, 255), (0, yAxis), (width, yAxis))


# display a message box once the game has ended
def displayMessageBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy
    except:
        pass


# generate snack for snake to eat
def generateSnakeSnack(rows, item):
    positions = item.snakeBody
    while True:
        xSnack = random.randrange(rows)
        ySnack = random.randrange(rows)
        # make sure the snack generated is not on the snake 
        if(len(list(filter(lambda z: z.position == (xSnack, ySnack), positions)))) > 0:
           continue
        else:
            break
    return (xSnack, ySnack)


def main():
    global width, rows, snakeGame, snakeSnack
    width = 500
    rows = 20
    game = pygame.display.set_mode((width, width))
    snakeGame = snake((255, 0, 0),(10, 10))

    snakeSnack = square(generateSnakeSnack(rows, snakeGame), color = (0, 255, 0))
    
    endGame = True
    clock = pygame.time.Clock()
    while endGame:
        pygame.time.delay(50)
        clock.tick(10)
        snakeGame.move()
        if snakeGame.snakeBody[0].position == snakeSnack.position:
            snakeGame.addSquare()
            snakeSnack = square(generateSnakeSnack(rows, snakeGame), color = (0, 255, 0))

        
        # if snake crashes into itself the game is over
        for x in range(len(snakeGame.snakeBody)):
            # check if the head of the snake is on top of any other position in the range of the snake body
            if snakeGame.snakeBody[x].position in list(map(lambda z: z.position, snakeGame.snakeBody[x + 1:])):
                displayMessageBox('Game Over!', "Score: " + str(len(snakeGame.snakeBody)))
                snakeGame.reset((10, 10))
                break
        
        redrawWindow(game) 


main()
