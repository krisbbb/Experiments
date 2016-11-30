import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

#check what formats are supported for your targetted devices
#for example try h264 video and acc audo for android using an mp4
#container


class VideoApp(App):

    def build(self):
        if len(argv) > 1:
            filename = argv[1]
        else:
            curdir = dirname(__file__)
            filename = join(curdir, 'Father.mp4')

        self.root = FloatLayout()
        self.video = Video(app=self, source=filename, state='play')
        self.root.add_widget(self.video)
        self.grid = None
        self.video.state = 'play'
        return self.root

if __name__ == '__main__':
    VideoApp().run()
