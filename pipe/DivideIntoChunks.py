import sys
import os

sys.path.append('../')

os.makedirs("./output/chunks/")

from module import DivideIntoChunks

DivideIntoChunks('./output/neso.mp3', './output/chunks/')