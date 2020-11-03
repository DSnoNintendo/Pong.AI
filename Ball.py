class Ball:
    def __init__(self, size, spawn_x, speed=None, color=None):
        self.size = size

        if color == None: self.color = (255,255,255)
        else: self.color = color

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
        self.x = spawn_x
        self.y = 0

    def BOUNCE_Y(self):
        self.change_y = self.change_y * -1

    def BOUNCE_X(self):
        self.change_x = self.change_x * -1

    def CORRECT_CEILING(self):
        self.y=0

    def CORRECT_FLOOR(self, screen):
        self.y = screen.height-self.size

    def CORRECT_WALL_L(self):
        self.x=0

    def CORRECT_WALL_R(self, screen):
        self.x = screen.width - self.size

    def TOUCHING_WALL_L(self):
        if self.x < 0: #return true if touching right or left side of screen
            return True
        else: return False

    def TOUCHING_WALL_R(self, screen):
        if self.x > screen.width - self.size: #return true if touching right or right side of screen
            return True
        else: return False

    def TOUCHING_CEILING(self):
        if self.y < 0: return True
        else: return False

    def TOUCHING_FLOOR(self, screen):
        if self.y > screen.height: return True
        else: return False

    def TOUCHING_PADDLE(self, paddle,gui):
        if self.x > paddle.x and self.x < paddle.x + paddle.width \
             and self.y == gui.height - paddle.height - self.size:
            return True
        else: return False

    def UPDATE(self):
        self.x += self.change_x
        self.y += self.change_y