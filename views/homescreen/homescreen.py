from kivy.uix.screenmanager import Screen

from library.dataStorage import DatabaseInteraction

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.db = DatabaseInteraction()

    def show_user_accounts(self):
        pass