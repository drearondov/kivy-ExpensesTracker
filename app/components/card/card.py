from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior


class Card(BoxLayout, ButtonBehavior):
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

    def update_card(self, data):
        image_path = {
            'Cash': 'assets/img/cash.png',
            'Credit': 'assets/img/credit.png'
        }

        currency_symbol = {
            'PEN': 'S/.',
            'USD': '$'
        }

        self.ids['card_title'].text = data['account_name'].upper()
        self.ids['card_image'].source = image_path[data['account_type']]
        self.ids['card_text'].text = f"{currency_symbol[data['account_currency']]} {data['account_balance']}"

        return self
