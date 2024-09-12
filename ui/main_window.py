import tkinter as tk
from tkinter import ttk
from chatbot.bot import CodeAssistBot
import threading

class CodeAssistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Assist Chatbot")

        # Set window size and make it resizable
        self.root.geometry("800x600")
        self.root.configure(bg="#f7f7f8")  # Light background color
        self.root.resizable(True, True)

        # Chatbot instance
        self.bot = CodeAssistBot()

        # Create a style for modern look
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#007AFF", foreground="white", font=("Helvetica", 12, "bold"))
        self.style.configure("TEntry", padding=5, fieldbackground="white", foreground="black", font=("Helvetica", 14))
        self.style.configure("TLabel", background="#f7f7f8", foreground="black", font=("Helvetica", 12))

        # Chat area (Light background with subtle borders)
        self.chat_area = tk.Text(self.root, height=25, width=80, bg="white", fg="black", wrap="word", font=("Helvetica", 12), padx=10, pady=10, bd=0, relief="flat")
        self.chat_area.grid(row=0, column=0, padx=20, pady=10, columnspan=2, sticky="nsew")
        self.chat_area.config(state=tk.DISABLED)  # Make the chat area read-only

        # Scrollbar for chat area
        self.scrollbar = ttk.Scrollbar(self.root, command=self.chat_area.yview)
        self.scrollbar.grid(row=0, column=2, sticky="ns")
        self.chat_area['yscrollcommand'] = self.scrollbar.set

        # Tags for alignment
        self.chat_area.tag_configure("left", justify="left")
        self.chat_area.tag_configure("right", justify="right")

        # Frame for input field and send button
        input_frame = tk.Frame(self.root, bg="#f7f7f8")  # Match the window background color
        input_frame.grid(row=1, column=0, padx=20, pady=10, columnspan=2, sticky="ew")

        # Create input area (simplified input box)
        self.user_input = tk.Entry(input_frame, width=70, font=("Helvetica", 14), relief="flat", bg="white", highlightthickness=1, highlightcolor="#007AFF", bd=0)
        self.user_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Send button with a more visible size and spacing
        self.send_button = tk.Button(input_frame, text="Send", command=self.send_message, bg="white", fg="#808080", font=("Helvetica", 12, "bold"), relief="flat", bd=0)
        self.send_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)

        # Adjust grid layout to allocate space properly for the input and button
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=0)

        # Make the layout responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def send_message(self):
        user_message = self.user_input.get()
        if user_message:
            self.chat_area.config(state=tk.NORMAL)  # Enable chat area for inserting new messages
            self.chat_area.insert(tk.END, "You: " + user_message + "\n", "right")
            self.chat_area.config(state=tk.DISABLED)  # Make chat area read-only again
            self.user_input.delete(0, tk.END)

            # Start a new thread to get the bot response
            thread = threading.Thread(target=self.get_bot_response, args=(user_message,))
            thread.start()

    def get_bot_response(self, user_message):
        bot_response = self.bot.generate_response(user_message)
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "Code_Assist: " + bot_response + "\n", "left")
        self.chat_area.config(state=tk.DISABLED)  # Disable chat area after inserting the message
        self.chat_area.yview(tk.END)  # Auto-scroll to the bottom

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CodeAssistApp(root)
    root.mainloop()