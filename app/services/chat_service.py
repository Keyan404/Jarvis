from app.services.groq_service import GroqService

class ChatService:
    def __init__(self):
        self.groq_service = GroqService()

    async def generate_response(self, user_message: str) -> str:
        # Business logic goes here (e.g. prompt shaping, context building, validation)
        # Simply calls Groq service to fetch the reply.
        return await self.groq_service.get_chat_completion(user_message)

chat_service = ChatService()
