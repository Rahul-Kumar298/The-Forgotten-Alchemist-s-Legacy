import random, time
# from speak import speak
from counttime import countdown_timer,sleep
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
    # speak("Welcome to the Wings of Fire!")
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
            # speak("Congratulations! The symbols align perfectly, unlocking the chamber.")
            return True
        else:
            print("\nThe symbols do not align correctly. You Lose!.")
            print("Game Over")
            # speak("Game Over")
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
    # speak("You are now inside the Wings Of Fire.")
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
        # speak(f"The temperature is set to {temp}°C.")

        if temp <= 0:
            print("River is freezing...")
            # speak("River is freezing...")
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
            # speak("River is unfreezing...")
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
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid container. Please enter a valid container name.")
        
        display_puzzle_instructions()
        
        if check_puzzle_solution():
            print("\nCongratulations! You have balanced the elements correctly and unlocked the next section.")
            # speak("Congratulations! You have balanced the elements correctly and unlocked the next section.")
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
    
    # speak("You step onto a narrow bridge that leads to the Fiery Guardian's chamber.")
    # speak("The bridge is rigged with pressure plates that trigger fire traps.")
    # speak("You must choose the correct sequence of steps to avoid falling into the fire pit below.")
    
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
            # speak("You successfully navigate the bridge and reach the other side.")
            return True
        else:
            print("\nYou triggered a fire trap! Try again.")
            # speak("You triggered a fire trap! Try again.")
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
                # speak("You defeated the guardian!")
                break
            guardian_turn()
            if player_health <= 0:
                print("\nYou were defeated by the guardian!")
                # speak("You were defeated by the guardian!")
                break

        # Post-battle outcome
        if player_health > 0:
            print("\nCongratulations! You won the battle!")
            # speak("Congratulations! You won the battle!")
            return True
            
        else:
            print("\nGame Over. You lost the battle.")
            # speak("Game Over")

    elif decision == '2':
        print("\nGuardian: You have to solve the three puzzles that I asked you.")
        # speak("You have to solve the three puzzle that I asked you.")
        print("\nThe first Puzzle is The Enchanted Forest")
        # speak("The first Puzzle is The Enchanted Forest")
        puzzle1 = "You are wandering through an enchanted forest and come across a fork in the path. One path leads to a treasure chest guarded by a friendly dragon. The other path leads to a trap door that drops you into a pit. There are two forest guides, one who always tells the truth and the other who always lies. You can ask only one question to find the path to the treasure. What do you ask?"
        options1 = """A) "Would the other guide say the treasure is on the left path?"
B) "Is the treasure on the left path?"
C) "Is the treasure on the right path?"
D) "Which path would you take to find the treasure?" """
        print(puzzle1)
        # speak(puzzle1)
        print("Your options are:")
        print(options1)
        answer1 = input("Enter your choice (A, B, C, D): ").strip().upper()

        if answer1 == 'A':
            print("\nCorrect! Well done.")
            print("\nThe second Puzzle is The Lost Key")
            # speak("The second Puzzle is The Lost Key")
            puzzle2 = "You find yourself in a room with three keys: gold, silver, and bronze. Each key opens a different chest, but only one chest contains the ultimate treasure. There are two inscriptions on the walls: 'The bronze key is not in the middle' and 'The ultimate treasure is not in the chest opened by the gold key.' Which key opens the chest with the ultimate treasure?"
            options2 = """A) Gold
B) Silver
C) Bronze
D) None of the above"""
            print(puzzle2)
            # speak(puzzle2)
            print("Your options are:")
            print(options2)
            answer2 = input("Enter your choice (A, B, C, D): ").strip().upper()

            if answer2 == 'B':
                print("\nCorrect! Excellent job.")
                print("\nThe third Puzzle is The Starry Night")
                # speak("The third Puzzle is The Starry Night")
                puzzle3 = """You are gazing at the starry night sky when you notice three constellations: Draco, Orion, and Ursa Major. Each constellation contains stars of different colors: red, blue, and yellow. The red star is not in Draco, the blue star is not in Orion, and the yellow star is not in Ursa Major. Which constellation contains the red star?"""
                options3 = """A) Draco
B) Ursa Major
C) Orion
D) None of the above"""
                print(puzzle3)
                # speak(puzzle3)
                print("Your options are:")
                print(options3)
                answer3 = input("Enter your choice (A, B, C, D): ").strip().upper()

                if answer3 == 'B':
                    print("\nCorrect! You have solved all the puzzles.")
                    # speak("Correct! You have solved all the puzzles.")
                    print("\nThe Guardian is pleased and grants you passage. You may proceed!")
                    return True
                else:
                    print("\nIncorrect answer. The Guardian is not convinced. Game Over.")
                    # speak("Game Over")

            else:
                print("\nIncorrect answer. The Guardian is not convinced. Game Over.")
                # speak("Game Over")

        else:
            print("\nIncorrect answer. The Guardian is not convinced. Game Over.")
            # speak("Game Over")

    else:
        print("\nInvalid input. Please enter '1' or '2'.")

