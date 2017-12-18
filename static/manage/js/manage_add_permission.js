/**
 * Created by rhj231223 on 2017/11/28.
 */

'use strict';

$(function () {
    var add_btn=$('.add_btn');

    add_btn.click(function(event){
        event.preventDefault();

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
            url:'/customs/add_permission_ajax/',
            data:{
                name:name.val(),
                desc:desc.val(),
                p_code:p_code.val(),
                handler_li:handler_li,
                menu_li:menu_li,
            },
            success:function(data){
                if(data['code']==200){
                    name.val('');
                    desc.val('');
                    p_code.val('');
                    handlers.each(function(){
                        $(this).prop('checked',false)
                    });

                    menus.each(function(){
                        $(this).prop('checked',false)
                    });

                    xtalert.alertSuccessToast('新增权限成功!');
                }
            }

        })

    })

});
