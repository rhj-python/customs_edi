# coding:utf-8
from datetime import datetime
import json

from flask import (Blueprint,
redirect,request,url_for,render_template,
abort,g)
from werkzeug.datastructures import ImmutableMultiDict

from models.customs_models import (Customs_Zone,
Company,Customs_Zone_Reply,Triple_Agreement,Triple_Status)
from models.common_models import (Proxy,
Import_Proxy_Agreement,Export_Proxy_Agreement,
Document,Document_Type,Trade_Mode,Pay_Mode,Declaration_Status,
Tax_Mode,Tax_Free_Mode,Transport_Mode,Transaction_Mode,Document_Type,Document,
Settlement_Mode,Use,Currency,Import_Customs_Declaration,
Export_Customs_Declaration,Commodity,
)
from decorators.customs_decorators import customs_login_required
from utils.ajax_to_form import ajax_form
from forms.customs_forms import (
CustomsAddZoneForm,CustomsEditZoneForm,
CustomsDeleteZoneForm,AgreementApprovalSuccessForm,
AgreementApprovalFailForm,
CustomsAddProxyAgreementForm,
ImportCustomsDeclarationForm,AddCommodityForm,
AddDocumentForm,EditImportDeclarationForm,
CollectTaxForm,CheckForm,RefundForm,CheckSuccessForm,
)
from forms.common_forms import AddTripleAgreementForm,CancelTripleAgreementForm
from utils import xtjson
from exts import db
from exts import customs_bp as bp
from models.model_helper import Helper,Filter_Agreement,Declaration_Class
from utils.pagination import pagination
from constants import SHOW_PAGE,SINGLE_PAGE_NUM
from models.tax_rate_helper import Tax_Calculator
from decorators.customs_decorators import permission_required



@bp.route('/')
@customs_login_required
def customs_index():
    return render_template('customs/customs_base.html')

@bp.route('/zone/')
@customs_login_required
def customs_zone():
    customs_zones=Customs_Zone.query.all()
    context=dict(customs_zones=customs_zones)
    return render_template('customs/customs_zone.html',**context)

@bp.route('/add_zone/',methods=['POST'])
def customs_add_zone():
    return ajax_form(CustomsAddZoneForm,request.form)

@bp.route('/edit_zone/',methods=['POST'])
def customs_edit_zone():
    return ajax_form(CustomsEditZoneForm,request.form)

@bp.route('/delete_zone/',methods=['POST'])
def customs_delete_zone():
    return ajax_form(CustomsDeleteZoneForm,request.form)

@bp.route('/triple_agreement/',methods=['GET'])
@customs_login_required
def customs_triple_agreement():
    agreements=g.employee.company.agreements
    search=request.args.get('search')
    if search:
        agreements=db.session.query(Triple_Agreement).join(Customs_Zone).filter(Customs_Zone.name.like('%'+search+'%')).order_by(Triple_Agreement.sign_time.desc()).all()

    context=dict(agreements=agreements)
    return render_template('customs/customs_triple_agreement.html',**context)

@bp.route('/add_triple_agreement/',methods=['GET','POST'])
@customs_login_required
def customs_add_triple_agreement():
    if request.method=='GET':
        now=datetime.now()
        all_zones=Customs_Zone.query.all()
        company_zones=map(lambda agreement:agreement.zone if agreement.status.id==1 or agreement.status.id==2 else None,g.employee.company.agreements)
        show_zones=list(set(all_zones)-set(company_zones))
        show_zones=sorted(show_zones,key=lambda zone:zone.id)
        context=dict(now=now,show_zones=show_zones)
        return render_template('customs/customs_add_triple_agreement.html',**context)
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
@customs_login_required
def customs_cancel_triple_agreement():
    return ajax_form(CancelTripleAgreementForm,request.form)

