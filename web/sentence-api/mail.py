from flask_mail import Mail

from app import create_app

def getEmailInstance():
    server = create_app()
    
    server.config['MAIL_SERVER']='smtp.mailtrap.io'
    server.config['MAIL_PORT'] = 2525
    server.config['MAIL_USERNAME'] = '005290e9bb6351'
    server.config['MAIL_PASSWORD'] = 'b1f0ba88458501'
    server.config['MAIL_USE_TLS'] = True
    server.config['MAIL_USE_SSL'] = False

    return Mail(server)
