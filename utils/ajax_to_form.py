# coding:utf-8
import xtjson


from flask import request,abort


def ajax_form_choice(form_class,*args,**kwargs):
    form = form_class(*args,**kwargs)
    if form.validate():
        return xtjson.json_result()
    else:
        return xtjson.json_params_error(message=form.get_error())

def ajax_form(form_class,*args,**kwargs):
    return ajax_form_choice(form_class,*args,**kwargs) if request.is_xhr else abort(404)