import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.env')

load_dotenv(APP_ROOT)

DEBUG = os.getenv('DEBUG')
MONGODB_URI = os.getenv('MONGODB_URI')
FLASK_ENV = os.getenv('FLASK_ENV')
PORT = os.getenv('PORT')
JWT_SECRET = os.getenv('JWT_SECRET')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
DOMAIN=os.getenv('DOMAIN')
