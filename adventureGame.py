import pygame
import adventurelib
from adventurelib import player
from adventurelib import enemy
from adventurelib import objects
import sys

class AdventureGame:

    def __init__( self, width, height, grid_size ):
        self.mGameOver = False
        self.mWidth = width
        self.mHeight = height

        self.mGridSize = grid_size
        self.mObjectSize = int(self.mGridSize)
        self.mObjectGap = int((self.mGridSize - self.mObjectSize)/2)
        self.mPlayerDead = False
        self.mPlayerWin = False
        self.mOutOfBounds = False

        #Contains all objects within the game
        self.mObjects = []
        #contains only the objects that are in the same room as the player
        self.mActiveObjects = []
        #contains all enemies in game
        self.mEnemies = []
        self.mActiveEnemies = []


        #Player
        w = self.mObjectSize
        h = self.mObjectSize
        x = int(self.mWidth / 2 - w / 2)
        y= int(self.mHeight / 2 - w / 2)
        speed = 5
        horizontal_gap = 15
        vertical_gap = 15
        self.mPlayerColor = (140,140,140)
        self.mPlayer = adventurelib.player.Player(x,y,w,h,x,y,speed,horizontal_gap,vertical_gap,(0,0))

        # Test Enemy
        '''w = self.mObjectSize
        h = self.mObjectSize
        x = int(self.mWidth / 2 - w / 2) + 100
        y= int(self.mHeight / 2 - w / 2) + 100
        speed = 7
        horizontal_gap = 15
        vertical_gap = 15
        self.mEnemy = adventurelib.enemy.Enemy(x,y,w,h,x,y,speed,horizontal_gap,vertical_gap,(0,0),100,100,(150,0,0))
        self.mEnemyl = []
        self.mEnemyl.append(self.mEnemy)
        self.mObjects.append(self.mEnemyl)'''

        # Room (0,1)

        self.mFloor_room_1_0 = adventurelib.objects.Floor( 0, 0, self.mWidth, self.mHeight, (1,0), (255, 255, 255))
        self.mFloors = [self.mFloor_room_1_0]
        self.mObjects.append( self.mFloors)

        self.mWater_List = []
        WaterColor = (32,16,207)

        self.mWater_object1_room_1_0 = adventurelib.objects.Water( 0, self.mHeight - self.mObjectSize, self.mObjectSize * 10, self.mObjectSize, ( 1,0 ) )
        self.mWater_object2_room_1_0 = adventurelib.objects.Water( 3 * self.mObjectSize, 3 * self.mObjectSize, 3 * self.mObjectSize, 2 * self.mObjectSize,( 1,0 )  )

        self.mWater_List.append( self.mWater_object2_room_1_0 )
        self.mWater_List.append( self.mWater_object1_room_1_0 )
        self.mObjects.append(self.mWater_List)

        w = self.mObjectSize/2
        h = self.mObjectSize/2
        x = int(self.mWidth / 2 - w / 2) + 100
        y= int(self.mHeight / 2 - w / 2) + 100
        speed = 10
        horizontal_gap = 15
        vertical_gap = 15

        self.mEnemy_1_room_1_0 = adventurelib.enemy.Enemy( x, y, w, h, x, y, speed, horizontal_gap, vertical_gap, None, (1,0), 100, 100, (1,10,231))
        self.mEnemy_2_room_1_0 = adventurelib.enemy.Enemy( x-250, y-300, w, h, x, y, speed, horizontal_gap, vertical_gap, None, (1,0), 100, 100, (1,10,231))

        self.mEnemiesRoom_1_0 = []
        #add enemies to list of enemies for room
        self.mEnemiesRoom_1_0.append(self.mEnemy_1_room_1_0)
        self.mEnemiesRoom_1_0.append(self.mEnemy_2_room_1_0)

        #add the list of enemies for this room to master list
        self.mEnemies.append(self.mEnemiesRoom_1_0)

        # Room (1,1)

        # Floor is appended to list first to ensure it is bottom layer being drawn
        self.mFloor_room_1_1 = adventurelib.objects.Floor( 0, 0, self.mWidth, self.mHeight, (1,1), (63, 64, 66))
        self.mFloors = [self.mFloor_room_1_1]
        self.mObjects.append( self.mFloors)

        self.mLava_List = []
        LavaOutline = [ (0,0), (0,self.mHeight - 100), (200, self.mHeight - 100), (200, self.mHeight - 255), (105, self.mHeight - 255), (105,0)]
        LavaColor = (207,16,32)

        self.mLava_object1_room_1_1 = adventurelib.objects.Lava( 0, 0, self.mWidth/4, self.mHeight/2.3, ( 1, 1 ) )
        self.mLava_object2_room_1_1 = adventurelib.objects.Lava( 0, self.mHeight/2.3, self.mWidth/3 , self.mHeight/3.3,( 1, 1 )  )

        self.mLava_List.append( self.mLava_object2_room_1_1 )
        self.mLava_List.append( self.mLava_object1_room_1_1 )
        self.mObjects.append(self.mLava_List)

        w = self.mObjectSize
        h = self.mObjectSize
        x = int(self.mWidth / 2 - w / 2) + 100
        y= int(self.mHeight / 2 - w / 2) + 100
        speed = 10
        horizontal_gap = 15
        vertical_gap = 15

        self.mEnemiesRoom1_1 = []

        self.mEnemy_room1_1 = adventurelib.enemy.Enemy( x, y, w, h, x, y, speed, horizontal_gap, vertical_gap, None, (1,1), 100, 100, (231,10,1))
        #add enemies to list of enemies for room
        self.mEnemiesRoom1_1.append(self.mEnemy_room1_1)
        #add the list of enemies for this room to master list
        self.mEnemies.append(self.mEnemiesRoom1_1)


        #Collectable Sword
        w = self.mObjectSize/2
        h = self.mObjectSize
        x = 150
        y = 150
        room = (0,0)
        sharedRoom = (0,0)
        self.mCSword = adventurelib.objects.CollectableSword(x,y,w,h,room,sharedRoom)
        self.mCSwordlist = []
        self.mCSwordlist.append(self.mCSword)
        self.mObjects.append( self.mCSwordlist )
        self.mActiveObjects.append(self.mCSwordlist)
        #self.mObjects.append(self.mCSword)

        #sword
        w = self.mObjectSize/2
        h = self.mObjectSize/3
        x = -100
        y= -100
        speed = 5
        horizontal_gap = 15
        vertical_gap = 15
        self.mSword = adventurelib.player.Sword(x,y,w,h,x,y,speed,horizontal_gap,vertical_gap,(0,0))
        self.mSwordl = []
        self.mSwordl.append(self.mSword)
        self.mObjects.append(self.mSwordl)
        #self.mObjects.append(self.mSword)


        #Water
        self.mWaters = []
        self.mActiveWaters = []
        w = self.mObjectSize * 12
        h = self.mObjectSize
        x = int(0)
        y = int(0)
        waterObj = adventurelib.objects.Water(x,y,w,h,(0, 0),(0, 0))
        self.mWaters.append(waterObj)
        self.mActiveObjects.append(waterObj)

        w = self.mObjectSize * 12
        h = self.mObjectSize
        x = int(0)
        y = self.mWidth - self.mObjectSize
        waterObj = adventurelib.objects.Water(x,y,w,h,(0, 0),(0, 0))
        self.mWaters.append(waterObj)
        self.mActiveObjects.append(waterObj)

        w = self.mObjectSize * 2
        h = self.mObjectSize *9
        x = int(0)
        y = int(self.mObjectSize)
        waterObj = adventurelib.objects.Water(x,y,w,h,(0, 0),(0, 0))
        self.mWaters.append(waterObj)
        self.mActiveObjects.append(waterObj)

        self.mObjects.append( self.mWaters )


        #Doors
        self.mDoors = []
        self.mActiveDoors = []
        VerticleDoorHeight = self.mHeight #45 #52 is the largest functional number here
        VerticleDoorWidth = 3 #5
        HorizontalDoorHeight = 3 #5
        HorizontalDoorWidth = self.mWidth #45

        self.mDoor0 = adventurelib.objects.Door( self.mWidth - VerticleDoorWidth , 0, VerticleDoorWidth, VerticleDoorHeight, (0, 0), (1, 0))
        self.mDoor0Invert = adventurelib.objects.Door( 0 , self.mHeight/2 - (VerticleDoorHeight / 2), VerticleDoorWidth, VerticleDoorHeight, (1, 0), (0, 0))

        self.mDoor1 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorWidth, HorizontalDoorHeight, (1, 0), (1, 1) )
        self.mDoor1Invert = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight) , HorizontalDoorWidth, HorizontalDoorHeight, (1, 1), (1, 0))

        self.mDoor2 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorHeight, HorizontalDoorWidth, (2, 0), (2, 1) )
        self.mDoor2Invert = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight), HorizontalDoorHeight, HorizontalDoorWidth, (2, 1), (2, 0))

        self.mDoor3 = adventurelib.objects.Door( 0 , (self.mHeight/2) - (VerticleDoorHeight / 2 ), VerticleDoorWidth, VerticleDoorHeight, (2, 1), (1, 1) )
        self.mDoor3Invert = adventurelib.objects.Door(  self.mWidth - VerticleDoorWidth , (self.mHeight/2) - (VerticleDoorHeight / 2 ), VerticleDoorWidth, VerticleDoorHeight, (1, 1), (2, 1))

        self.mDoor4 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2), 0, HorizontalDoorWidth, HorizontalDoorHeight, (2, 1), (2, 2) )
        self.mDoor4Invert = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2), (self.mHeight - HorizontalDoorHeight), HorizontalDoorWidth, HorizontalDoorHeight, (2, 2), (2, 1))

        self.mDoor5 = adventurelib.objects.Door( 0 , self.mHeight/2 - (VerticleDoorHeight / 2), VerticleDoorWidth, VerticleDoorHeight, (2, 2), (1, 2) )
        self.mDoor5Invert = adventurelib.objects.Door( self.mWidth - VerticleDoorWidth , (self.mHeight/2) - (VerticleDoorHeight / 2 ), VerticleDoorWidth, VerticleDoorHeight, (1, 2), (2, 2))

        self.mDoor6 = adventurelib.objects.Door(0 , (self.mHeight/2) - (VerticleDoorHeight / 2 ), VerticleDoorWidth, VerticleDoorHeight, (1, 2), (0, 2) )
        self.mDoor6Invert = adventurelib.objects.Door( self.mWidth - VerticleDoorWidth , (self.mHeight/2) - (VerticleDoorHeight / 2 ), VerticleDoorWidth, VerticleDoorHeight, (0, 2), (1, 2))


        self.mDoor7 = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight) , HorizontalDoorWidth, HorizontalDoorHeight, (0, 2), (0, 1) )
        self.mDoor7Invert = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorWidth, HorizontalDoorHeight, (0, 1), (0, 2))


        '''
        adds the first accesible door to the ActiveDoor list
        the rest that are unaccesible are added to the doors list
        '''
        self.mActiveDoors.append(self.mDoor0)

        self.mDoors.append(self.mDoor0)
        self.mDoors.append(self.mDoor0Invert)
        self.mDoors.append(self.mDoor1)
        self.mDoors.append(self.mDoor1Invert)
        self.mDoors.append(self.mDoor2)
        self.mDoors.append(self.mDoor2Invert)
        self.mDoors.append(self.mDoor3)
        self.mDoors.append(self.mDoor3Invert)
        self.mDoors.append(self.mDoor4)
        self.mDoors.append(self.mDoor4Invert)
        self.mDoors.append(self.mDoor5)
        self.mDoors.append(self.mDoor5Invert)
        self.mDoors.append(self.mDoor6)
        self.mDoors.append(self.mDoor6Invert)
        self.mDoors.append(self.mDoor7)
        self.mDoors.append(self.mDoor7Invert)

        self.mObjects.append(self.mDoors)

    def actOnPressJ(self):
        print("Sword X: " +str( self.mSword.getX()))
        print("Sword Y: " +str( self.mSword.getY()))

    def actOnPressA( self ):
        if "Sword" in self.mPlayer.mInventory:
            self.mSword = self.mPlayer.attack()
        return

    def actOnANotPressed(self):
        self.mSword = self.mPlayer.endAttack()
        return

    def actOnHoldA( self ):
        return

    def actOnPressUP( self ):
        self.mPlayer.up()
        return

    def actOnPressDOWN( self ):
        self.mPlayer.down()
        return

    def actOnPressLEFT( self ):
        self.mPlayer.left()
        return

    def actOnPressRIGHT( self ):
        self.mPlayer.right()
        return

    def actOnLeftClick( self, x, y ):
        return

    # Loop through active objects and process collisions based on class
    def checkCollisions(self):
        for obj in self.mActiveObjects:

            # Water
            if isinstance(obj, adventurelib.objects.Water):
                # If you collide with water, move out based on velocity
                if self.mPlayer.mRect.colliderect(obj.mRect):
                    #checks if the water object is really lava
                    self.check_player_hits_lava(obj)
                    if self.mPlayer.mDx > 0: # Moving right; Hit the left side of the obj
                        self.mPlayer.mRect.right = obj.mRect.left
                    if self.mPlayer.mDx < 0: # Moving left; Hit the right side of the obj
                        self.mPlayer.mRect.left = obj.mRect.right
                    if self.mPlayer.mDy > 0: # Moving down; Hit the top side of the obj
                        self.mPlayer.mRect.bottom = obj.mRect.top
                    if self.mPlayer.mDy < 0: # Moving up; Hit the bottom side of the obj
                        self.mPlayer.mRect.top = obj.mRect.bottom

                # Test Enemy Collide with water
                for enemys in self.mEnemies:
                    for enemy in enemys:
                        if enemy.getHealth() > 0:
                            if enemy.mRect.colliderect(obj.mRect):
                                if enemy.mDx > 0: # Moving right; Hit the left side of the obj
                                    enemy.mRect.right = obj.mRect.left
                                if enemy.mDx < 0: # Moving left; Hit the right side of the obj
                                    enemy.mRect.left = obj.mRect.right
                                if enemy.mDy > 0: # Moving down; Hit the top side of the obj
                                    enemy.mRect.bottom = obj.mRect.top
                                if enemy.mDy < 0: # Moving up; Hit the bottom side of the obj
                                    enemy.mRect.top = obj.mRect.bottom

            # Collectable Sword
            if isinstance(obj, adventurelib.objects.CollectableSword):
                # If you collide with a collectable, destroy the collectable and add it to players inventory
                if self.mPlayer.mRect.colliderect(obj.getRect()):
                    print("Sword Added To Inventory")
                    print("Press 'A' to use")
                    obj.destroy()
                    self.mPlayer.mInventory.append("Sword")

            #Enemy
            if isinstance(obj, adventurelib.enemy.Enemy):
                if self.mSword.mRect.colliderect(obj.mRect):
                    # print("Enemy HIT")
                    obj.destroy()
                if self.mPlayer.mRect.colliderect(obj.mRect):
                    if obj.getHealth() > 0:
                        self.mPlayer.looseHealth( 2 )
                        self.mPlayerColor = (255,0,0)


    def check_player_hits_lava(self, obj):
        if isinstance( obj, adventurelib.objects.Lava):
            self.mPlayer.looseHealth( 2 )
            self.mPlayerColor = (255,0,0)

    def check_player_dies_to_life_loss(self):
        if self.mPlayer.getHealth() <= 0:
            self.mGameOver = True


    #Finds the objects that are in the same room as  the player and adds them to self.mActiveObjects
    def add_current_obj_to_active_objects( self, objectsList ):
        for obj in objectsList:
            if obj.getRoomXY() == self.mPlayer.getRoomXY():
                self.mActiveObjects.append(obj)
        return

    def add_current_obj_in_lists_to_active_objects( self, objectList):
        #self.mActiveObjects = []
        for objlist in objectList:
            for obj in objlist:
                if obj.getRoomXY() == self.mPlayer.getRoomXY():
                    self.mActiveObjects.append(obj)
        return


    def checkPlayerEnterDoor( self ):
        for door in self.mActiveObjects:
            if isinstance( door, adventurelib.objects.Door ):
                if self.mPlayer.mRect.colliderect( door.mRect ):

                    self.mActiveObjects = []

                    #Makes the character start on the correct side of the room when entering a door
                    direction_when_enter_door = self.mPlayer.getFacing()
                    if direction_when_enter_door == "up":
                        self.mPlayer.setY( self.mHeight - 5 - self.mPlayer.getHeight() )

                        self.mPlayer.setX( self.mWidth/2 - (self.mPlayer.getWidth()/2))
                    elif direction_when_enter_door == "down":
                        self.mPlayer.setY( 5 )
                        self.mPlayer.setX(self.mWidth/2 - (self.mPlayer.getWidth()/2))
                    elif direction_when_enter_door == "right":
                        self.mPlayer.setX( 5 )
                        self.mPlayer.setY(self.mHeight/2 - (self.mPlayer.getHeight()/2))
                    elif direction_when_enter_door == "left":
                        self.mPlayer.setX( self.mWidth - 5 - self.mPlayer.getWidth() )
                        self.mPlayer.setY(self.mHeight/2 - (self.mPlayer.getHeight()/2))

                    direction_when_enter_door = -1

                    self.mPlayer.setRoomXY( door.getSharedRoomXY() )
                    self.mSword.setRoomXY( door.getSharedRoomXY() )
                    print( self.mPlayer.getRoomXY() )
                    self.add_current_obj_in_lists_to_active_objects(self.mObjects)

        return

    def reset_enemies_in_activeEnemies( self ):
        i = 0
        tempList = self.mEnemies[:]
        for e in self.mEnemies:
            del e
        self.mEnemies = tempList[:]


    def moveEnemies(self):
        self.mEnemy_room1_1.move_random()
        self.mEnemy_1_room_1_0.move_follow(self.mPlayer)
        self.mEnemy_2_room_1_0.move_follow(self.mPlayer)

    def resetEnemyPosition(self):
        if self.mPlayer.getRoomXY() != (1,1):
            self.mEnemy_room1_1.mRect.x = self.mEnemy_room1_1.getInitialXY()[0]
        if self.mPlayer.getRoomXY() != (1,0):
            self.mEnemy_1_room_1_0.mRect.x = self.mEnemy_1_room_1_0.getInitialXY()[0]
            self.mEnemy_1_room_1_0.mRect.y = self.mEnemy_1_room_1_0.getInitialXY()[1]
            self.mEnemy_2_room_1_0.mRect.x = self.mEnemy_2_room_1_0.getInitialXY()[0]
            self.mEnemy_2_room_1_0.mRect.y = self.mEnemy_2_room_1_0.getInitialXY()[1]

    def checkOutOfBounds(self):
        '''
        if self.mPlayer.outOfBounds(self.mWidth,self.mHeight):
            self.mPlayerDead = True'''

        return

    def evolve( self, dt ):
        self.mPlayerColor = (140,140,140)
        #tracking

        self.mActiveObjects = [] #moved this inside addcurrentobjtoactiveobjects
        #need a way to reset enemies when The room they are in is left
        #self.reset_enemies_in_activeEnemies()
        self.add_current_obj_in_lists_to_active_objects( self.mObjects )
        self.add_current_obj_in_lists_to_active_objects( self.mEnemies )

        #collisions
        self.checkPlayerEnterDoor()
        self.checkCollisions()

        #enemies

        self.moveEnemies()
        self.resetEnemyPosition()
        #sets GameOver to True if true
        self.check_player_dies_to_life_loss()
        if self.mGameOver == True:
            #kills the game
            pass
        return

    def drawPlayer(self,surface):
        rect = self.mPlayer.mRect
        pygame.draw.rect(surface,self.mPlayerColor,rect)
        return

    def drawSword(self,surface):
        swordColor = (140,0,0)
        rect = self.mSword.mRect
        pygame.draw.rect(surface,swordColor,rect)

        return

    # calls obj's 'draw' function.
	# can be used to draw objects that have independant draw methods within their class
    def drawObjects( self, surface ):
        for obj in self.mActiveObjects:
            if isinstance(obj,adventurelib.enemy.Enemy):
                if obj.getHealth() > 0:
                    obj.draw( surface )
            else:
                obj.draw( surface )

    def drawGameOver(self, surface ):
        if self.mGameOver:
            rect = pygame.Rect((self.mWidth / 2) - 275, (self.mHeight / 2) - 60,
                               600, 200)
            pygame.draw.rect(surface, (0, 0, 0), rect, 0)
            pygame.font.init()
            myFontGO = pygame.font.SysFont("Comic Sans", 100)
            gameOverDisplay = myFontGO.render("GAME OVER", False, (255, 255, 255))
            surface.blit(gameOverDisplay, ((self.mWidth / 2) -200 , self.mHeight / 2))\


    def drawLifeCounter(self, surface ):
        rect = pygame.Rect(self.mWidth - 90, 7, 80, 40)
        pygame.draw.rect(surface, (14, 41, 92), rect, 0)
        pygame.font.init()
        myFont = pygame.font.SysFont("Times New Roman", 35)
        healthDisplay = myFont.render(str(self.mPlayer.getHealth()), False, (255, 255, 255))
        surface.blit(healthDisplay, (self.mWidth - 78, 7))
        return

    # draws the current state of the system
    def draw( self, surface ):

        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, (255,255,255), rect, 0 )


        #self.drawWater(surface)
        #self.drawDoors(surface)
        self.drawObjects( surface )
        self.drawSword(surface)
        self.drawPlayer(surface)

        self.drawLifeCounter( surface )
        self.drawGameOver( surface )
