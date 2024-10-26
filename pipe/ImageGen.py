import sys
import os

sys.path.append('../')

from module import TextToImage, ImagePrompt

keywords = []
summary = ''

with open('./output/text/keywords.txt', "r") as f:
    keywords = f.read().split(" ")

with open('./output/text/summary.txt', "r") as f:
    summary = f.read()

for i in range(4):
    input = ImagePrompt(summary, keywords[i])
    TextToImage(input, f'./output/images/image{i}.png')