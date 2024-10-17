import os

PROJECT_ID = os.environ.get("PROJECT_ID")
LOCATION = os.environ.get("LOCATION")

GEMINI_MODEL_NAME = os.environ.get("GEMINI_MODEL_NAME", "gemini-1.5-flash-002")
ROOP_MODEL_PATH = os.environ.get("ROOP_MODEL_PATH")
SD_API_URL = os.environ.get("SD_API_URL")
SD_MODEL_CHECKPOINT = os.environ.get("SD_MODEL_CHECKPOINT", "dreamshaper_8")

PROMPT_TO_DESCRIBE_STYLE = """**Instructions**
Create a prompt that will be used with a Stable Diffusion-based model with the following requirements:
- The prompt should state if the person is a man or woman.
- The prompt should pay close attention and describe facial expression and body characteristics of the person in the input image.
- The prompt should not state the current outfit of the person in the input image.
- The prompt should not state the current posture of the person.
- The prompt should be descriptive and include the person details and no need a full stop at the ending.
- Finally, output into a valid JSON with "prompt" field
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
