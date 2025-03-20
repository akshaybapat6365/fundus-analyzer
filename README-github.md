# Fundus Image Analyzer

A web application that analyzes fundus (retinal) images using Google's Gemini AI to predict age, A1C levels, and LDL Cholesterol levels from retinal characteristics.

## 🌟 Features

- **AI-Powered Analysis**: Leverages Google's Gemini Vision models for detailed fundus image analysis
- **Client-side Processing**: All image processing happens in your browser
- **Advanced Analysis**: Uses Google's Gemini Pro Vision model for precise retinal image analysis  
- **Confidence Levels**: Provides confidence percentages with each prediction
- **No Server Required**: Runs entirely in the browser with direct API communication
- **Privacy Focused**: Your images never leave your browser except to be processed by Google's API

## 🚀 Live Demo

[Access the live application](https://akshaybapat6365.github.io/fundus-analyzer/)

Direct links:
- [Main version (direct.html)](https://akshaybapat6365.github.io/fundus-analyzer/direct.html)
- [Alternative version (simple.html)](https://akshaybapat6365.github.io/fundus-analyzer/simple.html)

## 🔑 API Key

The main version at direct.html already includes an API key for your convenience.

If you need your own API key (for the simple.html version), get it from [Google AI Studio](https://makersuite.google.com/app/apikey).

The app uses these models:
- `gemini-pro-vision` (primary)
- `gemini-1.5-pro` (fallback)

## 🔒 Privacy

This application processes all images directly in your browser. No images or data are uploaded to any server other than Google's API for analysis purposes.

## 🧑‍💻 Local Development

To run this project locally:

1. Clone the repository:
   ```
   git clone https://github.com/akshaybapat6365/fundus-analyzer.git
   ```

2. Navigate to the project directory:
   ```
   cd fundus-analyzer
   ```

3. Open the `direct.html` file in your browser or use a local development server:
   ```
   python3 -m http.server
   ```

4. Access the application at `http://localhost:8000/direct.html`

## 📚 Documentation

For detailed information:
- [VERSIONS.md](https://github.com/akshaybapat6365/fundus-analyzer/blob/main/VERSIONS.md) - Version history and lessons learned
- [BENCHMARK.md](https://github.com/akshaybapat6365/fundus-analyzer/blob/main/BENCHMARK.md) - Implementation comparison

## 📄 License

MIT License

## 👥 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/akshaybapat6365/fundus-analyzer/issues). 