# coding:utf-8
import json
from datetime import datetime

from flask import (Blueprint,g,abort,
redirect,request,url_for,render_template)

from decorators.front_decorators import front_login_required,front_trade_type
from models.common_models import (Business_Content,Proxy,Company,Pay_Mode,Trade_Mode,\
Import_Proxy_Agreement,Export_Proxy_Agreement,Import_Customs_Declaration,Export_Customs_Declaration,
Declaration_Status,
)
from exts import db
from forms.front_forms import (AddProxyAgreementForm,
AddProxyForm,CancelProxyFrom,OperateProxyAgreementForm,
FrontRefundReasonForm,FrontPayTaxNowForm)
from utils.ajax_to_form import ajax_form
from models.common_models import Document_Type
from models.model_helper import Helper,Choice_Model
from models.customs_models import (Triple_Agreement,
Customs_Zone,Employee,Triple_Status)
from models.front_models import Front_User
from utils import xtjson
from forms.common_forms import AddTripleAgreementForm,CancelTripleAgreementForm
from utils.pagination import pagination
from constants import SINGLE_PAGE_NUM,SHOW_PAGE
from models.model_helper import Search_Class
from models.ws_model_helper import single_chat,group_chat,Online

bp=Blueprint('front',__name__)

@bp.route('/')
@front_login_required
def front_index():
    return redirect(url_for('front.front_entrust_approval'))

@bp.route('/entrust_approval/')
@front_login_required
def front_entrust_approval():
    business_company=g.front_user.company
    customs_company=Company.query.filter_by(id=1).first()
    proxy=Proxy.query.filter_by(client_id=business_company.id,broker_id=customs_company.id).first()
    context={}
    if proxy:
        context.update(proxy=proxy)

    return render_template('front/front_entrust_approval.html',**context)

@bp.route('/agree_proxy/')
@front_login_required
def front_agree_proxy():
    return render_template('front/front_agree_proxy.html')

@bp.route('/customs_proxy/',methods=['GET'])
@front_login_required
def front_customs_proxy():

    business_contents=Business_Content.query.all()
    customs_company=Company.query.filter_by(id=1).first()
    business_company=g.front_user.company

    proxy=Proxy.query.filter_by(broker_id=customs_company.id,client_id=business_company.id).first()
    if not proxy:
        proxy = Proxy(is_active=True)
        proxy.broker = customs_company
        proxy.client = business_company
        db.session.add(proxy)
        db.session.commit()

    context=Helper.proxy_agreement_add(proxy.id)

    contents=request.args.get('contents',default='[1]')
    if contents:
        contents=[int(i) for i in json.loads(contents)]
    print contents

    expiry_time=request.args.get('expiry_time',type=int)

    context=dict(context,business_contents=business_contents,customs_company=customs_company,
                 business_company=business_company,
                 current_contents=contents,current_expiry_time=expiry_time)
    return render_template('front/front_customs_proxy.html',**context)

@bp.route('/add_proxy_agreement/',methods=['POST'])
@front_login_required
def front_add_agreement():
    return ajax_form(AddProxyAgreementForm,request.form)

@bp.route('/add_proxy/',methods=['POST'])
@front_login_required
def front_add_proxy():
    return ajax_form(AddProxyForm,request.form)

@bp.route('/cancel_proxy/',methods=['POST'])
@front_login_required
def front_cancel_proxy():
    return ajax_form(CancelProxyFrom,request.form)

@bp.route('/proxy_agreement_list/',methods=['GET'])
@front_login_required
def front_proxy_agreement_list():
    business_contents = Business_Content.query.all()
    customs_company = Company.query.filter_by(id=1).first()
    business_company = g.front_user.company


    proxy = Proxy.query.filter_by(broker_id=customs_company.id, client_id=business_company.id).first()

    context=Helper.proxy_agreement_add(proxy_id=proxy.id)

    context.update(business_contents=business_contents,customs_company=customs_company,
                    business_company=business_company)
    return render_template('front/front_proxy_agreement_list.html',**context)

