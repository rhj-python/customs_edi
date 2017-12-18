# coding:utf-8
from cStringIO import StringIO

from flask import (
Blueprint,make_response,request,session,
url_for,redirect,render_template,jsonify)
import qiniu

from utils.captcha.xtcaptcha import Captcha
from utils.rhjredis import Utils_Redis
from constants import QINIU_ACCESS_KEY,QINIU_SECRET_KEY,QINIU_BUCKET_NAME

bp=Blueprint('common',__name__,url_prefix='/common')


@bp.route('/graph_captcha/')
def graph_captcha():
    text,image=Captcha.gene_code()
    outer=StringIO()
    image.save(outer,'png')
    content=outer.getvalue()
    response=make_response(content)
    response.content_type='image/png'
    Utils_Redis.set(text.lower(),text.lower(),ex=2*60)

    return response

@bp.route('/qiniu_upload_token/')
def qiniu_upload_token():
    q=qiniu.Auth(QINIU_ACCESS_KEY,QINIU_SECRET_KEY)

    token=q.upload_token(QINIU_BUCKET_NAME)

    return jsonify(dict(uptoken=token))