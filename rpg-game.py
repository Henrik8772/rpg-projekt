# Imports

from random import randint
import tkinter
import tkinter.font as tkFont
from tkinter import *

# Stat varibles

player_hp = 100
player_base_attack = randint(3, 7)
gold = 0
potions = 0
armor = 8
mana = 50


# Tkinter

root = Tk()
root.title("RPG-WORLD")
root.geometry("800x600")

# Custom fonts and text size

custom_font = tkFont.Font(family="Arial", size=20)

# Configs

root.configure(bg="black")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Button cofigs
root.option_add("*Button*background", "black")
root.option_add("*Button*foreground", "white")
root.option_add("*Button*activeBackground", "black")
root.option_add("*Button*activeForeground", "white")
root.option_add("*Button*font", custom_font)
root.option_add("*Button*width", "25")

# Label configs
root.option_add("*Label*background", "black")
root.option_add("*Label*foreground", "white")
root.option_add("*Label*font", custom_font)

# Funktions (def)


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def explore():
    clear_screen()


def shop():
    clear_screen()


def menu_stats():
    clear_screen()


def game_menu():
    clear_screen()

    label = Label(
        root,
        text="WELCOME TO THE WORLD OF DRATHUS RPG")

    label.grid(row=0, column=1, pady=(75, 25))

    explore_button = Button(
        root,
        text="EXPLORE",
        command=explore)

    explore_button.grid(row=1, column=1, pady=(40, 15))

    shop_button = Button(
        root,
        text="SHOP",
        command=shop)

    shop_button.grid(row=2, column=1, pady=15)

    stats_button = Button(
        root,
        text="STATS",
        command=menu_stats)

    stats_button.grid(row=3, column=1, pady=15)

# The main loop


main_menu_label = Label(
    root,
    text="RPG-WORLD")

main_menu_label.grid(row=0, column=1, pady=(75, 25))

start_game_button = Button(
    root,
    text="START A NEW JOURNEY",
    command=game_menu)

start_game_button.grid(row=1, column=1, pady=(40, 15))

credit_menu_button = Button(
    root,
    text="CREDITS",
    command=None)

credit_menu_button.grid(row=2, column=1, pady=15)

exit_menu_button = Button(
    root,
    text="EXIT GAME",
    command=quit)

exit_menu_button.grid(row=3, column=1, pady=15)


root.mainloop()
