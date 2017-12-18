# coding:utf-8
from flask import abort,g,request,render_template
import json
from functools import wraps

from models.common_models import (
Import_Proxy_Agreement,Export_Proxy_Agreement,Proxy,
Trade_Mode,Pay_Mode,Document_Type,Declaration_Status,
Agreement_Status,Transport_Mode,Transaction_Mode,
Tax_Mode,Tax_Free_Mode,Use,Currency,Document,Commodity,
Import_Customs_Declaration,Export_Customs_Declaration,Settlement_Mode)
from constants import SHOW_PAGE,SINGLE_PAGE_NUM
from utils.pagination import pagination
from utils import xtjson
from exts import db
from forms.customs_forms import (ImportCustomsDeclarationForm,
EditImportDeclarationForm,ExportCustomsDeclarationForm,
EditExportDeclarationForm,)
from constants import IMPORT_DECLARATION_CODE,EXPORT_DECLARATION_CODE
from business_exts import trade_type_dic


class Filter_Agreement(object):


    filter_dict = {}

    def __init__(self,import_agreements,export_agreements):
        self.import_agreements=import_agreements
        self.export_agreements=export_agreements
        self.filter_dict={
                        1:self.show_all,2:self.show_import,3:self.show_export,
                        4:self.show_status_success,
                        5:self.show_status_approval,
                        6:self.show_status_failed
                          }

    def show_all(self):
        return (self.import_agreements,self.export_agreements)

    def show_import(self):
        return (self.import_agreements,None)

    def show_export(self):
        return (None,self.export_agreements)

    def _show_status(self,status_id):
        import_agreements = self.import_agreements.filter_by(status_id=status_id)
        export_agreements = self.export_agreements.filter_by(status_id=status_id)

        return (import_agreements, export_agreements)

    def show_status_success(self):
        return self._show_status(status_id=2)

    def show_status_approval(self):
        return self._show_status(status_id=1)

    def show_status_failed(self):
        return self._show_status(status_id=3)

