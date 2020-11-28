from os import stat
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

from library.settings import local_user

class TransactionForm(BoxLayout):
    """
    Class representing the form to add transactions.
    """
    def __init__(self, **kwargs) -> None:
        super(TransactionForm, self).__init__(**kwargs)
        self.category = None
        self.transaction_type = None

    def set_category(self, category) -> None:
        self.category = category

    def set_type(self, transaction_type):
        self.transaction_type = transaction_type

    def add_transaction(self, amount, date, description, account) -> None:
        """
        Receives form results and sends them to the database
        """
        data = {
            'date': str(date),
            'category': str(self.category),
            'transaction_type': str(self.transaction_type), # bool: True for expenses, False for income.
            'description': str(description),
            'amount': str(amount) # numerical value of the transaction.
        }
        local_user.new_transaction(data, account)
        self.parent.parent.show_accounts()
        # self.parent.parent.show_transactions()

    def slide(self, state) -> None:
        if state:
            pass
        else:
            animate = Animation(y=-self.size[1])
            animate.start(self)