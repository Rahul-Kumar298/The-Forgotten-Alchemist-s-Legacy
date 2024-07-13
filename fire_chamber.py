import random

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
    "The beginning of all combustion processes.",
    "Measure of thermal energy intensity.",
    "Process of changing one form into another.",
    "Maintaining harmony or equilibrium.",
    "It affects all processes, including the transformation of elements."
]
task_completed = 0
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
        except (ValueError, IndexError) as e:
            print(e)
            break
        
        if check_solution(player_sequence, correct_sequence):
            print("\nCongratulations! The symbols align perfectly, unlocking the chamber.")
            return True
            break
        else:
            print("\nThe symbols do not align correctly. You Lose!.")
            print("Game Over")
            break

a=play_flame_symbol_puzzle()
if a == 'True':
    task_completed = 1
    b = play_temperature_control_test()
    if b == 'True': 
        task_completed += 1
