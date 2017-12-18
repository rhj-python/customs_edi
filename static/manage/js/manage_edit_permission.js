/**
 * Created by rhj231223 on 2017/11/28.
 */

'use strict';

$(function () {
    var edit_btn=$('.edit_btn');

    edit_btn.click(function(event){
        event.preventDefault();

        var permission_id=$(this).attr('data_permission_id');

        var name=$('input[name=name]');
        var desc=$('input[name=desc]');
        var p_code=$('input[name=p_code]');
        var handlers=$('input[name=handlers]:checked');
        var menus=$('input[name=menus]:checked');

        var handler_li=[];
        var menu_li=[];

        handlers.each(function(){
            handler_li.push($(this).val());
        });

        menus.each(function(){
            menu_li.push($(this).val());
        });

        rhjajax.post({
            url:'/customs/edit_permission_ajax/',
            data:{
                permission_id:permission_id,
                name:name.val(),
                desc:desc.val(),
                p_code:p_code.val(),
                handler_li:handler_li,
                menu_li:menu_li,
            },
            success:function(data){
                if(data['code']==200){
                    handlers.each(function(){
                        $(this).prop('checked',false)
                    });

                    menus.each(function(){
                        $(this).prop('checked',false)
                    });

                    xtalert.alertSuccessToast('修改权限成功!');
                }else{
                    xtalert.alertInfo(data['message']);
                }
            }

        })

    })

});
