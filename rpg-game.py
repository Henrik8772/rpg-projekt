# Imports

from random import randint
import tkinter
import tkinter.font as tkFont
from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox

# world varibles

item_inventory = []

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
boss_attack = ""

bosses = [
    {
        "id": "goblin_boss",
        "zone": "forest",
        "required_item": "Kings Idol",
        "name": "Goblin King",
        "hp": 1000,
        "chance_for_pressure": 0,
        "attacks": [
            {
                "name": "Kings Judgment",
                "dmg_type": "percentage",
                "percent_range": (0.30, 0.50),
                "accuracy": 0.3
            },

            {
                "name": "Rapid Smash",
                "dmg_range": (10, 20),
                "hits_range": (1, 3),
                "accuracy": 0.5
            },

            {
                "name": "Stomp Fury",
                "dmg_range": (5, 7),
                "hits_range": (2, 6),
                "accuracy": 0.5
            }

        ]
    }
]

boss_items = [
    {
        "item_id": "goblin_boss",
        "name": "Kings Idol",
    }
]

monsters = [
    {
        "id": "forest",
        "name": "Goblin",
        "hp_range": (45, 125),
        "attacks": [
            {
                "name": "Clubing",
                "dmg_range": (10, 25)
            }
        ],
        "basic_drops": [
            {
                "name": "Scrap Metal",
                "drop_rate": 0.75,
                "quality_range": (0, 0),
                "quantity_range": (1, 10),
                "base_worth_range": (1, 1)
            },

            {
                "name": "Metal Alloy",
                "drop_rate": 0.20,
                "quality_range": (1, 100),
                "quantity_range": (1, 3),
                "base_worth_range": (3, 7)
            },

            {
                "name": "Mana Stone",
                "drop_rate": 0.05,
                "quality_range": (40, 100),
                "quantity_range": (1, 2),
                "base_worth_range": (10, 30)
            },

            {
                "name": "Transmutated Mana Stone",
                "drop_rate": 0.005,
                "quality_range": (80, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (100, 300)
            },

            {
                "name": "Kings Idol",
                "drop_rate": 0.009,
                "quality_range": (100, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (1, 1)
            }
        ],
        "monster_drops": [
            {
                "name": "Goblin Ear",
                "drop_rate": 0.5,
                "quality_range": (1, 100),
                "quantity_range": (1, 2),
                "base_worth_range": (2, 10)
            },

            {
                "name": "Lesser Goblin Core",
                "drop_rate": 0.4,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (10, 20)
            },

            {
                "name": "Mana Stone",
                "drop_rate": 0.5,
                "quality_range": (40, 100),
                "quantity_range": (1, 2),
                "base_worth_range": (10, 30)
            },

            {
                "name": "Kings Idol",
                "drop_rate": 0.02,
                "quality_range": (100, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (1, 1)
            }


        ],
        "rare_drops": [
            {
                "name": "Tome of Knowledge",
                "drop_rate": 0.03,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (200, 200)
            },

            {
                "name": "Medium Goblin Core",
                "drop_rate": 0.8,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (40, 90)
            },

            {
                "name": "Large Goblin Core",
                "drop_rate": 0.2,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (80, 170)
            },

            {
                "name": "Large Mana Stone",
                "drop_rate": 0.4,
                "quality_range": (50, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (100, 100)
            },

            {
                "name": "Wooden Club",
                "drop_rate": 0.6,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (20, 20),
                "weapon_stats": [
                    {
                        "dmg": 5
                    }
                ]
            },

            {
                "name": "Kings Idol",
                "drop_rate": 0.5,
                "quality_range": (100, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (1, 1)
            }
        ],
        "elite_drops": [
            {
                "name": "Goblin Kings Fury",
                "drop_rate": 0.001,
                "quality_range": (100, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (1500, 1500),
                "weapon_stats": [
                    {
                        "dmg": 40
                    }
                ]
            },

            {
                "name": "Divine Goblin Core",
                "drop_rate": 0.4,
                "quality_range": (70, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (200, 200)
            },

            {
                "name": "Large Goblin Core",
                "drop_rate": 0.75,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (80, 170)
            },

            {
                "name": "Tome of Knowledge",
                "drop_rate": 0.5,
                "quality_range": (1, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (200, 200)
            },

            {
                "name": "Potent Mana Stone",
                "drop_rate": 0.6,
                "quality_range": (60, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (175, 175)
            }

        ],

        "granted_drops": [
            {
                "name": "Kings Idol",
                "drop_rate": 1,
                "quality_range": (100, 100),
                "quantity_range": (1, 1),
                "base_worth_range": (1, 1)
            }
        ]

    },

    {
        "id": "mountains",
        "name": "Kobalt",
        "hp_range": (65, 120),
        "attacks": [
            {
                "name": "Bite",
                "dmg_range": (12, 20)
            }
        ],
        "basic_drops": [

        ],
        "monster_drops": [

        ],
        "rare_drops": [

        ],
        "elite_drops": [

        ]
    },

    {
        "id": "cavern",
        "name": "Screeching Bat",
        "hp_range": (20, 70),
        "attacks": [
            {
                "name": "Noise Blast",
                "dmg_range": (10, 25)
            }
        ],
        "basic_drops": [

        ],
        "monster_drops": [

        ],
        "rare_drops": [

        ],
        "elite_drops": [

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
        "dmg_range": (1000, 1000)
    },
    {
        "name": "Fatal Strike",
        "dmg_range": (15, 25)
    },

    # Mana/Magic attacks
    {
        "name": "Death's Dance",
        "dmg_range": (10, 20),
        "mana": 20
    },

    {
        "name": "Fireball",
        "dmg_range": (20, 40),
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

    active_boss = None
    for boss in bosses:
        if boss["zone"] == place_id and boss["required_item"] in item_inventory:
            active_boss = boss
            break

    if active_boss:
        boss_button = Button(root, text=f"CHALLANGE {active_boss["name"].upper()}", width=30,
                             fg="red", activeforeground="red", command=lambda b=active_boss: boss_fight(b))
        boss_button.pack(pady=20)

    return_menu()


def boss_fight(boss_data):
    clear_screen()
    boss_encounter(boss_data)


def boss_encounter(boss):
    clear_screen()
    stat_fix()

    boss_total_hp = boss["hp"]
    boss_name = boss["name"]

    venture = Label(
        root, text=f"The {boss["required_item"]} starts glowing wildly...")
    venture.pack(pady=(75, 25))

    def encounter_message():
        venture["text"] = (
            f"You have realised the {boss_name} from its slumber, PREPARE FOR BATTLE!!")
        venture.config(fg="red")

    def fight_start():
        global stat_ui, action_frame

        hp_label = Label(root, text=f"BOSS HP: {boss_total_hp}", fg="red")
        hp_label.pack(pady=5)

        ui_frame = Frame()
        main_attack_btn = Button(ui_frame, text="ATTACK",
                                 command=lambda: choose_attack(main_attack_btn, hp_label))
        main_attack_btn.pack(side="left", pady=50, padx=20)

        run_away_btn = Button(ui_frame, text="CAN'T ESCAPE",
                              state="disabled", fg="grey")
        run_away_btn.pack(side="right", pady=50, padx=20)
        ui_frame.pack(side="top", fill="x")

        action_frame = Frame(root, bg="black")
        action_frame.pack(side="top", pady=10)

        stat_ui = Listbox(root)
        stat_ui.insert(0, f"HEALTH: {player_hp_total:.0f}")
        stat_ui.insert(1, f"MANA: {mana_player}")
        stat_ui.pack(side="top", anchor="w", pady=30, padx=20)

    def choose_attack(btn, hp_label):
        btn.config(state="disabled")

        for widget in action_frame.winfo_children():
            widget.destroy()

        atk_names = [atk["name"] for atk in attacks]
        selector = ttk.Combobox(
            action_frame, values=atk_names, state="readonly", font=font_explore)
        selector.set("select Magic/Skill")
        selector.pack(pady=5)

        confirm = Button(action_frame, text="CONFIRM", width=10, font=font_explore,
                         command=lambda: finalize_attack(selector.get(), btn, hp_label))
        confirm.pack(pady=5)

    def finalize_attack(choice, btn, hp_label):
        nonlocal boss_total_hp
        global mana_player, player_hp_total

        if choice == "Select Magic/Skill":
            btn.config(state="normal")
            return

        atk_data = next((a for a in attacks if a["name"] == choice), None)

        if atk_data:
            if "mana" in atk_data:
                if mana_player < atk_data["mana"]:
                    messagebox.showwarning(
                        message="You don't have enough mana to cast this magic!!!")
                    btn.config(state="normal")
                    return
                else:
                    mana_player -= atk_data["mana"]

            skill_dmg = random.randint(
                atk_data["dmg_range"][0], atk_data["dmg_range"][1])
            dmg = player_attack + skill_dmg
            boss_total_hp -= dmg

            if boss_total_hp < 0:
                boss_total_hp = 0

        if boss_total_hp > 0:
            boss_attack_data = random.choice(boss["attacks"])

            if "accuracy" in boss_attack_data and random.random() > boss_attack_data["accuracy"]:
                boss_dmg = 0
                boss_missed = True

            else:
                boss_missed = False
                boss_dmg = 0

                if "dmg_range" in boss_attack_data:
                    if "hits_range" in boss_attack_data:
                        num_hits = random.randint(
                            boss_attack_data["hits_range"][0], boss_attack_data["hits_range"][1])
                    else:
                        num_hits = 1
                    for _ in range(num_hits):
                        boss_dmg = random.randint(
                            boss_attack_data["dmg_range"][0], boss_attack_data["dmg_range"][1])

                elif boss_attack_data.get("dmg_type") == "percentage":
                    percent_dmg = random.uniform(
                        boss_attack_data["percent_range"][0], boss_attack_data["percent_range"][1])
                    boss_dmg = int(player_hp_total * percent_dmg)

                else:
                    boss_dmg = 15

            player_hp_total -= boss_dmg
            if player_hp_total < 0:
                player_hp_total = 0

        hp_label.config(text=f"BOSS HP: {boss_total_hp}")

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

        def boss_feedback():
            if boss_missed:
                text_msg = f"The boss used {boss_attack_data["name"]} but MISSED!!!"
            else:
                text_msg = f"The {boss} used {boss_attack_data["name"]} dealing {boss_dmg} to you!!"
            boss_text_feedback = Label(
                action_frame, text=text_msg, fg="yellow")
            boss_text_feedback.pack()
            stat_ui.delete(0)
            stat_ui.insert(0, f"HEALTH: {player_hp_total:.0f}")
            root.after(1000, boss_text_feedback.destroy)

        if boss_total_hp != 0:
            player_feedback()
            root.after(2000, boss_feedback)

        if player_hp_total <= 0:
            messagebox.showinfo(
                message=f"GAME OVER!! You lost to The {boss_name}, you have died...")
            quit

        if boss_total_hp <= 0:
            global gold

            reward = randint(300, 500)
            if random.random() < luck:
                reward *= luck_multi
            gold += reward

            messagebox.showinfo(
                icon="question", message=f"Yippie you won and earned yourself {reward:.0f} gold coins!!!")

            if boss["required_item"] in item_inventory:
                item_inventory.remove(boss["required_item"])
                messagebox.showinfo(
                    message=f"The {boss["required_item"]} stops glowing and starts to disintegrate, disappearing before your eyes...")

            game_menu()

    root.after(1000, encounter_message)
    root.after(1500, fight_start)


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


def encounter():
    clear_screen()
    stat_fix()

    available_monsters = [m for m in monsters if m["id"] == place_id]
    if not available_monsters:
        return
    monster = random.choice(available_monsters)

    monster_total_hp = random.randint(
        monster["hp_range"][0], monster["hp_range"][1])

    roll_pressure = random.randint(1, 100)

    if roll_pressure >= 85 and roll_pressure < 95:
        pressure = 4
    elif roll_pressure >= 95 and roll_pressure <= 100:
        pressure = 5
    elif roll_pressure >= 60 and roll_pressure < 85:
        pressure = random.randint(1, 3)
    else:
        pressure = 0

    def encounter_message():
        if pressure > 0:
            venture["text"] = (
                f"You have encountered a {monster["name"]} with pressure lvl: {pressure}")
        else:
            venture["text"] = (
                f"You have encountered a {monster["name"]}")

    def fight_start():
        global stat_ui
        global action_frame
        nonlocal monster_total_hp

        if pressure in [1, 2, 3]:
            extra_hp = (monster_total_hp / 10) * 2
            monster_total_hp = monster_total_hp + extra_hp

        elif pressure == 4:
            monster_total_hp = monster_total_hp * 2

        elif pressure == 5:
            monster_total_hp = monster_total_hp * 4

        else:
            monster_total_hp = monster_total_hp

        hp_label = Label(root, text=(f"HP: {monster_total_hp:.0f}"), fg="red")
        hp_label.pack(pady=5)

        ui_frame = Frame()
        main_attack_btn = Button(ui_frame, text="ATTACK",
                                 command=lambda: choose_attack(main_attack_btn, hp_label))
        main_attack_btn.pack(side="left", pady=50, padx=20)
        run_away_btn = Button(ui_frame, text="RUN AWAY", command=escape)
        run_away_btn.pack(side="right", pady=50, padx=20)
        ui_frame.pack(side="top", fill="x")

        action_frame = Frame(root, bg="black")
        action_frame.pack(side="top", pady=10)

        stat_ui = Listbox(root)
        stat_ui.insert(1, f"HEALTH: {player_hp_total}")
        stat_ui.insert(2, f"MANA: {mana_total}")
        stat_ui.pack(side="top", anchor="w", pady=30, padx=20)

    def escape():
        if pressure in [1, 2, 3]:
            escape_chance = 0.50
        elif pressure == 4:
            escape_chance = 0.30
        elif pressure == 5:
            escape_chance = 0.25
        else:
            escape_chance = 0.50
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

            skill_dmg = random.randint(
                atk_data["dmg_range"][0], atk_data["dmg_range"][1])

            dmg = player_attack + skill_dmg
            monster_total_hp -= dmg

            if monster_total_hp < 0:
                monster_total_hp = 0

        if monster_total_hp > 0:
            global player_hp_total
            monster_attack_data = random.choice(monster["attacks"])
            if "dmg_range" in monster_attack_data:
                monster_dmg = random.randint(
                    monster_attack_data["dmg_range"][0], monster_attack_data["dmg_range"][1])
            else:
                monster_dmg = 10
            if pressure == 5:
                monster_dmg += 12

            elif pressure == 4:
                monster_dmg += 7

            elif pressure in [1, 2, 3]:
                monster_dmg += 4

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
                action_frame, text=f"The monster used {monster_attack_data["name"]} dealing {monster_dmg} to you!!", fg="yellow")
            monster_feedback.pack()
            stat_ui.delete(0)
            stat_ui.insert(0, f"HEALTH: {player_hp_total}")
            root.after(1000, monster_feedback.destroy)

        if monster_total_hp != 0:
            player_feedback()
            root.after(2000, feedback_monster)

        if monster_total_hp <= 0:
            global gold
            reward = randint(10, 30) * (monster["hp_range"][1]/100)
            if random.random() < luck:
                reward *= luck_multi
            gold += reward

            basic_loot = None
            loot = None
            granted_loot = None

            if pressure == 0:
                if monster.get("basic_drops"):
                    basic_loot = random.choice(monster["basic_drops"])
                    if random.random() > basic_loot["drop_rate"]:
                        basic_loot = None

            elif pressure in [1, 2, 3]:
                if monster.get("basic_drops"):
                    basic_loot = random.choice(monster["basic_drops"])
                    if random.random() > basic_loot["drop_rate"]:
                        basic_loot = None
                if monster.get("monster_drops"):
                    loot = random.choice(monster["monster_drops"])
                    if random.random() > loot["drop_rate"]:
                        loot = None

            elif pressure == 4:
                if monster.get("basic_drops"):
                    basic_loot = random.choice(monster["basic_drops"])
                    if random.random() > basic_loot["drop_rate"]:
                        basic_loot = None
                if monster.get("rare_drops"):
                    loot = random.choice(monster["rare_drops"])
                    if random.random() > loot["drop_rate"]:
                        loot = None

            elif pressure == 5:
                if monster.get("basic_drops"):
                    basic_loot = random.choice(monster["basic_drops"])
                    if random.random() > basic_loot["drop_rate"]:
                        basic_loot = None
                if monster.get("elite_drops"):
                    loot = random.choice(monster["elite_drops"])
                    if random.random() > loot["drop_rate"]:
                        loot = None

                if monster.get("granted_drops"):
                    granted_loot = random.choice(monster["granted_drops"])

            messagebox.showinfo(
                icon="question", message=f"Yippie you won and earned yourself {reward:.0f} gold coins!!!")

            if basic_loot:
                basic_quantity = random.randint(
                    basic_loot["quantity_range"][0], basic_loot["quantity_range"][1])
                for _ in range(basic_quantity):
                    item_inventory.append(basic_loot["name"])

            if granted_loot:
                granted_quantity = random.randint(
                    granted_loot["quantity_range"][0], granted_loot["quantity_range"][1])
                for _ in range(granted_quantity):
                    item_inventory.append(granted_loot["name"])

            if loot:
                loot_quantity = random.randint(
                    loot["quantity_range"][0], loot["quantity_range"][1])
                for _ in range(loot_quantity):
                    item_inventory.append(loot["name"])

            if basic_loot is None and loot is None and granted_loot is None:
                messagebox.showinfo(
                    icon="question", message="You got nothing :(")
            else:
                msg_text = "You got "

                if basic_loot:
                    msg_text += f"{basic_quantity}x {basic_loot["name"]}"

                if granted_loot:
                    if basic_loot:
                        msg_text += f" and {granted_quantity}x {granted_loot["name"]}"
                    else:
                        msg_text += f"{granted_quantity}x {granted_loot["name"]}"

                if loot:
                    if basic_loot or granted_loot:
                        msg_text += f" and {loot_quantity}x {loot["name"]}"
                    else:
                        msg_text += f"{loot_quantity}x {loot["name"]}"

                messagebox.showinfo(icon="question", message=msg_text)

            item_inventory.sort()
            keep_playing()

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


def update_inventory():
    if "display_items" in globals() and display_items.winfo_exists():
        display_items.delete(0, END)
        if item_inventory:
            for item in sorted(set(item_inventory)):
                display_items.insert(
                    END, f"{item_inventory.count(item)}x {item}")


def inventory():
    global display_items
    clear_screen()

    label = Label(root, text="YOUR INVENTORY")
    label.pack(pady=(75, 25))

    display_items = Listbox(root)
    display_items.pack(side="top", pady=(40, 15))
    update_inventory()
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
