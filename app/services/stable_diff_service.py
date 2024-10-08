import io
import base64
import requests
from PIL import Image
from typing import Dict, List, Optional

from app.constants.main import SD_MODEL_CHECKPOINT
from app.schema import Img2ImgResponse, Txt2ImgResponse


class StableDiffusionService:
    http_client: requests.Session
    base_url: str
    roop_model_path: str

    def __init__(
        self,
        http_client: requests.Session,
        base_url: str,
        roop_model_path: str
    ):
        self.http_client = http_client
        self.base_url = base_url
        self.roop_model_path = roop_model_path
        
    def generate_txt2img(
        self,
        base64_image: str,
        width: int,
        height: int,
        prompt: str,
        negative_prompt: str,
        controlnet_args: List[Dict[str, any]],
        roop_enabled: bool
    ) -> Txt2ImgResponse:
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "sampler_name": "DPM++ 2M",
            "scheduler": "karras",
            "seed": -1,
            "steps": 20,
            "cfg_scale": 7,
            "resize_mode": 0,
            "width": width,
            "height": height,
            "restore_faces": True,
            "save_images": True,
            "override_settings": {
                # "sd_model_checkpoint": "3dAnimationDiffusion_v10"
                "sd_model_checkpoint": SD_MODEL_CHECKPOINT
            },
            "alwayson_scripts": {}
        }

        if roop_enabled:
            payload["alwayson_scripts"].update({
                "roop": {
                    "args": self.get_roop_args(base64_image, self.roop_model_path)
                }
            })

        if controlnet_args:
            payload["alwayson_scripts"].update({
                "controlnet": {
                    "args": controlnet_args
                }
            })

        response = self.http_client.post(
            url=f'{self.base_url}/sdapi/v1/txt2img',
            json=payload,
            timeout=60
        )
        
        return Txt2ImgResponse.from_dict(response.json())

    def generate_img2img(
        self,
        base64_image: str,
        width: int,
        height: int,
        prompt: str,
        negative_prompt: str,
        controlnet_args: List[Dict[str, any]],
        roop_enabled: bool
    ) -> Img2ImgResponse:
        payload = {
            "init_images": [base64_image],
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "sampler_name": "DPM++ 2M",
            "scheduler": "karras",
            "seed": -1,
            "steps": 30,
            "cfg_scale": 7,
            "resize_mode": 0,
            "width": width,
            "height": height,
            "restore_faces": True,
            "save_images": True,
            "override_settings": {
                # "sd_model_checkpoint": "3dAnimationDiffusion_v10"
                "sd_model_checkpoint": SD_MODEL_CHECKPOINT
            },
            "alwayson_scripts": {}
        }

        if roop_enabled:
            payload["alwayson_scripts"].update({
                "roop": {
                    "args": self.get_roop_args(base64_image, self.roop_model_path)
                }
            })

        if controlnet_args:
            payload["alwayson_scripts"].update({
                "controlnet": {
                    "args": controlnet_args
                }
            })

        response = self.http_client.post(
            url=f'{self.base_url}/sdapi/v1/img2img',
            json=payload,
            timeout=60
        )
        
        return Img2ImgResponse.from_dict(response.json())

    def get_roop_args(self, base64_image: str, roop_model_path: str) -> List[any]:
        """
        sd-webui-roop args: https://github.com/s0md3v/sd-webui-roop/issues/82
        [
            img,
            enable,
            faces_index,
            model,
            face_restorer_name,
            face_restorer_visibility,
            upscaler_name,
            upscaler_scale,
            upscaler_visibility,
            swap_in_source,
            swap_in_generated,
        ]
        """
        roop_args = [
            base64_image,
            True,
            '0',
            roop_model_path,
            'CodeFormer',
            1,
            None,
            1,
            'None',
            False,
            True
        ]

        return roop_args
