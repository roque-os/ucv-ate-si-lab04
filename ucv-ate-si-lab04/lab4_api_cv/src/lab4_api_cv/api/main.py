import os, shutil
from fastapi import FastAPI, UploadFile
from lab4_api_cv.services.image_service import analizar_imagen

app = FastAPI()

@app.post("/analyze-image")
def analyze_image(file: UploadFile):
    os.makedirs("data", exist_ok=True)
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    resultado = analizar_imagen(path)
    return {"mensaje": "Procesamiento exitoso", "resultado": resultado}
