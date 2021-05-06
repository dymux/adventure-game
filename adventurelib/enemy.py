from adventurelib.movable import Movable
import pygame, random, time


class Enemy(Movable):

	def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, hg=0, vg=0, facing="", roomXY=(0, 0), health=0, damage=0, Color=(0, 0, 0),initalXY=(0,0)):
		Movable.__init__(self, x, y, w, h, dx, dy, s, facing, roomXY)
		self.mHorizontalGap = hg
		self.mVerticalGap = vg
		self.mRoomXY = roomXY
		self.mDamage = damage
		self.mHealth = health
		self.mColor = Color
		self.mTimer = 0
		self.mInitialXY = (x,y)
		return

	def getInitialXY(self):
		return self.mInitialXY

	def getDamage(self):
		return self.mDamage

	def getHealth(self):
		return self.mHealth

	def getColor(self):
		return self.mColor

	def getRoomXY(self):
		return self.mRoomXY

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

	def move_random(self):
		if self.mTimer % 7 == 0:
			direction = random.randint(1,4)
			if direction == 1:
				self.left()
			if direction == 2:
				self.up()
			if direction == 3:
				self.down()
			if direction == 4:
				self.right()
		self.mTimer += 1

	def move_follow(self, other):
		if self.mTimer % 5 == 0:
			if int(random.random()*2) == 0:
				if self.mRect.x < other.mRect.x:
					self.right()
				if self.mRect.x > other.mRect.x:
					self.left()
			else:
				if self.mRect.y > other.mRect.y:
					self.up()
				if self.mRect.y < other.mRect.y:
					self.down()
		self.mTimer += 1

	def draw(self, surface ):
		Color = self.getColor()
		rect = pygame.Rect(self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h )
		pygame.draw.rect(surface,Color,rect,0)

	def destroy(self):
		self.mHealth = 0
		self.mRect = pygame.Rect(0,0,0,0)
