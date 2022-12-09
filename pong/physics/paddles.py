import pygame
from physics.movement import Movement
from constants import *

class PaddleMovement(Movement):
    '''
    Class in charge of making the paddles move and doing it at the right speed when a key is pressed.
    '''
    def __init__(self):
        super().__init__()
             
    def execute(self, keys, left_paddle, right_paddle):
        '''
        ARGS:
            keys: calling pygame module code to make that the paddles move with certain keys
            left_paddle: First player paddle
            right_paddle: Second player paddle
        '''
        if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
            left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
            left_paddle.move(up=False)

        if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
            right_paddle.move(up=False)