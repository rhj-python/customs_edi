# coding:utf-8
from uuid import uuid4
from datetime import datetime

from exts import db
from base_models import BaseModel

class Customs_Declaration_Base(BaseModel):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    uuid=db.Column(db.String(100),unique=True,default=lambda:str(uuid4()))
    create_time=db.Column(db.DateTime,default=datetime.now)
    pre_entry_code=db.Column(db.String(100))
    declaration_code=db.Column(db.BigInteger,unique=True)
    bl_code=db.Column(db.String(100))
    case_code=db.Column(db.String(100))
    contract_code=db.Column(db.String(100))
    customs_date=db.Column(db.Date)
    business_company=db.Column(db.String(100))
    customs_company=db.Column(db.String(100))
    consignee=db.Column(db.String(100))
    vessel_name=db.Column(db.String(100))
    vessel_code=db.Column(db.String(100))
    trade_type=db.Column(db.String(100))
    license_code=db.Column(db.String(100))
    approval_code=db.Column(db.String(100))
    freight=db.Column(db.String(100))
    insurance_premiums=db.Column(db.String(100))
    sundry_charges=db.Column(db.String(100))
    packages_num=db.Column(db.Integer,default=1)
    packing_type=db.Column(db.String(100))
    gross_weight=db.Column(db.DECIMAL(10,2))
    net_weight=db.Column(db.DECIMAL(10,2))
    container_code=db.Column(db.String(100))
    marks=db.Column(db.String(200))
    tax_price = db.Column(db.DECIMAL(10, 2))
    refund_reason=db.Column(db.String(200))
    check_date=db.Column(db.Date)

class Import_Customs_Declaration(Customs_Declaration_Base,db.Model):
    __tablename__='import_customs_declaration'

    import_port=db.Column(db.String(100))
    import_date=db.Column(db.Date)
    tax_rate=db.Column(db.String(100))
    departure_country=db.Column(db.String(100))
    loading_port=db.Column(db.String(100))
    domestic_destination=db.Column(db.String(100))


    agreement_id=db.Column(db.Integer,db.ForeignKey('import_proxy_agreement.id'),unique=True)
    operator_id=db.Column(db.Integer,db.ForeignKey('employee.id'))
    status_id=db.Column(db.Integer,db.ForeignKey('declaration_status.id'))
    transport_mode_id=db.Column(db.Integer,db.ForeignKey('transport_mode.id'))
    trade_mode_id=db.Column(db.Integer,db.ForeignKey('trade_mode.id'))
    transaction_mode_id=db.Column(db.Integer,db.ForeignKey('transaction_mode.id'))
    tax_mode_id=db.Column(db.Integer,db.ForeignKey('tax_mode.id'))
    use_id=db.Column(db.Integer,db.ForeignKey('use.id'))

    customs_company_id = db.Column(db.Integer,db.ForeignKey('company.id'))
    business_company_id = db.Column(db.Integer,db.ForeignKey('company.id'))


    agreement=db.relationship('Import_Proxy_Agreement',uselist=False)
    operator=db.relationship('Employee',backref='import_declarations')
    status=db.relationship('Declaration_Status',backref='import_declarations')
    transport_mode=db.relationship('Transport_Mode',backref='import_declarations')
    trade_mode = db.relationship('Trade_Mode', backref='import_declarations')
    transaction_mode=db.relationship('Transaction_Mode',backref='import_declarations')
    tax_mode=db.relationship('Tax_Mode',backref='import_declarations')
    use=db.relationship('Use',backref='import_declarations')

    customs_company = db.relationship('Company',foreign_keys=[customs_company_id],backref=db.backref('customs_import_declarations',lazy='dynamic'))
    business_company = db.relationship('Company',foreign_keys=[business_company_id],backref=db.backref('business_import_declarations',lazy='dynamic'))

