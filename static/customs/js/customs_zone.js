/**
 * Created by rhj231223 on 2017/10/24.
 */

'use strict';

$(function () {
    var add_btn=$('.add_btn');
    add_btn.click(function(event){
        event.preventDefault();
        xtalert.alertOneInput({
            title:'新增关区',
            text:'请输入新增关区的名称',
            placeholder:'例如:浦江海关',
            confirmText:'新增',
            cancelText:'取消',
            confirmCallback:function(inputValue){
                rhjajax.post({
                    url:'/customs/add_zone/',
                    data:{
                        name:inputValue,
                    },
                    success:function(data){
                        if(data['code']==200){
                            xtalert.alertSuccessToast('新增关区成功!')
                            setTimeout(function(){
                                window.location.reload();
                            },1200)
                        }else{
                            xtlaert.alertInfo(data['message']);
                        }
                    }
                })
            }
        })
    })
});

$(function(){
    var edit_btn=$('.edit_btn');
    edit_btn.click(function(event){
        event.preventDefault();

        var id=$(this).attr('data_id');
        var old_name=$(this).attr('data_name');

        xtalert.alertOneInput({
            title:'编辑关区',
            text:'请输入新的关区名称!',
            placeholder:old_name,
            confirmCallback:function(inputValue){
                rhjajax.post({
                    url:'/customs/edit_zone/',
                    data:{
                        id:id,
                        name:inputValue,
                    },
                    success:function (data) {
                        if(data['code']==200){
                            xtalert.alertSuccessToast('关区修改成功!')
                            setTimeout(function(){
                                window.location.reload();
                            },1200)
                        }else{
                            xtalert.alertInfo(data['message']);
                        }
                    }
                })
            },
        })

    })
});

$(function(){
    var delete_btn=$('.delete_btn');
    delete_btn.click(function(event){
        event.preventDefault();

        var id=$(this).attr('data_id');
        var name=$(this).attr('data_name');

        xtalert.alertConfirm({
            title:'删除关区',
            text:'您确定要删除 '+name+' 吗?',
            confirmColor:'#BB0000',
            confirmText:'删除',
            cancelText:'再考虑一下!',
            confirmCallback:function(){
                rhjajax.post({
                    url:'/customs/delete_zone/',
                    data:{
                        id:id,
                    },
                    success:function(data){
                        if(data['code']==200){
                            setTimeout(function(){
                            xtalert.alertSuccessToast('关区删除成功!')
                        },100);
                        setTimeout(function(){
                            window.location.reload();
                        },1200)
                        }else{
                            setTimeout(function(){
                            xtalert.alertInfo(data['message'])
                        },100);
                        }
                    },

                })
            }
        })
    });


});