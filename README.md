# FastAPI 
 A simple, robust REST API built with FastAPI to serve personal profile data, skills, and career goals from a local JSON file.
 - Language: Python
 - API Framework: FastAPI
 - ASGI Server: Uvicorn
 - Data Handling: json 
## :hammer_and_wrench: Setup và Installation
Follow these steps to run the API locally.

1. Prerequisites
- You must have Python 3.x installed.

2. Clone the Repository

- git clone [https://github.com/Kaizzer0/my_fastapi.git](https://github.com/Kaizzer0/my_fastapi.git)

- cd main.py


3. Install Dependencies

- pip install fastapi uvicorn pydantic


4. Run the API

The application runs on Uvicorn. The --reload flag enables auto-reloading during development.

- uvicorn main:app --reload



The server will be live at http://127.0.0.1:8000.

