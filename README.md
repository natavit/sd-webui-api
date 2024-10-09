# stable-diffusion-controlnet-webapi

## Required Environment Variables

- `PROJECT_ID` - Google Cloud Project ID
- `LOCATION` - Google Cloud Region (e.g. us-central1, asia-southeast1, etc.)
- `GEMINI_MODEL_NAME` - Gemini Model Name (e.g. gemini-1.5-flash-002)
- `ROOP_MODEL_PATH` - Full path to the roop model
- `SD_API_URL` - Base URL of AUTOMATIC1111 Stable Diffusion WebUI API
- `SD_MODEL_CHECKPOINT` - Stable Diffusion Model Name

```bash
export PROJECT_ID=$(gcloud config get-value project)
export LOCATION="LOCATION"
export GEMINI_MODEL_NAME="GEMINI_MODEL_NAME"
export ROOP_MODEL_PATH="ROOP_MODEL_PATH"
export SD_API_URL="SD_API_URL"
export SD_MODEL_CHECKPOINT="SD_MODEL_CHECKPOINT"
```

## API Docs

FastAPI provides Swagger Docs that can be accessed via `/docs`

## Build

```bash
export REPOSITORY="REPOSITORY"
export IMAGE="IMAGE"
export TAG="TAG"

gcloud builds submit --tag $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE:$TAG
```

## Deploy

```bash
export SERVICE_NAME="SERVICE_NAME"

gcloud run deploy $SERVICE_NAME \
--image $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE:$TAG \
--platform managed \
--region $LOCATION \
--set-env-vars PROJECT_ID=$PROJECT_ID,LOCATION=$LOCATION,GEMINI_MODEL_NAME=$GEMINI_MODEL_NAME,ROOP_MODEL_PATH=$ROOP_MODEL_PATH,SD_API_URL=$SD_API_URL,SD_MODEL_CHECKPOINT=$SD_MODEL_CHECKPOINT \
--allow-unauthenticated
```
