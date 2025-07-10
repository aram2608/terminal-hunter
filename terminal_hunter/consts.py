from random import randint

RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
CYAN   = "\033[96m"
GRAY   = "\033[90m"

inventory = {
    'rope':2,
    'dagger':5,
    'potion':6,
    }

GOBLIN_LOOT_TABLE = [
    {'gold': randint(1, 5)},
    {'dagger': 1, 'gold': 1},
    {'tattered robes': 2},
    {'potion': 1},
]

TRAVELING_MERCHANT_ITEMS = [
    {'health potion' :5},
    {'mana potion' :7},
    {'iron sword' : 20},
    {'leather armor' : 15},
    {'magic scroll' : 25},
    {'elixir of strength' : 30},
    {'torch' : 2},
    {'rope' : 3},
    {'lockpick set': 10},
    {'bag of holding': 50},
    {'mysterious egg': 40},
    {'silver dagger': 18},
    {'boots of speed': 35},
    {'tattered map': 8},
    {'enchanted ring': 60},
]

PROMPT = f"{GREEN}{BOLD}Options:\n{RESET}"
PROMPT += f"{GRAY}`d`: display inventory.\n"
PROMPT += f"`l`: loot goblin.\n"
PROMPT += f"`c`: clean screan.\n"
PROMPT += f'`p`: drink potion.\n'
PROMPT += f"`q`: quit game. {RESET}"

IN_ARROW = f"{GREEN}>>>{RESET} "