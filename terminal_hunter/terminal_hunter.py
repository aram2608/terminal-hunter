from random import choice, randint

from .consts import *
from .player import *

class Terminal_Hunter:
    def __init__(self):
        self.player = Player(self)
        self.goblin = 1

    def clean_screen(self):
        """Cleans up the screan."""
        print('\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n')

    def game_loop(self):
        """The main game loop."""
        print(f"{CYAN}{BOLD}Welcome to Goblin Hunter!{RESET}")
        print(f"{GRAY}Type `q` to quit.{RESET}")
        print(PROMPT)
        while True:
            if self.player.health == 0:
                self.player.death()
                break
            choice = input(IN_ARROW)
            if choice == 'q':
                break
            elif choice == 'd':
                self.player.display_inventory()
            elif choice == 'l':
                self.player.loot_goblin()
            elif choice == 'c':
                self.clean_screen()
                print(PROMPT)