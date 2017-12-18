/**
 * Created by rhj231223 on 2017/11/25.
 */

'use strict';

//发送邮件的函数
$(function () {
    var send_captcha_btn=$('#send_captcha_btn');

    send_captcha_btn.click(function(event){
        event.preventDefault();

        var email=$('input[name=email]');


        rhjajax.post({
            url:'/customs/send_captcha_email/',
            data:{
                email:email.val(),
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('邮件发送成功,请注意查收!');

                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })


    })
});


//修改邮箱的函数

$(function () {
    var reset_email_btn=$('#reset_email_btn');

    reset_email_btn.click(function(event){
        event.preventDefault();

        var email=$('input[name=email]');
        var captcha=$('input[name=captcha]');

        rhjajax.post({
            url:'/customs/reset_email_post/',
            data:{
                email:email.val(),
                captcha:captcha.val(),
            },
            success:function(data){
                if(data['code']==200){
                    email.val('');
                    captcha.val('');
                    xtalert.alertSuccessToast('邮箱修改成功!');

                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })


    })
});
