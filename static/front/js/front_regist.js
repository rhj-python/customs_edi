/**
 * Created by rhj231223 on 2017/10/30.
 */

'use strict';

//发送短信验证码的函数
$(function () {
    var send_btn=$('#send_btn');

    send_btn.click(function(event){
        event.preventDefault();

        var phone=$('input[name=phone]').val();

        rhjajax.post({
            url:'/front_account/sms_captcha/',
            data:{
                phone:phone
            },
            success:function(data){
                if(data['code']==100){
                    setTimeout(function(){
                        xtalert.alertSuccessToast('短信发送成功!');
                    },100);
                    var count=600;
                    send_btn.attr('disabled','disabled');

                    var timer=setInterval(function(){
                        send_btn.text(count);
                        count--;

                        if(count<=0){
                            send_btn.removeAttr('disabled');
                            send_btn.text('发送短信');
                            clearInterval(timer)
                        }

                    },1000)

                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })

    });
});

//注册ajax提交的函数

$(function(){
    var regist_btn=$('#regist_btn');

    var graph_btn=$('#graph_btn');

    regist_btn.click(function(event){
        event.preventDefault();

        var phone=$('input[name=phone]').val();
        var sms_captcha=$('input[name=sms_captcha]').val();
        var username=$('input[name=username]').val();
        var password=$('input[name=password]').val();
        var password_repeat=$('input[name=password_repeat]').val();
        var company_name=$('input[name=company_name]').val();
        var company_address=$('input[name=company_address]').val();
        var customs_registration_code=$('input[name=customs_registration_code]').val();
        var organization_code=$('input[name=organization_code]').val();
        var legal_name=$('input[name=legal_name]').val();
        var graph_captcha=$('input[name=graph_captcha]');


        rhjajax.post({
            url:'/front_account/regist/',
            data:{
                phone:phone,
                sms_captcha:sms_captcha,
                username:username,
                password:password,
                password_repeat:password_repeat,
                company_name:company_name,
                company_address:company_address,
                customs_registration_code:customs_registration_code,
                organization_code:organization_code,
                legal_name:legal_name,
                graph_captcha:graph_captcha.val(),
            },
            success:function(data){
                if(data['code']==100){
                    setTimeout(function(){
                        xtalert.alertSuccessToast('用户注册成功!');
                    },100);
                    setTimeout(function(){
                        window.location='/';
                    },1200)
                }else{
                    graph_captcha.val('');
                    xtalert.alertInfo(data['message']);
                    graph_btn.click();
                }
            }
        })




    })

});