class Helper(object):
    # trade_type 必须在 'import_trade'和'export_trade\之间选择

    trade_type_dic = dict(import_trade=[Import_Proxy_Agreement, Import_Customs_Declaration, Use.query],
                          export_trade=[Export_Proxy_Agreement, Export_Customs_Declaration, Settlement_Mode.query])

    @classmethod
    def proxy_agreement_add(cls,proxy_id):
        proxy = Proxy.query.filter_by(id=proxy_id).first()
        document_types = Document_Type.query.all()
        trade_modes = Trade_Mode.query.all()
        pay_modes = Pay_Mode.query.all()
        if not proxy:
            abort(404)
        else:
            context = dict(proxy=proxy, document_types=document_types, trade_modes=trade_modes, pay_modes=pay_modes)
            return context

    @classmethod
    def proxy_agreement_edit(cls,agreement_type_id,agreement_uuid):
        agreement = ''
        if agreement_type_id == 1:
            agreement = Import_Proxy_Agreement.query.filter_by(uuid=agreement_uuid).first()
        elif agreement_type_id == 2:
            agreement = Export_Proxy_Agreement.query.filter_by(uuid=agreement_uuid).first()
        trade_modes = Trade_Mode.query.all()
        pay_modes = Pay_Mode.query.all()
        document_types = Document_Type.query.all()

        context = dict(agreement=agreement, current_proxy_agreement_type_id=agreement_type_id,
                       trade_modes=trade_modes, pay_modes=pay_modes, document_types=document_types)

        return context

    @classmethod
    def customs_declaration(cls,declarations,trade_type,page,filter_id,sort_id,asc_id,**kwargs):
        declaration_statuses = Declaration_Status.query.all()
        search=request.args.get('search')

        if search:
            declarations=Search_Class.search_content(search,declarations,**kwargs)
        else:
            if filter_id!=0:
                declarations=declarations.filter_by(status_id=filter_id)

            d=Declaration_Class(declarations,trade_type,sort_id,asc_id)

            declarations=d.query_declaration()

        total_page, start, end, page_li, pre_page, next_page = pagination(page,len(declarations),
                                                                          SINGLE_PAGE_NUM, SHOW_PAGE)

        context = dict(declarations=declarations[start:end], declaration_statuses=declaration_statuses,
                       current_page=page, current_filter_id=filter_id,
                       current_sort_id=sort_id, current_asc_id=asc_id,
                       total_page=total_page, page_li=page_li,
                       pre_page=pre_page, next_page=next_page, show_page=SHOW_PAGE)
        return context

    @classmethod
    def customs_declaration_include(cls):
        trade_modes = Trade_Mode.query
        transport_modes = Transport_Mode.query
        tax_modes = Tax_Mode.query
        tax_free_modes = Tax_Free_Mode.query
        transaction_modes = Transaction_Mode.query
        document_types = Document_Type.query
        currencys = Currency.query

        context = dict(
                    trade_modes=trade_modes,transport_modes=transport_modes,
                    tax_modes=tax_modes,tax_free_modes=tax_free_modes,
                    transaction_modes=transaction_modes,document_types=document_types,
                     currencys=currencys
                       )
        return context

    @classmethod
    def customs_declaration_template(cls,request,trade_type='import_trade'):

        agreement_model,declaration_model,others=cls.trade_type_dic.get(trade_type)
        agreements = db.session.query(agreement_model).outerjoin(declaration_model). \
            filter(declaration_model.agreement_id == None)

        context = Helper.customs_declaration_include()
        context.update(agreements=agreements)
        if trade_type=='import_trade':
            context.update(uses=others)
        else:
            context.update(settlement_modes=others)

        agreement_id = request.args.get('agreement_id')
        if agreement_id:
            current_agreement=agreement_model.query.filter_by(id=agreement_id).first()

            if current_agreement:
                context.update(current_agreement=current_agreement)
        return context

    @classmethod
    def customs_declaration_ajax(cls,form_class,request_form,trade_type='import_trade',edit=False,customs=False):
        agreement_model,declaration_model=cls.trade_type_dic.get(trade_type)[0:2]


        if edit:
            declaration_uuid = request_form.get('declaration_uuid')
            declaration = declaration_model.query.filter_by(uuid=declaration_uuid).first()
            if not declaration:
                return xtjson.json_params_error(message=u'没有找到该报关单')
        else:
            declaration=declaration_model()

        form = form_class(request_form)
        if form.validate():

            for k, v in form.data.iteritems():
                if hasattr(declaration, k):
                    setattr(declaration, k, v)

            commodity_li = request_form.getlist('commodity_li[]')
            document_li = request_form.getlist('document_li[]')

            declaration.commoditys=[]
            for c in commodity_li:
                commodity = Commodity()
                for k, v in json.loads(c).iteritems():
                    if hasattr(commodity, k):
                        setattr(commodity, k, v)
                declaration.commoditys.append(commodity)

            declaration.documents=[]
            for d in document_li:
                document = Document()
                for k, v in json.loads(d).iteritems():
                    if hasattr(document, k):
                        setattr(document, k, v)
                declaration.documents.append(document)

            agreement_id = form.agreement_id.data
            agreement = agreement_model.query.filter_by(id=agreement_id).first()
            status = Declaration_Status.query.filter_by(id=1).first()

            customs_status = Declaration_Status.query.filter_by(id=2).first()

            if customs:
                declaration.status = customs_status

            if not edit:
                declaration.operator_id = g.employee.id
                declaration.business_company = agreement.proxy.client
                declaration.customs_company = agreement.proxy.broker
                declaration.status = status
                db.session.add(declaration)

            if trade_type=='import_type':
                declaration.declaration_code = declaration.id + IMPORT_DECLARATION_CODE
            else:
                declaration.declaration_code = declaration.id + EXPORT_DECLARATION_CODE

            db.session.commit()
            return xtjson.json_result()

        else:
            return xtjson.json_params_error(message=form.get_error())

    # @classmethod
    # def add_ajax(cls,request_form,trade_type,customs):
    #     return cls.customs_declaration_ajax(ExportCustomsDeclarationForm, request_form,
    #         trade_type=trade_type, edit=False,customs=customs)
    #
    # @classmethod
    # def edit_ajax(cls,request_form,trade_type,customs):
    #     return cls.customs_declaration_ajax(
    #         EditExportDeclarationForm, request_form,trade_type=trade_type,
    #         edit=True, customs=customs)

    @classmethod
    def add_import_save_declaration(cls,request_form):
        return cls.customs_declaration_ajax(
            ImportCustomsDeclarationForm,request_form,
            trade_type='import_trade',edit=False,customs=False)

    @classmethod
    def add_import_submit_declaration(cls,request_form):
        return cls.customs_declaration_ajax(
            ImportCustomsDeclarationForm, request_form,
            trade_type='import_trade', edit=False, customs=True)

    @classmethod
    def edit_import_save_declaration(cls,request_form):
        return cls.customs_declaration_ajax(
            EditImportDeclarationForm, request_form,
            trade_type='import_trade', edit=True, customs=False)

    @classmethod
    def edit_import_submit_declaration(cls, request_form):
        return cls.customs_declaration_ajax(
            EditImportDeclarationForm, request_form,
            trade_type='import_trade', edit=True, customs=True)

    @classmethod
    def add_export_save_declaration(cls, request_form):
        return cls.customs_declaration_ajax(
            ExportCustomsDeclarationForm, request_form,
            trade_type='export_trade', edit=False, customs=False)

    @classmethod
    def add_export_submit_declaration(cls, request_form):
        return cls.customs_declaration_ajax(
            ExportCustomsDeclarationForm, request_form,
            trade_type='export_trade', edit=False, customs=True)

    @classmethod
    def edit_export_save_declaration(cls, request_form):
        return cls.customs_declaration_ajax(
            EditExportDeclarationForm, request_form,
            trade_type='export_trade', edit=True, customs=False)

    @classmethod
    def edit_export_submit_declaration(cls, request_form):
        return cls.customs_declaration_ajax(
            EditExportDeclarationForm, request_form,
            trade_type='export_trade', edit=True, customs=True)

