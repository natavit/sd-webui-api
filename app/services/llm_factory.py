from typing import Dict

from app.services.google_vertex_service import GoogleVertexService
from app.services.stable_diff_service import StableDiffusionService

import vertexai
from vertexai.generative_models import (GenerativeModel, GenerationConfig, SafetySetting)

import requests


class LLMFactory:

    @staticmethod
    def get_gemini_client(
        project_id: str,
        location: str,
        model_name: str,
        response_schema: Dict[str, str],
    ):
        vertexai.init(project=project_id, location=location)

        generative_model = GenerativeModel(model_name)

        generation_config = GenerationConfig(
            max_output_tokens=8192,
            temperature=1,
            top_p=0.95,
            top_k=1,
            response_mime_type="application/json",
            response_schema=response_schema
        )

        safety_settings = [
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_NONE),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_NONE),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_NONE),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_NONE),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_NONE),
        ]

        google_vertex_service = GoogleVertexService(
            generative_model,
            generation_config,
            safety_settings
        )

        return google_vertex_service

    @staticmethod
    def get_stable_diffusion_client(
        http_client: requests.Session,
        base_url: str,
        roop_model_path: str
    ):
        return StableDiffusionService(http_client, base_url, roop_model_path)
