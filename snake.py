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
red = (255, 0, 0)
blue = (0, 0, 55)

class Snake:
    def __init__(self):
        self.color = blue
        self.headX = random.randrange(0, width, pixels)
        self.headY = random.randrange(0, height, pixels)
        self.bodies = []
        self.bodyColor = 50
        self.state = "STOP" #STOP, UP, DOWN, RIGHT, LEFT

    def moveHead(self):
        if self.state == "UP":
            self.headY -= pixels
        if self.state == "DOWN":
            self.headY += pixels
        if self.state == "LEFT":
            self.headX -= pixels
        if self.state == "RIGHT":
            self.headX += pixels

    def moveBody(self):
        if len(self.bodies) > 0:
            for i in range(len(self.bodies) -1, -1, -1):
                if i == 0:
                    self.bodies[0].posX = self.headX
                    self.bodies[0].posY = self.headY
                else:
                    self.bodies[i].posX = self.bodies[i - 1].posX
                    self.bodies[i].posY = self.bodies[i - 1].posY

    def addBody(self):
        self.bodyColor += 10
        body = Body((0, 0, self.bodyColor), self.headX, self.headY)
        self.bodies.append(body)
                    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.headX, self.headY, pixels, pixels))
        if len(self.bodies) > 0:
            for body in self.bodies:
                body.draw(surface)

    def die(self):
        self.headX = random.randrange(0, width, pixels)
        self.headY = random.randrange(0, height, pixels)
        self.bodies = []
        self.bodyColor = 50
        self.state = "STOP"

class Body:
    def __init__(self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY
    
    def draw(self, surface):
        pygame.draw.rect( surface, self.color, (self.posX, self.posY, pixels, pixels))

class Apple:
    def __init__(self):
        self.color = red
        self.spawn()
    
    def spawn(self):
        self.posX = random.randrange(0, width, pixels)
        self.posY = random.randrange(0, height, pixels)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, pixels, pixels))

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

class Collision:
    def snake_clsn_apple(self, snake, apple):
        distance = math.sqrt(math.pow((snake.headX - apple.posX), 2) + math.pow((snake.headY - apple.posY), 2))
        return distance < pixels

    def snake_clsn_walls(self, snake):
        if snake.headX < 0 or snake.headX > width - pixels or snake.headY < 0 or snake.headY > height - pixels:
            return True
        return False
    def snake_clsn_body(self, snake):
        pass



def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

#Objects
    snake = Snake()
    apple = Apple()
    background = Background()
    collision = Collision()

    #Mainloop
    while True:
        background.draw(screen)
        snake.draw(screen)
        apple.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.state != "DOWN":
                        snake.state = "UP"
                if event.key == pygame.K_DOWN:
                    if snake.state != "UP":
                        snake.state = "DOWN"
                if event.key == pygame.K_LEFT:
                    if snake.state != "RIGHT":
                        snake.state = "LEFT"
                if event.key == pygame.K_RIGHT:
                    if snake.state != "LEFT":
                        snake.state = "RIGHT"

        if collision.snake_clsn_apple(snake, apple):
            apple.spawn()
            snake.addBody()
            #increase the score

        if collision.snake_clsn_walls(snake):
            #lose
            snake.die()
            apple.spawn()
            #reset score (score = 0)

        pygame.time.delay(115)
        
        #Movement
        snake.moveBody()
        snake.moveHead()

        pygame.display.update()        

main()