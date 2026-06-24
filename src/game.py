from email.policy import default

import pickups
import player
from pickups import inventory, Item
from src.grid import Grid
from src.player import Player
from src import pickups


# TODO: flytta denna till en annan fil
class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.player = Player(16, 5) # Ändrade x och Y för att få spelaren att börja närmare mitten.
        self.score = 0
        self.inventory = []

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g)


def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, I to show inventory and Q/X to quit  ")
        command = command.casefold()[:1]
        dx, dy = 0, 0
        if command == "w":# Funktionen för move player fanns i player men presenterar den mer easily digested
            dx,dy = 0, -1
             # Floor is lava, alla steg spelaren ta minskar score med 1.
        elif command == "a":
            dx,dy = -1, 0

        elif command == "s":
            dx,dy = 0,1

        elif command == "d":
            dx,dy = 1,0

        elif command == "i":
            print("Här är föremålen du plockat på dig:")
            for Item in inventory:
                print(Item.name)
        elif command == "q" or command == "x":
            break

        else:
            print("Invalid command")
            continue


        target_x = state.player.pos_x + dx # Nya variablar så att koden under maybe_item blir lättare att förstå.
        target_y = state.player.pos_y + dy
        maybe_item = state.g.get(target_x, target_y)

        if isinstance(maybe_item,pickups.Item):
            state.score += maybe_item.value
            print(f"You found {maybe_item.name}, värt {maybe_item.value} poäng") # Skriver ut item namn samt poäng.
            state.g.clear(target_x, target_y)
            inventory.append(maybe_item)


        if state.player.can_move(dx, dy, state.g):
            state.player.move(dx, dy)
            state.score -= 1
        else:
            print("Cannot move here, wall is blocking the path")

# Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
