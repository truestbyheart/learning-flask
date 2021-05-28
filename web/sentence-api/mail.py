from flask import Flask
from flask_mail import Mail

from config import MAIL_PASSWORD, MAIL_PORT, MAIL_SERVER, MAIL_USE_SSL, MAIL_USE_TLS, MAIL_USERNAME


def getEmailInstance():
    server = Flask(__name__)
    
    server.config['MAIL_SERVER'] = MAIL_SERVER
    server.config['MAIL_PORT'] = int(MAIL_PORT)
    server.config['MAIL_USERNAME'] = MAIL_USERNAME
    server.config['MAIL_PASSWORD'] = MAIL_PASSWORD
    server.config['MAIL_USE_TLS'] = bool(MAIL_USE_TLS)
    server.config['MAIL_USE_SSL'] = False

    return Mail(server)
