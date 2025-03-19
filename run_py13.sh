#!/bin/bash

# Set API key directly from the parameter
export GOOGLE_API_KEY="AIzaSyALC2C4RyPuxWi3VsFu_X5WpuBOqJN5qyc"

# Ensure we have a virtual environment
if [ ! -d "venv_py13" ]; then
  echo "Creating Python virtual environment..."
  python3 -m venv venv_py13
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv_py13/bin/activate

# Install dependencies with specific versions compatible with Python 3.13
echo "Installing compatible dependencies for Python 3.13..."
pip install --upgrade pip

# Install specific versions of packages that are compatible with Python 3.13
pip install fastapi==0.109.0 
pip install uvicorn==0.27.0 
pip install python-multipart==0.0.6 
pip install google-generativeai==0.3.2 
pip install python-dotenv==1.0.0 
pip install jinja2==3.1.3 
pip install aiofiles==23.2.1 
pip install typing-extensions==4.9.0 
pip install Pillow==10.2.0 
pip install pydantic==2.6.0

# Start the application
echo "Starting the application..."
echo "The application will be accessible at: http://localhost:8000"
echo "Press Ctrl+C to stop the application."
echo "================================================================="

# Run the application
exec uvicorn main:app --host 0.0.0.0 --port 8000 