# Fundus Image Analyzer

![Fundus Analyzer Banner](https://i.imgur.com/example.png)

A web application that analyzes fundus (retinal) images using Google's Gemini AI to predict age, A1C levels, and LDL Cholesterol levels from retinal characteristics.

## 🌟 Features

- **Dark Theme UI**: Pure black background with sleek, modern design inspired by Shadcn UI
- **Client-side Processing**: All image processing happens in your browser
- **Advanced Analysis**: Uses Google's Gemini 2.0 AI model for precise retinal image analysis  
- **Confidence Levels**: Provides confidence percentages with each prediction
- **No Server Required**: Runs entirely in the browser with direct API communication
- **Privacy Focused**: Your images never leave your browser except to be processed by Google's API

## 🚀 Live Demo

[Access the live application](https://yourusername.github.io/fundus-analyzer/)

## 📸 Screenshot

![Application Screenshot](https://i.imgur.com/example2.png)

## 🔑 API Key

You need a valid Google Gemini API key to use this application. The app uses a specific model:
- `gemini-2.0-flash-thinking-exp-01-21`

Get your API key from [Google AI Studio](https://makersuite.google.com/).

Your API key is stored only in your browser's local storage and is never sent to our servers.

## 🔒 Privacy

This application processes all images directly in your browser. No images or data are uploaded to any server other than Google's API for analysis purposes.

## 🧑‍💻 Local Development

To run this project locally:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fundus-analyzer.git
   ```

2. Navigate to the project directory:
   ```
   cd fundus-analyzer
   ```

3. Open the `index.html` file in your browser or use a local development server:
   ```
   python3 -m http.server
   ```

4. Access the application at `http://localhost:8000`

## 🔧 Technologies Used

- HTML5/CSS3
- JavaScript (ES6+)
- Google Generative AI SDK
- Tailwind CSS

## 📄 License

MIT License

## 👥 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/fundus-analyzer/issues). 