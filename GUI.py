import pygame

class GUI:
    def __init__(self, width, height, background=(120,0,0), name="pong.AI"):
        self.width = width
        self.height = height


        self.background = background


    def DRAW_BG(self, screen):
        screen.fill(self.background)

    def DRAW_PAD(self, paddle, screen):
        #if paddle is past left border
        if paddle.x <= 0:
            #reset position
            paddle.x = 0
        #if paddle is over right border
        if paddle.x >= self.width - 1 - paddle.width:
            paddle.x = self.width - 1 - paddle.width
        pygame.draw.rect(screen, paddle.color, [paddle.x, paddle.y, paddle.width, paddle.height])

    def DRAW_BALL(self, ball, paddle,screen):
        # this handles the movement of the ball.
        if ball.x < 0:  # make sure x doesn't go off board
            ball.x = 0
            ball.BOUNCE_X()  # switches + to negative and negative to positive

        elif ball.x > self.width - ball.size: #If ball goes off right of screen
            ball.x = self.width - ball.size
            ball.BOUNCE_X() # switch direction

        elif ball.y < 0: #if ball touches ceiling
            ball.y = 0
            ball.BOUNCE_Y()


        #If ball  touches paddle
        elif ball.x > paddle.x and ball.x < paddle.x + paddle.width \
                and ball.y == self.height-paddle.height-ball.size:
            ball.BOUNCE_Y()
            paddle.SCORE()

        elif ball.y > self.height: #If ball hits floor
            ball.BOUNCE_Y()
            paddle.score = 0
        pygame.draw.rect(screen, ball.color, [ball.x, ball.y, ball.width, ball.height])

    def UPDATE(self, paddle,screen, font):
        self.text = font.render("Score = " + str(paddle.score), True, (255,0,0))
        screen.blit(self.text, [self.width - self.width/4, self.height/6])
        #self.pygame.display.flip()