@bp.route('/agreement_list/<int:filter_id>/',methods=['GET','POST'])
@customs_login_required
def customs_agreement_list(filter_id=2):
    statuses=Triple_Status.query.all()
    agreements=Triple_Agreement.query.all()
    if filter_id!=0:
        agreements=db.session.query(Triple_Agreement).join(Triple_Status).filter(Triple_Status.id==filter_id)
    search=request.args.get('search')
    if search:
        agreements=db.session.query(Triple_Agreement).join(Company,Customs_Zone).filter(db.or_(Triple_Agreement.id.like('%'+search+'%'),
                Company.company_name.like('%'+search+'%'),Company.organization_code.like('%'+search+'%'),Customs_Zone.name.like('%'+search+'%'),
                ))
    context=dict(statuses=statuses,agreements=agreements,current_filter_id=filter_id)
    return render_template('customs/customs_agreement_list.html',**context)


@bp.route('/approval_success/<int:agreement_id>/',methods=['POST'])
@customs_login_required
def customs_approval_success(agreement_id):
    return ajax_form(AgreementApprovalSuccessForm,request.form)


@bp.route('/approval_fail/<int:agreement_id>/',methods=['GET','POST'])
@customs_login_required
def customs_approval_fail(agreement_id):
    if request.method=='GET':
        agreement=Triple_Agreement.query.filter_by(id=agreement_id).first()
        replys=db.session.query(Customs_Zone_Reply).filter(Customs_Zone_Reply.id.in_([4,5]))
        context=dict(agreement=agreement,replys=replys)
        return render_template('customs/customs_agreement_approval_fail.html',**context)
    else:
        return ajax_form(AgreementApprovalFailForm,request.form)

@bp.route('/proxy_list/',methods=['GET'])
@customs_login_required
def customs_proxy_list():
    customs_company=g.employee.company

    context=dict(customs_company=customs_company)
    return render_template('customs/customs_proxy_list.html',**context)


@bp.route('/proxy_detail/<int:proxy_id>/<int:filter_id>/',methods=['GET'])
@customs_login_required
def customs_proxy_detail(proxy_id,filter_id=1):
    search = request.args.get('search')
    proxy = Proxy.query.filter_by(id=proxy_id).first()
    if not proxy:
        abort(404)
    else:
        filter_class=Filter_Agreement(proxy.import_agreements,proxy.export_agreements)
        import_agreements,export_agreements=filter_class.filter_dict.get(filter_id)() if filter_class.filter_dict.get(filter_id) else (None,None)
        context = dict(proxy=proxy, import_agreements=import_agreements, export_agreements=export_agreements,current_filter_id=filter_id)

        if search:
            import_agreements = proxy.import_agreements.filter(
                db.or_(Import_Proxy_Agreement.id == int(search) if search.isdigit() else search,
                       Import_Proxy_Agreement.bl_code == int(search) if search.isdigit() else search)).order_by(
                Import_Proxy_Agreement.import_or_export_date.desc())
            export_agreements = proxy.export_agreements.filter(
                db.or_(Export_Proxy_Agreement.id == int(search) if search.isdigit() else search,
                       Export_Proxy_Agreement.bl_code == int(search) if search.isdigit() else search)).order_by(
                Export_Proxy_Agreement.import_or_export_date.desc())
            context.update(import_agreements=import_agreements,export_agreements=export_agreements)

        return render_template('customs/customs_proxy_detail.html', **context)

@bp.route('/add_proxy_agreement/<int:proxy_id>/',methods=['GET','POST'])
@customs_login_required
def customs_add_proxy_agreement(proxy_id):
    if request.method=='GET':
        context=Helper.proxy_agreement_add(proxy_id)
        return render_template('customs/customs_add_proxy_agreement.html',**context)
    else:
        print request.form
        return ajax_form( CustomsAddProxyAgreementForm,request.form)

@bp.route('/proxy_agreement_detail/<int:agreement_type_id>/<int:agreement_id>/',methods=['GET'])
@customs_login_required
def customs_proxy_agreement_detail(agreement_type_id,agreement_id):
    context = Helper.proxy_agreement_edit(agreement_type_id, agreement_id)
    return render_template('customs/customs_proxy_agreement_detail.html', **context)


