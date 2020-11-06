from datetime import date
from logging import root
from kivy.uix.screenmanager import Screen

from app.views.homescreen.homescreen import HomeScreen

from library import secrets
from library.authentication import Authentication
from library.settings import local_user


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.auth = Authentication()
        self.home = HomeScreen()
    
    def login(self, email, password):
        email = secrets.email
        password = secrets.password
        code, content = self.auth.login(email, password)

        if code == True:
            self.manager.current = 'home_screen'
            local_user.get_user_data(content)
            self.manager.ids['home_screen'].show_date()
            self.manager.ids['home_screen'].show_accounts()
            #self.manager.ids['home_screen'].show_transactions()
        else:
            self.ids['login_error'].text = content
