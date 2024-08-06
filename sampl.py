import pyttsx3
import time
import sys

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Letter content
letter_content = """
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

Good luck, adventurer. The tower awaits.
"""

# Display and speak text word by word
for word in letter_content.split():
    sys.stdout.write(word + ' ')
    sys.stdout.flush()
    speak_text(word)
    time.sleep(0.05)  # Adjust the delay as needed

