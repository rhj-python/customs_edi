/**
 * Created by rhj231223 on 2017/12/6.
 */

'use strict';

//推送广播消息
$(function(){
    var socket=io.connect('http://'+document.domain+':'+location.port);
    socket.on('connect',function(){
        var user_info=$('#user_info');
        var model=user_info.attr('data_model');
        var id=user_info.attr('data_id');
        var sender=model+'__'+id;
        window.sender=sender;
        var data={'sender':sender};
        socket.emit('conn',data)

    });

    socket.on('my_broadcast',function(data){
        var html=data['html_left'];
        var r_message=$('.r_message');
        r_message.prepend(html);
        r_message.scrollTop(0);
        mp_broadcast.click();
    });

    socket.on('disconnect',function(){
        var data={'sender':sender};
        socket.emit('conn',data)
    });

    // socket.on('my_event',function(data){
    //     var bs=$('#bs');
    //     if(bs.text()==''){
    //         bs.text(1);
    //     }else{
    //         var count=parseInt(bs.text());
    //         bs.text(count+1);
    //     }
    // })




});

//显示广播
$(function(){
    var mp_broadcast=$('#mp_broadcast');
    window.mp_broadcast=mp_broadcast;
    mp_broadcast.click(function(){
        var mp_grape=$('.mp_grape');
        window.mp_grape=mp_grape;
         mp_grape.slideDown();
         mp_broadcast.hide();
    })
});

//隐藏广播窗口显示小按钮
$(function(){
    var gly_minus=$('#gly_minus');
    gly_minus.click(function(){
        mp_grape.hide();
        mp_broadcast.slideDown();

    })

});



//永远显示最顶部
function alwaysTop(){
    var r_message=$('.r_message');
    r_message.scrollTop(0);
}