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
        Tile = grid.get(new_x, new_y)
        if Tile != grid.wall: # Värdena i denna motsvara gränsen på griden som jag hittade efter testning. Funktionen behöver göras om mycket om man vill tillåta att ändra griden i grid klassen.
            return True
        else:
            return False



