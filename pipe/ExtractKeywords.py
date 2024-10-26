import sys
import os

sys.path.append('../')

from module import GiveKeywords

summary = ''

with open("./output/text/summary.txt", "r") as f:
    summary = f.read()

keywords = GiveKeywords(summary)

keys = ''

for keyword in keywords:
    keys += keyword

with open("./output/text/keywords.txt", "w") as f:
    f.write(keys)