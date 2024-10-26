import os
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import warnings
import pyttsx3
import requests
from dotenv import load_dotenv
import subprocess
import requests
import io
from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips, VideoFileClip, AudioFileClip,  TextClip, CompositeVideoClip

def VideoToAudio(video_file, audio_path):
    command = ["ffmpeg", "-i", video_file, "-vn", "-acodec", "libmp3lame", "-ar", "16000", "-ac", "2", audio_path]

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)

def DivideIntoChunks(input_file, output_directory):
    chunk_length = 20

    base_name = os.path.basename(input_file).split('.')[0]
    
    command = [
        "ffmpeg", "-i", input_file, "-f", "segment", 
        "-segment_time", str(chunk_length), 
        "-c", "copy", os.path.join(output_directory, f"{base_name}_%03d.mp3")
    ]
    
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr.decode())

def SpeechToText(audio_file):
    load_dotenv()
    hf_token = os.getenv("HF_TOKEN")

    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-tiny"
    headers = {"Authorization": f"Bearer {hf_token}"}

    with open(audio_file, "rb") as f:
        data = f.read()

    result = requests.post(API_URL, headers=headers, data=data).json()

    if "text" in result:
        return result["text"]
    else:
        print("Error in transcription:", result)
        return None
    
def TextToSpeech(text, output_path):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 250)

    engine.save_to_file(text, output_path)
    engine.runAndWait()

def Chat(user_input):  
    command = f'ollama run llama3.2 -- prompt "{user_input}"'
    with os.popen(command) as process:
        output = process.read()
    
    return output.strip().split("failed to get console mode for stdout: The handle is invalid.")[1]

def Summarize(text):    
    user_input = "Correct the grammatical and spelling mistakes and conceptual errors if any, and then summarise this text to 1/4 of its original length and just give me the text without any of your justification or closure or any preceeding or succeding comments as such: " + text
    response = Chat(user_input)
    return response

def TextToImage(prompt, image_path):
    load_dotenv()

    hf_token = os.getenv("HF_TOKEN")

    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization": f"Bearer {hf_token}"}

    image_bytes = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "parameters": {
            "width": 576,
            "height": 1024
        }
    }).content

    image = Image.open(io.BytesIO(image_bytes))
    image_upscaled = image.resize((720, 1280), Image.LANCZOS)
    image_upscaled.save(image_path)

def GiveKeywords(text):
    user_input = "Analyse this entire text and give me four keywords in form of comma seperated values, no preceding or succeeding text : "+text
    response = Chat(user_input)

    response = response.split(",")
    return response

def ImagePrompt(context, keyword):
    user_input = "Refer to the context and keyword and then create a prompt for image generation that focuses on the keyword while abiding to the context, no preceding or succeeding text : Context: "+context+ "and Keyword: " + keyword
    response = Chat(user_input)

    return response

def ImageToVideo(images, output_video_path, video_length):
    image_duration = video_length / 4
    clips = [ImageClip(img).set_duration(image_duration) for img in images]

    video = concatenate_videoclips(clips, method="compose")
    video = video.set_fps(2)

    video.write_videofile(output_video_path, codec="libx264")

def MergeVideoAudio(input_video, input_audio, output_video):
    video_clip = VideoFileClip(input_video)
    audio_clip = AudioFileClip(input_audio)

    video_with_audio = video_clip.set_audio(audio_clip)

    video_with_audio.write_videofile(output_video, codec="libx264", audio_codec="libvorbis", fps=2)

def AddCaptionsToVideo(input_video, captions, output_video_path):
    words_per_chunk = 5
    video_clip = VideoFileClip(input_video)
    video_duration = video_clip.duration

    words = captions.split()
    transcript_chunks = [
        " ".join(words[i:i + words_per_chunk]) for i in range(0, len(words), words_per_chunk)
    ]

    num_chunks = len(transcript_chunks)
    chunk_duration = video_duration / num_chunks if num_chunks > 0 else video_duration

    caption_clips = []
    for i, text in enumerate(transcript_chunks):
        start_time = i * chunk_duration
        caption = (
            TextClip(text, fontsize=48, color="yellow", stroke_color="white", stroke_width=2, bg_color="black", method='caption')
            .set_position(("center", "bottom"))
            .set_start(start_time)
            .set_duration(chunk_duration)
        )
        caption_clips.append(caption)

    final_video = CompositeVideoClip([video_clip, *caption_clips])
    final_video.write_videofile(output_video_path, codec="libx264", fps=2)

# summary = '''Big O notation is used to determine if one function is asymptotically bigger than another. To do this, we need to check if one function is big O of the other function.

# Let's compare two functions: fn = n^2 log(n) and gn = n * log(n)^10. We need to find out which function is big O of the other. Big O notation essentially means "at most" or "less than or equal to".'''

# print(Chat("Analyse this entire text and give me four keywords in form of comma seperated values, no preceding or succeeding text : "+summary.replace("\n", " ")))