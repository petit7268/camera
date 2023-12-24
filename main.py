# pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
from filesharer import FileSharer

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder  # fait le lien avec le fichier .kv
# need to install Package opencv-python manually
import time
import requests

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None
        self.ids.camera.texture = None

        pass

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        file_path = f'files/{current_time}.png'
        self.ids.camera.export_to_png(file_path)
        self.manager.current = 'image_screen'


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
