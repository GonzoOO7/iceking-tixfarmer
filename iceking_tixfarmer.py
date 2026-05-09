# Make sure to stand at the ice king by the guru
import time
import keyboard

TIMES = 48

def info(text):
    print( "\033[3;34m" + text + "\033[m")


def action(text):
    print( "\033[1;36m" + text + "\033[m")

def click(key):
    keyboard.press_and_release(key)

def timeout(x):
    time.sleep(x)

def enter():
    action("Enter fight")
    click('e')
    timeout(6)

def call():
    action("Call calypso")
    for i in ['d', 's', 'space', 's', 'space']:
        click(i)
    timeout(3)

def paint():
    action("Paint king")
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
        action(f"Stab {i+1}x")
        for j in ['space', 'd', 'space']:
            click(j)
        timeout(5)

def await_calypso_win():
    info("Await calypso")
    timeout(6)
    info("Await victory")
    timeout(9)

def run_it_all():
    enter()
    call()
    paint()
    await_calypso_king()
    stabby_stab()
    await_calypso_win()

action(f"Ready for {TIMES} runs")
timeout(3)
for r in range(TIMES):
    run_it_all()
    if r == TIMES - 1:
        info(f"All done :) ({TIMES} times)")
        break
    else:
        info(f"Here we go again x{r+1}")

