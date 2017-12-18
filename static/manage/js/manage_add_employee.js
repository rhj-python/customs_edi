/**
 * Created by rhj231223 on 2017/11/27.
 */

'use strict';

$(function () {
    var add_btn=$('.add_btn');

    add_btn.click(function(event){
        event.preventDefault();

        var username=$('input[name=username]');
        var email=$('input[name=email]');
        var password=$('input[name=password]');
        var password_repeat=$('input[name=password_repeat]');
        var roles=$(':checkbox:checked');
        var role_li=[];
        roles.each(function(){
            role_li.push($(this).val());
        });


        rhjajax.post({
            url: '/customs/add_employee_ajax/',
            data: {
                username: username.val(),
                email: email.val(),
                password: password.val(),
                password_repeat: password_repeat.val(),
                role_li:role_li,
            },
            success:function(data){
                if(data['code']==200){
                    username.val('');
                    email.val('');
                    password.val('');
                    password_repeat.val('');
                    roles.each(function(){
                        $(this).prop('checked',false);
                    });

                    xtalert.alertSuccessToast('员工新增成功!');

                }else{
                    xtalert.alertInfo(data['message']);
                }
            }

        });

    })

});
