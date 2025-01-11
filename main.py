import os
from speak import speak
import json
def start_msg():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()

    print(("Welcome to the Forgotten Alchemist's Legacy!").center(120))
    speak("Welcome to the Forgotten Alchemist's Legacy!")

    print()
    print()
    overview = """The Forgotten Apprentice's Inheritance is a choose-your-own-adventure game in which you explore the empty Tower of Professor Thaddeus Evergreen, an infamous Alchemist. It is a game that is bursting with puzzles, moral questions, and even ending variations based on the chosen path of the player."""
    print(overview)
    return input("\nStart(y/n):")
    

def NewGame(game_state):
    intro = "The story also begins with getting a cryptic letter to investigate the tower of alchemy in each chambers. Fire, Water, Air, Space, Earth that reveals hints in the letter to gain access into these secrets through five elemental keys. The quest starts from the time you land on an enchanted tower out in the middle of nowhere."
    print()
    print()
    print(intro)
    print()
    print()
    place = {
        "Wings Of Fire": "Fire Chamber",
        "Aqua Maze": "Water Chamber",
        "Earth Nexus": "Earth Chamber",
        "Realm Of Air": "Air Chamber",
        "Astra Cosmo": "Space Chamber"
    }
    for index, value in enumerate(place.values(), start=1):
        print(f"{index}. {value}")

    choice = int(input("Enter the index for which chamber you want to go or 0 to exit: "))
    keys_collected = 0
    if choice== 1:
        game_state["location"] = "Wings Of Fire"
        if fire_chamber():
            keys_collected+=1
    elif choice == 2:
        game_state["location"] = "Aqua Maze"
        if water_chamber():
            keys_collected +=1
    elif choice == 3:
        game_state["location"] = "Earth Nexus"
        if earth_chamber():
            keys_collected +=1
    elif choice == 4:
        game_state["location"] = "Realm Of Air"
        if air_chamber():
            keys_collected +=1
    elif choice == 5:
        game_state["location"] = "Astra Cosmo"
        if space_chamber():
            keys_collected +=1
    elif choice ==0:
        exit_game()
    else:
        print("Enter a correct index")
    if keys_collected == 5:
        if display_final_msg():
            if play_final_part():
                print("You have succesfully completed the ") # complete it
                last_choice = input("Do you want to restart? (y/n) ")
                if last_choice.lower() == "y":
                    restart_game()
                else:
                    end_game()

def display_initial_msg(letter, element = ""):
    print()
    print("The letter has the following message:")
    print("""
Dear Seeker of Knowledge,

You have been chosen for a task of great importance and mystery. Professor Thaddeus Evergreen, the renowned and enigmatic alchemist, has left behind a legacy that awaits only the most worthy to uncover. His tower, shrouded in secrets and brimming with puzzles, calls to you.

In the heart of this tower lie the five elemental keys: Fire, Water, Air, Space, and Earth. Each key holds the power to unlock the profound mysteries of alchemy and reveal truths long hidden from the world. Your journey begins at the tower, an enchanted bastion of arcane wisdom, standing isolated in a forgotten land.

To commence your quest, you must solve the following puzzle to unlock the chamber gate. Within the pages of this letter, a clue awaits you. Read carefully and heed the words, for they will guide you through the initial trial.
""")
    print(letter)
    print("""
Find the answer, and you shall begin your journey into the depths of Professor Evergreen’s tower. Each elemental key is guarded by challenges that will test your wit, resolve, and moral compass. Choose wisely, for the path you take will shape your destiny and the fate of the alchemist's legacy.

May your mind be sharp and your heart steadfast.

With anticipation,
The Guardians of the Tower

Good luck, adventurer. The tower awaits.""")
    choice2 = input("Enter the answer to the puzzle or 0 to exit: ")
    if choice2 == 0:
        exit_game()
    elif choice2.capitalize() == element:
      print(f"You guess it right. The gate of {element} is opening. Have a great adventure.")
      return True
    
def gamelogic(games, element):
    task_completed = 0 
    for game in games: 
        while True: 
            if game(): # Call the function 
                if element != "blazing_bridge_trap":
                    task_completed += 1 
                    break # Move to the next game 
                else:
                    task_completed +=0
                    break
            else: 
                print("You failed to complete the current puzzle.") 
                choice = input("Would you like to try again (y/n)? ") 
                if choice.lower() != 'y': 
                    print("Exiting the game. Better luck next time!")
                    exit_game()
                else:
                    print("Restarting the puzzle. Give it another shot!")
                    restart_puzzle(game)             
    return task_completed # Exit the game return task_completed task_completed

def fire_chamber(game_state):
    letter = """
"I am a dancer, bright and bold,
Yet in my presence, none can hold.
I consume all, yet give new life,
In my heart, both warmth and strife.
Tame me, and your path is clear,
But lose control, and you must fear.
What am I?"
"""
    if  display_initial_msg(letter, "Fire"):
        from fire_chamber import play_flame_symbol_puzzle, play_temperature_control_test, blazing_bridge_trap, fiery_guardian_combat, flame_whispers_riddles, combustion_chess, fire_trap_mechanism, path_of_infernos
        game_array_fire = [play_flame_symbol_puzzle, play_temperature_control_test, blazing_bridge_trap, fiery_guardian_combat, flame_whispers_riddles, combustion_chess, fire_trap_mechanism, path_of_infernos]
        tasks = gamelogic(game_array_fire, "blazing_bridge_trap")
        if tasks == 10:
            print("You have succesfully completed all the tasks and claimed the fire elemental key.")
            return True
        else: 
            choice3 = input("Do you want to replay(y/n)? ")
            if choice3.capitalize() == "Y":
                pass

