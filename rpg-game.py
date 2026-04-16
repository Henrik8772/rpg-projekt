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

# Configs

root.config(bg="black")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# The main loop


main_menu_label = Label(root, text="RPG-WORLD",
                        font=custom_font, bg="black", fg="white")
main_menu_label.grid(row=0, column=1, pady=25)

start_game_button = Button(
    root, text="START A NEW JOURNEY", width=25, font=custom_font, bg="black", activebackground="black", activeforeground="white", fg="white", command=None)
start_game_button.grid(row=1, column=1, pady=20)

credit_menu_button = Button(
    root, text="CREDITS", width=25, font=custom_font, bg="black", activebackground="black", activeforeground="white", fg="white", command=None)
credit_menu_button.grid(row=2, column=1, pady=15)

exit_menu_button = Button(root, text="EXIT GAME",
                          width=25, font=custom_font, bg="black", activebackground="black", activeforeground="white", fg="white", command=None)
exit_menu_button.grid(row=3, column=1, pady=15)

root.mainloop()
