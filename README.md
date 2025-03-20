# Fundus Image Analyzer

A web application that analyzes fundus (retinal) images using Google's Gemini AI to predict age, A1C levels, and LDL Cholesterol levels from retinal characteristics.

## 🚀 Live Demo

Visit the live application: [https://akshaybapat6365.github.io/fundus-analyzer/](https://akshaybapat6365.github.io/fundus-analyzer/)

## 🌟 Features

- **AI-Powered Analysis**: Leverages Google's Gemini Vision models for detailed fundus image analysis
- **Multiple Implementations**: 
  - **[direct.html](https://akshaybapat6365.github.io/fundus-analyzer/direct.html)**: Simplified browser-only version with API key included
  - **[simple.html](https://akshaybapat6365.github.io/fundus-analyzer/simple.html)**: Alternative implementation with fallback model support
  - **FastAPI server**: For server-side processing to avoid CORS issues
- **Detailed Health Metrics**: Analyzes fundus images to estimate:
  - Age (±2 years)
  - HbA1c levels (with normal range reference)
  - LDL Cholesterol levels (with optimal range reference)
- **Confidence Indicators**: Provides confidence levels for each prediction
- **Diagnostic Reasoning**: Explains the retinal indicators that influenced each prediction

## 🧠 How It Works

The application uses advanced AI vision models to analyze fundus images by examining:
- Vessel patterns
- Optic disc morphology
- Macular appearance
- Age-related features (drusen, vascular tortuosity)
- Diabetic markers (microaneurysms, hemorrhages)
- Cholesterol indicators (arteriolar narrowing, lipid deposits)

## 📱 Usage Options

### Option 1: Direct Web Version (Recommended)
1. Visit [https://akshaybapat6365.github.io/fundus-analyzer/direct.html](https://akshaybapat6365.github.io/fundus-analyzer/direct.html)
2. Upload a fundus image by dragging and dropping or clicking to select
3. Click "Analyze Image" to receive detailed analysis

### Option 2: Alternative Web Version
1. Visit [https://akshaybapat6365.github.io/fundus-analyzer/simple.html](https://akshaybapat6365.github.io/fundus-analyzer/simple.html)
2. Enter your Google Gemini API key
3. Upload a fundus image and analyze

### Option 3: Server Options
For users who prefer server-side processing:

#### FastAPI Server
1. Create a `.env` file with your API key: `GOOGLE_API_KEY=your_key_here`
2. Install requirements: `pip install -r requirements.txt`
3. Run the server: `python main.py`
4. Access at `http://localhost:8000`

#### Simple Server
1. Create a `.env` file with your API key: `GOOGLE_API_KEY=your_key_here`
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python simple_server.py`
4. Browser should open automatically to `http://localhost:8000`

#### Docker
1. Build and run with Docker Compose: `docker-compose up -d`
2. Access at `http://localhost:8000`

## 🔑 API Key Information

The web versions use Google's Gemini API:
- The **direct.html** version has an API key included (may be subject to quota limits)
- The **simple.html** version requires you to input your own API key

To get your own API key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key (free tier available)
3. Enable the Gemini API for your key

## 🔍 Project Documentation

For detailed information about the different implementations and benchmarks:
- [VERSIONS.md](https://github.com/akshaybapat6365/fundus-analyzer/blob/main/VERSIONS.md) - Detailed version history and lessons learned
- [BENCHMARK.md](https://github.com/akshaybapat6365/fundus-analyzer/blob/main/BENCHMARK.md) - Performance comparison between implementations

## 🔒 Privacy

The browser-only versions process all images directly in your browser. Images are only sent to Google's API for analysis purposes and are not stored.

## 💻 Development

### Requirements
- Python 3.10+ (for server options only)
- Required packages in `requirements.txt` (for server options only)

### Project Structure
- `direct.html` - Main web implementation (recommended)
- `simple.html` - Alternative web implementation with fallback model
- `test.html` - Basic test page for GitHub Pages
- `index.html` - Redirects to direct.html
- `main.py` - FastAPI server implementation
- `simple_server.py` - Simple HTTP server implementation
- `templates/` & `static/` - Server-side resources

## 📄 License

MIT License

## 👥 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/akshaybapat6365/fundus-analyzer/issues). 