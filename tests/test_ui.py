import unittest
from ui.main_window import CodeAssistApp
import tkinter as tk

class TestCodeAssistApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = CodeAssistApp(self.root)

    def test_initial_setup(self):
        self.assertIsInstance(self.app.chat_area, tk.Text)
        self.assertIsInstance(self.app.user_input, tk.Entry)
        self.assertIsInstance(self.app.send_button, tk.Button)

if __name__ == '__main__':
    unittest.main()
