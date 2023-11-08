import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\TTS\\en-US\\Microsoft Sam')
text = "Hello, world! What is going on my guy. How are you doing"
engine.say(text)
engine.runAndWait()