class ChatbotAPIError(Exception):
    """Custom exception for chatbot API-related errors."""
    def __init__(self, message):
        super().__init__(message)