import unittest
from adventurelib.player import Player

class TestHealth(unittest.TestCase):

    def test_check_player_takes_correct_damage2(self):
        #setup
        self.mHealth = 100
        self.mExpectedHealth = 99
        self.p = Player( 480, 250, 50, 50, 0, 0, 0, 0, 0, 'right', roomXY = (0, 0))
        
        #stimulus
        self.p.looseHealth( 1)
        result = self.p.getHealth()

        #result
        self.assertEqual( result, self.mExpectedHealth )

    def test_check_player_takes_correct_damage50(self):
        #setup
        self.mHealth = 100
        self.mExpectedHealth = 50
        self.p = Player( 480, 250, 50, 50, 0, 0, 0, 0, 0, 'right', roomXY = (0, 0))
        
        #stimulus
        self.p.looseHealth( 50)
        result = self.p.getHealth()

        #result
        self.assertEqual( result, self.mExpectedHealth )

    def test_negative_health_loss_does_nothing(self):
        #setup
        self.p = Player( 480, 250, 50, 50, 0, 0, 0, 0, 0, 'right', roomXY = (0, 0))
        self.mExpectedHealth = 100 
       
        #stimulus
        self.p.looseHealth(-1)
        result = self.p.getHealth()
        
        #result
        self.assertEqual(result, self.mExpectedHealth)
        