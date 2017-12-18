/**
 * Created by rhj231223 on 2017/11/5.
 */

'use strict';

//选择操作的函数
$(function () {
    var submit_btn=$('.submit_btn');
    submit_btn.click(function(event){
        event.preventDefault();

        var agreement_type_id=$(this).attr('data_agreement_type_id');
        var agreement_id=$(this).attr('data_agreement_id');
        var operate_id=$(this).attr('data_operate_id');
        var status_id=$(this).attr('data_agreement_status_id');

        rhjajax.post({
            url:'/operate_proxy_agreement/',
            data:{
                agreement_type_id:agreement_type_id,
                agreement_id:agreement_id,
                operate_id:operate_id,
                status_id:status_id,
            },
            success:function(data){
                if(data['code']==200){
                    var msg='';
                    if(operate_id=='2'){
                        msg='建立委托协议成功!'
                    }else if(operate_id=='3'){
                        msg='该委托协议已拒绝!'
                    }
                    xtalert.alertSuccessToast(msg);
                    setTimeout(function(){
                        window.location='/proxy_agreement_list/';
                    },1200)

                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })

    });
});
