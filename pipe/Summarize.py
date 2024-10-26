import sys

sys.path.append('../')

from module import Summarize

transcript = ''

with open('./output/text/transcript.txt', 'r') as f:
    transcript = f.read()

summary = Summarize(transcript)

with open('./output/text/summary.txt', 'w') as f:
    f.write(summary)