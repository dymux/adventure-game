import sys
from adventurelib.locatable import Locatable
import pygame

class Movable(Locatable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0,facing="", roomXY = (0, 0)):
        Locatable.__init__(self, x, y, w, h, roomXY)
        self.mDx = dx
        self.mDy= dy
        self.mSpeed = s
        self.mFacing = "d"
        return

    def move(self):
        '''
        Every time that move() is called on a Movable object, if the
        desired position isn’t the same as the current position, the
        object will move up to speed pixels towards the desired position.
        '''
        if self.atDesiredLocation():
            return


        diffx = self.mDesiredX - self.mX
        diffy = self.mDesiredY - self.mY
        diff = abs(diffx) + abs(diffy)
        ratiox = float(diffx) / float(diff)
        ratioy = float(diffy) / float(diff)
        dx = int(ratiox * self.mSpeed)
        dy = int(ratioy * self.mSpeed)
        if abs(dx) > abs(diffx):
            dx = diffx
        if abs(dy) > abs(diffy):
            dy = diffy
        self.mX += dx
        self.mY += dy

        return

    def getDesiredX(self):
        return self.mDesiredX

    def getDesiredY(self):
        return self.mDesiredY

    def getSpeed(self):
        return self.mSpeed

    def getFacing(self):
        return self.mFacing

    def setDesiredX(self, dx):
        self.mDesiredX = dx
        return

    def setDesiredY(self, dy):
        self.mDesiredY = dy
        return

    def setSpeed(self, s):
        self.mSpeed = s
        return

    def atDesiredLocation(self):
        return self.mX == self.mDesiredX and self.mY == self.mDesiredY

    def outOfBounds(self, screen_width, screen_height):
        if self.getX() + self.getWidth() < 0:
            return True
        if self.getX() > screen_width:
            return True
        if self.getY() + self.getHeight() < 0:
            return True
        if self.getY() > screen_height:
            return True
        return False

    def __str__(self):
        s = "Movable<"+Locatable.__str__(self)+","+str(self.mDesiredX)+","+str(self.mDesiredY)+","+str(self.mSpeed)+">"
        return s

    def __repr__(self):
        return str(self)
