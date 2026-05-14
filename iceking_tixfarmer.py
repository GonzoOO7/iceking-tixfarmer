# Make sure to stand at the ice king by the guru
from math import ceil
from utils import *

ICE_KING_TIX = 19
GOAL_TIX = 900

def enter():
    notify("Enter fight")
    click('e')
    timeout(6)

def call():
    notify("Call calypso")
    for i in ['d', 's', 'space', 'd', 'd', 'd', 'space']:
        click(i)
    timeout(3)

def paint():
    notify("Paint king")
    for i in ['d', 'space', 'd', 'd', 'd', 'd', 'space', 'space']:
        click(i)
    timeout(4)

def await_calypso_king():
    info("Await calypso")
    timeout(3)
    info("Await king")
    timeout(3)

def stabby_stab():
    for i in range(2):
        notify(f"Stab {i + 1}x")
        for j in ['space', 'd', 'space']:
            click(j)
        timeout(5.5)

def await_calypso_win():
    info("Await calypso")
    timeout(6)
    info("Await victory")
    timeout(9)

def main(starting_tix = 0):
    runs = ceil((GOAL_TIX - starting_tix) / ICE_KING_TIX)
    notify(f"Ready for {runs} runs ({runs * ICE_KING_TIX} tix)")
    timeout(3)
    for r in range(runs):
        enter()
        call()
        paint()
        await_calypso_king()
        stabby_stab()
        await_calypso_win()
        if r == runs - 1:
            notify(f"All done :) ({runs} times)")
            break
        else:
            notify(f"Here we go again ({r+2}/{runs})")

if __name__ == "__main__":
    main()