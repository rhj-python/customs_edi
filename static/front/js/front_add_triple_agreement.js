/**
 * Created by rhj231223 on 2017/10/26.
 */

'use strict';

$(function () {
    var submit_btn=$('#submit_btn');


    submit_btn.click(function(event){
        event.preventDefault();

        var company_uuid=$(this).attr('data_company_uuid');
        var checked_zones=$('input[name=zones]:checked');
        var agree=$('input[name=agree]').val();
        var zone_li=[];
        checked_zones.each(function(){
            zone_li.push($(this).val())
        });

        rhjajax.post({
            url:window.location.href,
            data:{
                company_uuid:company_uuid,
                zone_li:zone_li,
                agree:agree,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('签约申请已提交至海关!')
                    setTimeout(function(){
                        window.location='/triple_agreement/'
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            },
        })



    })


});
