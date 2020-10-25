import os
os.environ['KIVY_IMAGE'] = 'sdl2'

import kivy
kivy.require('1.11.1')

from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

from kivy.app import App
from kivy.storage.jsonstore import JsonStore

from app.views.welcomescreen.welcomescreen import WelcomeScreen
from library.settings import local_user


class MainApp(App):

    def build(self):
        self.title = "Seneca's Wallet"
        self.welcomeScreen = WelcomeScreen()

    def on_start(self):
        try:
            local_store = JsonStore('library/local_user.json')
            local_user.local_ID = local_store.get('local_user')['local_ID']
        except:
            print('User not found')

    def on_stop(self):
        local_store = JsonStore('library/local_user.json')
        local_store.put('local_user', local_ID=local_user.local_ID)

if __name__ == "__main__":
    MainApp().run()