class Export_Customs_Declaration(Customs_Declaration_Base,db.Model):
    __tablename__='export_customs_declaration'

    export_port = db.Column(db.String(100))
    export_date = db.Column(db.Date)
    destination_country=db.Column(db.String(100))
    destination_port=db.Column(db.String(100))
    goods_origin_place=db.Column(db.String(100))
    manufacturer=db.Column(db.String(100))

    settlement_mode_id=db.Column(db.Integer,db.ForeignKey('settlement_mode.id'))
    agreement_id=db.Column(db.Integer,db.ForeignKey('export_proxy_agreement.id'))
    operator_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('declaration_status.id'))
    transport_mode_id = db.Column(db.Integer, db.ForeignKey('transport_mode.id'))
    trade_mode_id = db.Column(db.Integer, db.ForeignKey('trade_mode.id'))
    transaction_mode_id = db.Column(db.Integer, db.ForeignKey('transaction_mode.id'))
    tax_mode_id = db.Column(db.Integer, db.ForeignKey('tax_mode.id'))

    customs_company_id = db.Column(db.Integer,db.ForeignKey('company.id'))
    business_company_id = db.Column(db.Integer,db.ForeignKey('company.id'))


    settlement_mode=db.relationship('Settlement_Mode',backref='export_declarations')
    agreement = db.relationship('Export_Proxy_Agreement', uselist=False)
    operator = db.relationship('Employee', backref='export_declarations')
    status = db.relationship('Declaration_Status', backref='export_declarations')
    transport_mode = db.relationship('Transport_Mode', backref='export_declarations')
    trade_mode = db.relationship('Trade_Mode', backref='export_declarations')
    transaction_mode = db.relationship('Transaction_Mode', backref='export_declarations')
    tax_mode = db.relationship('Tax_Mode', backref='export_declarations')

    customs_company = db.relationship('Company',foreign_keys=[customs_company_id],backref=db.backref('customs_export_declarations',lazy='dynamic'))
    business_company = db.relationship('Company',foreign_keys=[business_company_id],backref=db.backref('business_export_declarations',lazy='dynamic'))


class Settlement_Mode(db.Model,BaseModel):
    __tablename__='settlement_mode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100), nullable=False)


class Commodity(db.Model,BaseModel):
    __tablename__='commodity'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    item_code=db.Column(db.String(100))
    create_time=db.Column(db.DateTime,default=datetime.now)
    hs_code=db.Column(db.String(10))
    commodity_name=db.Column(db.String(200))
    commodity_type=db.Column(db.String(200))
    quantity_and_unit=db.Column(db.String(100))
    country=db.Column(db.String(100))
    unit_price=db.Column(db.DECIMAL(10,4))
    total_price=db.Column(db.DECIMAL(10,2))

    currency_id=db.Column(db.Integer,db.ForeignKey('currency.id'))
    tax_free_mode_id=db.Column(db.Integer,db.ForeignKey('tax_free_mode.id'))
    import_declaration_id=db.Column(db.Integer,db.ForeignKey('import_customs_declaration.id'))
    export_declaration_id=db.Column(db.Integer,db.ForeignKey('export_customs_declaration.id'))

    currency=db.relationship('Currency',backref='commoditys')
    tax_free_mode=db.relationship('Tax_Free_Mode',backref='commoditys')
    import_declaration=db.relationship('Import_Customs_Declaration',backref='commoditys')
    export_declaration=db.relationship('Export_Customs_Declaration',backref='commoditys')


class Transaction_Mode(db.Model,BaseModel):
    __tablename__='transaction_mode'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    code=db.Column(db.Integer,unique=True)
    name=db.Column(db.String(100),nullable=False)

class Tax_Mode(db.Model,BaseModel):
    __tablename__='tax_mode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100), nullable=False)
    desc =db.Column(db.String(200))


class Currency(db.Model,BaseModel):
    __tablename__='currency'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    code=db.Column(db.Integer,unique=True)
    name=db.Column(db.String(100),nullable=False)
    e_name=db.Column(db.String(100),nullable=False)
    exchange_rate=db.Column(db.DECIMAL(10,4))

class Tax_Free_Mode(db.Model, BaseModel):
    __tablename__ = 'tax_free_mode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100), nullable=False)

class Use(db.Model, BaseModel):
    __tablename__ = 'use'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100), nullable=False)

class Document_Type(db.Model,BaseModel):
    __tablename__='document_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

class Document(db.Model,BaseModel):
    __tablename__='document'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    url=db.Column(db.String(200))
    create_time=db.Column(db.DateTime,default=datetime.now)

    document_type_id=db.Column(db.Integer,db.ForeignKey('document_type.id'))
    upload_user_id=db.Column(db.Integer,db.ForeignKey('employee.id'))
    import_customs_declaration_id=db.Column(db.Integer,db.ForeignKey('import_customs_declaration.id'))
    export_customs_declaration_id=db.Column(db.Integer,db.ForeignKey('export_customs_declaration.id'))

    document_type=db.relationship('Document_Type',backref='documents')
    upload_user=db.relationship('Employee',backref='documents')
    import_declaration=db.relationship('Import_Customs_Declaration',backref='documents')
    export_declaration=db.relationship('Export_Customs_Declaration',backref='documents')

class Declaration_Status(db.Model,BaseModel):
    __tablename__='declaration_status'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)


class Transport_Mode(db.Model,BaseModel):
    __tablename__='transport_mode'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    sign_id=db.Column(db.String(20),unique=True,nullable=False)
    name=db.Column(db.String(100),nullable=False)


