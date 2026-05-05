# Imports

from random import randint
import tkinter
import tkinter.font as tkFont
from tkinter import *
import random
from random import randint
from tkinter import ttk

monster = ""

# Stat varibles

player_hp = 100
player_attack = 7
gold = 0
potions = 0
armor = 8
mana_player = 50
crit_rate = 20

damage = player_attack


# Monsters

monsters = [
    {
        "name": "Goblin",
        "hp": randint(45, 125)
    },

    {
        "name": "Kobalt",
        "hp": randint(65, 120)
    }
]

# Shop items

potion = [
    {
        "name": "Healing Potion",
        "heal": 20,
        "gold": 3
    },

    {
        "name": "Mana Potion",
        "mana_regen": (5, 8),
        "length": (2, 4),
        "gold": 4
    },

    {
        "name": "Strength Potion",
        "damage": (3, 6),
        "length": (1, 3),
        "gold": 7
    }
]

weapons = [
    {
        "name": "Battle Axe",
        "damage": 20,
        "gold": 345
    },

    {
        "name": "A Damed Wish",
        "damage": 670,
        "gold": 9850,
        # "ability": "Final Wish: The player sacrifices 99 percent of remaining Hp to deliver a final wish apon the world instantly killing all enemys near you, This ability wont be able to be used after it has been unleashed once already, instead you permanently gain Intertwined Wishes passive on your class."
    }
]
# might add this or not using it as a reminder ik it wont work like this
passives = [
    {
        "name": "Intertwined Wishes",
        "gain": "All your attacks deal holy dmg and has a 10 percent chance to gain you 1 wish stack, at 10 wish stacks you instantly kill the next enemy and heal for the remaing hp of that said enemy."
    }
]

# Attacks

attacks = [
    # Combat skills/physical attacks

    # Mana/Magic attacks
    {
        "name": "Death's Dance",
        "dmg": randint(10, 20),
        "mana": 20
    },

    {
        "name": "Fireball",
        "dmg": randint(20, 40),
        "mana": 45
    }
]


# Tkinter

root = Tk()
root.title("RPG-WORLD")
root.geometry("1000x800")

button_frame = Frame()

# Custom fonts and text size


custom_font = tkFont.Font(family="Arial", size=20)
font_explore = tkFont.Font(family="Arial", size=15)

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

button_frame.option_add("*Frame*background", "black")

# Label configs
root.option_add("*Label*background", "black")
root.option_add("*Label*foreground", "white")
root.option_add("*Label*font", custom_font)

# Listbox configs
root.option_add("*Listbox*font", custom_font)
root.option_add("*Listbox*background", "black")
root.option_add("*Listbox*foreground", "white")

# Funktions (def)


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def return_menu():
    button_frame = Frame()
    button_frame.pack(side="top", fill="x")
    button = Button(button_frame, text="BACK", command=game_menu)
    button.pack(side="bottom", pady=10)


def explore():
    clear_screen()

    root.option_add("*Button*width", 15)
    label = Label(
        root, text="WHICH PLACE SHALL WE ADVENTURE THROUGH?")
    label.pack(pady=(75, 25))
    button_frame = Frame()

    button = Button(button_frame, text="FOREST", command=forest)
    button.pack(side="left", pady=50, padx=20)
    button = Button(button_frame, text="MOUNTAINS", command=forest)
    button.pack(side="right", pady=50, padx=20)
    button = Button(button_frame, text="CAVERN", command=forest)
    button.pack(side="top", pady=50, padx=20)
    button_frame.pack(side="top", fill="x")
    button = Button(root, text="Fight Early Access", command=encounter)
    button.pack(side="bottom", pady=10)


def open_new_window(name):
    new_window = Toplevel(root)
    new_window.title(name)
    new_window.geometry("500x400")


