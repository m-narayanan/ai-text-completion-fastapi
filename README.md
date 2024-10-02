# AI-Based Text Completion with FastAPI

This is a simple backend service that generates AI-based text completions based on user prompts using the Groq API and FastAPI.

## Features
- Accepts a prompt from the user via a POST request
- Returns AI-generated text completions

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/m-narayanan/ai-text-completion-fastapi
   cd ai-text-completion-fastapi


2. **Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies:


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install Dependencies**
Install the required Python libraries using the requirements.txt file:


pip install -r requirements.txt


4. **Set the Groq API Key**
You need to create a .env file to store your API key. Create a file named .env in the root of the project and add the following line:


GROQ_API_KEY=your_groq_api_key_here
Replace your_groq_api_key_here with your actual Groq API key.

5. **Run the FastAPI Server**
Start the FastAPI development server using Uvicorn:

uvicorn main:app --reload
The server should start at http://127.0.0.1:8000.

6. **Test the API**
You can now test the API using curl or any API client (like Postman). Here's an example using curl:

curl -X POST -H "Content-Type: application/json" -d "{\"prompt\":\"Once upon a time\"}" http://localhost:8000/complete-text


The expected response should look like this:
json
Copy code
{
  "completion": "Once upon a time, there was a small village in the mountains..."
}


