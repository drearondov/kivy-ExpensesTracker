from datetime import datetime
from kivy.uix.boxlayout import BoxLayout

from library.settings import local_user
from library.variables import categories, currency_format

class Transaction(BoxLayout):
    """
    Class representing a single transaction.
    """
    def __init__(self, **kwargs):
        super(Transaction, self).__init__(**kwargs)

    def build_transaction(self, transaction):
        self.ids['type'].source = categories[transaction['category']]
        self.ids['description'].text = transaction['description']

        if transaction['transaction_type']:
            self.ids['amount'].text = currency_format[transaction['currency']].format(-float(transaction['amount']))
        else:
            self.ids['amount'].text = currency_format[transaction['currency']].format(float(transaction['amount']))

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
        
        daily_total = 0

        for transaction in transactions_list:
            if transaction['transaction_type']:
                daily_total -= float(transaction['amount'])
            else:
                daily_total += float(transaction['amount'])

        account_currency = local_user.accounts.val()[account]['account_currency']

        self.ids['daily_total'].text = currency_format[account_currency].format(daily_total)

        return self
