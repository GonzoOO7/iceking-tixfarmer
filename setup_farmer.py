from utils import *

def select_deck(deck_index):
    notify("Open cards")
    click("tab")
    for i in range (4):
        click("d")
    click("space")

    notify("Open decks")
    click("s")
    click("s")
    click("d")
    click("d")
    click("space")

    notify(f"Get deck with idx={deck_index}")
    click("s")
    for i in range(deck_index):
        click("s")
    click("space")

    notify("Load deck")
    click("d")
    for i in range(3):
        click("a")
    click("s")
    click("space")

    click("tab")

def setup_fast_travel():
    click("tab")
    for i in range(7):
        click("d")
    click("space")
    click("tab")
