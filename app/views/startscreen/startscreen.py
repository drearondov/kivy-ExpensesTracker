from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen

from app.views.welcomescreen.welcomescreen import WelcomeScreen
from app.views.homescreen.homescreen import HomeScreen

from library.settings import local_user

class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
    
    def fetch_local_user(self):
        """
        Find if there is a local user.
        """
        local_store = JsonStore('library/local_user.json')
        local_user.local_ID = local_store.get('local_user')['local_ID']

        if local_user.local_ID != "":
            self.manager.current = 'home_screen'
            local_user.get_user_data(local_user.local_ID)
            self.manager.ids['home_screen'].show_date()
            self.manager.ids['home_screen'].show_accounts()
            #self.manager.ids['home_screen'].show_transactions()
        else:
            self.manager.current = 'welcome_screen'
