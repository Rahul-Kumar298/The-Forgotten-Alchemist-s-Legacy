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
"Wings of Fire" is an infernal chamber within the legendary alchemist's tower, enveloped in an eternal blaze. Its walls flicker with ancient alchemical symbols, puzzles intertwined with the essence of combustion. Fiery guardians prowl, challenging intruders with their blazing might. Only those who master the art of controlling flames and deciphering the secrets of alchemy can survive its scorching trials and unlock the elemental mysteries within."""
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

        if temp == 0:
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
        if temp2 == 100:
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

# Blazing Bridge Trap Implementation
def blazing_bridge_trap():
    correct_path = [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (3, 3), (2, 4), (1, 3), (0, 4)]
    
    print("\nYou step onto a narrow bridge that leads to the Fiery Guardian's chamber.")
    print("The bridge is rigged with pressure plates that trigger fire traps.")
    print("You must choose the correct sequence of steps to avoid falling into the fire pit below.")
    
    speak("You step onto a narrow bridge that leads to the Fiery Guardian's chamber.")
    speak("The bridge is rigged with pressure plates that trigger fire traps.")
    speak("You must choose the correct sequence of steps to avoid falling into the fire pit below.")
    
    # Display the bridge with start and end points
    print("Start point -> O X O O O <- End point")
    print("               O O X O X")
    print("               X O O X O")
    print("               O O X O O")
    print("               O X O X O")

    

    while True:
        print("\nEnter your sequence of steps as row,col pairs (e.g., '0,0 1,0 2,1 ...')")
        player_input = input("Your steps: ").strip()
        
        try:
            player_steps = [(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in player_input.split()]
        except (ValueError, IndexError) as e:
            print("Invalid input. Please enter your steps in the correct format.")
            continue
        
        if player_steps == correct_path:
            print("\nYou successfully navigate the bridge and reach the other side.")
            speak("You successfully navigate the bridge and reach the other side.")
            return True
        else:
            print("\nYou triggered a fire trap! Try again.")
            speak("You triggered a fire trap! Try again.")
            
            return False


def fiery_guardian_combat():
    print("Deep within the alchemist's tower, a searing heat heralds the arrival of the Fiery Guardian. Clad in flames and towering before you, its eyes blaze with elemental power. The air crackles with anticipation as you face a choice: confront the guardian in battle or unlock its secrets through ancient puzzles. Your path forward hinges on this fiery trial.")
    print("You can battle a combat with guardian or solve the puzzles to pacify the guardian.")
    decision = int(input("Enter 1 for combat or 2 for solve the puzzle."))
    if decision == 1:
        pass
    elif decision == 2:
        pass
    else:
        print("Invalid input. Please enter a valid numeric value.")
    