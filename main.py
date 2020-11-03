from GUI import GUI
from Paddle import Paddle
from Ball import Ball
import random
import pygame
import neat
import os
from pygame.locals import *
import math







def main(genomes,config):
    colors = [(255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0), (255, 100, 10), (255, 255, 0),
              (0, 255, 170), (115, 0, 0), (180, 255, 100), (255, 100, 180),
              (240, 0, 255), (127, 127, 127), (255, 0, 230), (100, 40, 0), (0, 50, 0), (0, 0, 100), (210, 150, 75),
              (255, 200, 0), (255, 255, 100), (0, 255, 255), (200, 200, 200),
              (50, 50, 50), (230, 220, 170), (200, 190, 140), (235, 245, 255)]

    pygame.init()

    # Fixes freeze when both direction keys are pressed
    # pygame.key.set_repeat(10, 10)

    GAME_SPEED = 6
    SCORE_FONT = pygame.font.SysFont('Calibri', 15, False, False)


    nets = []  # neural networds
    ge = []  # genomes
    pads = []  # paddles
    balls = []  # balls

    high_score =0

    for _, g in genomes:
        color = random.choice(colors)
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        pads.append(Paddle(100, 20, SCREEN_WIDTH/2, SCREEN_HEIGHT, color=color))
        balls.append(Ball(15, random.randrange(5, SCREEN_WIDTH - 10, 5), color=color))

        g.fitness = 0
        ge.append(g)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

        #if all paddles have lost
        if len(pads) == 0: break


        for x, pad in enumerate(pads):


            pads[x].UPDATE() #update position variables
            balls[x].UPDATE() #update position variables

            output = nets[x].activate( ( pads[x].GET_CENTER(), pads[x].GET_DIST_FROM_CENTER(balls[x]), pads[x].GET_DIST_FROM_LEFT(balls[x]), pads[x].GET_DIST_FROM_RIGHT(balls[x])  ) )
            i = output[0]

            if i >0 :
                pad.MOVE_LEFT()
            elif i < 0:
                pad.MOVE_RIGHT()
            else:
                pad.STOP()


            # if ball touches floor remove ball and paddle from list
            if balls[x].TOUCHING_FLOOR(gui):
                ge[x].fitness -= 5
                pads[x].score = 0
                #balls[x].BOUNCE_Y()
                ge.pop(x)
                nets.pop(x)
                balls.pop(x)
                pads.pop(x)
                continue

            # If ball touching paddle add to fitness and score
            elif balls[x].TOUCHING_PADDLE(pads[x], gui):
                ge[x].fitness+=10
                pads[x].SCORE() #add point
                balls[x].BOUNCE_Y()
                #set new high score
                if pads[x].score > high_score: high_score = pads[x].score

            elif balls[x].TOUCHING_WALL_L():
                balls[x].CORRECT_WALL_L()
                balls[x].BOUNCE_X()


            elif balls[x].TOUCHING_WALL_R(gui):

                balls[x].CORRECT_WALL_R(gui)
                balls[x].BOUNCE_X()

            elif balls[x].TOUCHING_CEILING():
                balls[x].CORRECT_CEILING()
                balls[x].BOUNCE_Y()

            if pads[x].TOUCHING_WALL_L():
                #discourage genome from touching wall
                ge[x].fitness -= .1
                pads[x].CORRECT_WALL_L()


            if pads[x].TOUCHING_WALL_R(gui):
                pads[x].CORRECT_WALL_R(gui)


            #gui.REDRAW(balls[x], pads[x], screen)

        gui.DRAW_BG(screen)

        gui.REDRAW2(balls, pads, screen)

        gui.UPDATE_SCORE(high_score, screen, SCORE_FONT)

        pygame.display.flip()

        clock.tick(GAME_SPEED * 10)




def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 1000)


if __name__ == "__main__":
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    gui = GUI(SCREEN_WIDTH, SCREEN_HEIGHT)

    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    flags = DOUBLEBUF
    screen = pygame.display.set_mode(size, flags)

    pygame.display.set_caption("pong.AI")

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "AI/config-feedforward.txt")
    run(config_path)

