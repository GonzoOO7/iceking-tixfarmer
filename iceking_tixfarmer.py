# Make sure to stand at the ice king by the guru
from utils import *

TIMES = 50


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

def main():
    notify(f"Ready for {TIMES} runs")
    timeout(3)
    for r in range(TIMES):
        enter()
        call()
        paint()
        await_calypso_king()
        stabby_stab()
        await_calypso_win()
        if r == TIMES - 1:
            info(f"All done :) ({TIMES} times)")
            break
        else:
            info(f"Here we go again x{r+1}")

if __name__ == "__main__":
    main()