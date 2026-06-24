from grid import Grid


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid ): # Skrev om funktionen med nya variablar för ny x och y position.
        new_x = self.pos_x + x
        new_y = self.pos_y + y
        Tile = grid.get(new_x, new_y) # En ny variabel som innehåller hela grid.get(new_x, new_y) som är funktionen för att checka ny position.
        if Tile != grid.wall: #Om den nya position inte består av en grid.wall skall True returneras, annars False
            return True
        else:
            return False



