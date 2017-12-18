# coding:utf-8
from exts import mail
from flask_mail import Message

def send_mail(subject,receivers,body=None,html=None):
    assert receivers
    if not body and not html:
        return False
    if isinstance(receivers,str) or isinstance(receivers,unicode):
        receivers=[receivers]
    message=Message(subject=subject,recipients=receivers,body=body,html=html)
    try:
        mail.send(message)
    except:
        return False
    return True