class Declaration_Class(object):

    sort_dic={1:'create_time',2:'status_id',3:'business_company_id',4:'import_port',5:'customs_date',6:'trade_mode_id',7:'tax_mode_id'}
    trade_type_dic={'import_trade':'import_port','export_trade':'export_port'}
    asc_dic={1:False,2:True}
    search_dic={}

    def __init__(self,declarations,trade_type,sort_id,asc_id):
        self.sort_dic[4] = self.trade_type_dic.get(trade_type)
        self.trade_type=trade_type
        self.declarations=declarations
        self.sort_id=sort_id
        self.asc_id=asc_id


    @property
    def _d_model(self):
        if not isinstance(self.declarations,list):
            return list(self.declarations)
        else:
            return self.declarations

    @property
    def _d_sort(self):
        return self.sort_dic.get(self.sort_id)

    @property
    def _d_asc(self):
        return self.asc_dic.get(self.asc_id)

    def query_declaration(self):
        return sorted(self._d_model, key=lambda declaration:getattr(declaration,self._d_sort) if getattr(declaration,self._d_sort) else 0,reverse=self._d_asc)



class Search_Class(object):
    search_dic = {}

    @classmethod
    def _d_model(cls,declarations):
        if not isinstance(declarations, list):
            return list(declarations)
        else:
            return declarations

    @classmethod
    def _automatic(cls,declaration,content):
        li = []
        declaration = 'declaration'
        for _, v in cls.search_dic.iteritems():
            li.append('content in unicode(%s.%s)' % (declaration, v))
        print '-'*30
        print 'or'.join(li)
        print '-'*30
        return ' or '.join(li)

    @classmethod
    def search_content(cls, content,declarations,**kwargs):
        # filter(lambda declaration:content in 'declaration.xx',cls.declarations)
        cls.search_dic.update(**kwargs)
        content = unicode(content)
        return filter(lambda declaration: eval(cls._automatic(content,declaration)), cls._d_model(declarations))
        # return cls.automatic(content)

class Choice_Model(object):

    @classmethod
    def choice_model(cls,trade_type):
        model = trade_type_dic.get(trade_type)
        return model

    @classmethod
    def choice_one(cls,trade_type,declaration_uuid):
        model=cls.choice_model(trade_type)
        if not model:
            abort(404)
        else:
            declaration = model.query.filter_by(uuid=declaration_uuid).first()
            if not declaration:
                abort(404)
            else:
                context = dict(declaration=declaration)
                return context

if __name__=='__main__':
    # declarations=Import_Customs_Declaration.query
    # print Search_Class.search_content(u'一般贸易',declarations,search_1='trade_mode.name')
    pass




