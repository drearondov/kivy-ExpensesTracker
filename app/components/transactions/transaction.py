from datetime import datetime
from kivy.uix.boxlayout import BoxLayout

from library.settings import local_user
from library.variables import categories, currency_format

class Transaction(BoxLayout):
    """
    Class representing the transactions for each account.
    """
    def __init__(self, **kwargs):
        super(Transaction, self).__init__(**kwargs)

    def build_transaction(self, transaction):
        self.ids['type'].source = categories[transaction['category']]
        self.ids['description'].text = transaction['description']
        self.ids['amount'].text = currency_format[transaction['currency']].format(transaction['amount'])

        return self

class DailyTransactions(BoxLayout):
    """
    Class representing the transactions grouped by day.
    """
    def __init__(self, **kwargs):
        super(DailyTransactions, self).__init__(**kwargs)

    def build_daily_transactions(self, transaction_date, transactions_list, account):
        """
        Returns a block of one day's transaction
        """
        self.ids['transaction_date'].text = transaction_date.strftime('%A %d')
        # Calculate daily total

        return self
