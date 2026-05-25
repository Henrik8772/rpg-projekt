# Imports

from random import randint
import tkinter
import tkinter.font as tkFont
from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox

# world varibles


place_id = ""

monster = ""

# Stat varibles
player_speed = 360
player_hp = 100
player_hp_total = player_hp
player_attack = 7
gold = 0
potions = 0
armor = 8
mana_total = 50
mana_player = mana_total
crit_rate = 20
luck = 0.20
luck_multi = randint(1, 2)

damage = player_attack


# Monsters

monster_attack = ""

monsters = [
    {
        "id": "forest",
        "name": "Goblin",
        "hp": randint(45, 125),
        "pressure": randint(1, 5),
        "attacks": [
            {
                "name": "Clubing",
                "dmg": randint(10, 25)
            }
        ]
    },

    {
        "id": "mountains",
        "name": "Kobalt",
        "hp": randint(65, 120),
        "pressure": randint(1, 5),
        "attacks": [
            {
                "name": "Bite",
                "dmg": randint(12, 20)
            }
        ]
    },

    {
        "id": "cavern",
        "name": "Screeching Bat",
        "hp": randint(20, 70),
        "pressure": randint(1, 5),
        "attacks": [
            {
                "name": "Noise Blast",
                "dmg": randint(10, 25)
            }
        ]
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
    {
        "name": "DEBUGGER",
        "dmg": 1000
    },
    {
        "name": "Fatal Strike",
        "dmg": randint(15, 25)
    },

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

# Messagebox configs
root.option_add("*Messagebox*font", font_explore)

# Funktions (def)


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def stat_fix():
    global mana_player, player_hp_total
    mana_player = mana_total
    player_hp_total = player_hp


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
    button = Button(button_frame, text="MOUNTAINS", command=mountains)
    button.pack(side="right", pady=50, padx=20)
    button = Button(button_frame, text="CAVERN", command=cavern)
    button.pack(side="top", pady=50, padx=20)
    button_frame.pack(side="top", fill="x")


def keep_playing():
    clear_screen()
    label = Label(root, text="WANNA KEEP EXPLORING?")
    label.pack(pady=(75, 25))
    button_frame = Frame()

    button = Button(button_frame, text="YES", command=explore)
    button.pack(side="left", pady=50, padx=20)
    button = Button(button_frame, text="NO", command=game_menu)
    button.pack(side="right", pady=50, padx=20)
    button_frame.pack(side="top")


def ran_away():
    clear_screen()
    label = Label(root, text="YOU MANAGED TO ESCAPE!!")
    label.pack(pady=(75, 25))
    button_frame = Frame()

    label2 = Label(root, text="You wanna explore somewhere else?")
    label2.pack(pady=(10, 25))

    button = Button(button_frame, text="YES", command=explore)
    button.pack(side="left", pady=50, padx=20)
    button = Button(button_frame, text="NO", command=game_menu)
    button.pack(side="right", pady=50, padx=20)
    button_frame.pack(side="top")


def open_new_window(name):
    new_window = Toplevel(root)
    new_window.title(name)
    new_window.geometry("500x400")


def encounter():
    clear_screen()
    stat_fix()
    monster = random.choice(monsters)

    for id in monster["id"]:
        if id in monster["id"] != place_id:
            monster = random.choice(monsters)

    def encounter_message():
        venture["text"] = (
            f"You have encountered a {monster["name"]} with pressure lvl: {monster['pressure']}")

    def fight_start():
        global stat_ui
        hp_label = Label(root, text=(f"HP: {monster_total_hp}"), fg="red")
        hp_label.pack(pady=5)

        ui_frame = Frame()
        main_attack_btn = Button(ui_frame, text="ATTACK",
                                 command=lambda: choose_attack(main_attack_btn, hp_label))
        main_attack_btn.pack(side="left", pady=50, padx=20)
        run_away_btn = Button(ui_frame, text="RUN AWAY", command=escape)
        run_away_btn.pack(side="right", pady=50, padx=20)
        ui_frame.pack(side="top", fill="x")

        stat_ui = Listbox(root)
        stat_ui.insert(1, f"HEALTH: {player_hp_total}")
        stat_ui.insert(2, f"MANA: {mana_total}")
        stat_ui.pack(side="left", pady=30, padx=20)

        global action_frame

        action_frame = Frame(root, bg="black")
        action_frame.pack(pady=10)

    def escape():
        if monster["pressure"] == 1 or 2 or 3:

            escape_chance = 0.50
            escapist = escape_chance * (player_speed / 100)
            escape_total = escape_chance + escapist

            if escape_total > 1:
                escape_total = 1

            if random.random() < escape_total:
                ran_away()
            else:
                return

        if monster["pressure"] == 4:

            escape_chance = 0.30
            escapist = escape_chance * (player_speed / 100)
            escape_total = escape_chance + escapist

            if escape_total > 1:
                escape_total = 1

            if random.random() < escape_total:
                ran_away()
            else:
                return

        if monster["pressure"] == 5:

            escape_chance = 0.25
            escapist = escape_chance * (player_speed / 100)
            escape_total = escape_chance + escapist

            if escape_total > 1:
                escape_total = 1

            if random.random() < escape_total:
                ran_away()
            else:
                return

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
                    warn = messagebox.showwarning(
                        message="You dont have enough mana to cast the magic!!!", )
                    return

                else:
                    if "mana" in atk_data:
                        mana_player -= atk_data["mana"]

            dmg = player_attack + atk_data["dmg"]
            monster_total_hp -= dmg

            if monster_total_hp < 0:
                monster_total_hp = 0

        if monster_total_hp > 0:
            global player_hp_total
            monster_attack = random.choice(monster["attacks"])
            monster_dmg = monster_attack["dmg"]
            player_hp_total -= monster_dmg
            if player_hp_total < 0:
                player_hp_total = 0

        hp_label.config(text=f"HP: {monster_total_hp}")

        for widget in action_frame.winfo_children():
            widget.destroy()

        btn.config(state="normal")

        def player_feedback():
            feedback = Label(
                action_frame, text=f"Dealt {dmg} damage!", fg="yellow")
            feedback.pack()
            stat_ui.delete(1)
            stat_ui.insert(1, f"MANA: {mana_player}")
            feedback1 = Label(
                action_frame, text=f"You have {mana_player} mana left!", fg="light blue")
            feedback1.pack()
            root.after(1000, feedback.destroy)
            root.after(1000, feedback1.destroy)

        def feedback_monster():
            monster_feedback = Label(
                action_frame, text=f"The monster used {monster_attack["name"]} dealing {monster_dmg} to you!!", fg="yellow")
            monster_feedback.pack()
            stat_ui.delete(0)
            stat_ui.insert(0, f"HEALTH: {player_hp_total}")
            root.after(1000, monster_feedback.destroy)

        if monster_total_hp != 0:
            player_feedback()
            root.after(2000, feedback_monster)

        if monster_total_hp <= 0:
            global gold
            reward = randint(10, 30) * (monster["hp"]/100)
            if random.random() < luck:
                reward *= luck_multi
            gold += reward
            victory = messagebox.showinfo(
                icon="question", message=f"Yippie you won and earned yourself {reward:.0f} gold coins!!!")
            keep_playing()

    if monster["id"] == place_id:
        monster_total_hp = monster["hp"]
        venture = Label(root, text=f"You venture out into the {place_id}")
        venture.pack(pady=(75, 25))
        root.after(1000, encounter_message)
        root.after(1500, fight_start)


def forest():
    global place_id
    place_id = "forest"
    clear_screen()
    encounter()


def cavern():
    global place_id
    place_id = "cavern"
    clear_screen()
    encounter()


def mountains():
    global place_id
    place_id = "mountains"
    clear_screen()
    encounter()


def inventory():
    clear_screen()
    return_menu()


def shop():
    clear_screen()
    label = Label(root, text="ORXYS SHOP")
    label.pack(pady=(75, 25))

    label_gold = Label(root, text=f"GOLD: {gold:.0f}", fg="gold")
    label_gold.pack()

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
    display_stats.insert(4, f"MANA: {mana_player}")
    display_stats.insert(5, f"CRIT RATE: {crit_rate}%")

    display_stats.pack(side="top", pady=(40, 15))

    return_menu()


def game_menu():
    clear_screen()
    stat_fix()

    label = Label(
        root,
        text="WELCOME TO THE WORLD OF DRATHUS RPG")

    label.pack(pady=(75, 25))

    label_gold = Label(root, text=f"GOLD: {gold:.0f}", fg="gold")
    label_gold.pack()

    explore_button = Button(
        root,
        text="EXPLORE",
        command=explore)

    explore_button.pack(pady=(40, 15))

    inventory_button = Button(
        root,
        text="INVENTORY",
        command=inventory)

    inventory_button.pack(pady=(15))

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
