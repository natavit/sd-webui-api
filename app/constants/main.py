import os

PROJECT_ID = os.environ.get("PROJECT_ID")
LOCATION = os.environ.get("LOCATION")

GEMINI_MODEL_NAME = os.environ.get("GEMINI_MODEL_NAME", "gemini-1.5-flash-002")
ROOP_MODEL_PATH = os.environ.get("ROOP_MODEL_PATH")
SD_API_URL = os.environ.get("SD_API_URL")
SD_MODEL_CHECKPOINT = os.environ.get("SD_MODEL_CHECKPOINT", "dreamshaper_8")

PROMPT_TO_DESCRIBE_STYLE = """**Instructions**
You are an expert Stable Diffusion prompt designer. You are tasked to design a prompt that will be used with the Stable Diffusion-based DreamShaper model to change the outfit of the person in the given picture.
**Requirements**
1. The prompt should state if the person is a man or woman.
2. The prompt should instruct to change the outfit into {outfit_style}.
2.1 If the outfit is a dress, the prompt should also mention the length of the dress.
2.2 If the outfit contains a risk to copy right issues, the prompt should mention that the outfit is a "concept" or "inspired by".
3. The prompt should pay close attention and describe facial expression and body characteristics of the person in the input image.
4. The prompt should not state the current outfit of the person in the input image.
5. The prompt should instruct lighting and background image to be blurry, but relevant to the new outfit.

Finally, output into a valid JSON with "prompt".
"""

DESCRIBE_STYLE_RESPONSE_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "prompt": {
            "type": "STRING",
        }
    },
    "required": ["prompt"],
}

IMAGE_MAX_WIDTH = 960
IMAGE_MAX_HEIGHT = 1416
