from utils import *

def main():
    # warp guru
    warp(['s', 'd'])

    # walk guru
    turn("a")
    dash()

    # warp ice
    for i in [2, 2, 3, 3, 2, 2, 6, 2, 4, 2, 3, 3, 5, 3, 3, 1]:
        click('e')
        timeout(i)

    # walk king
    notify("walk to king")
    turn("d")
    for i in range(4):
        dash()
    turn("s")
