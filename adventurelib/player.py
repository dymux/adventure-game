from adventurelib.movable import Movable
from adventurelib.movable import Locatable
import pygame

class Sword(Movable):
	def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, hg=0, vg=0,facing ="", roomXY = (0, 0)):
		Movable.__init__(self, x, y, w, h, dx, dy, s,facing, roomXY)
		self.mRoomXY = roomXY
	def getRoomXY(self):
		return self.mRoomXY

	def setRoomXY(self, newTuple ):
		self.mRoomXY = newTuple

	def getFacing(self):
		return self.mFacing

	def getRect(self):
		return self.mRect

	def draw(self, surface ):
		Color = (50,50,50)
		rect = pygame.Rect(self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h )
		pygame.draw.rect(surface,Color,rect,0)

class Player(Movable):

	def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, hg=0, vg=0,facing ="", roomXY = (0, 0)):
		Movable.__init__(self, x, y, w, h, dx, dy, s,facing, roomXY)
		self.mHorizontalGap = hg
		self.mVerticalGap = vg
		self.mRoomXY = roomXY
		self.mFacing = facing
		self.mInventory = []
		self.mHealth = 100
		self.mWidth = w
		self.mHeight = h
		return

	def getHealth(self):
		return self.mHealth

	def looseHealth( self, healthLost ):
		if healthLost < 0:
			return
		if self.mHealth - healthLost <= 0:
			self.mHealth = 0
			return
		self.mHealth -= healthLost
		return

	def getRoomXY(self):
		return self.mRoomXY

	def getFacing(self):
		return self.mFacing

	def getRect(self):
		return (self.mX,self.mY,self.mWidth,self.mHeight)

	def getHorizontalGap(self):
		return self.mHorizontalGap

	def getVerticalGap(self):
		return self.mVerticalGap

	def setHorizontalGap(self, hg):
		self.mHorizontalGap = hg
		return

	def setVerticalGap(self, vg):
		self.mVerticalGap = vg
		return

	def setRoomXY( self, newGridTuple ):
		self.mRoomXY = newGridTuple

	def outOfBounds(self, screen_width, screen_height):
		if self.getX() < 0:
			return True
		if self.getX() + self.getWidth() > screen_width:
			return True
		if self.getY() < 0:
			return True
		if self.getY() + self.getHeight() > screen_height:
			return True
		return False

	def move(self, dx, dy):
		# Move each axis separately.
		if dx != 0:
			self.move_single_axis(dx, 0)
		else:
			self.move_single_axis(0, dy)

	def move_single_axis(self, dx, dy):

		# Move the rect
		self.mRect.x += dx
		self.mRect.y += dy
		self.mDx = dx
		self.mDy = dy

	def attack(self):
		swordWidth = self.mRect.w/2
		swordHeight = self.mRect.h/3
		if self.getFacing() == "right":
			sword = Sword( self.mRect.x + self.mRect.w , self.mRect.y + (self.mRect.h/2.75) ,swordWidth, swordHeight, 0, 0, 0, 0, 0,self.mFacing, self.mRoomXY)
		elif self.getFacing() == "left":
			sword = Sword( self.mRect.x - (self.mRect.w/2)  , (self.mRect.y + (self.mRect.h/2.75)) ,swordWidth, swordHeight, 0, 0, 0, 0, 0,self.mFacing, self.mRoomXY)
		elif self.getFacing() == "up":
			sword = Sword( self.mRect.x + (self.mRect.w/2.75) , self.mRect.y - self.mRect.h/2 , swordHeight,swordWidth, 0, 0, 0, 0, 0,self.mFacing, self.mRoomXY)
		elif self.getFacing() == "down":
			sword = Sword( self.mRect.x + (self.mRect.w/2.75) , self.mRect.y + self.mRect.h , swordHeight,swordWidth, 0, 0, 0, 0, 0,self.mFacing, self.mRoomXY)
		else:
			sword = Sword( self.mRect.x + self.mRect.w , self.mRect.y + (self.mRect.h/2.75) ,swordWidth, self.mRect.h/3, 0, 0, 0, 0, 0,self.mFacing, self.mRoomXY)

		return sword

	def endAttack(self):
		w = 0
		h = 0
		x = -100
		y= -100
		sword = Sword( x , y,w, h, 0, 0, 0, 0, 0,self.mFacing, self.mRoomXY)
		return sword

	def up(self):
		self.move(0,-1 * self.mSpeed)
		self.mFacing = "up"

	def down(self):
		self.move(0,self.mSpeed)
		self.mFacing = "down"

	def left(self):
		self.move(-1 * self.mSpeed,0)
		self.mFacing = "left"

	def right(self):
		self.move(self.mSpeed,0)
		self.mFacing = "right"

	def draw(self, surface ):
		Color = (50,50,50)
		rect = pygame.Rect(self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h )
		pygame.draw.rect(surface,Color,rect,0)

	def __str__(self):
		s = "Player<"+Movable.__str__(self)+","+str(self.mHorizontalGap)+","+str(self.mVerticalGap)+">"
		return s

	def __repr__(self):
		return str(self)
