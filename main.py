import os
from speak import speak

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

print(("Welcome to the Forgotten Alchemist's Legacy!").center(120))
speak("Welcome to the Forgotten Alchemist's Legacy!")

print()
print()
overview = """The Forgotten Apprentice's Inheritance is a choose-your-own-adventure game in which you explore the empty Tower of Professor Thaddeus Evergreen, an infamous Alchemist. It is a game that is bursting with puzzles, moral questions, and even ending variations based on the chosen path of the player."""
print(overview)

intro = "The story also begins with getting a cryptic letter to investigate the tower of alchemy. Fire, Water, Air, Space, Earth that reveals hints in the letter to gain access into these secrets through five elemental keys. The quest starts from the time you land on an enchanted tower out in the middle of nowhere."
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
place_list = list(place.values())


print()
print("The letter has the following message:")
speak("The letter has the following message:")
letter = """
Dear Seeker of Knowledge,

You have been chosen for a task of great importance and mystery. Professor Thaddeus Evergreen, the renowned and enigmatic alchemist, has left behind a legacy that awaits only the most worthy to uncover. His tower, shrouded in secrets and brimming with puzzles, calls to you.

In the heart of this tower lie the five elemental keys: Fire, Water, Air, Space, and Earth. Each key holds the power to unlock the profound mysteries of alchemy and reveal truths long hidden from the world. Your journey begins at the tower, an enchanted bastion of arcane wisdom, standing isolated in a forgotten land.

To commence your quest, you must solve the first of many puzzles. Within the pages of this letter, a clue awaits you. Read carefully and heed the words, for they will guide you through the initial trial.

"I am a dancer, bright and bold,
Yet in my presence, none can hold.
I consume all, yet give new life,
In my heart, both warmth and strife.
Tame me, and your path is clear,
But lose control, and you must fear.
What am I?"

Find the answer, and you shall begin your journey into the depths of Professor Evergreen’s tower. Each elemental key is guarded by challenges that will test your wit, resolve, and moral compass. Choose wisely, for the path you take will shape your destiny and the fate of the alchemist's legacy.

Once you have obtained the first key, place it upon this letter. Doing so will reveal the next puzzle and guide you to the chamber of another element. Your quest will continue as you unlock the secrets of the tower, one key at a time.

May your mind be sharp and your heart steadfast.

With anticipation,
The Guardians of the Tower

Good luck, adventurer. The tower awaits."""

print(letter)

