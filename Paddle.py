class Paddle:
    def __init__(self, width, height, x,y, speed=None,color= (255,0,0)):
        # paddle dimensions
        self.width = width
        self.height = height

        #Control where paddle will move when keys pressed
        self.change_x = 0
        self.change_y = 0

        #Actual position of paddle
        self.x = x
        self.y = y

        if speed == None: self.speed = 6
        else: self.speed = speed
        self.color = color
        self.score = 0

        self.LOST = False

    def MOVE_LEFT(self):
        self.change_x = 0-self.speed

    def MOVE_RIGHT(self):
        self.change_x = self.speed

    def STOP(self):
        self.change_x = 0

    def SCORE(self):
        self.score += 1

    def UPDATE(self):
        self.x += self.change_x

