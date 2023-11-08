from bardapi import Bard
import os
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\TTS\\en-US\\Microsoft Sam')

os.environ['_BARD_API_KEY'] = 'cwhSUCmRTY88lb5cb-TNQxPg_AO7dy2jN3m4z4soh5Rd8Q9FdaOrGXrRfTNnq3Xq6PG_HQ.'



while True:

    # Recognizer object
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak: ")
        audio = r.listen(source)

    input_text = None
    # Try to recognize the speech in the audio
    try:
        input_text = r.recognize_google(audio)
        print(input_text)
    except sr.UnknownValueError:
        print("Could not recognize speech")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    response = Bard().get_answer(input_text)['content']
    engine.say(response)
    engine.runAndWait()
    print(response)

