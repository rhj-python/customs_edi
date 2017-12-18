# coding:utf-8

from flask import (Blueprint,
redirect,request,url_for,render_template,
views,session)


from forms.customs_forms import CustomsLoginForm,CustomsEmployeeLoginForm
from decorators.customs_decorators import customs_login_required
from constants import CUSTOMS_SESSION_ID,EMPLOYEE_SESSION_ID

bp=Blueprint('customs_account',__name__,url_prefix='/customs_account')


@bp.route('/')
def customs_account_index():
    return u'customs_index'


class Customs_Login(views.MethodView):
    def get(self,**kwargs):
        context=dict(**kwargs)
        return render_template('customs/customs_customs_login.html',**context)

    def post(self):
        form= CustomsLoginForm(request.form)
        if form.validate():
            next=request.args.get('next')
            if next:
                return redirect(next)
            else:
                return redirect(url_for('customs.customs_index'))
        else:
            return self.get(message=form.get_error())

bp.add_url_rule('/customs_login/',view_func=Customs_Login.as_view('customs_login'))

@bp.route('/customs_logout/')
def customs_logout():
    if session.get(CUSTOMS_SESSION_ID):
        session.pop(CUSTOMS_SESSION_ID)
    else:
        session.pop(EMPLOYEE_SESSION_ID)
    return redirect(url_for('customs_account.customs_choice_login',next='/customs/'))


class Customs_Employee_Login(views.MethodView):
    def get(self,**kwargs):
        context=dict(**kwargs)
        return render_template('customs/customs_employee_login.html',**context)

    def post(self):
        form= CustomsEmployeeLoginForm(request.form)
        if form.validate():
            next=request.args.get('next')
            if next:
                return redirect(next)
            else:
                return redirect(url_for('customs.customs_index'))
        else:
            return self.get(message=form.get_error())

bp.add_url_rule('/employee_login/',view_func=Customs_Employee_Login.as_view('employee_login'))


@bp.route('/choice_login/')
def customs_choice_login():
    next=request.args.get('next','')
    context=dict(next=next)
    return render_template('customs/customs_choice_login.html',**context)