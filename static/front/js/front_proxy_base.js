/**
 * Created by rhj231223 on 2017/11/2.
 */

'use strict';

//显示委托协议和关闭委托协议的函数
$(function () {
    var add_agreement_btn=$('#add_agreement_btn');
    var agreement_toggle=$('#agreement_toggle');
    var agreement_cancel_btn=$('#agreement_cancel_btn');

    add_agreement_btn.click(function(event){
        event.preventDefault();

        agreement_toggle.slideDown();

    });

    agreement_cancel_btn.click(function(){
        event.preventDefault();
        agreement_toggle.slideUp();
    })


});

//提交委托协议的函数
$(function(){
    var agreement_submit_btn=$('#agreement_submit_btn');

    agreement_submit_btn.click(function(event){
        event.preventDefault();

        var proxy_id=$(this).attr('data_proxy_id');

        var goods_name=$('input[name=goods_name]');
        var trade_class=$('select[name=trade_class]');
        var hs_code=$('input[name=hs_code]');
        var total_price=$('input[name=total_price]');
        var customs_price=$('input[name=customs_price]');
        var import_or_export_date=$('input[name=import_or_export_date]');
        var bl_code=$('input[name=bl_code]');
        var trade_mode_id=$('select[name=trade_mode_id]');
        var country=$('input[name=country]');
        var other=$('input[name=other]');
        var telephone=$('input[name=telephone]');
        var pay_mode_id=$('select[name=pay_mode_id]');

        var expiry_time=$('select[name=expiry_time_id]').val();
        var contents_many=$('input[name=content]:checked');
        var contents=[];
        contents_many.each(function(){
            contents.push($(this).val());
        });


        rhjajax.post({
            url:'/add_proxy_agreement/',
            data:{
                proxy_id:proxy_id,
                goods_name:goods_name.val(),
                trade_class:trade_class.val(),
                hs_code:hs_code.val(),
                total_price:total_price.val(),
                customs_price:customs_price.val(),
                import_or_export_date:import_or_export_date.val(),
                bl_code:bl_code.val(),
                trade_mode_id:trade_mode_id.val(),
                country:country.val(),
                other:other.val(),
                telephone:telephone.val(),
                pay_mode_id:pay_mode_id.val(),
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('建立协议成功!');
                    setTimeout(function(){
                        var new_src='';
                                new_src=xtparam.setParam('/customs_proxy/','contents',JSON.stringify(contents));
                                new_src=xtparam.setParam(new_src,'expiry_time',expiry_time);
                                window.location=new_src;
                    },1200);
                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })
    })
});

//提交委托书的函数
$(function(){
    var submit_proxy_btn=$('#submit_proxy_btn');
    submit_proxy_btn.click(function(event){
        event.preventDefault();

        var proxy_id=$(this).attr('data_proxy_id');
        var contents=$('input[name=contents]:checked');
        var content_li=[];
        var expiry_time_id=$('select[name=expiry_time_id]').val();

        contents.each(function(){
            content_li.push($(this).val());
        });

        rhjajax.post({
            url:'/add_proxy/',
            data:{
                proxy_id:proxy_id,
                content_li:content_li,
                expiry_time_id:expiry_time_id,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('发送申请成功!');
                    setTimeout(function(){
                        window.location='/'
                    },1200)
                }else{
                    xtalert.alertInfo(data['message']);
                }
            },
        })

    })
});

//取消委托书申请的函数
$(function(){
    var cancel_proxy_btn=$('#cancel_proxy_btn');
    cancel_proxy_btn.click(function(event){
        event.preventDefault();

        var proxy_id=$(this).attr('data_proxy_id');

        xtalert.alertConfirm({
            title:'确认取消',
            text:'取消申请将会删除已建立的委托协议和委托书,您确定要取消申请吗?',
            confirmColor:'#cc0000',
            confirmCallback:function(){
                rhjajax.post({
                    url:'/cancel_proxy/',
                    data:{
                        proxy_id:proxy_id,
                    },
                    success:function(data){
                        if(data['code']==200){
                            setTimeout(function(){
                                xtalert.alertSuccessToast('已取消申请!');
                            },100);
                            setTimeout(function(){
                                window.location.reload();
                            },1200);
                        }else{
                            setTimeout(function(){
                                xtalert.alertInfo(data['message']);
                            },100)
                        }
                    },
                })
            },

        })

    })
});