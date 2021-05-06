from adventurelib.immovable import Immovable
import pygame
class Door(Immovable):

	def __init__(self, x=0, y=0, w=0, h=0, roomXY = (0, 0), sharedRoomXY = (0 ,0) ):
		Immovable.__init__(self, x, y, w, h, roomXY)
		self.mRoomXY = roomXY
		self.mSharedRoomXY = sharedRoomXY
		self.mX = x
		self.mY = y
		self.mWidth = w
		self.mHeight = h

		return

	def getRoomXY(self):
		return self.mRoomXY

	def getSharedRoomXY(self):
		return self.mSharedRoomXY

	def draw( self, surface ):
		doorColor = ( 0, 0, 0 )
		rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight )
		pygame.draw.rect(surface,doorColor,rect,0)

class CollectableSword(Immovable):
	def __init__(self, x=0, y=0, w=0, h=0, roomXY = (0, 0), sharedRoomXY = (0 ,0) ):
		Immovable.__init__(self, x, y, w, h, roomXY)
		self.mRoomXY = roomXY
		self.mSharedRoomXY = sharedRoomXY
		self.mX = x
		self.mY = y
		self.mWidth = w
		self.mHeight = h

		return

	def getRoomXY(self):
		return self.mRoomXY

	def getSharedRoomXY(self):
		return self.mSharedRoomXY

	def draw( self, surface ):
		color = ( 140, 0, 0 )
		rect = pygame.Rect(self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h )
		pygame.draw.rect(surface,color,rect,0)

	def destroy(self):
		self.mRect = pygame.Rect(0,0,0,0)

class Water(Immovable):

	def __init__(self, x=0, y=0, w=0, h=0, roomXY = (0, 0), sharedRoomXY = (0 ,0) ):
		Immovable.__init__(self, x, y, w, h, roomXY)
		self.mRoomXY = roomXY
		self.mSharedRoomXY = sharedRoomXY
		self.mX = x
		self.mY = y
		self.mWidth = w
		self.mHeight = h

		return

	def getRoomXY(self):
		return self.mRoomXY

	def getSharedRoomXY(self):
		return self.mSharedRoomXY

	def draw( self, surface ):
		color = ( 0, 0, 140)
		rect = pygame.Rect(self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h )
		pygame.draw.rect(surface,color,rect,0)


class Lava(Water):

	def __init__(self, x=0, y=0, w=0, h=0, roomXY = (0, 0) ):
		Immovable.__init__(self, x, y, w, h, roomXY)
		self.mRoomXY = roomXY
		self.mX = x
		self.mY = y
		self.mWidth = w
		self.mHeight = h

		return

	def draw( self, surface ):
		color = ( 200, 21, 13)
		rect = pygame.Rect( self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h)
		pygame.draw.rect(surface,color,rect,0)

class Floor(Immovable):

	def __init__( self, x = 0, y = 0, w = 0, h = 0, roomXY = (0, 0), color = (0,0,0)):
		Immovable.__init__(self, x, y, w, h, roomXY)	
		self.mRoomXY = roomXY
		self.mX = x
		self.mY = y
		self.mWidth = w
		self.mHeight = h
		self.mColor = color
		
		return

	def draw(self, surface):
		rect = pygame.Rect(self.mRect.x, self.mRect.y, self.mRect.w, self.mRect.h )
		pygame.draw.rect(surface,self.mColor,rect,0)

	def getRoomXY(self):
		return self.mRoomXY