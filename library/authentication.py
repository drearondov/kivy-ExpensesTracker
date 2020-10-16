import pyrebase
import requests

from library.database import local_user
from library.secrets import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

class Authentication():

    def __init__(self):
        self.auth = firebase.auth()

    def login(self, email, password):
        try:
            sign_in_request = self.auth.sign_in_with_email_and_password(email, password)
            localID = sign_in_request['localId']
            local_user.local_ID = localID
            return True, localID

        except requests.exceptions.HTTPError as e:
            response = e.args[0].response
            error_response = response.json()['error']['message']

            error_message = {
                'INVALID_EMAIL': 'Please insert a valid email address.',
                'MISSING_PASSWORD': 'Please enter your password.',
                'EMAIL_NOT_FOUND': 'Email not registered, please sign up.',
                'INVALID_PASSWORD': 'Wrong password.'
            }

            return False, error_message[error_response]

    def signup(self, email, password):
        try:
            sign_up_request = self.auth.create_user_with_email_and_password(email, password)
            
            return True, sign_up_request

        except requests.exceptions.HTTPError as e:
            response = e.args[0].response
            error_response = response.json()['error']['message']

            error_message = {
                'INVALID_EMAIL': 'Please insert a valid email address.',
                'MISSING_PASSWORD': 'Please add a valid password.',
                'WEAK_PASSWORD: Password should be at least 6 characters': 'Password should be at least 6 characters.',
                'EMAIL_EXIST': 'User already exist.'
            }

            return False, error_message[error_response]


if __name__ == "__main__":
    pass
