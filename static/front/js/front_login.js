/**
 * Created by rhj231223 on 2017/10/31.
 */

'use strict';

$(function () {
    var login_btn=$('#login_btn');
    var graph_btn=$('#graph_btn');

    login_btn.click(function(event){
        event.preventDefault();

        var phone=$('input[name=phone]').val();
        var password=$('input[name=password]').val();
        var graph_captcha=$('input[name=graph_captcha]');
        var remember=$('input[name=remember]').val();

        rhjajax.post({
            url:window.location.href,
            data:{
              phone:phone,
              password:password,
              graph_captcha:graph_captcha.val(),
              remember:remember,
            },
            success:function(data){
                if(data['code']==200){
                    setTimeout(function(){
                        xtalert.alertSuccessToast('用户登录成功!');
                    },100);
                    setTimeout(function(){
                        window.location=data['data']
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
