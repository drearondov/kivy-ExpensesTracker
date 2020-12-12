from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from app.components.card.card import Card
from app.components.transactions.transaction import DailyTransactions, Transaction
from app.components.transactionform.transactionform import TransactionForm
from library.settings import local_user


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def show_date(self):
        today = date.today()
        self.ids['today'].text = today.strftime("%A, %d/%m/%Y")
        self.ids['time_period'].text = today.strftime("%B %Y").upper()

        username = local_user.user_info['first_name']
        self.ids['user_name'].markup = True
        self.ids['user_name'].text = f"Hello [font=assets/fonts/BalooBhai2-Bold]{username}![/font]"

    def show_accounts(self):
        accounts = local_user.accounts

        if accounts != None:
            for account in accounts.each():
                account_card = Card(group='accounts').update_card(account.val())
                self.ids['accounts_slider'].add_widget(account_card)

    def show_transactions(self, account='account_01', date_object=date.today()):
        transactions_data = local_user.get_monthly_transactions(account, date_object)

        for transaction_date, transactions_list in transactions_data.items():
            daily_transaction = DailyTransactions().build_daily_transactions(transaction_date, transactions_list, account)
            self.ids['transaction_slider'].add_widget(daily_transaction)

            for transaction in transactions_list:
                transaction = Transaction().build_transaction(transaction)
                self.ids['transaction_slider'].add_widget(transaction)

    def change_month(self, direction):
        current_time =  datetime.strptime(self.ids['time_period'].text.lower(),"%B %Y")
        month = relativedelta(months=1)

        if direction: # If true, add one month
            current_time += month
        else:
            current_time -= month

        self.ids['time_period'].text = current_time.strftime("%B %Y").upper()
        self.ids['transaction_slider'].clear_widgets()

        self.show_transactions(date_object=current_time)