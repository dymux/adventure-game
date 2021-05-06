import unittest
from adventurelib.enemy import Enemy

class TestEnemy(unittest.TestCase):

    def test_check_enemy_moves_left(self):
        #setup
        x = 100
        y = 100
        w = 10
        h = 10
        dx = 0
        dy = 0
        s = 10
        hg = 15
        vg= 15
        self.enemy = Enemy(x,y,w,h,dx,dy,s,hg,vg,"",(0,0),100,0,(0,0,0),(0,0))
        self.expectedX = 100 - s


        #stimulus
        self.enemy.left()
        result = self.enemy.getX()

        #result
        self.assertEqual( result, self.expectedX )

    def test_check_enemy_moves_right(self):
        #setup
        x = 100
        y = 100
        w = 10
        h = 10
        dx = 0
        dy = 0
        s = 10
        hg = 15
        vg= 15
        self.enemy = Enemy(x,y,w,h,dx,dy,s,hg,vg,"",(0,0),100,0,(0,0,0),(0,0))
        self.expectedX = 100 + s


        #stimulus
        self.enemy.right()
        result = self.enemy.getX()

        #result
        self.assertEqual( result, self.expectedX )

    def test_check_enemy_moves_up(self):
        #setup
        x = 100
        y = 100
        w = 10
        h = 10
        dx = 0
        dy = 0
        s = 10
        hg = 15
        vg= 15
        self.enemy = Enemy(x,y,w,h,dx,dy,s,hg,vg,"",(0,0),100,0,(0,0,0),(0,0))
        self.expectedY = 100 - s


        #stimulus
        self.enemy.up()
        result = self.enemy.getY()

        #result
        self.assertEqual( result, self.expectedY )

    def test_check_enemy_moves_down(self):
        #setup
        x = 100
        y = 100
        w = 10
        h = 10
        dx = 0
        dy = 0
        s = 10
        hg = 15
        vg= 15
        self.enemy = Enemy(x,y,w,h,dx,dy,s,hg,vg,"",(0,0),100,0,(0,0,0),(0,0))
        self.expectedY = 100 + s


        #stimulus
        self.enemy.down()
        result = self.enemy.getY()

        #result
        self.assertEqual( result, self.expectedY )

if __name__ == '__main__':
    unittest.main()
