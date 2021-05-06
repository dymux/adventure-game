import unittest
import adventureGame
from adventureGame import AdventureGame
from adventurelib.player import Player
import adventurelib


#self.add_current_obj_in_lists_to_active_objects(self.mObjects)

    # def add_current_obj_in_lists_to_active_objects( self, objectList) :
    #     for objlist in objectList:
    #         for obj in objlist:
    #             if obj.getRoomXY() == self.mPlayer.getRoomXY():
    #                 self.mActiveObjects.append(obj)

class TestRoomTracking(unittest.TestCase):

    def test_Object_list_updates_correct_object_room_1_0(self):
        #setup
        self.mWidth = 500
        self.mHeight = 500
        VerticleDoorHeight = self.mHeight
        VerticleDoorWidth = 3
        HorizontalDoorHeight = 3
        HorizontalDoorWidth = self.mWidth

        self.mObjects = []
        self.mDoors = []
        self.mActiveObjects = []

        self.mDoor0 = adventurelib.objects.Door( self.mWidth - VerticleDoorWidth , 0, VerticleDoorWidth, VerticleDoorHeight, (0, 0), (1, 0))
        self.mDoor0Invert = adventurelib.objects.Door( 0 , self.mHeight/2 - (VerticleDoorHeight / 2), VerticleDoorWidth, VerticleDoorHeight, (1, 0), (0, 0))

        self.mDoor1 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorWidth, HorizontalDoorHeight, (1, 0), (1, 1) )
        self.mDoor1Invert = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight) , HorizontalDoorWidth, HorizontalDoorHeight, (1, 1), (1, 0))

        self.mDoor2 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorHeight, HorizontalDoorWidth, (2, 0), (2, 1) )
        self.mDoor2Invert = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight), HorizontalDoorHeight, HorizontalDoorWidth, (2, 1), (2, 0))

        self.mActiveObjects.append( self.mDoor0 )

        self.mDoors.append( self.mDoor0 )
        self.mDoors.append( self.mDoor0Invert )
        self.mDoors.append( self.mDoor1 )
        self.mDoors.append( self.mDoor1Invert )
        self.mDoors.append( self.mDoor2 )
        self.mDoors.append( self.mDoor2Invert )

        self.mObjects.append( self.mDoors)

        self.game = adventureGame.AdventureGame( 500, 500, 50 )

        self.mPlayer = Player( 480, 250, 50, 50, 0, 0, 0, 0, 0, 'right', roomXY = (1, 0))
        self.mHealth = 100
        self.mExpectedHealth = 99

        #stimulus
        self.mActiveObjects = []
        AdventureGame.add_current_obj_in_lists_to_active_objects(self, self.mObjects )

        result = len(self.mActiveObjects)
        self.mExpectedNunberOfObjects = 2
        self.assertEqual( result, self.mExpectedNunberOfObjects  )



    def test_Object_list_updates_correct_object_room_2_0(self):
        #setup
        self.mWidth = 500
        self.mHeight = 500
        VerticleDoorHeight = self.mHeight
        VerticleDoorWidth = 3
        HorizontalDoorHeight = 3
        HorizontalDoorWidth = self.mWidth

        self.mObjects = []
        self.mDoors = []
        self.mActiveObjects = []

        self.mDoor0 = adventurelib.objects.Door( self.mWidth - VerticleDoorWidth , 0, VerticleDoorWidth, VerticleDoorHeight, (0, 0), (1, 0))
        self.mDoor0Invert = adventurelib.objects.Door( 0 , self.mHeight/2 - (VerticleDoorHeight / 2), VerticleDoorWidth, VerticleDoorHeight, (1, 0), (0, 0))

        self.mDoor1 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorWidth, HorizontalDoorHeight, (1, 0), (1, 1) )
        self.mDoor1Invert = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight) , HorizontalDoorWidth, HorizontalDoorHeight, (1, 1), (1, 0))

        self.mDoor2 = adventurelib.objects.Door( (self.mWidth / 2) - (HorizontalDoorWidth / 2) , 0, HorizontalDoorHeight, HorizontalDoorWidth, (2, 0), (2, 1) )
        self.mDoor2Invert = adventurelib.objects.Door( (self.mWidth/2) - (HorizontalDoorWidth / 2) , self.mHeight - ( HorizontalDoorHeight), HorizontalDoorHeight, HorizontalDoorWidth, (2, 1), (2, 0))

        self.mActiveObjects.append( self.mDoor0 )

        self.mDoors.append( self.mDoor0 )
        self.mDoors.append( self.mDoor0Invert )
        self.mDoors.append( self.mDoor1 )
        self.mDoors.append( self.mDoor1Invert )
        self.mDoors.append( self.mDoor2 )
        self.mDoors.append( self.mDoor2Invert )

        self.mObjects.append( self.mDoors)

        self.game = adventureGame.AdventureGame( 500, 500, 50 )

        self.mPlayer = Player( 480, 250, 50, 50, 0, 0, 0, 0, 0, 'right', roomXY = (2, 0))
        self.mHealth = 100
        self.mExpectedHealth = 99

        #stimulus
        self.mActiveObjects = []
        AdventureGame.add_current_obj_in_lists_to_active_objects(self, self.mObjects )

        result = len(self.mActiveObjects)
        self.mExpectedNunberOfObjects = 1
        self.assertEqual( result, self.mExpectedNunberOfObjects  )



        