/**
 * Created by rhj231223 on 2017/10/29.
 */

'use strict';

$(function () {
    var url=window.location.href;
    if(url.indexOf('triple_agreement')>=0){
        var triple_agreement=$('.triple_agreement');
        triple_agreement.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('entrust_approval')>=0){
        var entrust_approval=$('.entrust_approval');
        entrust_approval.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('declaration_status_query')>=0){
        var declaration_status_query=$('.declaration_status_query');
        declaration_status_query.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('msg')>=0){
        var msg=$('.msg');
        msg.addClass('active').siblings().removeClass('active');
    }

});
