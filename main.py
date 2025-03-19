import os
from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from pathlib import Path
import base64
from dotenv import load_dotenv
import logging
from typing import List
import io
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY not found in environment variables")
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    logger.error(f"Failed to configure Gemini: {str(e)}")
    raise

app = FastAPI(title="Fundus Image Analyzer", debug=True)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Constants
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_IMAGE_TYPES = {"JPEG", "JPG", "PNG"}
MODEL_NAME = "gemini-2.0-flash-thinking-exp-01-21"  # Updated to match simple_server.py

# Create directories for static files and templates
templates_dir = Path("templates")
static_dir = Path("static")
templates_dir.mkdir(exist_ok=True)
static_dir.mkdir(exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="templates")

def validate_image(contents: bytes) -> bool:
    """Validate image format and content."""
    try:
        # Try to open the image with PIL
        img = Image.open(io.BytesIO(contents))
        
        # Check if format is allowed
        if img.format not in ALLOWED_IMAGE_TYPES:
            return False
        
        # Verify image can be read
        img.verify()
        return True
    except Exception as e:
        logger.error(f"Image validation failed: {str(e)}")
        return False

def prepare_image_for_gemini(contents: bytes) -> str:
    """Prepare image for Gemini API."""
    try:
        # Convert to RGB if needed
        img = Image.open(io.BytesIO(contents))
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        # Save as JPEG in memory
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Encode to base64
        return base64.b64encode(img_byte_arr).decode('utf-8')
    except Exception as e:
        logger.error(f"Image preparation failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process image")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to render home page")

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        # Validate file size
        contents = await file.read()
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="File size too large (max 10MB)")
        
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Validate image content
        if not validate_image(contents):
            raise HTTPException(status_code=400, detail="Invalid image format or content")
        
        # Prepare image for Gemini
        image_base64 = prepare_image_for_gemini(contents)
        
        # Initialize Gemini Pro Vision model
        model = genai.GenerativeModel(MODEL_NAME)
        
        # Create the prompt for analysis
        prompt = """
        Analyze this fundus image and provide the following information:

        1. Estimated age of the person (within 2 years)
        - Include confidence level (%)
        - Base this on retinal characteristics, vessel patterns, and any age-related changes

        2. Estimated A1C level
        - Include confidence level (%)
        - Consider vessel health, any diabetic changes, and microaneurysms if present
        - Provide the value in % with a normal range of 4-5.6%

        3. Estimated LDL Cholesterol level
        - Include confidence level (%)
        - Look for signs of arteriolar narrowing, vessel changes
        - Provide the value in mg/dL with optimal being <100 mg/dL

        Format your response in plain text (not markdown) with simple sections for each category.
        For each prediction, explain the key indicators that led to your assessment.
        If you cannot make a confident prediction for any metric, please state so rather than guessing.
        """
        
        # Generate response from Gemini with safety settings
        safety_settings = {
            "HARM_CATEGORY_HARASSMENT": "block_none",
            "HARM_CATEGORY_HATE_SPEECH": "block_none",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "block_none",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "block_none",
        }
        
        response = model.generate_content(
            [prompt, image_base64],
            safety_settings=safety_settings,
            generation_config={
                "temperature": 0.2,
                "top_p": 0.8,
                "top_k": 40
            }
        )
        
        return {
            "success": True,
            "analysis": response.text
        }
        
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error analyzing image: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while analyzing the image. Please try again."
        )

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Fundus Image Analyzer server...")
    uvicorn.run(
        "main:app",  # Use string reference instead of app object
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True  # Enable auto-reload for development
    )
