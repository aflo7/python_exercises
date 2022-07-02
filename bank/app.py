import os
from cryptography.fernet import Fernet

import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
from regex import E
load_dotenv()

googleToken = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
cryptoToken = os.environ.get("CRYPTOCODE")
cred = credentials.Certificate(googleToken)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bank-79eda-default-rtdb.firebaseio.com/'
})
bank_users = db.reference('/users')

def get_number_of_users():
    current_users = bank_users.get()
    if current_users is None:
        return 0
    return len(current_users)

def create_new_user(name=None, amount="0", membership_status=None):
    size = get_number_of_users()
    
    bank_users.update({size: {
        'name': name,
        'amount': amount,
        'membership_status': membership_status
    }})
    

# def encrypt(message: bytes, key: bytes) -> bytes:
#     return Fernet(key).encrypt(message)

# def decrypt(token: bytes, key: bytes) -> bytes:
#     return Fernet(key).decrypt(token)

# create_new_user("Andres", "150", "silver")