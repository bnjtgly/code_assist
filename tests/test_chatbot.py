import unittest
from chatbot.bot import CodeAssistBot

class TestCodeAssistBot(unittest.TestCase):

    def setUp(self):
        self.bot = CodeAssistBot()

    def test_generate_response(self):
        response = self.bot.generate_response("What is Python?")
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_handle_empty_input(self):
        response = self.bot.generate_response("")
        self.assertTrue("Error" in response)

if __name__ == '__main__':
    unittest.main()
