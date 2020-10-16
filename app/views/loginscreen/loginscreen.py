from datetime import date
from kivy.uix.screenmanager import Screen

from library.authentication import Authentication
from library.database import local_user
from app.views.homescreen.homescreen import HomeScreen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.auth = Authentication()
        self.home = HomeScreen()
    
    def login(self, email, password):
        code, content = self.auth.login(email, password)

        if code == True:
            self.manager.current = 'home_screen'
            local_user.get_user_data(content)
            self.manager.ids['home_screen'].show_date()
            self.manager.ids['home_screen'].show_accounts()
            self.manager.ids['home_screen'].show_transactions()
            # populate homescreen
        else:
            self.ids['login_error'].text = content
