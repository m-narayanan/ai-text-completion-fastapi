# AI-Based Text Completion with FastAPI

This project provides a simple backend service that generates AI-based text completions based on user prompts using the Groq API and FastAPI.

## Features
- Accepts a prompt from the user via a POST request.
- Returns AI-generated text completions.

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/m-narayanan/ai-text-completion-fastapi
cd ai-text-completion-fastapi
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Set the Groq API Key
Create a `.env` file in the root of the project to store your API key. Add the following line to the file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Replace `your_groq_api_key_here` with your actual Groq API key.

### 5. Run the FastAPI Server
Start the FastAPI development server using Uvicorn:
```bash
uvicorn main:app --reload
```
The server should start at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 6. Test the API
You can test the API using `curl` or any API client (like Postman). Here's an example using `curl`:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"prompt\":\"Once upon a time\"}" http://localhost:8000/complete-text
```

The expected response should look like this:
```json
{
  "completion": "Once upon a time, there was a small village in the mountains..."
}
```

