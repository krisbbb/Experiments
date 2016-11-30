import kivy
kivy.require('1.2.0')

from kivy.uix.video import Video
from kivy.uix.label import Label

from os import listdir
from os.path import isfile, join, splitext

class SignQuizAssets:
    def __init__(self, **kwargs):
        self.assetdir = kwargs["dir"]
        files = [f for f in listdir(self.assetdir) if isfile(join(self.assetdir, f))]
        self.assets = {}
        for f in files:
            filename = join(self.assetdir, f)
            key = splitext(f)[0]
            self.assets[key] = filename
    
    def ListAssets(self):
        return list(self.assets.keys())
    
    def GetAsset(self, type, assetKey):
        if(type == "text"):
            return Label(text=assetKey)
        if(type == "sign"):
            return Video(source=self.assets[assetKey], state='play', options={'eos': 'loop'}) 



