import time
import keyboard

def info(text):
    print( "\033[3;34m" + text + "\033[m")


def notify(text):
    print( "\033[1;36m" + text + "\033[m")

def click(key):
    if key == 'e':
        info("bla bla bla")
    keyboard.press_and_release(key)
    timeout(.1)

def timeout(x):
    time.sleep(x)

def turn(key):
    notify(f"turn {key}")
    keyboard.press(key)
    timeout(.1)
    keyboard.release(key)

def dash():
    notify("dash")
    click('shift')
    timeout(2)

def walk(key, dur):
    click(key)
    keyboard.press(key)
    timeout(dur)
    keyboard.release(key)

def warp(sequence):
    notify("warp")
    for i in ['tab'] + sequence + ['space', 'tab']:
        click(i)
    timeout(3)