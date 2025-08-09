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

    def display_options(self):
        """Function to redisplay the prompt."""
        print(PROMPT)

    def spawn_traveling_merchant(self):
        """The spawn logic for the traveling merchant."""
        spawn = randint(1,5)
        if spawn == 5:
            print(f'{BLUE}The traveling merchant has appeared!{RESET}')
            self.traveling_merchant()

    def traveling_merchant(self):
        """Spawn parameters for traveling merchant."""
        items = choice(TRAVELING_MERCHANT_ITEMS)
        print(f'{BOLD}{GREEN}Items for sale:{RESET}')
        for item, count in items.items():
            # Prints item with a column
            print(f"{GRAY}{item:<10} {count:>3}{RESET}")

    def game_loop(self):
        """The main game loop."""
        print(f"{CYAN}{BOLD}Welcome to Goblin Hunter!{RESET}")
        print(f"{GRAY}Type `q` to quit.{RESET}")
        print(PROMPT)
        while True:
            if self.player.health == 0:
                self.player.death()
                break
            self.spawn_traveling_merchant()
            choice = input(IN_ARROW)
            if choice == 'q':
                break
            elif choice == 'd':
                self.player.display_inventory()
            elif choice == 'l':
                self.player.loot_goblin()
            elif choice == 'p':
                self.player.drink_potion()
            elif choice == 'o':
                self.display_options()
            elif choice == 'c':
                self.clean_screen()
                print(f'{GRAY}Display options: `o`{RESET}')