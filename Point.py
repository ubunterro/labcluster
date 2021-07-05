from math import sqrt

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init
        self.cluster = -1

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), "," , str(self.cluster), ")"])

    def distance(self, b):
        return sqrt((self.x - b.x) ** 2 + (self.y - b.y) ** 2)
