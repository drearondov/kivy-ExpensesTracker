from datetime import datetime

from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex as hex_color

from library.settings import local_user
from library.variables import currency_format

class TransactionForm(BoxLayout):
    """
    Class representing the form to add transactions.
    """
    def __init__(self, **kwargs) -> None:
        super(TransactionForm, self).__init__(**kwargs)
        self.category = 'food'
        self.transaction_type = False
        self.account = 'account_01' # REVIEW: Set default values for user
        self.currency = 'PEN'

    def set_category(self, category) -> None:
        self.category = category

    def set_type(self, transaction_type):
        self.transaction_type = transaction_type

    def validate_form(self, amount, date, description) -> None:
        """
        Validates data entered in the transaction form and calls for addition if
        the information is valid.
        """
        data = {}
        validation_list = []

        # Validate amount
        try:
            float(amount)
            data['amount'] = str(amount)
            validation_list.append(True)
        except ValueError:
            self.ids['transaction_amount'].hint_text = "Please enter a valid amount"
            self.ids['transaction_amount'].hint_text_color = hex_color("#CC241D")
            validation_list.append(False)

        # Validate date
        try:
            datetime.strptime(date, "%d/%m/%Y")
            data['date'] = str(date)
            validation_list.append(True)
        except ValueError:
            self.ids['transaction_date'].hint_text = "Date entered does not match format dd/mm/yyyy"
            self.ids['transaction_date'].hint_text_color = hex_color("#CC241D")
            validation_list.append(False)

        # Validate description
        if len(description) == "0":
            self.ids['transaction_description'].hint_text = "Please enter a description"
            self.ids['transaction_description'].hint_text_color = hex_color("#CC241D")
            validation_list.append(False)
        else:
            data['description'] = str(description)
            validation_list.append(True)

        # Items that come from selectors and dropdowns
        data['account'] = str(self.account)
        data['category'] = str(self.category)
        data['transaction_type'] =  self.transaction_type
        data['transaction_currency'] = str(self.currency)

        if False in validation_list:
            pass
        else:
            self.add_transaction(data)

    def add_transaction(self, data) -> None:
        """
        Receives validated data and sends it to the database.
        """
        local_user.new_transaction(data, data['account'])
        self.parent.parent.show_accounts()
        self.parent.parent.show_transactions()

    def slide(self, state, *args) -> None:
        if state:
            animate = Animation(pos_hint={'top': 0.9})
            animate.start(self)
        else:
            animate = Animation(pos_hint={'top': -0.1})
            animate.start(self)