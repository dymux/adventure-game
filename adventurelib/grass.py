from adventurelib.immovable import Immovable

class Grass(Immovable):

    def __init__(self, x=0, y=0, w=0, h=0,roomXY = (0, 0)):
        Immovable.__init__(self, x, y, w, h,roomXY)

    def hits(self, other):
        return self.overlapWithLocatable(other)

    def __str__(self):
        s = "Grass<"+Immovable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)
