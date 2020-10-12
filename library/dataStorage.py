import pyrebase

from kivy.app import App

from library.secrets import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

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

    def get_users_data(self, local_ID):
        user_name = self.db.child('users').child(str(local_ID)).child('first_name').get()
        return user_name.val()

    def get_user_accounts(self, local_ID):
        accounts = self.db.child('users').child(str(local_ID)).child('accounts').get()
        return accounts

if __name__ == "__main__":
    db = DatabaseInteraction()
    accounts = db.get_user_accounts('9nKKe68S1LNHx0ZtK3JTXTJN1X83')
    print(accounts.val())