token = os.environ.get("firebase-service-key")

cred = credentials.Certificate(f"path/to/{token}.json")
firebase_admin.initialize_app(cred)
ref = db.reference("/")