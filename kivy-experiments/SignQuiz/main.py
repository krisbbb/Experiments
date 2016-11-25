import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty

from signquiz import SignQuiz

class QuizLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(QuizLayout, self).__init__(**kwargs)
        self.widget = Label()
        self.add_widget(self.widget)
    
    def AddWidget(self, widget):
        oldwidget = self.widget
        self.widget = widget
        self.remove_widget(oldwidget)
        self.add_widget(widget)

class LayoutButton(ButtonBehavior, QuizLayout):
    def __init__(self, **kwargs):
        super(LayoutButton, self).__init__(**kwargs)

class SignQuizGui(BoxLayout):
    stats = ObjectProperty(None)
    question = ObjectProperty(None)

    option0 = ObjectProperty(None)
    option1 = ObjectProperty(None)
    option2 = ObjectProperty(None)
    option3 = ObjectProperty(None)

    selection = ObjectProperty(None)
    confirmation = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SignQuizGui, self).__init__(**kwargs)
        self.signquiz = SignQuiz()
        self.signquiz.SetCallback(self.SignQuizCallback)
        self.signquiz.NewQuiz()

    def SignQuizCallback(self, target, type, arg):
        widget = Label(text=arg)
        if(type == "video"):
            widget = Video(source=arg, state='play', options={'eos': 'loop'})
        self.ids[target].AddWidget(widget)
        
    def OnPress(self, buttonName):
        self.signquiz.SelectOption(buttonName)
    
class SignQuizApp(App):

    def build(self):
        return SignQuizGui()

if __name__ == '__main__':
    SignQuizApp().run()
