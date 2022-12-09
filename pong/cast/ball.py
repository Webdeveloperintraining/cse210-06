from constants import *
import pygame

class Ball:
    """
    what we want from the ball is  x , y and the radius
    x = x-coordinate
    y = y-coordinate
    radius = radius of the ball
    x_vel = volocity in X
    y_vel = velocity in Y
    """
    
    MAX_VEL = 5

    def __init__(self, x, y, radius, color):
        """Constructs a new ball."""
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        self.color = color

    def draw(self, win):
         """Gets the window.
        
        Returns:
            help to draw the ball
        """
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        """help in the movement of the ball"""
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
