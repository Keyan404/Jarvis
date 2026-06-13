import httpx
import logging
from app.config.settings import settings

logger = logging.getLogger(__name__)

class GroqService:
    def __init__(self):
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.3-70b-versatile" # Stable production Groq model

    async def get_chat_completion(self, message: str) -> str:
        api_key = settings.groq_api_key

        if not api_key:
            logger.warning("GROQ_API_KEY is not configured. Running in fallback simulation mode.")
            return f"[Simulated Response] You said: '{message}'. Please configure your GROQ_API_KEY in the .env file to enable live AI responses."

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are Jarvis, a highly intelligent, futuristic, and helpful personal AI assistant. Keep responses helpful, clear, and concise."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(self.api_url, headers=headers, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    return data["choices"][0]["message"]["content"]
                else:
                    error_msg = f"Groq API returned status {response.status_code}: {response.text}"
                    logger.error(error_msg)
                    return f"Error: Unable to get response from Groq. (Status Code: {response.status_code})"
                    
        except httpx.RequestError as exc:
            error_msg = f"HTTP Request failed while contacting Groq: {exc}"
            logger.error(error_msg)
            return "Error: Network communication issue with AI service."
        except Exception as exc:
            error_msg = f"Unexpected error in GroqService: {exc}"
            logger.error(error_msg)
            return "Error: An unexpected internal error occurred."
