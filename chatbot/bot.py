from openai import OpenAI
from config import OPENAI_API_KEY
from chatbot.exceptions import ChatbotAPIError

class CodeAssistBot:
    def __init__(self):
        try:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
        except Exception as e:
            raise ChatbotAPIError(f"Failed to initialize OpenAI client: {e}")

    def generate_response(self, user_input):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )

            # Extract and return the 'content' field from the 'message' object
            return completion.choices[0].message.content
        except Exception as e:
            raise ChatbotAPIError(f"Error while generating response: {e}")