def flame_whispers_riddles():
    print("As you enter this chamber, a strange voice from a statue welcomes you.")
    # speak("Hello! I am the Soul of Fire. You seem to be quite interesting. You have cleared the previous obstacles, but your journey ends here if you cannot answer the questions I ask. And I  know that you will definitely not give the correct answer.")
    # speak("So be prepared and look at the inscription on the left wall.")
    # print("You have to answer five questions that the guardian asks. You have thirty seconds to answer each question and get three chances to respond. The guardian will speak the puzzle only once, so listen carefully. If you don't listen carefully and want to hear it again, you will lose a chance.")
    sleep(5)
    riddle = ["I am not alive, but I grow; I don't have lungs, but I need air; I have no mouth, but water kills me. What am I?","Until I am measured, I am not known. Yet you miss me, when I have flown. What am I?","Some try to hide, some try to cheat, but time will show, we always will meet. Try as you might, to guess my name, I promise you'll know, when you do claim. Who am I?","What goes through cities and fields, but never moves?","If you drop me I am sure to crack, but give me a smile and I will always smile back. What am I?"]
    answers = ["Fire", "Time","Death","Road","Mirror"]
    count = 0
    for i in range(len(riddle)):
        print("The riddle is ")
        j = 0
        while j < 3:
            # speak(riddle[i])
            countdown_timer(20)
            answer = input("Enter the answer of the riddle : ")
            if answer.lower() == answers[i].lower():
                count +=1
                # speak("Interesting. You are quite impressive.")
                print("The flare of the flame decreases.")
                sleep(3)
                break
            print("The flare of the flame increases.")
            j +=1
        if j == 3:  # Check if the player has used all attempts
            print(f"You have used all your chances for this riddle. The correct answer was '{answers[i]}'.")
    if count == 5:
        print("Your knowledge is unmeasurable. And I am amazed with your skills so I think that you can definately get the fire elemental key. Best of luck! and remember your most powerful weapon is your mind.")
    else:
        print("As I say your journey ends here and you are not allow to go further.")
        print("Game Over.")
        print("Better Luck next time!")



# Function to simulate damage and display health
def take_damage(damage):
    global player_health
    player_health -= damage
    print(f"Flames burst from the board! You take {damage} damage. Current health: {player_health}")
    if player_health <= 0:
        print("You have been consumed by the flames. Game Over!")
        return False
    return True

def combustion_chess():
    global player_health
    player_health = 100  # Initial health
    max_mistakes = 2  # Allow more mistakes
    mistakes = 0
    time_limit = 20  # seconds per move (longer time)

    # Correct sequence based on the clues (easier version)
    correct_sequence = ["Knight", "Bishop", "Queen", "Rook", "King"]

    # Available pieces to move
    pieces = ["Rook", "King", "Bishop", "Knight", "Queen"]
    random.shuffle(pieces)  # Shuffle pieces to make it less predictable

    # Introduction
    print("You stand before the Combustion Chessboard.")
    print("The floor glows with fiery runes, a chessboard where only the correct sequence of moves will let you pass.")
    print("Incorrect moves will trigger flames, testing your resolve and health.")
    print()

    print("You notice runes glowing faintly beneath the chess pieces, each symbol hinting at the path.")
    print("Available pieces to move:")
    for i, piece in enumerate(pieces, 1):
        print(f"{i}. {piece}")

    # Game logic with a time limit and consequences for incorrect moves
    for move_number in range(1, len(correct_sequence) + 1):
        print(f"\nYou have {time_limit} seconds to make your move!")
        
        # Display hint/riddle before each move
        if move_number == 1:
            print("Clue 1: 'I leap over others, swift and unpredictable.'")  # Knight's ability to leap over pieces
        elif move_number == 2:
            print("Clue 2: 'I move diagonally, wise and graceful.'")  # Bishop's diagonal movement
        elif move_number == 3:
            print("Clue 3: 'I can move in any direction, the most powerful.'")  # Queen's flexibility
        elif move_number == 4:
            print("Clue 4: 'I move straight, side to side, and stand tall.'")  # Rook's straight movement
        elif move_number == 5:
            print("Clue 5: 'I can only move one square at a time, but I am the leader.'")  # King’s cautious movement

        # Ask the player to choose a piece to move, with a timer
        start_time = time.time()
        player_choice = input(f"Choose piece to move for step {move_number}: ")

        # Check if player runs out of time
        if time.time() - start_time > time_limit:
            print("You took too long! The flames burst from the board.")
            if not take_damage(15):  # Reduced damage for taking too long
                break
            continue

        # Check if the player's choice matches the correct move
        if pieces[int(player_choice)-1] == correct_sequence[move_number - 1]:
            print(f"Correct! You moved the {pieces[int(player_choice)-1]} safely.")
        else:
            mistakes += 1
            print(f"Wrong move! The {pieces[int(player_choice)-1]} triggered flames!")
            if mistakes > max_mistakes:
                print("Too many mistakes! The flames overwhelm you.")
                print("Game Over!")
                break
            if not take_damage(10):  # Reduced damage for incorrect moves
                break

    # Check if the player successfully completed the puzzle
    if player_health > 0 and mistakes <= max_mistakes:
        print("\nCongratulations! You solved the Combustion Chess puzzle.")
        print("The hidden passage is unlocked, and you may proceed.")
    else:
        print("\nYou failed the puzzle. Try again.")


