/**
 * Created by rhj231223 on 2017/11/7.
 */

'use strict';

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

        // var expiry_time=$('select[name=expiry_time_id]').val();
        // var contents_many=$('input[name=content]:checked');
        // var contents=[];
        // contents_many.each(function(){
        //     contents.push($(this).val());
        // });


        rhjajax.post({
            url:window.location.href,
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
                    xtalert.alertSuccessToast('发送委托协议申请成功!');
                    setTimeout(function(){
                        window.location='/customs/proxy_detail/'+proxy_id+'/1/';
                    },1200);
                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })
    })
});