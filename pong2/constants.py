import pygame

'''
constants vars that are used through out files
'''

# score needed to win
WINNING_SCORE = 10

# clock speed
FPS = 60

# colors used in game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# paddle and ball size
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# screen width and height
WIDTH, HEIGHT = 700, 500


# initalizes pygame
pygame.init()

# creates the pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# creates the font used by the game
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

pygame.display.set_caption("Pong")



