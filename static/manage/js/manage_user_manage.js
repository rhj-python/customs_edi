/**
 * Created by rhj231223 on 2017/11/29.
 */

'use strict';

$(function () {
    var black_btn=$('.black_btn');
    black_btn.click(function(event) {
        event.preventDefault();

        var user_id = $(this).attr('data_user_id');
        var want_active = $(this).attr('data_want_active');

        rhjajax.post({
            url: '/customs/user_black_ajax/',
            data: {
                user_id: user_id,
                want_active: want_active,
            },
            success: function (data) {
                if(data['code']==200){
                    var msg='';
                    if(want_active=='0'){
                        msg='拉黑操作成功!'
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
            },


        })
    })
});
