import pyttsx3
import platform

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # Get details of available voices
    os_name = platform.system()  # Detect operating system
    
    if os_name == "Windows":
        # Windows typically has male (index 0) and female (index 1) voices
        engine.setProperty('voice', voices[1].id)  # Female voice
    elif os_name == "Darwin":  # macOS
        # macOS voices are managed differently, selecting the first voice
        engine.setProperty('voice', voices[0].id)
    elif os_name == "Linux":
        # Linux TTS may vary, setting to default voice (first one)
        engine.setProperty('voice', voices[0].id)
    else:
        # Default to first voice if OS is unknown
        engine.setProperty('voice', voices[0].id)

    engine.setProperty("rate", 150)  # Set speaking rate
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello, this is a test of the text-to-speech engine!")
