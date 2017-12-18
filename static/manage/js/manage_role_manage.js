/**
 * Created by rhj231223 on 2017/11/28.
 */

'use strict';

$(function () {
    var delete_btn=$('.delete_btn');


    delete_btn.click(function(event){
        event.preventDefault();

        var role_id=$(this).attr('data_role_id');
        var role_name=$(this).attr('data_role_name');

        xtalert.alertConfirm({
            title:'确认删除',
            text:'您确定要删除 ' + role_name + ' 职位吗?',
            confirmColor:'#ff0000',
            confirmCallback:function(){
                rhjajax.post({
                    url:'/customs/delete_role_ajax/',
                    data:{
                        role_id:role_id,
                        role_name:role_name,
                    },
                    success:function(data){
                        if(data['code']==200){
                            setTimeout(function(){
                                xtalert.alertSuccessToast('职位删除成功!');
                            },100);
                            setTimeout(function(){
                                window.location.reload();
                            },1200);

                        }else{
                            setTimeout(function(){
                                xtalert.alertInfo(data['message']);
                            },100)
                        }
                    }
                })
            }

        })


    });
});