def encounter():
    clear_screen()
    monster = random.choice(monsters)
    monster_total_hp = monster["hp"]

    def encounter_message():
        venture["text"] = (f"You have encountered a {monster["name"]}")

    def fight_start():
        hp_label = Label(root, text=(f"HP: {monster_total_hp}"), fg="red")
        hp_label.pack(pady=5)

        button_frame = Frame()
        main_attack_btn = Button(button_frame, text="ATTACK",
                                 command=lambda: choose_attack(main_attack_btn, hp_label))
        main_attack_btn.pack(side="left", pady=50, padx=20)
        button_frame.pack(side="top", fill="x")

        global action_frame

        action_frame = Frame(root, bg="black")
        action_frame.pack(pady=10)

    def choose_attack(btn, hp_label):
        btn.config(state="disabled")

        for widget in action_frame.winfo_children():
            widget.destroy()

        atk_names = [atk["name"] for atk in attacks]
        selector = ttk.Combobox(
            action_frame, values=atk_names, state="readonly", font=font_explore)
        selector.set("Select Magic/Skill")
        selector.pack(pady=5)

        confirm = Button(action_frame, text="CONFIRM", width=10,
                         font=font_explore, command=lambda: finalize_attack(selector.get(), btn, hp_label))
        confirm.pack(pady=5)

    def finalize_attack(choice, btn, hp_label):
        nonlocal monster_total_hp
        global mana_player

        if choice == "Select Magic/Skill":
            return

        atk_data = next((a for a in attacks if a["name"] == choice), None)
        if choice:
            if "mana" in atk_data:
                if mana_player < atk_data["mana"]:
                    warn = Warning(text="Your dont have enough mana")
                    return
                else:
                    if "mana" in atk_data:
                        mana_player -= atk_data["mana"]

            dmg = player_attack + atk_data["dmg"]
            monster_total_hp -= dmg

        hp_label.config(text=f"HP: {monster_total_hp}")

        for widget in action_frame.winfo_children():
            widget.destroy()

        btn.config(state="normal")

        feedback = Label(
            action_frame, text=f"Dealt {dmg} damage!", fg="yellow")
        feedback.pack()
        feedback = Label(
            action_frame, text=f"You have {mana_player} mana left!", fg="light blue")
        feedback.pack()
        root.after(1000, feedback.destroy)

    venture = Label(root, text="You venture out into the forest")
    venture.pack(pady=(75, 25))
    root.after(1000, encounter_message)
    root.after(1500, fight_start)


def forest():
    clear_screen()


def shop():
    clear_screen()

    return_menu()


def menu_stats():
    clear_screen()
    label = Label(
        root,
        text="YOUR STATS")

    label.pack(pady=(75, 25))

    display_stats = Listbox(root)

    display_stats.insert(1, f"HEALTH: {player_hp}")
    display_stats.insert(2, f"ARMOR: {armor}")
    display_stats.insert(3, f"DAMAGE: {player_attack}")
    display_stats.insert(4, f"CRIT RATE: {crit_rate}%")

    display_stats.pack(side="top", pady=(40, 15))

    return_menu()


def game_menu():
    clear_screen()

    label = Label(
        root,
        text="WELCOME TO THE WORLD OF DRATHUS RPG")

    label.pack(pady=(75, 25))

    explore_button = Button(
        root,
        text="EXPLORE",
        command=explore)

    explore_button.pack(pady=(40, 15))

    shop_button = Button(
        root,
        text="SHOP",
        command=shop)

    shop_button.pack(pady=15)

    stats_button = Button(
        root,
        text="STATS",
        command=menu_stats)

    stats_button.pack(pady=15)

# The main loop


main_menu_label = Label(
    root,
    text="RPG-WORLD")

main_menu_label.pack(pady=(75, 25))

start_game_button = Button(
    root,
    text="START A NEW JOURNEY",
    command=game_menu)

start_game_button.pack(pady=(40, 15))

credit_menu_button = Button(
    root,
    text="CREDITS",
    command=None)

credit_menu_button.pack(pady=15)

exit_menu_button = Button(
    root,
    text="EXIT GAME",
    command=quit)

exit_menu_button.pack(pady=15)


root.mainloop()
