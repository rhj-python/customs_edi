/**
 * Created by rhj231223 on 2017/12/6.
 */

'use strict';

$(function () {
    var main_m=$('.main_m');


});


// $(function(){
//     var socket=io.connect('http://'+document.domain+':'+location.port);
//     socket.on('connect',function(){
//         var user_info=$('#user_info');
//         var model=user_info.attr('data_model');
//         var id=user_info.attr('data_id');
//         var sender=model+'__'+id;
//         var data={'sender':sender};
//         socket.emit('join_connect',data)
//
//     });
//
//
//     socket.on('my_event',function(data){
//         console.log(1);
//        var sender=data['sender'];
//        var model_id=$('span[data_model_id=sender]')
//         if(model_id.text()==''){
//            model_id.text(1);
//         }else{
//             count=parseInt(model_id.text());
//             model_id.text(count+1);
//         }
//     })
// });
