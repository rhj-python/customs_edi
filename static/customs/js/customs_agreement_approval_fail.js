/**
 * Created by rhj231223 on 2017/10/28.
 */

'use strict';

$(function () {
    var fail_btn=$('#fail_btn');
    fail_btn.click(function(event){
        event.preventDefault();

        var agreement_id=$(this).attr('data_agreement_id');
        var reply_id=$('select[name=reply]').val();

        rhjajax.post({
            url:'/customs/approval_fail/'+agreement_id+'/',
            data:{
                agreement_id:agreement_id,
                reply_id:reply_id,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('审批未通过操作完成!');
                    setTimeout(function(){
                        window.location='/customs/agreement_list/2/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            },
        })

    })
});