c2 = input("Enter the answer to the puzzle: ")
if c2.capitalize() == "Fire":
    print("You guessed the right place. You are going to 'Wings of Fire - Fire Chamber', a great place full of adventures.")

    print()
    from fire_chamber import play_flame_symbol_puzzle, play_temperature_control_test, blazing_bridge_trap, fiery_guardian_combat, Alchemy_Recipe_Riddle
    # Main game logic
    task_completed = 0

    if play_flame_symbol_puzzle():
        task_completed = 1
        print()
        print()
        if play_temperature_control_test():
            task_completed += 1
            print()
            print()
            if blazing_bridge_trap():
                task_completed += 1
                if fiery_guardian_combat():
                    task_completed += 1
                    print()
                    print()
                    if Alchemy_Recipe_Riddle():
                        task_completed+=1
                        print()
                        print()
    print(f"Tasks completed: {task_completed}")
    speak(f"You have completed {task_completed} tasks out of 20 tasks to get the fire elemental key.")

    if task_completed == 20:
        print("Place the Fire Elemental Key upon the letter to get the next puzzle.")
        second_part_of_letter = """
Congratulations, Seeker.

You have successfully obtained the first key and unlocked the secrets of the Fire Chamber. As you place the Fire Key upon this letter, you will unveil the next challenge that awaits you in the next Chamber.

Prepare yourself, for the challenges of this chamber which are deep and filled with their own set of mysteries. To proceed, you must solve the riddle that will guide you to the key hidden within the next chamber.

Next Chamber Riddle:

"I am the mirror of the sky,
Yet I am not made of clouds or light.
I flow through valleys, soft and sly,
And with me, you quench your thirst and might.
My embrace can be gentle or fierce,
And my depths hold secrets vast and clear.
What am I?"

Solve this riddle to reveal the path forward. The next Key, when discovered, will help you navigate through the next trials within the tower. Each chamber presents a new challenge, demanding not only your intellect but also your courage and resolve.

Continue with determination, and may the currents guide you.

With resolve,
The Guardians of the Tower

Good luck, adventurer. The next element awaits."""
        print(second_part_of_letter)
        c3 = input("Enter the answer to the puzzle: ")
        if c3.capitalize() == "Water":
            print("You guessed the right place. You are going to 'Aqua Maze - Water Chamber ' another great place full of adventures.")
            from water_chamber import *
            water_task_completed = 0
            print(f"Tasks completed: {water_task_completed}")
            speak(f"You have completed {water_task_completed} tasks out of 20 tasks to get the fire elemental key.")
            if water_task_completed == 20:
                print("Place the Water Elemental Key upon the letter to get the next puzzle.")
                third_part_of_letter ="""
Well done, Seeker.

You have conquered the trials of the Water Chamber and secured the second key. As you place the Water Key upon this letter, you shall now unveil the next challenge awaiting you.

Prepare yourself, for this new chamber is one of stability and strength, holding secrets buried deep within its depths. To proceed, you must solve the riddle that will guide you to the key hidden among the stones and soil of this chamber.

Riddle:

"I am ancient, yet ever new,
Rooted deep where shadows grow.
My strength lies in the quiet, the still,
And in my embrace, all seeds will fulfill.
I shape the land with my patient hand,
And within me, great treasures stand.
What am I?"

Solve this riddle to reveal the path forward. The key, when found, will grant you access to further trials within the tower. Each chamber you conquer brings you closer to unlocking the full legacy of Professor Evergreen.

Press on with fortitude, for the trials ahead will test your endurance and wisdom.

With steadfastness,
The Guardians of the Tower

Good luck, adventurer. The next element awaits."""
                print(third_part_of_letter)
                c4 = input("Enter the answer to the puzzle: ")
                if c4.capitalize() == "Earth":
                    print("You guessed the right place. You are going to 'Earth Nexus - Earth Chamber ' another great place full of adventures.")
                    from earth_chamber import *
                    earth_task_completed = 0
                    print(f"Tasks completed: {earth_task_completed}")
                    speak(f"You have completed {earth_task_completed} tasks out of 20 tasks to get the fire elemental key.")
                    if earth_task_completed == 20:
                        print("Place the Earth Elemental Key upon the letter to get the next puzzle.")
                        fourth_part_of_letter = """
Impressive work, Seeker.

You have successfully navigated the challenges and secured the key from the previous chamber. As you place that key upon this letter, you will now reveal the next trial that awaits you.

Prepare yourself for the upcoming challenge, where the essence of the next trial holds the key to your progress. To advance, you must solve the riddle that will guide you to the key hidden among the currents and whispers of this ethereal space.

Riddle:

"I am invisible but ever near,
Moving swiftly without a trace.
I fill your lungs and carry sound,
And in my grasp, things gently sway.
I can be a whisper or a storm,
And in my touch, the world transforms.
What am I?"

Solve this riddle to uncover the path forward. The key you seek will unlock new mysteries and guide you further into the depths of the tower. Each chamber brings you closer to the ultimate discovery, and your journey continues with each challenge you overcome.

Stay vigilant and ready, for the path ahead will require both insight and agility.

With anticipation,
The Guardians of the Tower

Good luck, adventurer. The next element awaits."""
                        print(fourth_part_of_letter)
                        c5 = input("Enter the answer to the puzzle: ")
                        if c5.capitalize() == "Air":
                            print("You guessed the right place. You are going to 'Realm of Air - Air Chamber ' another great place full of adventures.")
                            from air_chamber import *
                            air_task_completed = 0
                            print(f"Tasks completed: {air_task_completed}")
                            speak(f"You have completed {air_task_completed} tasks out of 20 tasks to get the fire elemental key.")
                            if air_task_completed == 20:
                                print("Place the Air Elemental Key upon the letter to get the next puzzle.")
                                fifth_part_of_letter = """
Congratulations, Seeker.

You have successfully secured the key from the previous challenge. As you place that key upon this letter, you will unveil the final trial that lies ahead.

Prepare yourself for the ultimate challenge, where the essence of the final trial will test your understanding of the vast and boundless. To proceed, you must solve the riddle that will guide you to the key hidden in the expanse of this enigmatic space.

Riddle:

"I stretch beyond the reach of sight,
A vast domain where stars ignite.
I hold the realms of time and space,
And in my depths, secrets find their place.
I am both the limit and the guide,
In my embrace, the answers hide.
What am I?"

Solve this riddle to reveal the path forward. The key you seek will grant you access to the final mysteries within the tower.

When you have collected all five keys—Fire, Water, Air, Earth, and the one you now seek—place them all upon this letter. Doing so will reveal the ultimate secret of Professor Evergreen’s legacy and unlock the path to the final chamber.

Your journey is nearly complete, and the final chamber will bring you closer to unlocking the full legacy of Professor Evergreen. Press on with courage and insight, for the final trial will test the limits of your resolve.

With anticipation,
The Guardians of the Tower

Good luck, adventurer. The end of your quest is near."""
                                print(fourth_part_of_letter)
                                c6 = input("Enter the answer to the puzzle: ")
                                if c6.capitalize() == "Space":
                                    print("You guessed the right place. You are going to 'Astra Cosmo - Space Chamber ' another great place full of adventures.")
                                    from space_chamber import *
                                    space_task_completed = 0
                                    print(f"Tasks completed: {space_task_completed}")
                                    speak(f"You have completed {space_task_completed} tasks out of 20 tasks to get the fire elemental key.")
                                    if space_task_completed == 20:
                                        print("Place the all five Elemental Key upon the letter to get the further information.")
                                        final_part_of_letter ="""
Congratulations, Seeker.

You have traversed the trials and secured all five keys: Fire, Water, Air, Earth, and the final one you have just acquired. As you place these keys upon this letter, a crucial step remains before you can unlock the true legacy of Professor Thaddeus Evergreen.

Before you lies a grand door, the gateway to the heart of the alchemist’s legacy. To open this door, you must place each key in its rightful position according to the riddles you have solved. Each key corresponds to a specific place, and only by placing them correctly will you reveal the secrets within.

Refer to the riddles provided in the letters for guidance:

The Fire Key will find its place where the trials of flame are tested.
The Water Key belongs where the currents of clarity and depth are revealed.
The Earth Key should be set where the roots and strength of the land lie.
The Air Key will be placed where the whispers and breezes of the ethereal realm flow.
The final key, guided by the vast expanse of the cosmos, will complete the puzzle.
Arrange the keys accordingly to unlock the door and gain access to the alchemist’s ultimate legacy. The path you have walked has led you to this final moment of discovery. Use your knowledge and insight to unveil what lies beyond.

May your resolve be unwavering as you complete your journey and unlock the true secrets of Professor Evergreen’s Tower.

With reverence and respect,
The Guardians of the Tower"""
                                    else:
                                        print("You had not completed all the tasks.")
                                        print("Game Over")
                                        speak("Game Over")
                            else:
                                print("You had not completed all the tasks.")
                                print("Game Over")
                                speak("Game Over")
                    else:
                        print("You had not completed all the tasks.")
                        print("Game Over")
                        speak("Game Over")
            else:
                print("You had not completed all the tasks.")
                print("Game Over")
                speak("Game Over")
        else:
            print("You had not completed all the tasks.")
            print("Game Over")
            speak("Game Over")
    else:
        print("You had not completed all the tasks.")
        print("Game Over")
        speak("Game Over")
else:
    print("Solve the puzzle correctly.")
    print("Better luck next time.")
    print("Game Over.")
    speak("Game Over.")
    print("Thank you for playing.")