@bp.route('/agreement_detail/<int:agreement_type_id>/<string:agreement_uuid>/')
@front_login_required
def front_agreement_detail(agreement_type_id,agreement_uuid):
    context=Helper.proxy_agreement_edit(agreement_type_id,agreement_uuid)

    return render_template('front/front_agreement_detail.html',**context)

@bp.route('/operate_proxy_agreement/',methods=['POST'])
@front_login_required
def front_agree_proxy_agreement():
    return ajax_form( OperateProxyAgreementForm,request.form)

@bp.route('/triple_agreement/',methods=['GET'])
@front_login_required
def front_triple_agreement():
    agreements = g.front_user.company.agreements
    search = request.args.get('search')
    if search:
        agreements = db.session.query(Triple_Agreement).join(Customs_Zone).filter(
            Customs_Zone.name.like('%' + search + '%')).order_by(Triple_Agreement.sign_time.desc()).all()

    context = dict(agreements=agreements)
    return render_template('front/front_triple_agreement.html', **context)

@bp.route('/add_triple_agreement/',methods=['GET','POST'])
@front_login_required
def front_add_triple_agreement():
    if request.method=='GET':
        now=datetime.now()
        all_zones=Customs_Zone.query.all()
        company_zones=map(lambda agreement:agreement.zone if agreement.status.id==1 or agreement.status.id==2 else None,g.front_user.company.agreements)
        show_zones=list(set(all_zones)-set(company_zones))
        show_zones=sorted(show_zones,key=lambda zone:zone.id)
        context=dict(now=now,show_zones=show_zones)
        return render_template('front/front_add_triple_agreement.html',**context)
    else:
        form=AddTripleAgreementForm(request.form)
        if form.validate():
            company_uuid=request.form.get('company_uuid')
            zone_li=request.form.getlist('zone_li[]')

            company=Company.query.filter_by(uuid=company_uuid).first()
            if not company:
                return xtjson.json_params_error(message=u'没有找到该企业!')
            else:
                for zone_id in zone_li:
                    zone=Customs_Zone.query.filter_by(id=zone_id).first()
                    db_agreement=Triple_Agreement.query.filter_by(zone_id=zone.id,company_id=company.id).first()
                    status=Triple_Status.query.filter_by(id=2).first()
                    if not db_agreement:
                        agreement=Triple_Agreement(sign_time=datetime.now())
                        agreement.status=status
                        company.agreements.append(agreement)
                        zone.agreements.append(agreement)
                    else:
                        db_agreement.status = status
                        db_agreement.reply=None

                db.session.commit()
                return xtjson.json_result()
        else:
            return xtjson.json_params_error(message=form.get_error())

@bp.route('/cancel_triple_agreement/',methods=['POST'])
@front_login_required
def front_cancel_triple_agreement():
    return ajax_form(CancelTripleAgreementForm, request.form)

