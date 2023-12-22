# pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
from filesharer import FileSharer

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder # fait le lien avec le fichier .kv
#need to install [ackage opencv-python manually
import requests

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camara.play = True

    def stop(self):
        self.ids.camara.play = False

    def capture(self):
        pass

class ImageScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
