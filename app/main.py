from fastapi import FastAPI, Form
import io
import base64
from PIL import Image
import requests
import json

from app.constants.main import DESCRIBE_STYLE_RESPONSE_SCHEMA, GEMINI_MODEL_NAME, LOCATION, PROJECT_ID, PROMPT_TO_DESCRIBE_STYLE, ROOP_MODEL_PATH, SD_API_URL
import app.schema as _schema

from typing import Annotated

from app.services.llm_factory import LLMFactory
from app.utils.image_utils import ImageUtils

app = FastAPI()

google_vertex_service = LLMFactory.get_gemini_client(
    PROJECT_ID,
    LOCATION,
    GEMINI_MODEL_NAME,
    DESCRIBE_STYLE_RESPONSE_SCHEMA
)

stable_diff_service = LLMFactory.get_stable_diffusion_client(
    requests.Session(),
    SD_API_URL,
    ROOP_MODEL_PATH
)


@app.get("/")
def read_root():
    return {"message": "Google Cloud"}


@app.post("/api/v1/change-outfit")
async def change_outfit(data: Annotated[_schema.ChangeOutfitRequest, Form()]) -> _schema.ChangeOutfitResponse:
    image_bytes = await data.ref_image.read()
    pil_image = Image.open(io.BytesIO(image_bytes))
    mimetype = pil_image.get_format_mimetype()
    # width, height = pil_image.size
    
    new_width, new_height = ImageUtils.calculate_resized_dimensions(pil_image, 1416, 960)
    
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    style = data.style
    # num_of_outputs = data.num_of_outputs

    response_str = google_vertex_service.generate_content(
        prompt=PROMPT_TO_DESCRIBE_STYLE.format(outfit_style=style),
        base64_image=base64_image,
        mimetype=mimetype,
    )

    response_json = json.loads(response_str)

    prompt = response_json["prompt"]
    final_prompt = f'((masterpiece)), (extremely intricate:1.2), (realistic:0.5), (digital painting:1), ({style.lower()}:1.3), {prompt}, <lora:more_details:0.3>, (high detail:1.1), (detailed face:1.2), (perfect composition:1.4)'
    negative_prompt = "nsfw, not safe for work, BadDream, (UnrealisticDream:1.2), blurry, text, watermark, lowres"

    # img2img args
    controlnet_openpose_args = {
        "enabled": True,
        "module": "openpose_full",
        "model": "control_v11p_sd15_openpose [cab727d4]",
        "control_mode": "Balanced"
    }

    response = stable_diff_service.generate_img2img(
        base64_image=base64_image,
        width=new_width,
        height=new_height,
        prompt=final_prompt,
        negative_prompt=negative_prompt,
        controlnet_args=[controlnet_openpose_args],
        roop_enabled=True
    )
    
    # txt2img args
    # controlnet_openpose_args = {
    #     "enabled": True,
    #     "image": base64_image,
    #     "module": "openpose_full",
    #     "model": "control_v11p_sd15_openpose [cab727d4]",
    #     "control_mode": "Balanced"
    # }
    
    # response = stable_diff_service.generate_txt2img(
    #     base64_image=base64_image,
    #     width=960,
    #     height=1416,
    #     prompt=final_prompt,
    #     negative_prompt=negative_prompt,
    #     controlnet_args=[controlnet_openpose_args],
    #     roop_enabled=True
    # )

    return _schema.ChangeOutfitResponse(
        status_code=200,
        status="success",
        data={
            "images": [response.images[0]]
        }
    )