@bp.route('/declaration_status_query/<int:page>/<int:trade_id>/<int:status_id>/<int:sort_id>/<int:asc_id>/',methods=['GET'])
@front_login_required
def front_declaration_status_query(page=1,trade_id=0,status_id=0,sort_id=5,asc_id=2):
    import_declarations=g.front_user.company.business_import_declarations
    export_declarations=g.front_user.company.business_export_declarations
    business_company=g.front_user.company
    statuses=Declaration_Status.query.all()
    search=request.args.get('search')
    if search:
        declarations = list(import_declarations) + list(export_declarations)
        declarations=Search_Class.search_content(search,declarations,search_1='bl_code',search_2='declaration_code',search_3='customs_date')

    else:
        if trade_id==1:
            export_declarations=[]
        elif trade_id==2:
            import_declarations=[]

        declarations=list(import_declarations)+list(export_declarations)


        if status_id!=0:
            declarations=filter(lambda declaration:declaration.status_id==status_id,declarations) if declarations else []


        asc=True

        if asc_id==1:
            asc=False


        if sort_id==5:
            declarations=sorted(declarations,key=lambda declaration: declaration.customs_date,reverse=asc)
        elif sort_id==2:
            declarations = sorted(declarations, key=lambda declaration: declaration.status_id, reverse=asc)

        elif sort_id==7:
            declarations = sorted(declarations, key=lambda declaration: declaration.tax_mode_id, reverse=asc)


    total_num=len(declarations) if declarations else 0

    total_page,start,end,page_li,pre_page,next_page=pagination(page,total_num,SINGLE_PAGE_NUM,SHOW_PAGE)


    context=dict(declarations=declarations[start:end],total_page=total_page,page_li=page_li,
                 pre_page=pre_page,next_page=next_page,show_page=SHOW_PAGE,
                 business_company=business_company,statuses=statuses,
                 current_page=page,current_status_id=status_id,current_trade_id=trade_id,
                 current_sort_id=sort_id,current_asc_id=asc_id)
    return render_template('front/front_declaration_status_query.html',**context)


@bp.route('/import_declaration_detail/<string:declaration_uuid>/',methods=['GET'])
@front_login_required
@front_trade_type
def front_import_declaration_detail(declaration_uuid):
    pass

@bp.route('/export_declaration_detail/<string:declaration_uuid>/',methods=['GET'])
@front_login_required
@front_trade_type
def front_export_declaration_detail(declaration_uuid):
   pass

@bp.route('/refund_reason/',methods=['POST'])
@front_login_required
def front_refund_reason():
    form=FrontRefundReasonForm(request.form)
    if form.validate():
        context=dict(refund_reason=form.declaration.refund_reason)
        return xtjson.json_result(data=context)
    else:
        return xtjson.json_params_error(message=form.get_error())


@bp.route('/check/<string:trade_type>/<string:declaration_uuid>/',methods=['GET'])
@front_login_required
def front_check(trade_type,declaration_uuid):
    context=Choice_Model.choice_one(trade_type,declaration_uuid)
    return render_template('front/front_check.html',**context)

@bp.route('/pay_tax/<string:trade_type>/<string:declaration_uuid>/',methods=['GET'])
@front_login_required
def front_pay_tax(trade_type,declaration_uuid):
    context=Choice_Model.choice_one(trade_type,declaration_uuid)
    return render_template('front/front_pay_tax.html',**context)

@bp.route('/pay_tax_now/',methods=['POST'])
@front_login_required
def front_pay_tax_now():
    return ajax_form(FrontPayTaxNowForm,request.form)

@bp.route('/msg_single/',methods=['GET'])
@front_login_required
def front_msg_single():
    employees=Employee.query.all()
    online_set = Online.online_set
    context=dict(employees=employees,online_set=online_set)
    return render_template('front/front_msg_single.html',**context)

@bp.route('/msg_group/',methods=['GET'])
@front_login_required
def front_msg_group():
    groups = [Front_User]
    context = dict(groups=groups)
    return render_template('front/front_msg_group.html', **context)

@bp.route('/msg_single_detail/<string:model_name>/<string:receiver_name>/')
@front_login_required
def front_msg_single_detail(model_name,receiver_name):
    model=eval(model_name).query.filter_by(username=receiver_name).first()

    s_model=g.front_user.__class__.__name__
    s_id = g.front_user.id
    sender='%s__%s' %(s_model,s_id)
    receiver='%s__%s' %(model_name,model.id)
    messages=single_chat(sender,receiver)

    context=dict(model=model,model_name=model_name,messages=messages)
    return render_template('front/front_msg_single_detail.html',**context)


@bp.route('/msg_group_detail/<string:group_name>/',methods=['GET'])
@front_login_required
def front_msg_group_detail(group_name):
    receiver='%s__%s' %(group_name,'none')
    messages=group_chat(receiver)

    context=dict(group_name=group_name,messages=messages)
    return render_template('front/front_msg_group_detail.html',**context)
