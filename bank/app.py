import os
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
cred = credentials.Certificate(token)
firebase_admin.initialize_app(cred)
