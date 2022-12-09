import pygame


WINNING_SCORE = 10

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7


WIDTH, HEIGHT = 700, 500


pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

pygame.display.set_caption("Pong")



