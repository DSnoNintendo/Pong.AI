class Ball:
    def __init__(self, size, start_x, speed=None, color=(255, 255, 255)):
        self.size = size

        self.color=color

        self.width = size
        self.height = size

        # speed of the ball
        if (speed == None):
            self.change_x = 5
            self.change_y = 5
        else:
            self.change_x = speed
            self.change_y = speed

        # initial position of the ball
        self.x = start_x
        self.y = 0

    def BOUNCE_Y(self):
        self.change_y = self.change_y * -1

    def BOUNCE_X(self):
        self.change_x = self.change_x * -1

    def UPDATE(self):
        self.x += self.change_x
        self.y += self.change_y