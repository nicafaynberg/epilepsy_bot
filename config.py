import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
APP_NAME = os.getenv("APP_NAME")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
PORT = int(os.environ.get('PORT', '8443'))
