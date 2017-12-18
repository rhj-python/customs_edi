/**
 * Created by rhj231223 on 2017/11/24.
 */

'use strict';

$(function () {
    var pay_tax_btn=$('#pay_tax_btn');

    pay_tax_btn.click(function(event){
        event.preventDefault();


        var declaration_model=$(this).attr('data_declaration_model');
        var declaration_uuid=$(this).attr('data_declaration_uuid');

        rhjajax.post({
            url:'/pay_tax_now/',
            data:{
                declaration_model:declaration_model,
                declaration_uuid:declaration_uuid,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('支付成功');
                    setTimeout(function(){
                        window.location.reload();
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })
    });
});
