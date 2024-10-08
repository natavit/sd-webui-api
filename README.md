# stable-diffusion-controlnet-webapi

## Required Environment Variables
- `PROJECT_ID` - Google Cloud Project ID
- `LOCATION` - Google Cloud Region (e.g. us-central1, asia-southeast1, etc.)
- `GEMINI_MODEL_NAME` - Gemini Model Name (e.g. gemini-1.5-flash-002)
- `ROOP_MODEL_PATH` - Full path to the roop model
- `SD_API_URL` - Base URL of AUTOMATIC1111 Stable Diffusion WebUI API
- `SD_MODEL_CHECKPOINT` - Stable Diffusion Model Name

```bash
EXPORT PROJECT_ID=$(gcloud config get-value project)
EXPORT LOCATION="LOCATION"
EXPORT GEMINI_MODEL_NAME="GEMINI_MODEL_NAME"
EXPORT ROOP_MODEL_PATH="ROOP_MODEL_PATH"
EXPORT SD_API_URL="SD_API_URL"
EXPORT SD_MODEL_CHECKPOINT="SD_MODEL_CHECKPOINT"
```

