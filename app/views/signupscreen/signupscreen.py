from kivy.uix.screenmanager import Screen

from library.authentication import Authentication
from library.dataStorage import DatabaseInteraction

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.auth = Authentication()
        self.db = DatabaseInteraction()

    def signup(self, username, first_name, last_name, email, password):
        code , content = self.auth.signup(email, password)

        if code == True:
            self.db.create_new_user(content['localId'], username, first_name, last_name, email)
            self.manager.current = 'home_screen'
        else:
            self.ids['sign_up_error'].text = content