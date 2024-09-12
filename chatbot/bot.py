import openai
from config import OPENAI_API_KEY


class CodeAssistBot:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def generate_response(self, user_input):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"