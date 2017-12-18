# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import InputRequired

from models.common_models import Import_Customs_Declaration,Export_Customs_Declaration

class BaseForm(FlaskForm):
    def get_error(self):
        _,v=self.errors.popitem()
        message=v[0]
        return message

    def get_errors(self):
        li=[v for _,v in self.errors.iteritems()]
        message='<br>'.join(li)
        return message


class DeclarationBaseForm(BaseForm):
    declaration_uuid=StringField(validators=[InputRequired(message=u'必须指定报关单uuid!')])
    declaration_model=StringField(validators=[InputRequired(message=u'必须指定贸易类型!')])

    declaration=''

    def validate(self):

        if not super(DeclarationBaseForm, self).validate():
            return False
        else:
            declaration_uuid=self.declaration_uuid.data
            declaration_model=self.declaration_model.data

            model=eval(declaration_model)
            if not model:
                self.declaration_model.errors.append(u'没有找到该类型!')

            declaration=model.query.filter_by(uuid=declaration_uuid).first()
            if not declaration:
                self.declaration_uuid.errors.append(u'没有找到啊该报关单')
                return False
            else:
                self.declaration=declaration
                return True