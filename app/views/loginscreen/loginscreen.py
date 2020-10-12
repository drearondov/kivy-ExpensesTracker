from kivy.uix.screenmanager import Screen

from library.authentication import Authentication
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
            self.manager.ids['home_screen'].show_date(content)
            self.manager.ids['home_screen'].show_accounts(content)
            # populate homescreen
        else:
            self.ids['login_error'].text = content
