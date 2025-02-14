from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
import qrcode
import io
import base64
from fastapi.responses import JSONResponse

app=FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:5173"] if using Vite
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class QRRequest(BaseModel):
    url: HttpUrl #ensures valid URL format

@app.post("/generate_qr")
async def generate_qr(request: QRRequest):
    try:
        #Generate QR Code
        qr=qrcode.make(request.url)
        buffer=io.BytesIO()
        qr.save(buffer, format="PNG")
        qr_base64 =base64.b64encode(buffer.getvalue()).decode()

        return JSONResponse(content={"qr_code": qr_base64})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))