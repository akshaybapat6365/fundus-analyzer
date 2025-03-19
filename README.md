# Fundus Image Analyzer

A web application that analyzes fundus images using Google's Gemini AI to predict age, A1C levels, and LDL Cholesterol levels from retinal characteristics.

## Features

- Pure black dark theme UI with modern Shadcn-inspired design
- Client-side image processing with Google Gemini AI
- Immediate analysis results with confidence levels
- Completely browser-based - no server required
- Mobile-responsive design

## Demo

Access the live demo: https://yourusername.github.io/fundus-analyzer/

## How to Use

1. Visit the web application
2. Enter your Google Gemini API key (from [Google AI Studio](https://makersuite.google.com/))
3. Upload a fundus image by dragging and dropping or clicking to select
4. Click "Analyze Image"
5. View the detailed analysis results

## API Key

You need a valid Google Gemini API key to use this application. The app uses the following model:
- `gemini-2.0-flash-thinking-exp-01-21`

Your API key is stored only in your browser's local storage and is never sent to our servers.

## Privacy

This application processes all images directly in your browser. No images or data are uploaded to any server other than Google's API for analysis purposes.

## Local Development

To run this project locally:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fundus-analyzer.git
   ```

2. Open the `index.html` file in your browser or use a local development server.

## Technologies Used

- HTML5/CSS3
- JavaScript (ES6+)
- Google Generative AI SDK
- Tailwind CSS

## License

MIT License 