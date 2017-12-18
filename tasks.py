# coding:utf-8
from celery import Celery

from exts import app
from utils.xtmail import send_mail
from utils.alidayu_sms import ali_cms

def make_celery(app):
    celery=Celery(app.import_name,broker='redis://:2312231223@192.168.1.4:6379/',
                  backend='redis://:2312231223@192.168.1.4:6379')
    BaseTask=celery.Task

    class ContextTask(BaseTask):
        abstract=True

        def __call__(self,*args,**kwargs):
            with app.app_context():
                return BaseTask.__call__()

    celery.Task=ContextTask
    return celery


celery=make_celery(app)

# celery -A tasks.celery worker

@celery.task
def celery_send_email(subject,receivers,body=None,html=None):
    with app.app_context():
        return send_mail(subject=subject,receivers=receivers,body=body,html=html)


@celery.task
def celery_send_sms(telephone,captcha):
    with app.app_context():
        return ali_cms(telephone,captcha)

