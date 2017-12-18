# coding:utf-8

from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf import CSRFProtect
from flask_socketio import SocketIO

import config

app = Flask('customs_edi')
app.debug = True
app.config.from_object(config)

CSRFProtect(app)
db=SQLAlchemy(app)
mail=Mail(app)
socketio=SocketIO(app)

customs_bp=Blueprint('customs',__name__,url_prefix='/customs')