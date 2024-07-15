''''''



import pyttsx3

engine=pyttsx3.init()

def speak(text):
    engine.say(text) # text is the string that you want to be spoken out loud by your computer's built-in speech synthesizer engine.
    engine.runAndWait()

task_completed = 2


