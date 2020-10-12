import os
os.environ['KIVY_IMAGE'] = 'sdl2'

import kivy
kivy.require('1.11.1')

from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

from kivy.app import App

from app.views.welcomescreen.welcomescreen import WelcomeScreen
from app.views.loginscreen.loginscreen import LoginScreen


class MainApp(App):
    title = "Seneca's Wallet"

    welcomeScreen = WelcomeScreen()
    loginScreen = LoginScreen()


if __name__ == "__main__":
    MainApp().run()