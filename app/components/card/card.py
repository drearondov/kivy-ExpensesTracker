from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.utils import get_color_from_hex as hex_color

from library.variables import account_type, currency_format


class Card(ToggleButtonBehavior, BoxLayout):
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

    def change_state(self):
        card_data = {
            'card_title': self.ids['card_title'].text,
            'card_image': self.ids['card_image'].source,
            'card_text': self.ids['card_text'].text
        }

        if self.state == 'down':
            with self.canvas.before:
                Color(0.2, 0.2, 0.2, 1)
                RoundedRectangle(size=self.size, pos=self.pos, radius=[36])

            with self.canvas:
                RoundedRectangle(size=self.size, pos=self.pos, radius=[36], source= 'assets/img/card_black.png')

            self.ids['card_title'].color = hex_color('#FDFDFD')
            self.ids['card_image'].source = card_data['card_image'].replace('.png', '_white.png')
            self.ids['card_text'].color = hex_color('#FDFDFD')
        else:
            with self.canvas.before:
                Color(0.949, 0.949, 0.949, 1)
                RoundedRectangle(size=self.size, pos=self.pos, radius=[36])

            with self.canvas:
                RoundedRectangle(size=self.size, pos=self.pos, radius=[36], source= 'assets/img/card.png')
            
            self.ids['card_title'].color = hex_color('#333333')
            self.ids['card_image'].source = card_data['card_image'].replace('_white.png', '.png')
            self.ids['card_text'].color = hex_color('#333333')
