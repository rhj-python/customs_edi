# coding:utf-8

from flask import (request,render_template,
abort,redirect,url_for,g)


from exts import customs_bp as bp
from decorators.customs_decorators import customs_login_required
from utils.ajax_to_form import ajax_form
from forms.manage_forms import (ManageResetPwdForm,
ManageResetEmailForm,ManageAddEmployeeForm,
ManageEditEmployeeForm,ManageBlackEmployeeForm,
ManageAddRoleForm,ManageEditRoleForm,ManageDeleteRoleForm,
ManageAddPermissionForm,ManageEditPermissionForm,
ManageUserBlackForm,)
from tasks import celery_send_email
from utils.captcha.xtcaptcha import Captcha
from utils.rhjredis import Utils_Redis
from utils import xtjson
from decorators.customs_decorators import permission_required,manage_permission_required
from models.manage_models import (Role,
Permission,Handler,Menu)
from models.customs_models import Employee,Company
from models.front_models import Front_User


@bp.route('/profile/',methods=['GET'])
@customs_login_required
def manage_profile():
    return render_template('manage/manage_profile.html')

@bp.route('/reset_pwd/',methods=['GET'])
@customs_login_required
def manage_reset_pwd():
    return render_template('manage/manage_reset_pwd.html')

@bp.route('/reset_pwd_post/',methods=['POST'])
@customs_login_required
def manage_reset_pwd_post():
    return ajax_form(ManageResetPwdForm,request.form)

@bp.route('/reset_email/',methods=['GET'])
@customs_login_required
def manage_reset_email():
    return render_template('manage/manage_reset_email.html')

@bp.route('/reset_email_post/',methods=['POST'])
@customs_login_required
def manage_reset_email_post():
    return ajax_form(ManageResetEmailForm,request.form)

@bp.route('/send_captcha_email/',methods=['POST'])
@customs_login_required
def manage_send_captcha_email():
    email=request.form.get('email')
    Captcha.number=6
    code=Captcha.gene_text()
    Captcha.number=4
    db_code=Utils_Redis.get('email')
    if db_code:
        return xtjson.json_params_error(message=u'已向该邮箱发送邮件了,请稍后再试!')
    else:
        Utils_Redis.set(email,code.lower(),ex=10*60)

        dic=dict(subject=u'报关系统修改邮箱验证码',receivers=email,body=u'您的验证码为 %s 在10分钟有效' %code)
        celery_send_email.delay(**dic)

        return xtjson.json_result()


@bp.route('/employee_manage/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_employee_manage():
    employees=g.employee.company.employees
    roles=Role.query
    context=dict(employees=employees,roles=roles)
    return render_template('manage/manage_employee_manage.html',**context)

@bp.route('/add_employee/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_add_employee():
    roles=Role.query
    context=dict(roles=roles)
    return render_template('manage/manage_add_employee.html',**context)

@bp.route('/add_employee_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_add_employee_ajax():
    return ajax_form(ManageAddEmployeeForm,request.form)

@bp.route('/edit_employee/<int:employee_id>/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_edit_employee(employee_id):
    employee=Employee.query.filter_by(id=employee_id).first()
    roles=Role.query
    context=dict(emp=employee,roles=roles)
    return render_template('manage/manage_edit_employee.html', **context)

@bp.route('/edit_employee_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_edit_employee_ajax():
    return ajax_form(ManageEditEmployeeForm,request.form)

@bp.route('/black_employee_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_black_employee_ajax():
    return ajax_form(ManageBlackEmployeeForm,request.form)

@bp.route('/role_manage/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_role_manage():
    roles=Role.query
    context=dict(roles=roles)
    return render_template('manage/manage_role_manage.html',**context)

@bp.route('/add_role/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_add_role():
    roles=Role.query
    permissions=Permission.query
    context=dict(roles=roles,permissions=permissions)
    return render_template('manage/manage_add_role.html',**context)

@bp.route('/add_role_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_add_role_ajax():
    return ajax_form(ManageAddRoleForm,request.form)


@bp.route('/edit_role/<int:role_id>/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_edit_role(role_id):
    role=Role.query.filter_by(id=role_id).first()
    permissions=Permission.query
    if not role:
        abort(404)

    context=dict(role=role,permissions=permissions)
    return render_template('manage/manage_edit_role.html',**context)

@bp.route('/edit_role_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_edit_role_ajax():
    return ajax_form(ManageEditRoleForm,request.form)

@bp.route('/delete_role_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_delete_role():
    return ajax_form(ManageDeleteRoleForm,request.form)


@bp.route('/permission_manage/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_permission_manage():
    permissions=Permission.query
    context=dict(permissions=permissions)
    return render_template('manage/manage_permission_manage.html',**context)

@bp.route('/add_permission/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_add_permission():
    handlers=Handler.query
    menus=Menu.query
    context=dict(handlers=handlers,menus=menus)
    return render_template('manage/manage_add_permission.html',**context)

@bp.route('/add_permission_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_add_permissions_ajax():
    return ajax_form(ManageAddPermissionForm,request.form)

@bp.route('/edit_permission/<int:permission_id>/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_edit_permission(permission_id):
    permission=Permission.query.filter_by(id=permission_id).first()
    if not permission:
        abort(404)
    else:
        handlers = Handler.query
        menus = Menu.query
        permission=permission
        context = dict(handlers=handlers, menus=menus,permission=permission)
        return render_template('manage/manage_edit_permission.html', **context)

@bp.route('/edit_permission_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_edit_permission_ajax():
    return ajax_form(ManageEditPermissionForm,request.form)


@bp.route('/user_manage/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_user_manage():
    users=Front_User.query
    context=dict(users=users)
    return render_template('manage/manage_user_manage.html',**context)


@bp.route('/user_black_ajax/',methods=['POST'])
@customs_login_required
@manage_permission_required
def manage_user_black_ajax():
    return ajax_form(ManageUserBlackForm,request.form)

@bp.route('/client_company_list/',methods=['GET'])
@customs_login_required
@manage_permission_required
def manage_client_company_list():
    companys=Company.query.filter(Company.id!=g.employee.company.id)
    context=dict(companys=companys)
    return render_template('manage/manage_client_company_list.html',**context)