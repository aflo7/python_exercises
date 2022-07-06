
import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

googleToken = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
bank_password = os.environ.get("BANK-MANAGER-PASSWORD")
cred = credentials.Certificate(googleToken)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://bank-79eda-default-rtdb.firebaseio.com/"}
)
# list of User objects. index starting at 0
bank_users = db.reference("/users")


def get_number_of_users():
    current_users = bank_users.get()
    if current_users is None:
        return 0
    return len(current_users)


# accepts a BankUser object
def create_new_user(u):
    size = get_number_of_users()

    bank_users.update(
        {
            size: {
                "name": u.name,
                "amount": u.amount,
                "membership_status": u.membership_status,
            }
        }
    )


def read_user_data():
    print("-----")
    li = bank_users.get()

    for user in li:
        print(user)
    print("-----")


def delete_user(u):
    li = bank_users.get()
    for user in li:
        if (
            user["amount"] == u.amount
            and user["membership_status"] == u.membership_status
            and user["name"] == u.name
        ):
            li.remove(user)
            break
    bank_users.set(li)


# update BankUser values, but only if you have a password. one password(bank_password) is able to update all user info
# old_data and new_data are separate BankUser objects
def update_user_info(password, old_data, new_data):
    if password != bank_password:
        return 0
    li = bank_users.get()

    for user in li:
        if (
            user["amount"] == old_data.amount
            and user["membership_status"] == old_data.membership_status
            and user["name"] == old_data.name
        ):
            user["amount"] = new_data.amount
            user["membership_status"] = new_data.membership_status
            user["name"] = new_data.name
            break
    bank_users.set(li)
    return 1 #success