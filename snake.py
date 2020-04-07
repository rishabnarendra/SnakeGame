import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox 

# width, height and rows for the snake game, can be changed based upon difficulty level
width = 500
height = 500
rows = 20


# class that represent our snake object and controls its movement and appearence 
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

    # reset the game if it ends
    def reset(self, postion):
        self.head = square(position[0])
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.directionX = 0
        self.directionY = 1



    def addSquare(self):
        snakeTail = self.body[-1]
        directionX = tail.directionX
        directionY = tail.directionY

        # add square to correct location and give it the correct direction of movement
        if directionX == 1 and directionY == 0:
            self.body.append(square(snakeTail.position[0] - 1, snakeTail.position[1]))
        elif directionX == -1 and directionY == 0:
            self.body.append(square(snakeTail.position[0] + 1, snakeTail.position[1]))
        elif directionX == 0 and directionY == 1:
            self.body.append(square(snakeTail.position[0], snakeTail.position[1] - 1))
        elif directionX == 0 and directionY == -1:
            self.body.append(square(snakeTail.position[0], snakeTail.position[1] + 1))
        self.body[-1].directionX = directionX
        self.body[-1].directionY = directionY
          

    # draw the squares of the snake
    def draw(self, game):
        for index, square in enumerate(self.body):
            if index == 0:
                square.draw(game, true)
            else:
                square.draw(game)



# class that represents the look of the snake and its movement 
class square(object):
    # initialize the square object 
    def initialize(self, start, directionX = 1, directionY = 0, color = (255, 0, 0)):
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
        distance = self.width // self.rows
        xIndex = self.position[0]
        yIndex = self.position[1]

        # draw the lines inside the grid to avoid difficulty of seeing seperating lines (this is drawing the moving squares of the snake)
        pygame.draw.rect(game, self.color, (xIndex * distance + 1, yIndex * distance + 1, distance - 2, distance - 2))
        
        # draw the eyes of the snake, don't worry about the mathematical formula used to position the eyes
        if eyes:
            center = distance // 2
            radius = 3
            eye1 = (xIndex * distance + center - radius, yIndex * distance + 8)
            eye2 = (xIndex * distance + distance - radius * 2, yIndex * distance + 8)
            pygame.draw.circle(game, (0, 0, 0), eye1, radius)
            pygame.draw.circle(game, (0, 0, 0), eye2, radius)


def main():
    global snakeGame, snakeSnack
    game = pygame.display.set_mode((width, height))
    snakeGame = snake((255, 0, 0),(10, 10))
    
    snakeSnack = square(generateSnakeSnack(rows, snakeGame), color = (0, 255, 0))
    
    endGame = True
    clock = pygame.time.Clock()
    while(endGame):
        pygame.time.delay(50)
        clock.tick(10)
        snakeGame.move()

        if snakeGame.body[0].position == snakeSnack.position:
            snackGame.addCube()
            snakeSnack = square(generateSnakeSnack(rows, snakeGame), color = (0, 255, 0))

        # if snake crashes into itself the game is over
        for x in range(len(snakeGame.body)):
            # check if the head of the snake is on top of any other position in the range of the snake body
            if snakeGame.body[x].position in list(map(lambda z: z.position, snackGamebody[x + 1:])):
                print('Score: ', len(snackGame.body))
                displayMessageBox('Game Over!', 'Play Again ... ')
                snakeGame.reset((10, 10))
                break;
        
        redrawWindow(game)  


# redraw game window after each iteration
def redrawWindow(game):
    global snakeGame, snakeSnack
    game.fill((0, 0, 0))
    snakeGame.draw(game)
    snakeSnack.draw(game)
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
def generateSnakeSnack(item):
    positions = item.body
    while True:
        xSnack = rand.randrange(rows)
        ySnack = rand.randrange(rows)
        # make sure the snack generated is not on the snake 
        if(len(list(filter(lambda z: z.position == (xSnack, ySnack), positions)))) > 0:
           continue
        else:
            break
    return (xSnack, ySnack)

main()
