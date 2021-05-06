import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
from adventureGame import AdventureGame

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
grid_size = 50
TITLE = "Adventure Game"
# pixels width
WINDOW_WIDTH  = 500
# pixels high
WINDOW_HEIGHT = 500
# frames per second
DESIRED_RATE  = 30

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = AdventureGame( width, height, grid_size )
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # keys contains all keys currently held down
        # newkeys contains all keys pressed since the last frame
        # Use pygame.K_? as the keyboard keys.
        # Examples: pygame.K_a, pygame.K_UP, etc.
        # if pygame.K_UP in newkeys:
        #    The user just pressed the UP key
        #
        # buttons contains all mouse buttons currently held down
        # newbuttons contains all buttons pressed since the last frame
        # Use 1, 2, 3 as the mouse buttons
        # if 3 in buttons:
        #    The user is holding down the right mouse button
        #
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame

        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        otherPressed = False
        if pygame.K_a in keys:
            self.mGame.actOnPressA( )
        else:
            self.mGame.actOnANotPressed()

        if pygame.K_j in keys:
            self.mGame.actOnPressJ()
        if pygame.K_UP in keys and not otherPressed:
            self.mGame.actOnPressUP( )
            otherPressed = True

        if pygame.K_DOWN in keys and not otherPressed:
            self.mGame.actOnPressDOWN( )
            otherPressed = True

        if pygame.K_LEFT in keys and not otherPressed:
            self.mGame.actOnPressLEFT( )
            otherPressed = True

        if pygame.K_RIGHT in keys and not otherPressed:
            self.mGame.actOnPressRIGHT( )
            otherPressed = True

        if 1 in newbuttons:
            self.mGame.actOnLeftClick( x, y )

        self.mGame.evolve( dt )

        return

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )
