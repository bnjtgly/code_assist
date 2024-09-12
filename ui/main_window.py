import tkinter as tk
from chatbot.bot import CodeAssistBot
import threading


class CodeAssistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Assist Chatbot")

        # Chatbot instance
        self.bot = CodeAssistBot()

        # Create chat area
        self.chat_area = tk.Text(self.root, height=20, width=50)
        self.chat_area.pack(pady=10)

        # Create input area
        self.user_input = tk.Entry(self.root, width=40)
        self.user_input.pack(pady=5)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self):
        user_message = self.user_input.get()
        if user_message:
            self.chat_area.insert(tk.END, "You: " + user_message + "\n")
            self.user_input.delete(0, tk.END)

            # Start a new thread to get the bot response
            thread = threading.Thread(target=self.get_bot_response, args=(user_message,))
            thread.start()

    def get_bot_response(self, user_message):
        bot_response = self.bot.generate_response(user_message)
        self.chat_area.insert(tk.END, "Code_Assist: " + bot_response + "\n")