/**
 * Created by rhj231223 on 2017/11/25.
 */

'use strict';

$(function () {
    var reset_pwd_btn=$('#reset_pwd_btn');
    reset_pwd_btn.click(function(event){
        event.preventDefault();

        var old_password=$('input[name=old_password]');
        var new_password=$('input[name=new_password]');
        var new_password_repeat=$('input[name=new_password_repeat]');

        rhjajax.post({
            url:'/customs/reset_pwd_post/',
            data:{
                old_password:old_password.val(),
                new_password:new_password.val(),
                new_password_repeat:new_password_repeat.val(),
            },
            success:function(data){
                if(data['code']==200){
                    old_password.val('');
                    new_password.val('');
                    new_password_repeat.val('');
                    xtalert.alertSuccessToast('密码修改成功!')
                }else{
                    xtalert.alertInfo(data['message'])
                }
            }
        })

    })
});
