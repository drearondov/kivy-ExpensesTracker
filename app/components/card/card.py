from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior

from library.variables import account_type, currency_format


class Card(BoxLayout, ButtonBehavior):
    """
    Class representing a card with each account stats.
    """
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

    def update_card(self, data):
        self.ids['card_title'].text = data['account_name'].upper()
        self.ids['card_image'].source = account_type[data['account_type']]
        self.ids['card_text'].text = currency_format[data['account_currency']].format(data['account_balance'])

        return self
