
import pygame

from constants import *

class Animate:
    '''
    class in charge of animating the game
    '''
    
    
    def draw(self, win, paddles, ball, left_score, right_score):
        
        '''
        updates the screen for players
        
        args:
            self: reference to class
            win: main pygame window
            paddles: are players paddles
            ball: is the ball
            left_score: left players score
            rigth_score: right players score
            
        return: 
            none
        '''
        
        win.fill(BLACK)

        # renders text on screen
        left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
        right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
        win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
        win.blit(right_score_text, (WIDTH * (3/4) -
                                    right_score_text.get_width()//2, 20))

        # draws the paddles
        for paddle in paddles:
            paddle.draw(win)

        # draws the center line
        for i in range(10, HEIGHT, HEIGHT//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

        # draws the ball
        ball.draw(win)
        
        # updates the display
        pygame.display.update()