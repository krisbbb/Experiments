class SignQuiz():

    def SetCallback(self, callback):
        self.callback = callback
    
    def SelectOption(self, target):
        self.callback(target, "video", "Father.mp4")

    def NewQuiz(self):
        self.callback("stats", "text", "select NEW for new quiz")
        self.callback("confirmation", "text", "NEW")
