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

PROMPT = f"{GREEN}{BOLD}Options:\n{RESET}"
PROMPT += f"{GRAY}`d`: display inventory.\n"
PROMPT += f"`l`: loot goblin."
PROMPT += f"`c`: clean screan {RESET}"

IN_ARROW = f"{GREEN}>>>{RESET} "