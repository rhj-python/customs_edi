# coding:utf-8


from flask import (Blueprint,
redirect,views,request,session,url_for,render_template)


from forms.front_forms import (SMSCaptchaForm, FrontRegistForm,
FrontLoginForm
)
from utils.ajax_to_form import ajax_form
from utils import xtjson
from constants import FRONT_SESSION_ID


bp=Blueprint('front_account',__name__,url_prefix='/front_account')

@bp.route('/')
def front_account_index():
    return u'front_account_index'

class Front_Login_View(views.MethodView):
    def get(self):
        return render_template('front/front_login.html')

    def post(self):
        form= FrontLoginForm(request.form)
        next=request.args.get('next','/')
        if form.validate():
            return xtjson.json_result(data=next)
        else:
            return xtjson.json_params_error(message=form.get_error())


bp.add_url_rule('/login/',view_func=Front_Login_View.as_view('front_login'))

class Front_Regist_View(views.MethodView):
    def get(self):
        return render_template('front/front_regist.html')

    def post(self):
        return ajax_form(FrontRegistForm,request.form)


bp.add_url_rule('/regist/',view_func=Front_Regist_View.as_view('front_regist'))

@bp.route('/sms_captcha/',methods=['POST'])
def front_sms_captcha():
    return ajax_form(SMSCaptchaForm,request.form)

@bp.route('/logout/',methods=['GET'])
def front_logout():
    id=session.get(FRONT_SESSION_ID)
    if id:
        session.pop(FRONT_SESSION_ID)
    return redirect(url_for('front_account.front_login'))

