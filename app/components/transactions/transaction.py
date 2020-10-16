from datetime import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from library.database import local_user
from library.variables import sub_categories, currency_format

class Transaction(BoxLayout):
    """
    Class representing the transactions for each account.
    """
    def __init__(self, **kwargs):
        super(Transaction, self).__init__(**kwargs)

    def build_transaction(self, transaction):
        self.ids['type'].source = sub_categories[transaction['sub_category']]
        self.ids['description'].text = transaction['description']
        self.ids['amount'].text = currency_format[transaction['currency']].format(transaction['amount'])

        return self

class DailyTransactions(GridLayout):
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

        for transaction in transactions_list:
            print(local_user.accounts.val()[account]['account_currency'])
            transaction['currency'] = local_user.accounts.val()[account]['account_currency']
            transaction_block = Transaction().build_transaction(transaction)
            self.add_widget(transaction_block)

        return self
