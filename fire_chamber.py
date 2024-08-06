import random
from speak import speak

# Define the symbols and their meanings (example symbols)
symbols = {
    "🔥": "Ignition",
    "🌡️": "Heat Intensity",
    "🔄": "Transformation",
    "⚖️": "Balance",
    "⏳": "Time"
}

# Hints for each symbol in corresponding order
hints = [
    "I'm the spark that sets things ablaze, In engines, rockets, and stoves I play. Turn the key or strike a match, I'm the force that lights the hatch. What am I?",
    "Measure of thermal energy intensity.",
    "Process of changing one form into another.",
    "What hangs in the middle, teetering on a beam? Equilibrium’s secret, a delicate dream.",
    "I can crawl, I can fly, I have hands but no legs or wings either. What am I?"
]

# Shuffle symbols and hints together in the same order
def shuffle_symbols_and_hints():
    symbol_list = list(symbols.keys())
    shuffled_symbols_display = symbol_list[:]
    random.shuffle(shuffled_symbols_display)
    shuffled_symbols = symbol_list[:]  # Keep a consistent shuffled order for hints and correct sequence
    random.shuffle(shuffled_symbols)
    shuffled_hints = [hints[list(symbols.keys()).index(symbol)] for symbol in shuffled_symbols]
    return shuffled_symbols_display, shuffled_symbols, shuffled_hints

# Generate a random sequence of symbols and corresponding shuffled hints for the puzzle
def generate_puzzle_sequence():
    shuffled_symbols_display, shuffled_symbols, shuffled_hints = shuffle_symbols_and_hints()
    return shuffled_symbols_display, shuffled_symbols, shuffled_hints

# Display the puzzle to the player
def display_puzzle(sequence, shuffled_hints):
    print("Arrange the symbols in the correct sequence to unlock the chamber:")
    for idx, symbol in enumerate(sequence, start=1):
        print(f"{idx}. {symbol} - {symbols[symbol]}")
    print("\nHints (in correct order of symbols):")
    for i, hint in enumerate(shuffled_hints, start=1):
        print(f"{i}. {hint}")

# Check if the player's solution is correct
def check_solution(player_sequence, correct_sequence):
    return set(player_sequence) == set(correct_sequence)

# Example usage in your game scenario
def play_flame_symbol_puzzle():
    shuffled_symbols_display, correct_sequence, shuffled_hints = generate_puzzle_sequence()
    player_sequence = []

    print(("Welcome to the Wings of Fire!").center(120))
    speak("Welcome to the Wings of Fire!")
    print()
    intro = """\
'' Wings of Combustion '' is an infernal chamber inside the legendary alchemist's tower, enveloped in an ageless fire. Their walls were flickering with an old alchemic symbol, puzzle entangled in the nature of combustion. The fierce guards were prowling, challenging the intruder with their blazing fire. Only the one who knows how to control fire and deciphers the secret of chemistry can pass the strictest test and discover the secret of the elemental mystery inside."""
    print(intro)
    print()
    print("You encounter a stone tablet adorned with glowing symbols.")
    display_puzzle(shuffled_symbols_display, shuffled_hints)
    
    # Player attempts to solve the puzzle
    while True:
        print("\nEnter the sequence numbers of symbols in any order (e.g., '1 2 3 4 5')")
        player_input = input("Your sequence: ").strip()
        
        try:
            player_sequence = [correct_sequence[int(idx) - 1] for idx in player_input.split()]
        except (ValueError, IndexError):
            print("Invalid input. Please enter the sequence numbers correctly.")
            continue
        
        if check_solution(player_sequence, correct_sequence):
            print("\nCongratulations! The symbols align perfectly, unlocking the chamber.")
            speak("Congratulations! The symbols align perfectly, unlocking the chamber.")
            return True
        else:
            print("\nThe symbols do not align correctly. You Lose!.")
            print("Game Over")
            speak("Game Over")
            return False

# Define initial temperature readings for various devices
temperature_readings = {
    "Central Thermometer": 25,  # in Celsius
    "Wall Gauge": 30,
    "Ceiling Sensor": 28,
    "Floor Plate": 22
}

