import os
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.security import APIKeyHeader
from starlette.requests import Request

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Create uploads directory if it doesn't exist
os.makedirs("static/uploads", exist_ok=True)

# Generate API token
API_TOKEN = str(uuid.uuid4())

api_key_header = APIKeyHeader(name="X-API-Key")


def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "api_token": API_TOKEN})

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...), api_key: str = Depends(get_api_key)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image")
    
    file_hash = uuid.uuid4().hex
    file_name = f"{file_hash}.jpg"
    file_path = f"static/uploads/{file_name}"
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"filename": file_name}

@app.get("/images/")
async def list_images(api_key: str = Depends(get_api_key)):
    images = [f for f in os.listdir("static/uploads") if f.lower().endswith(('.jpeg', '.jpg'))]
    return {"images": images}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)