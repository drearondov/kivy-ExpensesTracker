import pyrebase
import requests

from secrets import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

# Authentication
class Authentication():

    def __init__(self):
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        pass

    def sign_up(self, email, password):
        try:
            sign_up_request = self.auth.create_user_with_email_and_password(email, password)
        except requests.exceptions.HTTPError as e:
            response = e.args[0].response
            error_message = response.json()['error']['message']
            print(error_message)
