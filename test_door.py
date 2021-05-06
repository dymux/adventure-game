import unittest
import adventureGame
from adventureGame import AdventureGame
import adventurelib
from adventurelib import player
from adventurelib.player import Player




class TestDoor( unittest.TestCase ):

    def test_door0RoomXY(self):
        expectedRoomXY = (0,0)
        expectedRoomXYInvert = (1,0)


        #setup
        VerticleDoorHeight = 500 
        VerticleDoorWidth = 3
        HorizontalDoorHeight = 3
        HorizontalDoorWidth = 500

        self.AdventureGame = adventureGame.AdventureGame( 500, 500, 50)
        door0 = adventurelib.objects.Door( 500 - VerticleDoorWidth , 0, VerticleDoorWidth, VerticleDoorHeight, (0, 0), (1, 0))
        

        #stimulus
        
        #result

        self.assertEqual( door0.getRoomXY(), (0,0))

    def test_door0RoomXYInvert(self):
        expectedRoomXY = (0,0)
        expectedRoomXYInvert = (1,0)


        #setup
        VerticleDoorHeight = 500 
        VerticleDoorWidth = 3
        HorizontalDoorHeight = 3
        HorizontalDoorWidth = 500

        self.AdventureGame = adventureGame.AdventureGame( 500, 500, 50)
        door0 = adventurelib.objects.Door( 500 - VerticleDoorWidth , 0, VerticleDoorWidth, VerticleDoorHeight, (0, 0), (1, 0))
        

        #stimulus
        
        #result

        self.assertEqual( door0.getSharedRoomXY(), (1,0))


      