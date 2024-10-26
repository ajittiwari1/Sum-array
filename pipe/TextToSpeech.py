import sys
import os

sys.path.append('../')

from module import TextToSpeech

summary = ''

with open('./output/text/summary.txt', "r") as f:
    summary = f.read()

TextToSpeech(summary, './output/audio/summary.mp3')