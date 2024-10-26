import sys
import os

sys.path.append('../')

from module import SpeechToText

chunks = ['neso_000.mp3', 'neso_001.mp3', 'neso_002.mp3']

transcript = ''

for chunk in chunks:
    chunk = "./output/chunks/"+chunk
    transcript += SpeechToText(chunk)

with open('./output/text/transcript.txt', 'w') as f:
    f.write(transcript)