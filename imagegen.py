import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": f"Bearer {hf_token}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print('done')
    return response.content

width, height = 576, 1024

image_bytes = query({
    "inputs": "A realistic portrait of a ronin riding a horse",
    "parameters": {
        "width": width,
        "height": height
    }
})

image = Image.open(io.BytesIO(image_bytes))
image_upscaled = image.resize((720, 1280), Image.LANCZOS)
image_upscaled.save("image.png")
image_upscaled.show()