class Company(db.Model,BaseModel):

    __tablename__='company'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    uuid=db.Column(db.String(100),default=lambda:str(uuid4()),nullable=False)
    company_name=db.Column(db.String(100),nullable=False)
    company_address=db.Column(db.String(200))
    customs_registration_code=db.Column(db.String(10),nullable=False,unique=True)
    organization_code=db.Column(db.String(9),nullable=False,unique=True)
    legal_name=db.Column(db.String(100),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)

class Proxy(db.Model,BaseModel):

    __tablename__='proxy'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    create_time=db.Column(db.DateTime,default=datetime.now)
    expiry_time=db.Column(db.DateTime)
    is_active=db.Column(db.Boolean,default=True)

    broker_id=db.Column(db.Integer,db.ForeignKey('company.id'))
    client_id=db.Column(db.Integer,db.ForeignKey('company.id'))

    broker=db.relationship('Company',foreign_keys=[broker_id],backref='broker_proxys')
    client=db.relationship('Company',foreign_keys=[client_id],backref='client_proxys')


class Business_Content(db.Model,BaseModel):
    __tablename__='business_content'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),unique=True,nullable=False)

    proxys=db.relationship('Proxy',secondary='proxy_to_business_content',backref='contents')

class Proxy_To_Business_Content(db.Model,BaseModel):
    __tablename__='proxy_to_business_content'

    proxy_id=db.Column(db.Integer,db.ForeignKey('proxy.id'),primary_key=True)
    business_content_id=db.Column(db.Integer,db.ForeignKey('business_content.id'),primary_key=True)


class Proxy_Agreement_Base(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid=db.Column(db.String(100),unique=True,default=lambda:str(uuid4()))
    goods_name = db.Column(db.String(60), nullable=False)
    hs_code = db.Column(db.String(10), nullable=False)
    total_price = db.Column(db.DECIMAL(10, 2), nullable=False)
    customs_price = db.Column(db.DECIMAL(10, 2))
    import_or_export_date = db.Column(db.Date, nullable=False)
    bl_code = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(100))
    other=db.Column(db.Text)

class Agreement_Status(db.Model,BaseModel):

    __tablename__='agreement_status'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False,unique=True)

class Import_Proxy_Agreement(db.Model,Proxy_Agreement_Base):
    __tablename__='import_proxy_agreement'

    origin_country = db.Column(db.String(100))

    proxy_id=db.Column(db.Integer,db.ForeignKey('proxy.id'))
    pay_mode_id=db.Column(db.Integer,db.ForeignKey('trade_mode.id'))
    trade_mode_id=db.Column(db.Integer,db.ForeignKey('pay_mode.id'))
    status_id=db.Column(db.Integer,db.ForeignKey('agreement_status.id'))


    proxy=db.relationship('Proxy',backref=db.backref('import_agreements',lazy='dynamic'))
    trade_mode=db.relationship('Trade_Mode',backref='import_agreements')
    pay_mode=db.relationship('Pay_Mode',backref='import_agreements')
    status=db.relationship('Agreement_Status',backref='import_agreements')
    declaration=db.relationship('Import_Customs_Declaration',uselist=False)


class Export_Proxy_Agreement(db.Model,Proxy_Agreement_Base):

    __tablename__ = 'export_proxy_agreement'

    destination_country=db.Column(db.String(100))

    proxy_id = db.Column(db.Integer, db.ForeignKey('proxy.id'))
    pay_mode_id = db.Column(db.Integer, db.ForeignKey('trade_mode.id'))
    trade_mode_id = db.Column(db.Integer, db.ForeignKey('pay_mode.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('agreement_status.id'))

    proxy = db.relationship('Proxy', backref=db.backref('export_agreements',lazy='dynamic'))
    trade_mode = db.relationship('Trade_Mode', backref='export_agreements')
    pay_mode = db.relationship('Pay_Mode', backref='export_agreements')
    status=db.relationship('Agreement_Status',backref='export_agreements')
    declaration = db.relationship('Export_Customs_Declaration', uselist=False)

class Trade_Mode(db.Model,BaseModel):

    __tablename__='trade_mode'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    code=db.Column(db.String(10),unique=True,nullable=False)
    name=db.Column(db.String(100),nullable=False)

class Pay_Mode(db.Model,BaseModel):

    __tablename__='pay_mode'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)


class Tax_Rate(db.Model,BaseModel):
    __tablename__='tax_rate'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    hs_code=db.Column(db.String(100),nullable=False)
    name=db.Column(db.String(100),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    import_tax_rate=db.Column(db.String(100),nullable=False)
    export_tax_rate=db.Column(db.String(100),nullable=False)

