import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 250)

text = ''
with open("output.txt") as f:
    text = f.read()

engine.save_to_file(text, 'output.mp3')
engine.runAndWait()