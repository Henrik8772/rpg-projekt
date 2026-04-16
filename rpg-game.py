# Imports

import tkinter
import tkinter.font as tkFont
from tkinter import *


# Stats

# Tkinter

root = Tk()
root.title("RPG-WORLD")
root.geometry("800x600")

# Custom fonts and text size

custom_font = tkFont.Font(family="Arial", size=20)

# The main loop

main_menu_label = Label(root, text="RPG-WORLD", font=custom_font)
main_menu_label.pack(pady=10)

start_game_button = Button(
    root, text="START A NEW JOURNEY", width=25, font=custom_font, command=None)
start_game_button.pack(pady=20)

credit_menu_button = Button(
    root, text="CREDITS", width=25, font=custom_font, command=None)
credit_menu_button.pack(pady=15)

exit_menu_button = Button(root, text="EXIT GAME",
                          width=25, font=custom_font, command=None)
exit_menu_button.pack(pady=15)

root.mainloop()
