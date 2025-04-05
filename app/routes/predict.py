from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.utils.image_utils import preprocess_image
from app.model.model import DeepfakeModel
from app.config import ALLOWED_EXTENSIONS
import shutil
import os
import uuid
import asyncio  # <-- Import asyncio

router = APIRouter()
model = DeepfakeModel()

@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    filename = file.filename or ""
    extension = filename.rsplit(".", 1)[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"File type '{extension}' not allowed. Please upload a .jpg, .jpeg or .png")

    unique_filename = f"{uuid.uuid4()}.{extension}"
    file_path = os.path.join("temp", unique_filename)
    os.makedirs("temp", exist_ok=True)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"[INFO] Saved uploaded file to {file_path}")

        image_array = preprocess_image(file_path)
        result = model.predict(image_array)

        # ⏳ Add delay here before returning response
        await asyncio.sleep(3)  # Delay for 3 seconds

        return JSONResponse(content={"prediction": result})

    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed due to internal error.")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"[INFO] Temp file {file_path} deleted.")
