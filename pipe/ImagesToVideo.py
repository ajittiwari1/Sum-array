import sys
import os

sys.path.append('../')

from module import ImageToVideo, MergeVideoAudio, AddCaptionsToVideo

images = [
    './output/images/image0.png',
    './output/images/image1.png',
    './output/images/image2.png',
    './output/images/image3.png'
]

ImageToVideo(images, './output/video/output_video_no_voice.mp4', 20)

MergeVideoAudio('./output/video/output_video_no_voice.mp4', './output/audio/summary.mp3', './output/video/output_video_no_captions.mp4')

summary = ''

with open("./output/text/summary.txt", "r") as f:
    summary = f.read()

AddCaptionsToVideo('./output/video/output_video_no_captions.mp4', summary, './output/video/output_video.mp4')