@bp.route('/import_declaration_list/<int:page>/<int:filter_id>/<int:sort_id>/<int:asc_id>/',methods=['GET'])
@customs_login_required
@permission_required('handler','customs_view')
def customs_import_declaration(page=1,filter_id=0,sort_id=1,asc_id=1):
    declarations=g.employee.company.customs_import_declarations
    context=Helper.customs_declaration(declarations,'import_trade',page,filter_id,sort_id,asc_id,search_1='pre_entry_code',search_2='business_company.company_name')
    return render_template('customs/customs_import_declaration_list.html',**context)


@bp.route('/export_declaration_list/<int:page>/<int:filter_id>/<int:sort_id>/<int:asc_id>/',methods=['GET'])
@customs_login_required
def customs_export_declaration(page=1,filter_id=0,sort_id=1,asc_id=1):
    declarations=g.employee.company.customs_export_declarations
    context = Helper.customs_declaration(declarations,'export_trade',page,filter_id,sort_id,asc_id,search_1='pre_entry_code',search_2='business_company.company_name')
    search = request.args.get('search')
    if search:
        declarations = filter(lambda
                                  declaration: search in declaration.pre_entry_code or search in declaration.business_company.company_name,
                              declarations)
        context.update(declarations=declarations)

    return render_template('customs/customs_export_declaration_list.html',**context)

@bp.route('/add_import_declaration/',methods=['GET'])
@customs_login_required
def customs_add_import_declaration():
    context = Helper.customs_declaration_template(request, trade_type='import_trade')
    return render_template('customs/customs_add_import_declaration.html', **context)


@bp.route('/add_import_declaration_ajax/',methods=['POST'])
@customs_login_required
def customs_add_import_declaration_ajax():
    return Helper.add_import_save_declaration(request.form)

@bp.route('/add_import_declaration_submit/',methods=['POST'])
@customs_login_required
def customs_add_import_declaration_submit():
    return Helper.add_import_submit_declaration(request.form)


@bp.route('/edit_import_declaration/<string:declaration_uuid>/',methods=['GET'])
@customs_login_required
def customs_edit_import_declaration(declaration_uuid):
    declaration=Import_Customs_Declaration.query.filter_by(uuid=declaration_uuid).first()
    agreements=Import_Proxy_Agreement.query.all()
    uses=Use.query.all()

    context=Helper.customs_declaration_include()
    context.update(declaration=declaration,uses=uses,agreements=agreements)
    return render_template('customs/customs_edit_import_declaration.html',**context)

@bp.route('/edit_import_declaration_ajax/',methods=['POST'])
@customs_login_required
def customs_edit_import_declaration_ajax():
    return Helper.edit_import_save_declaration(request.form)


@bp.route('/edit_import_declaration_submit/',methods=['POST'])
@customs_login_required
def customs_edit_import_declaration_submit():
    return Helper.edit_import_submit_declaration(request.form)


@bp.route('/add_export_declaration/',methods=['GET'])
@customs_login_required
def customs_add_export_declaration():
    context=Helper.customs_declaration_template(request,trade_type='export_trade')
    return render_template('customs/customs_add_export_declaration.html', **context)

@bp.route('/add_export_declaration_ajax/',methods=['POST'])
@customs_login_required
def customs_add_export_declaration_ajax():
    return Helper.add_export_save_declaration(request.form)

@bp.route('/add_export_declaration_ajax/',methods=['POST'])
@customs_login_required
def customs_add_export_declaration_submit():
    return Helper.add_export_submit_declaration(request.form)

