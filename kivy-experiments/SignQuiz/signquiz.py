import random

class SignQuiz():
    def __init__(self, **kwargs):
        self.words = kwargs["words"]

    def SetCallback(self, callback):
        self.callback = callback
    
    def SelectOption(self, target):
        type = random.choice(['text', 'sign'])
        word = random.choice(self.words)
        self.callback(target, type, word)

    def NewQuiz(self):
        self.callback("stats", "text", "select NEW for new quiz")
        self.callback("confirmation", "text", "NEW")
