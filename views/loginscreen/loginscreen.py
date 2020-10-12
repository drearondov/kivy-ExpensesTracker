from kivy.uix.screenmanager import Screen

from library.authentication import Authentication
#from views.homescreen.homescreen import HomeScreen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.auth = Authentication()
    
    def login(self, email, password):
        code, content = self.auth.login(email, password)

        if code == True:
            self.manager.current = 'home_screen'
            # populate homescreen
        else:
            self.ids['login_error'].text = content
