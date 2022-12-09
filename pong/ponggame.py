import pygame
from constants import *
from cast.ball import Ball
from cast.paddle import Paddle

from physics.collision import Collide
from physics.paddles import PaddleMovement

from animate.animate import Animate


def main():
    '''
    The main function to run pong
    args: none
    return: none
    '''
    run = True
    clock = pygame.time.Clock()

    # creates paddles for left side and right side
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT, RED)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, BLUE)
    
    # creates the ball for the game
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, ORANGE)
    
    # creates instances of Collide(), PaddleMovement() and Animate() to run the game
    handle_collision = Collide()
    handle_paddle_movement = PaddleMovement()
    draw = Animate()

    # user scores
    left_score = 0
    right_score = 0

    # runs the game continuosly
    while run:
        # sets clock speed
        clock.tick(FPS)
        
        # redraws the window
        draw.draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        # checks for if user quits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # gets keys pressed and moves the paddles accordingly 
        keys = pygame.key.get_pressed()
        handle_paddle_movement.execute(keys, left_paddle, right_paddle)

        # moves the ball and handles the collision
        ball.move()
        handle_collision.execute(ball, left_paddle, right_paddle)

        # checks if a player has scored
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        # checks if a player has won
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        # displays who won if someone won
        # then restarts the game after 5 sec
        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0


    # quits the game
    pygame.quit()


if __name__ == '__main__':
    main()