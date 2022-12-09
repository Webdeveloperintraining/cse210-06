
import pygame

from constants import *

class Animate:
    
    
    def draw(self, win, paddles, ball, left_score, right_score):
        win.fill(BLACK)

        left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
        right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
        win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
        win.blit(right_score_text, (WIDTH * (3/4) -
                                    right_score_text.get_width()//2, 20))

        for paddle in paddles:
            paddle.draw(win)

        for i in range(10, HEIGHT, HEIGHT//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

        ball.draw(win)
        pygame.display.update()