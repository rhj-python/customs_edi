/**
 * Created by rhj231223 on 2017/11/27.
 */

'use strict';

$(function () {
    var add_btn=$('.add_btn');
    add_btn.click(function(event){
        event.preventDefault();

        var name=$('input[name=name]');
        var desc=$('input[name=desc]');
        var permissions=$(':checkbox:checked');
        var permission_li=[];

        permissions.each(function(){
            permission_li.push($(this).val())
        });

        rhjajax.post({
            url:'/customs/add_role_ajax/',
            data:{
                name:name.val(),
                desc:desc.val(),
                permission_li:permission_li,
            },
            success:function(data){
                if(data['code']==200){
                    name.val('');
                    desc.val('');
                    permissions.each(function(){
                        $(this).prop('checked',false);
                    });
                    xtalert.alertSuccessToast('职位新增成功!')

                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })

    })
});
