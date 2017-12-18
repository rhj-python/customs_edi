/**
 * Created by renhuijun on 2017/5/8.
 */

'use strict';

var rhjajax={
    'get':function(args){
        args['method']='get';
        this.ajax(args);
    },
    'post':function(args){
        args['method']='post';
        this.ajax(args)
    },
    'ajax':function(args){
        this._ajaxSetup();
        $.ajax(args)
    },
    '_ajaxSetup':function(){
        $.ajaxSetup({
            'beforeSend':function(xhr,settings){
                if(!/^(GET|HEAD|OPTIONS|TRACK)$/i.test(settings.type) && !this.crossDomain){
                    var csrftoken=$('meta[name=csrf_token]').attr('content');
                    xhr.setRequestHeader('X-CSRFToken',csrftoken)
                }
            }
        })
    }

};

// var rhjjson={
//     'set':function(url,type,params,msg_success,timeout,msg_on,msg_off,msg_key,msg_value){
//
//         rhjajax.ajax({
//             url:url ? type:window.location.href(),
//             type:type ? type:'post',
//             data:params,
//             success:function(data){
//                 msg_on=msg_on?msg_on:false;
//                 msg_off=msg_off?msg_off:false;
//                 if(data['code']==200){
//                     if(msg_success){
//                         xtalert.alertSuccessToast(msg=msg_suceess)
//                     }else{
//                         if(msg_key==msg_value){
//                             msg=msg_on
//                         }else{
//                             msg=msg_off
//                         }
//                         xtalert.alertSuccessToast(msg=msg)
//                     }
//                     var timeout=timeout?timeout:false;
//
//                     if(timeout){
//                         setTimeout(function(){
//                         window.location.reload()
//                         },1200)
//                     }
//
//                 }else{
//                     xtalert.alertInfo(msg='错误')
//                 }
//             }
//         })



//     }
// };