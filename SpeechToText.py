import os
import requests
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-tiny"
headers = {"Authorization": f"Bearer {hf_token}"}

def query(data):
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def transcribe_audio(filename):
    with open(filename, "rb") as f:
        data = f.read()

    result = query(data)

    if "text" in result:
        return result["text"]
    else:
        print("Error in transcription:", result)
        return None

output = transcribe_audio("sample.mp3")
if output:
    print("Transcription:", output)