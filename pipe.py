import os
from module import *
import time

os.makedirs('temp_audio/output_chunks', exist_ok=True)
os.makedirs('temp_text', exist_ok=True)
os.makedirs('temp_image', exist_ok=True)
os.makedirs('temp_video', exist_ok=True)
os.makedirs('final_video', exist_ok=True)

def clean_temp_files():
    for folder in ['temp_audio/output_chunks', 'temp_text', 'temp_image', 'temp_video']:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            os.remove(file_path)
    for folder in ['temp_audio', 'temp_text', 'temp_image', 'temp_video']:
        os.rmdir(folder)
    print("Temporary files cleaned up.")

# file_path = input("Please provide the path to your MP4 or MP3 file: ")
file_path = "./neso.mp4"
if not os.path.exists(file_path):
    print(f"File {file_path} does not exist.")
    exit(1)

file_extension = file_path.split('.')[-1].lower()
audio_path = file_path.replace('.mp4', '.mp3') if file_extension == "mp4" else file_path

if file_extension == "mp4":
    VideoToAudio(file_path, audio_path)
    print(f"Converted {file_path} to MP3.")
else:
    print(f"Using existing MP3 file: {file_path}")

DivideIntoChunks(audio_path, 'temp_audio/output_chunks')
print("Audio divided into 20-second chunks.")

audio_chunks = os.listdir('temp_audio/output_chunks')
transcriptions = []

for chunk in audio_chunks:
    chunk_path = os.path.join('temp_audio/output_chunks', chunk)
    transcription = SpeechToText(chunk_path)
    if transcription:
        transcriptions.append(transcription)
print("Converted audio chunks to text.")

summaries = []
for i in range(0, len(transcriptions), 3):
    text_to_summarize = " ".join(transcriptions[i:i+3])
    summary = Summarize(text_to_summarize)
    if summary:
        summaries.append(summary)
print("Summarized the transcribed text.")

images = []
for summary in summaries:
    summary = f'''{summary}'''
    summary = summary.replace("\n", " ")
    keywords = GiveKeywords(summary)
    print("Keywords: ", keywords)

    for keyword in keywords:
        prompt = ImagePrompt(summary, keyword.strip())
        image_path = f'temp_image/{keyword.strip().replace(" ", "_")}.png'
        TextToImage(prompt, image_path)
        time.sleep(1000)
        images.append(image_path)
        print(f"Generated Image for '{keyword.strip()}': {image_path}")

print("Generated relevant images based on improved prompts.")

video_path = 'temp_video/output_video.mp4'
ImageToVideo(images, video_path, len(images) * 20)
print("Created video from generated images.")

final_video_path = 'final_video/final_output_video.mp4'
MergeVideoAudio(video_path, audio_path, final_video_path)
print("Merged video with audio.")

captions = " ".join(transcriptions)
AddCaptionsToVideo(final_video_path, captions, final_video_path)
print("Added captions to the final video.")

print(f"Final video created: {final_video_path}")

clean_temp_files()