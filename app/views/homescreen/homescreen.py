from datetime import date

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from app.components.card.card import Card
from library.dataStorage import DatabaseInteraction


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.db = DatabaseInteraction()

    def show_date(self, local_ID):
        today = date.today()
        self.ids['today'].text = today.strftime("%A, %d. %B %Y")
        self.ids['time_period'].text = today.strftime("%B %Y").upper()

        username = self.db.get_users_data(local_ID)
        self.ids['user_name'].markup = True
        self.ids['user_name'].text = f"Hello [font=assets/fonts/Anton-Regular]{username}![/font]"

    def show_accounts(self, local_ID):
        accounts = self.db.get_user_accounts(local_ID)

        if accounts != None:
            for account in accounts.each():
                account_card = Card().update_card(account.val())
                self.ids['accounts_slider'].add_widget(account_card)


        add_card = Builder.load_string('''
BoxLayout:
    canvas:
        Color:
            rgba: hex('#FFFFFF')
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [36]

    ImageButton:
        source: 'assets/img/plus.png'
        on_press: print('Add account')
        ''')

        self.ids['accounts_slider'].add_widget(add_card)
