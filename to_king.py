from utils import *

def main():
    notify("Warp to ze guru")
    warp(['s', 'd'])

    notify("Walk to ze guru")
    turn("a")
    dash()

    notify("Talk about how cold you feel O_O")
    for i in [2, 2, 3, 3, 2, 2, 6, 2, 4, 2, 3, 3, 5, 3, 3, 1]:
        click('e')
        timeout(i)

    notify("Walk to king")
    turn("d")
    for i in range(4):
        dash()
    turn("s")
