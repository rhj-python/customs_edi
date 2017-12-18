# coding:utf-8
import constants
import top


def ali_cms(telephone,captcha):
    app_key = constants.ALIDAYU_APP_KEY
    app_secret = constants.ALIDAYU_APP_SECRET
    req = top.setDefaultAppInfo(app_key, app_secret)
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.extend = ""
    req.sms_type = 'normal'
    req.sms_free_sign_name = constants.ALIDAYU_SIGN_NAME

    req.sms_param = constants.ALIDAYU_SMS_PARAMS % (captcha)

    req.rec_num = telephone.decode('utf-8').encode('ascii')
    req.sms_template_code = constants.ALIDAYU_TEMPLATE_CODE
    resp = req.getResponse()
    return resp
