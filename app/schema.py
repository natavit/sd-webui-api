from typing import Dict, List, Optional
from fastapi import UploadFile

from dataclasses import dataclass
from dataclasses_json import dataclass_json

import pydantic as _pydantic


class _PromptBase(_pydantic.BaseModel):
    seed: Optional[int] = -1
    num_inference_steps: int = 10
    guidance_scale: float = 7.5


@dataclass_json
@dataclass
class ChangeOutfitRequest(_PromptBase):
    style: str
    num_of_outputs: int = 1
    ref_image: UploadFile


@dataclass_json
@dataclass
class Img2ImgResponse:
    images: List[str]


@dataclass_json
@dataclass
class Txt2ImgResponse:
    images: List[str]


@dataclass_json
@dataclass
class ChangeOutfitImageData:
    images: List[str]

@dataclass_json
@dataclass
class ChangeOutfitResponse:
    status_code: int
    status: str
    data: ChangeOutfitImageData
