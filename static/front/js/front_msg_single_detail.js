/**
 * Created by rhj231223 on 2017/12/3.
 */

'use strict';

//初始化wangEditor
$(function () {
    var E=window.wangEditor;
    var editor=new E('#editor1','#editor2');
    editor.create();
    window.editor=editor;
});

//websocket
$(function(){
    var socket=io.connect('http://'+document.domain+':'+location.port);
    socket.on('connect',function(){
        var user_info=$('#user_info');
        var model=user_info.attr('data_model');

        var id=user_info.attr('data_id');
        var self_room=model+'__'+id;
        window.sender=self_room;

        var data={'self_room':self_room};

        socket.emit('join_connect',data);

    });

    var send_btn=$('#send_btn');
    send_btn.click(function(event){
        event.preventDefault();
        var receiver_info=$('#receiver_info');
        var model=receiver_info.attr('data_model');
        var id=receiver_info.attr('data_id');
        var receiver=model+'__'+id;
        var sender=window.sender;
        var content=editor.txt.html();
        var sender_name=$('#sender_name').text();
        var data={'receiver':receiver,'sender':sender,'content':content,'sender_name':sender_name};

        console.log(receiver);
        console.log(sender_name);

        socket.emit('my_event',data);
        editor.txt.clear();
    });

    socket.on('my_event',function(data){
        var sender=data['sender'];

        var user_info=$('#user_info');
        var model=user_info.attr('data_model');

        var id=user_info.attr('data_id');
        var self=model+'__'+id;

        var html='';

        console.log(sender);
        console.log(self);

        if(sender!=self){
            html=data['html_left'];
        }else{
            html=data['html_right'];
        }
        var show_content=$('.content');
        show_content.append(html);
        alwaysBottom();
    })



});

$(function(){
    alwaysBottom();
});

//聊天功能,总是显示底部
function alwaysBottom(){
    var cn=$('.content');
    var top=cn.prop('scrollHeight');
    cn.scrollTop(top);
}