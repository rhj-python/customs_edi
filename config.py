# coding:utf-8
import os
from datetime import timedelta

# csrf配置
SECRET_KEY=os.urandom(24)


# 数据库配置
USERNAME='root'
PASSWORD='2312231223'

HOST='127.0.0.1'
PORT='3306'

DATABASE='customs_edi'
CHARSET='charset=utf8'

SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@{}:{}/{}?{}' .format(
    USERNAME,PASSWORD,HOST,PORT,DATABASE,CHARSET
)

DB_URI=SQLALCHEMY_DATABASE_URI

SQLALCHEMY_TRACK_MODIFICATIONS=False

# session配置
PERMANENT_SESSION_LIFETIME=timedelta(days=60)


# mail配置
MAIL_SERVER='smtp.qq.com'
MAIL_PORT='587'

MAIL_USERNAME='657930342@qq.com'
MAIL_PASSWORD='jjqyoamssczwbfbf'

MAIL_DEFAULT_SENDER='657930342@qq.com'
MAIL_USE_TLS=True