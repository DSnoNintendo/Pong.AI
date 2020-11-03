import math
class Paddle:
    def __init__(self, width, height, x,y, speed=None,color= None):
        # paddle dimensions
        self.width = width
        self.height = height

        #Control where paddle will move when keys pressed
        self.change_x = 0
        self.change_y = 0

        #Actual position of paddle
        self.x = x
        self.y = y - self.height

        if speed == None: self.speed = 6
        else: self.speed = speed
        if color == None: self.color = (255,0,0)
        else: self.color = color
        self.score = 0
        self.high_score = 0

        self.LOST = False

    def GET_CENTER(self):
        return self.x - self.width / 2

    def GET_RIGHT(self):
        return self.x + self.width - 5

    def GET_LEFT(self):
        return self.x + 5

    def GET_DIST_FROM_LEFT(self, ball):
        return math.sqrt(((ball.x - self.GET_LEFT()) ** 2) + ((ball.y - self.y) ** 2))

    def GET_DIST_FROM_RIGHT(self, ball):
        return math.sqrt(((ball.x - self.GET_RIGHT()) ** 2) + ((ball.y - self.y) ** 2))

    def GET_DIST_FROM_CENTER(self, ball):
        return math.sqrt(((ball.x - self.GET_CENTER()) ** 2) + ((ball.y - self.y) ** 2))

    def MOVE_LEFT(self):
        self.change_x = 0-self.speed

    def MOVE_RIGHT(self):
        self.change_x = self.speed

    def STOP(self):
        self.change_x = 0

    def TOUCHING_WALL_L(self):
        # if paddle is past left border
        if self.x <= 0:
            return True
        else: return False

    def TOUCHING_WALL_R(self, screen):
        # if paddle is over right border
        if self.x >= screen.width - 1 - self.width:
            return True
        else : return False

    def CORRECT_WALL_L(self):
        self.x = 0

    def CORRECT_WALL_R(self, screen):
        self.x = screen.width - 1 - self.width

    def SCORE(self):
        self.score += 1

    def UPDATE(self):
        self.x += self.change_x
        self.change_x = 0