def water_chamber(game_state):
    letter = """
"I am the mirror of the sky,
Yet I am not made of clouds or light.
I flow through valleys, soft and sly,
And with me, you quench your thirst and might.
My embrace can be gentle or fierce,
And my depths hold secrets vast and clear.
What am I?"

"""
    if display_initial_msg(letter, "water"):
        from water_chamber import play_with_water
        game_array_water = [play_with_water]
        tasks = gamelogic(game_array_water)
        if tasks == 10:
            print("You have succesfully completed all the tasks and claimed the water elemental key.")

def earth_chamber(game_state):
    letter ="""
Riddle:

"I am ancient, yet ever new,
Rooted deep where shadows grow.
My strength lies in the quiet, the still,
And in my embrace, all seeds will fulfill.
I shape the land with my patient hand,
And within me, great treasures stand.
What am I?"
"""
    if display_initial_msg(letter, "earth"):
        from earth_chamber import play_with_earth
        game_array_earth = [play_with_earth]
        tasks = gamelogic(game_array_earth)
        if tasks == 10:
            print("You have succesfully completed all the tasks and claimed the earth elemental key.")

def air_chamber(game_state):
    letter = """
Riddle:

"I am invisible but ever near,
Moving swiftly without a trace.
I fill your lungs and carry sound,
And in my grasp, things gently sway.
I can be a whisper or a storm,
And in my touch, the world transforms.
What am I?"
"""
    if display_initial_msg(letter, "air"):
        from air_chamber import play_with_air
        game_array_air = [play_with_air]
        tasks = gamelogic(game_array_air)
        if tasks == 10:
            print("You have succesfully completed all the tasks and claimed the air elemental key.")

def space_chamber(game_state):
    letter = """

Riddle:

"I stretch beyond the reach of sight,
A vast domain where stars ignite.
I hold the realms of time and space,
And in my depths, secrets find their place.
I am both the limit and the guide,
In my embrace, the answers hide.
What am I?"
"""
    if display_initial_msg(letter, "space"):
        from space_chamber import play_with_space
        game_array_space = [play_with_space]
        tasks = gamelogic(game_array_space)
        if tasks == 10:
            print("You have succesfully completed all the tasks and claimed the space elemental key.")

def display_final_msg(game_state):
    final_part_of_letter ="""
Congratulations, Seeker.

You have traversed the trials and secured all five keys. As you place these keys upon this letter, a crucial step remains before you can unlock the true legacy of Professor Thaddeus Evergreen.

Before you lies a grand door, the gateway to the heart of the alchemist’s legacy. To open this door, you must place each key in its rightful position according to the following riddle. Each key corresponds to a specific place, and only by placing them correctly will you reveal the secrets within.

Final Riddle:

"First, where strength and roots hold tight,
Lay the symbol of ancient might.

Second, where whispers ride the breeze,
Place the token that moves with ease.

Third, where shadows dance with light,
Position the spark that burns so bright.

Fourth, where reflections show what's pure,
Set the emblem that flows secure.

Last, where the endless void does trace,
Put the sign from boundless space."

Arrange the keys accordingly to unlock the door and gain access to the alchemist’s ultimate legacy. The path you have walked has led you to this final moment of discovery. Use your knowledge and insight to unveil what lies beyond.

May your resolve be unwavering as you complete your journey and unlock the true secrets of Professor Evergreen’s Tower.

With reverence and respect,
The Guardians of the Tower

Good luck, adventurer. The culmination of your quest awaits."""
    print(final_part_of_letter)
    print("(1 for fire, 2 for water, 3 for earth, 4 for air, and 5 for space)")
    keys_order = input("Enter the order of keys (like 1,2,3,4,5):")
    if keys_order == "3,4,1,2,5":
        return True

def exit_game():
    pass
def restart_puzzle(game):
    pass
def play_final_part():
    from final_part import play_final_part

def restart_game():
    pass
def end_game():
    pass
def game_loop(game_state): 
    while True:
        NewGame(game_state)
def main_menu(): 
    print("\nMain Menu:") 
    print("1. Start New Game") 
    print("2. Load Game") 
    print("3. Quit") 
    return input("Choose an option (1/2/3): ")

def start_new_game(player_name): 
    game_state = { "player_name": player_name, 
                    "location": "entrance", 
                    "health": 100, 
                    "inventory": [] } 
    return game_loop(game_state)

def load_game(): 
    try: 
        with open('saved_game.json', 'r') as f: 
            game_state = json.load(f)
            return game_loop(game_state) 
    except FileNotFoundError: 
        print("No saved game found. Starting a new game.")
        return start_new_game()
    
def save_game(game_state): 
    with open('saved_game.json', 'w') as f: 
        json.dump(game_state, f) 
        print("Game saved.")
        
def play_game():
    if start_msg().lower() == "y":
        player_name = input("What is your name, brave adventurer? ")
        while True:
            choice = main_menu()
            if choice == 1:
                game_stat = start_new_game(player_name)
            elif choice == "2": 
                game_state = load_game() 
            elif choice == "3": 
                print("Thank you for playing The Forgotten Alchemist's Legacy. Farewell!") 
                break 
            else: print("Invalid choice. Try again.")
        
            save_game(game_state)