def display_chamber():
    print("You are now inside the Wings Of Fire.")
    speak("You are now inside the Wings Of Fire.")
    print("Now you are in chamber which contains several temperature measuring devices. ")
    print()
    print("The chamber contains several devices showing temperature readings:")
    for device, temperature in temperature_readings.items():
        print(f"{device}: {temperature}°C")
    print()
    print("In this chamber there is a river. On the side where you are there is a puzzle, but due to darkness, the puzzle is not visible. On the other side of the river, there is a lantern. ")
    print("You can decrease or increase the temperature to cross the river.")
    c3 = input("What can you do to go the other side of the river?(enter 1 to decrease or 2 to increase)\n")
    if c3 == "1":
        temp = int(input("Enter the temperature(to freeze or unfreeze the river): "))
        print()
        speak(f"The temperature is set to {temp}°C.")

        if temp <= 0:
            print("River is freezing...")
            speak("River is freezing...")
            print("Now you can cross the river.")
            print()
        else:
            print("You can't cross the river.")
    else:
        print("Incorrect.")
        print("You can't continue further.")

# Define initial temperature readings for the containers
container_temperatures = {
    "Fire Container": 80,
    "Water Container": 20,
    "Earth Container": 25,
    "Air Container": 15
}

def display_puzzle_instructions():
    print("Puzzle: Balancing the Elements")
    print("Adjust the temperatures of the four elemental containers according to the following rules:")
    print("1. The Fire Container must be at least twice as hot as the Earth Container.")
    print("2. The Water Container must be exactly 10°C cooler than the Earth Container.")
    print("3. The Air Container must be 5°C warmer than the Water Container.")
    print("4. The sum of all container temperatures must equal 180°C.")
    print()
    print("Current temperatures:")
    for container, temp in container_temperatures.items():
        print(f"{container}: {temp}°C")

def check_puzzle_solution():
    fire = container_temperatures["Fire Container"]
    water = container_temperatures["Water Container"]
    earth = container_temperatures["Earth Container"]
    air = container_temperatures["Air Container"]

    if (fire >= 2 * earth and
        water == earth - 10 and
        air == water + 5 and
        (fire + water + earth + air) == 180):
        return True
    else:
        return False

def play_temperature_control_puzzle():
    display_puzzle_instructions()
    hi = input("Do you want a hint? (y/n) ")
    if hi == "y":
        print("Inside the frozen river there is a glass bottle which contains a hint paper.")
        temp2 = int(input("Enter the temperature(to freeze or unfreeze the river): "))
        print()
        if temp2 >= 100:
            print("River is unfreezing...")
            speak("River is unfreezing...")
            print()
            print("""Hints:
The Fire Container must be the hottest.
The Water Container is cooler than the Earth Container.
The Air Container is warmer than the Water Container but cooler than the Fire Container.
The total of all temperatures should equal 180°C.""")
            print()
        else:
            print("The river is not unfreezing. You can't view the hint. ")
    
    while True:
        container = input("Enter the container you want to adjust (Fire, Water, Earth, Air Container) or 'exit' to quit: ").title().strip()
        print()
        if container.lower() == 'exit':
            break
        
        if container in container_temperatures:
            try:
                new_temperature = int(input(f"Enter new temperature for {container}: ").strip())
                container_temperatures[container] = new_temperature
                print(f"{container} is now set to {new_temperature}°C.")
                print()
            except ValueError:
                speak("Invalid input. Please enter a numeric value.")
        else:
            speak("Invalid container. Please enter a valid container name.")
        
        display_puzzle_instructions()
        
        if check_puzzle_solution():
            print("\nCongratulations! You have balanced the elements correctly and unlocked the next section.")
            speak("Congratulations! You have balanced the elements correctly and unlocked the next section.")
            return True
        else:
            print("\nThe temperatures are not balanced correctly. Keep trying!")

def play_temperature_control_test():
    display_chamber()
    
    if play_temperature_control_puzzle():
        return True
    return False