def fire_trap_mechanism():
    print("\n*** Fire Trap Mechanism Challenge ***\n")
    print("You enter a narrow hallway filled with fire traps.")
    print("Some traps are triggered by changes in temperature, while others respond to movement.")
    print("You notice a set of levers and dials on the wall at the end of the hallway.")

    # Step 1: Initial trap observation
    print("\nStep 1: Observe the fire traps carefully.")
    print("You notice that the fire bursts every 5 seconds.")
    
    # Simulating trap observation
    for i in range(3):
        time.sleep(5)
        print(f"Fire bursts! (Cycle {i+1})")

    # Step 2: Movement-based traps
    print("\nStep 2: Dealing with movement-sensitive pressure plates.")
    print("You need to deactivate the pressure plates.")
    
    input("To deactivate the pressure plates, pull the correct lever (press Enter to continue)...")
    
    # Lever choice: right lever deactivates, wrong lever results in failure
    lever_choice = input("Which lever do you pull? (1 for left, 2 for right): ").strip()
    
    if lever_choice == "2":
        print("\nYou pulled the right lever and deactivated the pressure plates.")
    else:
        print("\nYou pulled the wrong lever! Flames erupt from the ground!")
        print("Game Over. Try again.")
        return
    
    # Step 3: Temperature control
    print("\nStep 3: Adjust the room's temperature to safely cross.")
    print("The room has two temperature controls: hot and cold.")
    
    temp_choice = input("Do you set the room to (1) hot or (2) cold? ").strip()

    if temp_choice == "2":
        print("\nYou set the room temperature to cold, calming the flames.")
    else:
        print("\nYou set the room temperature to hot, triggering more flames!")
        print("Game Over. Try again.")
        return
    
    # Step 4: Safely crossing the fire traps
    print("\nThe traps have been disarmed, and the flames have subsided.")
    print("You carefully proceed through the hallway and reach the other side safely.")
    print("Congratulations! You've passed the Fire Trap Mechanism challenge.")

def path_of_infernos():
    print("You step into the Path of Infernos.")
    print("The walls glow with rhythmic bursts of fire, and the air feels heavy with heat.")
    # speak("The fire dances to a rhythm. Watch, and the path will reveal itself.")
    print("\nYour objective: Navigate through the maze, avoid the flames, and solve the puzzle to reach the pedestal.\n")

    # Step 1: Observe Flame Patterns
    print("The flames burst in the following pattern: (ON for 2 seconds, OFF for 3 seconds)")
    print("Hint: Move only during the OFF state.")
    input("Press Enter to continue...")

    # Step 2: Navigate the First Segment
    print("\n--- First Segment: Simple Timing ---")
    for i in range(3):  # Three flame bursts
        print("The flames are ON!")
        time.sleep(2)
        print("The flames are OFF! Move quickly!")
        move = input("Type 'move' to advance: ").strip().lower()
        if move != "move":
            print("You hesitated and got burned! Try again.")
            return False
    print("You have successfully crossed the first segment!\n")

    # Step 3: Avoid Hidden Pressure Plates
    print("--- Second Segment: Hidden Pressure Plates ---")
    safe_path = random.randint(1, 3)  # Randomly set the safe path (1, 2, or 3)
    print("There are three paths ahead. Only one is safe. Choose wisely.")
    choice = int(input("Choose a path (1, 2, or 3): "))
    if choice != safe_path:
        print("You triggered a pressure plate! Flames engulf you. Try again.")
        return False
    print("You avoided the traps and moved forward!\n")

    # Step 4: Solve the Lever Puzzle
    print("--- Third Segment: Solve the Puzzle ---")
    print("You reach a row of levers blocking the path. Rearrange the symbols to disable the fire traps.")
    puzzle_solution = "132"  # Correct lever order
    attempt = input("Enter the correct lever order (e.g., 132): ").strip()
    if attempt != puzzle_solution:
        print("The levers were incorrect! Flames erupt from the walls. Try again.")
        return False
    print("The traps are disabled, and the path is clear!\n")

    # Step 5: Navigate Final Stretch
    print("--- Final Segment: Erratic Flames ---")
    print("The flames now burst unpredictably. Observe carefully and time your moves.")
    success = False
    for i in range(3):
        flame_state = random.choice(["ON", "OFF"])
        print(f"The flames are {flame_state}!")
        if flame_state == "ON":
            print("Wait for the flames to go OFF.")
            time.sleep(1)
        else:
            move = input("Type 'move' to advance: ").strip().lower()
            if move != "move":
                print("You hesitated and got burned! Try again.")
                return False
            success = True
    if not success:
        print("You failed to cross the final stretch. Try again.")
        return False

    # Step 6: Reach the Pedestal
    print("\nCongratulations! You have reached the pedestal and claimed the key to the Path of Infernos.")
    return True

