import os
os.environ['KIVY_IMAGE'] = 'sdl2'

import kivy
kivy.require('1.11.1')

from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from firebase import Authentication


class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class NewLogScreen(Screen):
    pass


GUI = Builder.load_file('main.kv')

class MainApp(App):
    
    def build(self):
        self.auth = Authentication()

        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

if __name__ == "__main__":
    MainApp().run()