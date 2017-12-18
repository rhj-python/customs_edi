/**
 * Created by rhj231223 on 2017/11/27.
 */

'use strict';

$(function () {
    var edit_btn=$('.edit_btn');

    edit_btn.click(function(event){
        event.preventDefault();

        var employee_id=$(this).attr('data_employee_id');
        var roles=$(':checkbox:checked');
        var role_li=[];
        roles.each(function(){
            role_li.push($(this).val());
        });


        rhjajax.post({
            url: '/customs/edit_employee_ajax/',
            data: {
                employee_id:employee_id,
                role_li:role_li,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('员工信息修改成功!');

                }else{
                    xtalert.alertInfo(data['message']);
                }
            }

        });

    })

});

$(function(){
    var black_btn=$('.black_btn');

    black_btn.click(function(event){
        event.preventDefault();

        var employee_id=$(this).attr('data_employee_id');
        var want_active=$(this).attr('data_want_active');

        rhjajax.post({
            url:'/customs/black_employee_ajax/',
            data:{
                employee_id:employee_id,
                want_active:want_active,
            },
            success:function(data){
                if(data['code']==200){
                    var msg='';
                    if(want_active=='0'){
                        msg='拉黑操作成成!'
                    }else{
                        msg='取消拉黑成功!'
                    }
                    xtalert.alertSuccessToast(msg);
                    setTimeout(function(){
                        window.location.reload();
                    },1200)

                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })

    })
});
