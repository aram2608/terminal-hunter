from random import choice, randint

from .consts import *

class Terminal_Hunter:
    def __init__(self):
        pass

    def display_inventory(self, inv):
        """Function the display the current inventory."""
        print(f'{BOLD}{GREEN}Inventory:{RESET}')
        total_items = 0
        for item, count in inv.items():
            # Prints item with a column
            print(f"{GRAY}{item:<10} {count:>3}{RESET}")
            total_items += count
        print(f"{GREEN}Total number of items: {total_items}{RESET}")

    def loot_goblin(self):
        """A function to update the inventory after looting a goblin."""
        loot = choice(GOBLIN_LOOT_TABLE)
        for item, amount in loot.items():
            inventory[item] = inventory.get(item, 0) + amount
        print(f"{YELLOW}You looted: {loot}{RESET}")

    def clean_screen(self):
        """Cleans up the screan."""
        print('\n','\n','\n','\n','\n','\n','\n','\n','\n')

    def game_loop(self):
        """The main game loop."""
        print(f"{CYAN}{BOLD}Welcome to Goblin Hunter!{RESET}")
        print(f"{GRAY}Type `q` to quit.{RESET}")
        print(PROMPT)
        while True:
            choice = input(IN_ARROW)
            if choice == 'q':
                break
            elif choice == 'd':
                self.display_inventory(inventory)
            elif choice == 'l':
                self.loot_goblin()
            elif choice == 'c':
                self.clean_screen()
                print(PROMPT)