import pyrebase
import requests

from kivy.app import App

from secrets import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

# Authentication
class Authentication():

    def __init__(self):
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        pass

    def sign_up(self, username, first_name, last_name, email, password):
        try:
            sign_up_request = self.auth.create_user_with_email_and_password(email, password)
            
            database = App.get_running_app().db
            database.create_new_user(sign_up_request['localId'], username, first_name, last_name, email)


        except requests.exceptions.HTTPError as e:
            response = e.args[0].response
            error_response = response.json()['error']['message']

            error_message = {
                'INVALID_EMAIL': 'Please insert a valid email address.',
                'MISSING_PASSWORD': 'Please add a valid password.',
                'WEAK_PASSWORD: Password should be at least 6 characters': 'Password should be at least 6 characters.',
                'EMAIL_EXIST': 'User already exist.'
            }

            App.get_running_app().root.ids['new_log_screen'].ids['sign_up_error'].text = error_message[error_response]

# Database
class DatabaseInteraction():

    def __init__(self):
        self.db = firebase.database()

    def create_new_user(self, local_ID, username, first_name, last_name, email, currency="PEN"):
        data = {
            'username': str(username),
            'first_name': str(first_name),
            'last_name': str(last_name),
            'email': str(email),
            'currency': str(currency),
        }
        self.db.child('users').child(str(local_ID)).set(data)
        App.get_running_app().change_screen('home_screen')

    # def create_new_account(self, local_ID, account_name, account_type):
    #     try:
    #         accounts = self.db.child(local_ID).child('accounts').get()
    #         last_account = accounts.each()[-1]
    #         last_account.key()
            #self.db.child('users').child(token_ID).child('accounts').child(f'account_{account_counter}')

    # def create_new_transaction(self, ammount, date, description, main_category, sub_category, transaction_type):
    #     pass
