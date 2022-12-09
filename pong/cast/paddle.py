from constants import *
import pygame

class Paddle:

    '''
    what we want from the paddle is  x , y , width and height
    we will change x and y base on the movement of the paddle 
        x = X-coordinate
        y = Y-coordinate
        width = width of the rectangle
        height = height of the rectangle
    '''
    VEL = 4

    def __init__(self, x, y, width, height, color):
        """Constructs a new Paddle."""
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        """
        gets the window 
        returns:
        draw the rectangle. 
        """
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        """
        gets tru or falso 
        returns:
        help in the movement of the paddle 
        """
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
