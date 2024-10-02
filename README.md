
# AI-Based Text Completion Service

This project is a simple FastAPI-based backend service that generates AI-based text completions using the Groq API. It accepts a user prompt and returns AI-generated text based on the prompt.

## Features
- **/complete-text Endpoint**: Accepts a prompt from the user via a POST request and returns an AI-generated text completion.

## Requirements
- Python 3.7+
- Groq API Key
- FastAPI
- Uvicorn

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/ai-text-completion-fastapi.git
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
You need to create a `.env` file to store your API key. Create a file named `.env` in the root of the project and add the following line:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

### 5. Run the FastAPI Server
Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server should start at `http://127.0.0.1:8000`.

### 6. Test the API
You can now test the API using `curl` or any API client (like Postman). Here's an example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"prompt\":\"Once upon a time\"}" http://localhost:8000/complete-text
```

The expected response should look like this:

```json
{
  "completion": "Once upon a time, there was a small village in the mountains..."
}
```



## Project Structure

- `main.py`: Contains the FastAPI app and the `/complete-text` endpoint.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: Stores your Groq API key (this file is not included in the repository for security reasons).
