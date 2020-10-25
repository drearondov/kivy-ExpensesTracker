import pyrebase

from collections import defaultdict
from datetime import datetime
from kivy.app import App

from library.secrets import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

class User():
    """
    Class in charge of interacting with the firebase database.
    """

    def __init__(self) -> None:
        self.db = firebase.database()
        self.local_ID = ''
        self.user_info = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'currency': '',
        }
        self.user_data = None
        self.accounts = None

    def create_new_user(self, local_ID, username, first_name, last_name, email, currency="PEN"):
        data = {
            'username': str(username),
            'first_name': str(first_name),
            'last_name': str(last_name),
            'email': str(email),
            'currency': str(currency),
        }
        self.db.child('users').child(str(local_ID)).set(data)

    def get_user_data(self, local_ID):
        self.user_data = self.db.child('users').child(str(local_ID)).get()
        self.user_info = self.user_data.val()
        self.accounts = self.db.child('users').child(str(local_ID)).child('accounts').get()


    def get_monthly_transactions(self, account, date_object):
        """
        Returns a dictionary of transactions grouped by date.
        """
        transactions = self.db.child('users').child(str(self.local_ID)).child('accounts').child(str(account)).child('transactions').get()
        transactions = self.db.sort(transactions, "date", True)
        monthly_transactions = defaultdict(list)
        
        for transaction in transactions.each():
            transaction_date = datetime.strptime(transaction.val()['date'], '%d/%m/%Y')
            
            if transaction_date.month == date_object.month:
                monthly_transactions[transaction_date].append(transaction.val())

        return monthly_transactions #already sorted

    def new_transaction(self, amount, category, sub_category, date, description, transaction_type, account):
        data = {
            'date': str(date),
            'category': str(category),
            'sub_category': str(sub_category),
            'transaction_type': str(transaction_type),
            'description': str(description),
            'amount': str(amount)
        }
        self.db.child('users').child(self.local_ID).child('accounts').child(account).child('transactions').push(data)


if __name__ == "__main__":
    pass