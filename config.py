import os

from dotenv import load_dotenv
import json
load_dotenv()

TOKEN = os.getenv("TOKEN")
APP_NAME = os.getenv("APP_NAME")
GOOGLE_CREDENTIALS = json.loads(os.getenv("GOOGLE_CREDENTIALS", "{}"))
USERS = json.loads(os.getenv("USERS", "[]"))
PORT = int(os.environ.get('PORT', '8443'))
