# Fundus Image Analyzer

![Fundus Analyzer](https://i.imgur.com/example.png)

A web application that analyzes fundus (retinal) images using Google's Gemini AI to predict age, A1C levels, and LDL Cholesterol levels from retinal characteristics.

## Live Demo

Visit the live application: [https://akshaybapat6365.github.io/fundus-analyzer/](https://akshaybapat6365.github.io/fundus-analyzer/)

## 🌟 Features

- **Modern UI**: Pure black dark theme with sleek Shadcn-inspired design
- **Multiple Run Options**: 
  - Browser-only mode with client-side processing
  - FastAPI server with additional features
  - Simple Python HTTP server for quick deployment
- **Advanced Analysis**: Uses Google's Gemini 2.0 AI models for precise retinal image analysis
- **Privacy Focused**: Client-side option processes all images in your browser

## 🚀 Quick Start

### Option 1: Browser Only (No Server)
1. Open `index.html` directly in your browser
2. Enter your Google Gemini API key when prompted
3. Upload a fundus image and analyze

### Option 2: FastAPI Server
1. Create a `.env` file with your API key: `GOOGLE_API_KEY=your_key_here`
2. Install requirements: `pip install -r requirements.txt`
3. Run the server: `python main.py`
4. Access at `http://localhost:8000`

### Option 3: Simple Server
1. Create a `.env` file with your API key: `GOOGLE_API_KEY=your_key_here`
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python simple_server.py`
4. Browser should open automatically to `http://localhost:8000`

### Option 4: Docker
1. Build and run with Docker Compose: `docker-compose up -d`
2. Access at `http://localhost:8000`

## 🔑 API Key

You need a valid Google Gemini API key to use this application. The app uses one of these models:
- `gemini-2.0-flash-thinking-exp-01-21` (client-side and simple server)
- `gemini-pro-vision` (FastAPI server)

Get your API key from [Google AI Studio](https://makersuite.google.com/).

## 🔒 Privacy

The browser-only version processes all images directly in your browser. No images or data are uploaded to any server other than Google's API for analysis purposes.

## 💻 Development

### Requirements
- Python 3.10+
- Required packages in `requirements.txt`

### Project Structure
- `index.html` - Standalone browser version
- `templates/` - HTML templates for FastAPI
- `static/` - CSS and other static assets
- `main.py` - FastAPI implementation
- `simple_server.py` - Simple HTTP server implementation
- `Dockerfile` & `docker-compose.yml` - Docker configuration

## 📄 License

MIT License

## 👥 Contributing

Contributions, issues, and feature requests are welcome! 