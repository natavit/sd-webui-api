from typing import Dict, Optional

from vertexai.generative_models import (GenerativeModel, GenerationConfig, SafetySetting, Part)


class GoogleVertexService:
    client: GenerativeModel
    generation_config: GenerationConfig
    safety_settings: Optional[SafetySetting] = None

    def __init__(
        self,
        client: GenerativeModel,
        generation_config: GenerationConfig,
        safety_settings: Optional[SafetySetting] = None,
    ):
        self.client = client
        self.generation_config = generation_config
        self.safety_settings = safety_settings

    def generate_content(
            self,
            prompt: str,
            base64_image: str,
            mimetype: str
    ) -> Dict[str, any]:
        image_part = Part.from_dict(
            part_dict={
                "inlineData": {
                    "mimeType": mimetype,
                    "data": base64_image
                }
            }
        )

        response = self.client.generate_content(
            [image_part, prompt],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )

        return response.text
