from utils import *


def main():
    warp(['s'])

    info("up up")
    walk("w", 4)

    info("and away")
    walk("a", 11.5)

    info("back up we go")
    walk("w", 4)

    for i in range(4):
        click('e')
        timeout(1.5)

    notify("gimme gold")
    for i in range(6):
        click('space')
        timeout(.75)

    notify("bye")
    dash()