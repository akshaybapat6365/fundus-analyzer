#!/bin/bash

# Fundus Image Analyzer Run Script
# This script provides different ways to run the Fundus Image Analyzer

# Text colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    echo "Please install Python 3 and try again."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo -e "${YELLOW}No .env file found. Creating one...${NC}"
    echo -n "Enter your Google Gemini API key: "
    read API_KEY
    echo "GOOGLE_API_KEY=$API_KEY" > .env
    echo -e "${GREEN}.env file created with your API key.${NC}"
else
    echo -e "${GREEN}Found existing .env file.${NC}"
fi

# Function to run browser-only version
run_browser_only() {
    echo -e "${BLUE}Running browser-only version...${NC}"
    if command -v open &> /dev/null; then
        open index.html  # macOS
    elif command -v xdg-open &> /dev/null; then
        xdg-open index.html  # Linux
    elif command -v start &> /dev/null; then
        start index.html  # Windows
    else
        echo -e "${YELLOW}Could not automatically open the browser.${NC}"
        echo "Please open index.html manually in your browser."
    fi
}

# Function to run with Python SimpleHTTPServer
run_simple_server() {
    echo -e "${BLUE}Running with simple Python server...${NC}"
    echo -e "${YELLOW}Installing requirements...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}Starting server...${NC}"
    python3 simple_server.py
}

# Function to run with FastAPI
run_fastapi() {
    echo -e "${BLUE}Running with FastAPI...${NC}"
    echo -e "${YELLOW}Installing requirements...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}Starting server...${NC}"
    python3 main.py
}

# Function to run with Docker
run_docker() {
    echo -e "${BLUE}Running with Docker...${NC}"
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}Error: Docker is required but not installed.${NC}"
        echo "Please install Docker and try again."
        return 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}Error: Docker Compose is required but not installed.${NC}"
        echo "Please install Docker Compose and try again."
        return 1
    fi
    
    echo -e "${GREEN}Starting Docker container...${NC}"
    docker-compose up -d
    echo -e "${GREEN}Docker container started!${NC}"
    echo -e "Access the application at: ${BLUE}http://localhost:8000${NC}"
}

# Display menu
echo -e "${GREEN}=== Fundus Image Analyzer ===${NC}"
echo -e "Choose how to run the application:"
echo -e "${BLUE}1${NC}. Browser only (no server)"
echo -e "${BLUE}2${NC}. Simple Python server"
echo -e "${BLUE}3${NC}. FastAPI server"
echo -e "${BLUE}4${NC}. Docker"
echo -e "${BLUE}q${NC}. Quit"
echo -n "Enter your choice: "
read choice

case $choice in
    1)
        run_browser_only
        ;;
    2)
        run_simple_server
        ;;
    3)
        run_fastapi
        ;;
    4)
        run_docker
        ;;
    q|Q)
        echo -e "${GREEN}Goodbye!${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac 