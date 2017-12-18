/**
 * Created by rhj231223 on 2017/10/27.
 */

'use strict';

//过滤操作的函数
$(function () {
    var filter=$('select[name=filter]');
    var filter_id='';
    filter.change(function(){
        filter_id=$(this).val();
        window.location='/customs/agreement_list/'+filter_id+'/';
    })
});

$(function(){
    var success_btn=$('.success_btn');
    success_btn.click(function(event){
        event.preventDefault();

        var agreement_id=$(this).attr('data_agreement_id');

        rhjajax.post({
            url:'/customs/approval_success/'+agreement_id+'/',
            data:{
                agreement_id:agreement_id,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('审批成功!');
                    setTimeout(function(){
                        window.location.reload();
                    },1200)
                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        });

    })
});