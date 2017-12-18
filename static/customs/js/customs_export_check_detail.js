/**
 * Created by rhj231223 on 2017/11/20.
 */

'use strict';


//征税的函数
$(function(){
    var collect_tax_btn=$('#collect_tax_btn');
    collect_tax_btn.click(function(event){
        event.preventDefault();

        var declaration_uuid=$(this).attr('data_declaration_uuid');
        var declaration_model=$(this).attr('data_declaration_model');

        rhjajax.post({
            url:'/customs/export_collect_tax/',
            data:{
                declaration_uuid:declaration_uuid,
                declaration_model:declaration_model,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('征税操作成功!');
                    setTimeout(function(){
                        window.location='/customs/customs_export_check/1/0/5/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })

    })
});

//查验的函数
$(function(){
    var check_btn=$('#check_btn');
    check_btn.click(function(event){
        event.preventDefault();

        var declaration_uuid=$(this).attr('data_declaration_uuid');
        var declaration_model=$(this).attr('data_declaration_model');

        rhjajax.post({
            url:'/customs/export_check_commodity/',
            data:{
                declaration_uuid:declaration_uuid,
                declaration_model:declaration_model,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('查验操作成功!')
                    setTimeout(function(){
                        window.location='/customs/customs_export_check/1/0/5/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })
    })
});

//退单下拉函数
$(function(){
    var cancel_btn=$('#cancel_btn');
    var refund_div=$('#refund_div');
    cancel_btn.click(function(event){
        event.preventDefault();

        refund_div.slideToggle();

    })
});

//退单操作的函数
$(function(){
    var refund_btn=$('#refund_btn');
    refund_btn.click(function(event){
        event.preventDefault();

        var declaration_uuid=$(this).attr('data_declaration_uuid');
        var declaration_model=$(this).attr('data_declaration_model');
        var refund_reason=$('textarea[name=refund_reason]');

        rhjajax.post({
            url:'/customs/export_refund/',
            data:{
                declaration_uuid:declaration_uuid,
                declaration_model:declaration_model,
                refund_reason:refund_reason.val(),
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('退单操作成功!');
                    setTimeout(function(){
                        window.location='/customs/customs_export_check/1/0/5/1/'
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        });

    });

});

//查验通过的函数
$(function(){
    var success_btn=$('#success_btn');
        success_btn.click(function(event){
        event.preventDefault();

        var declaration_model=$(this).attr('data_declaration_model');
        var declaration_uuid=$(this).attr('data_declaration_uuid');

        rhjajax.post({
            url:'/customs/export_check_success/',
            data:{
                declaration_model:declaration_model,
                declaration_uuid:declaration_uuid,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('该批货物已查验通过!')
                    setTimeout(function(){
                        window.location='/customs/customs_export_check/1/0/5/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })
    })
});