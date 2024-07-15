import os
clear = lambda: os.system('cls')
clear()
print(("Welcome to the Forgotten Alchemist's Legacy!").center(120))
print()
print()
overveiw = """"The Forgotten Alchemist’s Legacy" is a text-based adventure game where players explore the abandoned tower of Professor Thaddeus Evergreen, a legendary alchemist. The game is filled with puzzles, ethical dilemmas, and multiple endings based on player choices."""
print(overveiw)

intro = "You receive a cryptic letter inviting you to explore the alchemist's tower. The letter hints at five elemental keys required to unlock the secrets within: Fire, Water, Air, Space and Earth. The quest begins with your arrival at the mysterious, enchanted tower."
print()
print()
print(intro)
print()
print()


place = {
    "Wings Of Fire": "Fire Chamber",
    "Aqua Maze": "Water Chamber",
    "Earth Nexus":"Earth Chamber",
    "Realm Of Air":"Air Chamber",
    "Astra Cosmo":"Space Chamber"
         }
place_list = list(place.values())

c1 = input("Do you want to accept the challenge? (y/n): ")

if c1 == "y":
    print("You accept the challenge.")
    print()
    print("Now , You have to decide where you want to go first.")
    for i in range(len(place_list)):
        print(f"{i+1}. {place_list[i]}")
    c2=int(input("Enter the index of your desired locations: "))
    print()
    if c2 == 1:
        chosen_place = place_list[c2 - 1]
        print(f"You decided to go to {chosen_place}, Your are going to {list(place.keys())[c2 - 1]}.")
        print()
        from fire_chamber import play_flame_symbol_puzzle,play_temperature_control_test
                # Main game logic
        task_completed = 0

        if play_flame_symbol_puzzle():
            task_completed = 1
            print()
            print()
            if play_temperature_control_test():
                task_completed += 1

        print(f"Tasks completed: {task_completed}")
        
        
    elif c2 == 2:
        chosen_place = place_list[c2 - 1]
        print(f"You decided to go to {chosen_place}. \nYour are going to {list(place.keys())[c2 - 1]}.")
        
    elif c2 == 3:
        chosen_place = place_list[c2 - 1]
        print(f"You decided to go to {chosen_place}. \nYour are going to {list(place.keys())[c2 - 1]}.")
        
    elif c2 == 4:
        chosen_place = place_list[c2 - 1]
        print(f"You decided to go to {chosen_place}. \nYour are going to {list(place.keys())[c2 - 1]}.")
        
    elif c2 == 5:
        chosen_place = place_list[c2 - 1]
        print(f"You decided to go to {chosen_place}. \nYour are going to {list(place.keys())[c2 - 1]}.")
    else:
        print("Invalid input.")
        print("You are not playing it correctly.")
        print("GoodBye")

elif c1 == "n":
    print("You didn't accept the challenge.")
    print("Game Over.")
    print("Thank you for playing.")
else:
    print("Invalid input.")
    print("You are not playing it correctly.")
    print("GoodBye")