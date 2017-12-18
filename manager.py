# coding:utf-8
from functools import wraps


from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from exts import app,db
from models import (
customs_models,common_models,
front_models,manage_models,websocket_models,
)



Customs_User=customs_models.Customs_User
Company=common_models.Company
Employee=customs_models.Employee



manager=Manager(app)
migrate=Migrate(app,db)

manager.add_command('db',MigrateCommand)


def encode_option(func):
    @wraps(func)
    def wrapper(**kwargs):
        for k,v in kwargs.iteritems():
            kwargs[k]=v.decode('gbk').encode('utf-8')
        return func(**kwargs)
    return wrapper

@manager.option('-u','--username',dest='username')
@manager.option('-e','--email',dest='email')
@manager.option('-p','--password',dest='password')
def add_customs_user(username,email,password):
    db_customs_user=Customs_User.query.filter_by(email=email).first()
    if not db_customs_user:
        customs_user=Customs_User(username=username,email=email,password=password)
        db.session.add(customs_user)
        db.session.commit()
        print u'customs %s create success!' %username
    else:
        print u'this email has exists'


@manager.option('-n','--company_name',dest='company_name')
@manager.option('-a','--company_address',dest='company_address')
@manager.option('-r','--rcode',dest='rcode')
@manager.option('-o','--ocode',dest='ocode')
@manager.option('-l','--legal_name',dest='legal_name')
@encode_option
def add_company(company_name,company_address,rcode,ocode,legal_name):
    db_company=Company.query.filter_by(customs_registration_code=rcode).first()
    if db_company:
        print u'this company is existed'
    else:
        company=Company(
            company_name=company_name,company_address=company_address,
            customs_registration_code=rcode,organization_code=ocode,
            legal_name=legal_name
        )
        db.session.add(company)
        db.session.commit()
        print 'create company success!'

@manager.option('-u','--username',dest='username')
@manager.option('-e','--email',dest='email')
@manager.option('-p','--password',dest='password')
@encode_option
def add_employee(username,email,password):
    db_employee=Employee.query.filter_by(email=email).first()
    if db_employee:
        print 'db_employee is existed'
    else:
        employee=Employee(username=username,email=email,password=password)
        employee.company_id=1
        db.session.add(employee)
        db.session.commit()
        print u'add employee success'



if __name__=='__main__':
    manager.run()