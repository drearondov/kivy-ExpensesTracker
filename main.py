import os

os.environ['KIVY_IMAGE'] = 'sdl2'

import kivy
kivy.require('1.11.0')

from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

from kivy.app import App
from kivy.storage.jsonstore import JsonStore

from app.views.startscreen.startscreen import StartScreen
from app.views.loginscreen.loginscreen import LoginScreen
from app.views.signupscreen.signupscreen import SignupScreen
from app.views.homescreen.homescreen import HomeScreen
from app.views.welcomescreen.welcomescreen import WelcomeScreen

from library.settings import local_user


class MainApp(App):

    def build(self):
        self.title = "moneyBox"

    def on_start(self):

        self.root.current = 'start_screen'

        local_store = JsonStore('library/local_user.json')
        local_user.local_ID = local_store.get('local_user')['local_ID']

        if local_user.local_ID != "":
            self.root.current = 'home_screen'
            local_user.get_user_data(local_user.local_ID)
            self.root.ids['home_screen'].show_date()
            self.root.ids['home_screen'].show_accounts()
            self.root.ids['home_screen'].show_transactions()
        else:
            self.root.current = 'welcome_screen'

    def on_stop(self):
        local_store = JsonStore('library/local_user.json')
        local_store.put('local_user', local_ID=local_user.local_ID)

if __name__ == "__main__":
    MainApp().run()