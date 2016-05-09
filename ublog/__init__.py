# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'username@qq.com'  # os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = 'password'  # os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'username@qq.com'

from routes import mail

mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:903326@localhost/ublog'

from models import db

db.init_app(app)

import ublog.routes
