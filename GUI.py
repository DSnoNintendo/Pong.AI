import pygame

class GUI:
    def __init__(self, width, height, background=None):
        self.width = width
        self.height = height

        if background == None: self.background=(120,0,0)
        else: self.background = background

        self.high_score = 0


    def DRAW_BG(self, screen):
        screen.fill(self.background)


    def REDRAW(self, ball, paddle,screen):
        pygame.draw.rect(screen, ball.color, [ball.x, ball.y, ball.width, ball.height])
        pygame.draw.rect(screen, paddle.color, [paddle.x, paddle.y, paddle.width, paddle.height])


    def REDRAW2(self, balls, paddles,screen):
        for x, ball in enumerate(balls):
            pygame.draw.rect(screen, ball.color, [ball.x, ball.y, ball.width, ball.height])
            pygame.draw.rect(screen, paddles[x].color, [paddles[x].x, paddles[x].y, paddles[x].width, paddles[x].height])

    def UPDATE_SCORE(self, score,screen, font):
        self.text = font.render("Score = " + str(score), True, (255,0,0))
        screen.blit(self.text, [self.width - self.width/4, self.height/6])

        if score > self.high_score:
            self.high_score = score
        self.text = font.render("High Score = " + str(self.high_score), True, (255, 0, 0))
        screen.blit(self.text, [self.width - self.width / 4, self.height / 4])