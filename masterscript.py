from setup_farmer import *
from utils import *

import iceking_tixfarmer
import to_king
import get_gold

# Your stuff
STARTING_TIX = int(input("Current tix (if this isn't an int, screw you i'm not gonna add exception handling to this): "))
DECK_INDEX = int(input("Deck index (same as above...): "))
start_at_king = input("Start at king? leave empty otherwise: ") != ""
print(start_at_king)

# Gimme, gimme, gimme some time after script-mount
info("Ready (3s)")
timeout(3)
info("Go go go")

# Goto king if not there
if not start_at_king:
    select_deck(DECK_INDEX)
    setup_fast_travel()
    to_king.main()
# Run da program
while True: # You can break with esc, check out utils
    iceking_tixfarmer.main(STARTING_TIX)
    get_gold.main()
    STARTING_TIX = 0
    to_king.main()
