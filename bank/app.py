import os
from firebase_admin import credentials
from dotenv import load_dotenv
load_dotenv()

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
token = os.environ.get("firebase-service-key")
print(token)