from random import choice, randint
from .consts import *

class Player:
    def __init__(self, th):  
        self.health = 10
        self.inventory = {
            'rope':2,
            'dagger':5,
            'potion':6,
            }
        
        
    def display_inventory(self):
        """Function the display the current inventory."""
        print(f'{BOLD}{GREEN}Inventory:{RESET}')
        total_items = 0
        for item, count in self.inventory.items():
            # Prints item with a column
            print(f"{GRAY}{item:<10} {count:>3}{RESET}")
            total_items += count
        print(f"{GREEN}Total number of items: {total_items}{RESET}")

    def loot_goblin(self):
        """A function to update the inventory after looting a goblin."""
        loot = choice(GOBLIN_LOOT_TABLE)
        success_chance = randint(1,2)
        if success_chance == 1:
            for item, amount in loot.items():
                self.inventory[item] = self.inventory.get(item, 0) + amount
            print(f"{YELLOW}You looted: {loot}{RESET}")
        else:
            print(f"{RED}Attempt failed!{RESET}")
            self.health -= 1
            print(self.health * "\u2764\ufe0f")

    def drink_potion(self):
        """A function to restore the players health."""
        if 'potion' in self.inventory:
            if self.health < 10:
                self.inventory['potion'] -= 1
                self.health += 2
                print(f'{MAGENTA}Health restored!{RESET}')
                print(self.health * "\u2764\ufe0f")
            else:
                print(f'{MAGENTA}Your health is already full.{RESET}')
        else:
            print(f'{RED}You are out of potions!{RESET}')

    def trade_items(self):
        pass

    def death(self):
        """The player dies."""
        if self.health == 0:
            print(f"{RED}Your health has reached zero!\nYou are dead.{RESET}")