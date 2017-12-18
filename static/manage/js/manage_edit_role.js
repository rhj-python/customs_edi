/**
 * Created by rhj231223 on 2017/11/27.
 */

'use strict';

$(function () {
    var edit_btn=$('.edit_btn');
    edit_btn.click(function(event){
        event.preventDefault();

        var role_id=$(this).attr('data_role_id');
        var permissions=$(':checkbox:checked');
        var permission_li=[];

        permissions.each(function(){
            permission_li.push($(this).val())
        });

        rhjajax.post({
            url:'/customs/edit_role_ajax/',
            data:{
                role_id:role_id,
                permission_li:permission_li,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('职位信息修改成功!')

                }else{
                    xtalert.alertInfo(data['message']);
                }
            }
        })

    })
});
