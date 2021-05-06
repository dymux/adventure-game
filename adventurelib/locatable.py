import pygame
class Locatable:

    def __init__(self, x=0, y=0, w=0, h=0, roomXY = (0, 0)):
        self.mRect = pygame.Rect(x,y,w,h)
        self.mRoom = roomXY
        return

    def getRoom(self):
        return self.mRoom

    def setRoom(self, newTuple):
        self.mRoom = newTuple
		
    def getX(self):
        return self.mRect.x

    def getY(self):
        return self.mRect.y

    def getWidth(self):
        return self.mRect.w

    def getHeight(self):
        return self.mRect.h

    def getRect(self):
        return self.mRect

    def setX(self, x):
        self.mRect.x = x
        return

    def setY(self, y):
        self.mRect.y = y
        return

    def setWidth(self, width):
        self.mRect.w = width
        return

    def setHeight(self, height):
        self.mRect.h = height
        return

    def containsPoint(self, x, y):
        if( (x >= self.getX()) and
            (x <= self.getX() + self.getWidth()) and
            (y >= self.getY()) and
            (y <= self.getY() + self.getHeight()) ):
            return True
        return False

    def containsLocatable(self, other):
        ox1 = other.getX()
        ox2 = ox1 + other.getWidth()
        oy1 = other.getY()
        oy2 = oy1 + other.getHeight()
        opoints = [ (ox1,oy1), (ox1,oy2), (ox2,oy2), (ox2,oy1) ]
        for op in opoints:
            x, y = op
            if not self.containsPoint(x, y):
                return False
        return True

    def overlapWithLocatable(self, other):
        sx1 = self.getX()
        sx2 = sx1 + self.getWidth()
        sy1 = self.getY()
        sy2 = sy1 + self.getHeight()
        spoints = [ (sx1,sy1), (sx1,sy2), (sx2,sy2), (sx2,sy1) ]

        ox1 = other.getX()
        ox2 = ox1 + other.getWidth()
        oy1 = other.getY()
        oy2 = oy1 + other.getHeight()
        opoints = [ (ox1,oy1), (ox1,oy2), (ox2,oy2), (ox2,oy1) ]

        for sp in spoints:
            x, y = sp
            if other.containsPoint(x, y):
                return True

        for op in opoints:
            x, y = op
            if self.containsPoint(x, y):
                return True

        return False

    def hits(self, other):
        return False


    def __str__(self):
        s = "Locatable<"+str(self.mX)+","+str(self.mY)+","+str(self.mWidth)+","+str(self.mHeight)+">"
        return s

    def __repr__(self):
        return str(self)
