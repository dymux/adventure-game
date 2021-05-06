import unittest
from adventurelib.player import Player
from adventurelib.player import Sword

class TestPlayer(unittest.TestCase):

	def test_check_player_attack_right(self):
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
		self.player = Player(x,y,w,h,dx,dy,s,hg,vg,"right",(0,0))
		self.expectedSwordX = int(x+w)
		self.expectedSwordY = int(y + (h/2.75))
		self.expectedSwordW = int(w/2)
		self.expectedSwordH = int(h/3)
		#stimulus
		result = self.player.attack()

		#result
		self.assertEqual( result.getX(), self.expectedSwordX)
		self.assertEqual( result.getY(), self.expectedSwordY)
		self.assertEqual( result.getWidth(), self.expectedSwordW)
		self.assertEqual( result.getHeight(), self.expectedSwordH)

	def test_check_player_end_attack(self):
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
		self.player = Player(x,y,w,h,dx,dy,s,hg,vg,"right",(0,0))
		self.expectedSwordX = -100
		self.expectedSwordY = -100
		self.expectedSwordW = 0
		self.expectedSwordH = 0
		#stimulus
		self.player.attack()
		result = self.player.endAttack()

		#result
		self.assertEqual( result.getX(), self.expectedSwordX)
		self.assertEqual( result.getY(), self.expectedSwordY)
		self.assertEqual( result.getWidth(), self.expectedSwordW)
		self.assertEqual( result.getHeight(), self.expectedSwordH)

if __name__ == '__main__':
	unittest.main()
