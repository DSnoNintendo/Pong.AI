from GUI import GUI
from Paddle import Paddle
from Ball import Ball
import random
import pygame


pygame.init()

#Fixes freeze when both direction keys are pressed
pygame.key.set_repeat(10,10)

GAME_SPEED = 6
SCORE_FONT = pygame.font.SysFont('Calibri', 15, False, False)

#Initializing the display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
gui = GUI(SCREEN_WIDTH, SCREEN_HEIGHT)

size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong.AI")

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_START_X = SCREEN_WIDTH/2
PADDLE_START_Y = SCREEN_HEIGHT - PADDLE_HEIGHT
PADDLE_SPEED = 6
pad = Paddle(PADDLE_WIDTH,PADDLE_HEIGHT, PADDLE_START_X,PADDLE_START_Y, speed=PADDLE_SPEED)

BALL_START_X = random.randrange(5,SCREEN_WIDTH-10,5)
BALL_SIZE = 15
BALL_SPEED = PADDLE_SPEED-1
ball = Ball(BALL_SIZE, BALL_START_X,speed=BALL_SPEED)

# game's main loop
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:  # PADDLE MOVEMENT
            if event.key == pygame.K_LEFT:
                pad.MOVE_LEFT()
            elif event.key == pygame.K_RIGHT:
                pad.MOVE_RIGHT()

        # PADDLE WILL MOVE UNTIL KEY IS RAISED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pad.STOP()

    gui.DRAW_BG(screen)
    #screen.fill(BLACK)

    pad.UPDATE()
    #paddle.x += pad_change_x

    ball.UPDATE()
    #ball_x += ball_change_x
    #ball_y += ball_change_y

    gui.DRAW_PAD(pad, screen)
    # drawpad(screen, paddle.x, paddle.y)

    gui.DRAW_BALL(ball,pad, screen)




    """"
    # score board
    font = pygame.font.SysFont('Calibri', 15, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text, [600, 100])
    """
    gui.UPDATE(pad, screen, SCORE_FONT)

    pygame.display.flip()
    clock.tick(GAME_SPEED * 10)

pygame.quit()