@bp.route('/edit_export_declaration/<string:declaration_uuid>/',methods=['GET'])
@customs_login_required
def customs_edit_export_declaration(declaration_uuid):
    declaration=Export_Customs_Declaration.query.filter_by(uuid=declaration_uuid).first()
    agreements=Export_Proxy_Agreement.query.all()
    settlement_modes=Settlement_Mode.query.all()

    context=Helper.customs_declaration_include()
    context.update(declaration=declaration,agreements=agreements,settlement_modes=settlement_modes)
    return render_template('customs/customs_edit_export_declaration.html',**context)

@bp.route('/edit_export_declaration_ajax/',methods=['POST'])
@customs_login_required
def customs_edit_export_declaration_ajax():
    return Helper.edit_export_save_declaration(request.form)

@bp.route('/edit_export_declaration_submit/',methods=['POST'])
@customs_login_required
def customs_edit_export_declaration_submit():
    return Helper.edit_export_submit_declaration(request.form)


@bp.route('/customs_import_check/<int:page>/<int:filter_id>/<int:sort_id>/<int:asc_id>/')
@customs_login_required
def customs_import_check(page=1,filter_id=0,sort_id=5,asc_id=1):
    declarations=Import_Customs_Declaration.query.filter(Import_Customs_Declaration.status_id!=1)
    context=Helper.customs_declaration(declarations, 'import_trade', page, filter_id, sort_id, asc_id,search_1='declaration_code',search_2='customs_date')

    return render_template('customs/customs_import_check.html',**context)

@bp.route('/customs_export_check/<int:page>/<int:filter_id>/<int:sort_id>/<int:asc_id>/')
@customs_login_required
def customs_export_check(page=1,filter_id=0,sort_id=5,asc_id=1):
    declarations=Export_Customs_Declaration.query.filter(Export_Customs_Declaration.status_id!=1)
    context=Helper.customs_declaration(declarations, 'export_trade', page, filter_id, sort_id, asc_id,search_1='declaration_code',search_2='customs_date')

    return render_template('customs/customs_export_check.html',**context)

@bp.route('/customs_import_check_detail/<string:declaration_uuid>/')
@customs_login_required
def customs_import_check_detail(declaration_uuid):
    declaration=Import_Customs_Declaration.query.filter_by(uuid=declaration_uuid).first()
    context=dict(declaration=declaration)
    if not declaration:
        abort(404)
    else:
        return render_template('customs/customs_import_check_detail.html',**context)

@bp.route('/import_collect_tax/',methods=['POST'])
@customs_login_required
def customs_import_collect_tax():
    return ajax_form(CollectTaxForm,request.form)

@bp.route('/import_check_commodity/',methods=['POST'])
@customs_login_required
def customs_import_check_commodity():
    return ajax_form(CheckForm,request.form)

@bp.route('/import_refund/',methods=['POST'])
@customs_login_required
def customs_import_refund():
    return ajax_form(RefundForm,request.form)

@bp.route('/customs_export_check_detail/<string:declaration_uuid>/')
@customs_login_required
def customs_export_check_detail(declaration_uuid):
    declaration = Export_Customs_Declaration.query.filter_by(uuid=declaration_uuid).first()
    context = dict(declaration=declaration)
    if not declaration:
        abort(404)
    else:
        return render_template('customs/customs_export_check_detail.html', **context)

@bp.route('/export_collect_tax/',methods=['POST'])
@customs_login_required
def customs_export_collect_tax():
    return ajax_form(CollectTaxForm,request.form)

@bp.route('/export_check_commodity/',methods=['POST'])
@customs_login_required
def customs_export_check_commodity():
    return ajax_form(CheckForm,request.form)

@bp.route('/export_refund/',methods=['POST'])
@customs_login_required
def customs_export_refund():
    return ajax_form(RefundForm,request.form)

@bp.route('/import_check_success/',methods=['POST'])
@customs_login_required
def customs_import_check_success():
    return ajax_form(CheckSuccessForm,request.form)

@bp.route('/export_check_success/',methods=['POST'])
@customs_login_required
def customs_export_check_success():
    return ajax_form(CheckSuccessForm,request.form)