def blazing_bridge_trap():
    # Correct path, ensure this matches the actual solution path
    correct_path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]

    print("\nYou step onto a narrow bridge that leads to the Fiery Guardian's chamber.")
    print("The bridge is rigged with pressure plates that trigger fire traps.")
    print("You must choose the correct sequence of steps to avoid falling into the fire pit below.")
    
    speak("You step onto a narrow bridge that leads to the Fiery Guardian's chamber.")
    speak("The bridge is rigged with pressure plates that trigger fire traps.")
    speak("You must choose the correct sequence of steps to avoid falling into the fire pit below.")
    
    # Display the bridge with start and end points
    print("Start point -> O X O O O")
    print("               O O X O X")
    print("               X O O X O")
    print("               O X O X O")
    print("               X X O O O <- End point")

    while True:
        print("\nEnter your sequence of steps as row,col pairs (e.g., '0,0 1,0 2,1 ...')")
        player_input = input("Your steps: ").strip()
        
        try:
            player_steps = [(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in player_input.split()]
        except (ValueError, IndexError) as e:
            print("Invalid input. Please enter your steps in the correct format.")
            continue
        
        print(f"Player steps: {player_steps}")
        print(f"Correct path: {correct_path}")

        if player_steps == correct_path:
            print("\nYou successfully navigate the bridge and reach the other side.")
            speak("You successfully navigate the bridge and reach the other side.")
            return True
        else:
            print("\nYou triggered a fire trap! Try again.")
            speak("You triggered a fire trap! Try again.")
            return False


def fiery_guardian_combat():
    print("The arrival of the Fiery guardian is announced deep within the walls of the alchemist's tower. They are dressed in flame and loom ahead of you, and their eyes are blazed with elemental power. The atmosphere trembles with anticipation as you make a choice: face your enemy in battle or reveal a secret using an ancient puzzle. This relentless test is a cornerstone of your journey forward.")
    print("You can battle the guardian in combat or solve the puzzles to pacify the guardian.")
    decision = input("Enter 1 for combat or 2 for solve the puzzles: ")

    if decision == '1':
        # Initialize player and guardian stats
        player_health = 100
        player_attack_power = 20
        player_defense = 10

        guardian_health = 80
        guardian_attack_power = 15

        # Function to simulate player's turn
        def player_turn():
            print("\nPlayer's Turn")
            action = input("Choose your action (attack / defend): ").strip().lower()

            if action == "attack":
                nonlocal guardian_health
                guardian_health -= player_attack_power
                print(f"You attack the guardian! Guardian's health is now {guardian_health}")
            elif action == "defend":
                nonlocal player_health
                # Reduce incoming damage by player's defense
                player_health -= max(0, guardian_attack_power - player_defense)
                print(f"You defend against the guardian's attack! Your health is now {player_health}")
            else:
                print("Invalid action. Please choose attack or defend.")

        # Function to simulate guardian's turn
        def guardian_turn():
            print("\nGuardian's Turn")
            nonlocal player_health
            # Simulate guardian's attack
            player_health -= guardian_attack_power
            print(f"The guardian attacks! Your health is now {player_health}")

        # Main combat loop
        while player_health > 0 and guardian_health > 0:
            player_turn()
            if guardian_health <= 0:
                print("\nYou defeated the guardian!")
                speak("You defeated the guardian!")
                break
            guardian_turn()
            if player_health <= 0:
                print("\nYou were defeated by the guardian!")
                speak("You were defeated by the guardian!")
                break

        # Post-battle outcome
        if player_health > 0:
            print("\nCongratulations! You won the battle!")
            speak("Congratulations! You won the battle!")
            return True
            
        else:
            print("\nGame Over. You lost the battle.")
            speak("Game Over")

    elif decision == '2':
        print("\nGuardian: You have to solve the three puzzles that I asked you.")
        speak("You have to solve the three puzzle that I asked you.")
        print("\nThe first Puzzle is The Enchanted Forest")
        speak("The first Puzzle is The Enchanted Forest")
        puzzle1 = "You are wandering through an enchanted forest and come across a fork in the path. One path leads to a treasure chest guarded by a friendly dragon. The other path leads to a trap door that drops you into a pit. There are two forest guides, one who always tells the truth and the other who always lies. You can ask only one question to find the path to the treasure. What do you ask?"
        options1 = """A) "Would the other guide say the treasure is on the left path?"
B) "Is the treasure on the left path?"
C) "Is the treasure on the right path?"
D) "Which path would you take to find the treasure?" """
        print(puzzle1)
        speak(puzzle1)
        print("Your options are:")
        print(options1)
        answer1 = input("Enter your choice (A, B, C, D): ").strip().upper()

        if answer1 == 'A':
            print("\nCorrect! Well done.")
            print("\nThe second Puzzle is The Lost Key")
            speak("The second Puzzle is The Lost Key")
            puzzle2 = "You find yourself in a room with three keys: gold, silver, and bronze. Each key opens a different chest, but only one chest contains the ultimate treasure. There are two inscriptions on the walls: 'The bronze key is not in the middle' and 'The ultimate treasure is not in the chest opened by the gold key.' Which key opens the chest with the ultimate treasure?"
            options2 = """A) Gold
B) Silver
C) Bronze
D) None of the above"""
            print(puzzle2)
            speak(puzzle2)
            print("Your options are:")
            print(options2)
            answer2 = input("Enter your choice (A, B, C, D): ").strip().upper()

            if answer2 == 'B':
                print("\nCorrect! Excellent job.")
                print("\nThe third Puzzle is The Starry Night")
                speak("The third Puzzle is The Starry Night")
                puzzle3 = """You are gazing at the starry night sky when you notice three constellations: Draco, Orion, and Ursa Major. Each constellation contains stars of different colors: red, blue, and yellow. The red star is not in Draco, the blue star is not in Orion, and the yellow star is not in Ursa Major. Which constellation contains the red star?"""
                options3 = """A) Draco
B) Ursa Major
C) Orion
D) None of the above"""
                print(puzzle3)
                speak(puzzle3)
                print("Your options are:")
                print(options3)
                answer3 = input("Enter your choice (A, B, C, D): ").strip().upper()

                if answer3 == 'B':
                    print("\nCorrect! You have solved all the puzzles.")
                    speak("Correct! You have solved all the puzzles.")
                    print("\nThe Guardian is pleased and grants you passage. You may proceed!")
                    return True
                else:
                    print("\nIncorrect answer. The Guardian is not convinced. Game Over.")
                    speak("Game Over")

            else:
                print("\nIncorrect answer. The Guardian is not convinced. Game Over.")
                speak("Game Over")

        else:
            print("\nIncorrect answer. The Guardian is not convinced. Game Over.")
            speak("Game Over")

    else:
        print("\nInvalid input. Please enter '1' or '2'.")


def Alchemy_Recipe_Riddle():
    print("The game starts off in the chamber \"Wings of Fire\" you will be encountering a major puzzle with an alchemical apparatus and it cannot. Meaning you have to make a special drugged potion in order for the raging inferno and heat can rage without killing u. Before you, sets a riddle that points the way to which concoction of items is correct based on their numerical value. Once you have solved the riddle and prepared this potion, pour it onto the flames to neutralize them - doing so will also allow you to proceed further into that particular chamber.")

    
    def alchemical_apparatus():
        import time

        print("You arrive at the mystical alchemical workbench. It's covered with intricate carvings and various alchemical tools.")
        print("In front of you, a stone plaque on the wall begins to glow, revealing an inscription.")
        time.sleep(2)

        riddle = (
            "\nTo calm the raging fire, three things you need,\n"
            "Mix them together with great care, indeed.\n"
            "First, the warmth of the sun, shining bright,\n"
            "Next, the breath of a storm, cool and light.\n"
            "Lastly, the water from the earth, refreshing and clear,\n"
            "Combine them well, and the fire will disappear.\n"
            "The sun's warmth is like golden rays,\n"
            "The storm's breath is a cool breeze that sways,\n"
            "The earth's water is a clear, cool stream,\n"
            "What potion will you make to end this fiery dream?\n"
        )
        
        print(riddle)
        time.sleep(2)
        
        # Ingredients available
        ingredients = {
            "Sulfur": "Warmth of the Sun",
            "Nitrogen": "Breath of a Storm",
            "Water": "Water from the Earth"
        }
        
        # User input to mix ingredients
        print("You need to choose the right ingredients to mix.")
        print("Here are the available ingredients:")
        
        for ingredient, description in ingredients.items():
            print(f"{ingredient}: {description}")
        
        chosen_ingredients = []
        
        while len(chosen_ingredients) < 3:
            ingredient = input("\nEnter the name of an ingredient to add to the mix: ").strip()
            if ingredient in ingredients and ingredient not in chosen_ingredients:
                chosen_ingredients.append(ingredient)
                print(f"{ingredient} added to the mix.")
            else:
                print("Invalid ingredient or already added. Please choose a different ingredient.")
        
        # Check if the correct ingredients were chosen
        if set(chosen_ingredients) == {"Sulfur", "Nitrogen", "Water"}:
            print("\nYou carefully mix the ingredients together in the cauldron.")
            time.sleep(2)
            print("The mixture bubbles and glows, creating a shimmering potion.")
            time.sleep(2)
            print("You have created the Fire Extinguishing Elixir!")
            time.sleep(2)
            print("You use the potion to neutralize the flames in the chamber.")
            time.sleep(2)
            print("The flames die down, allowing you to safely proceed further into the chamber.")
        else:
            print("\nYou mix the ingredients together, but nothing happens.")
            time.sleep(2)
            print("It seems you didn't use the right combination of ingredients.")
            time.sleep(2)
            print("The flames continue to burn fiercely, blocking your path.")
            time.sleep(2)
            print("You'll need to try again and choose the correct ingredients.")

    # Start the alchemical apparatus puzzle
    alchemical_apparatus()


