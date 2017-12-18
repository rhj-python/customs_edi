/**
 * Created by rhj231223 on 2017/11/23.
 */

'use strict';

$(function () {

    var trade=$('select[name=trade_filter_id]');
    var status=$('select[name=status_filter_id]');
    var sort=$('select[name=sort_id]');
    var asc=$('button[name=asc_id]');

    var asc_value=asc.attr('data_code');
    // 贸易种类切换的函数
    trade.change(function(){
        var trade_id=$(this).val();
        window.location='/declaration_status_query/'+'1/'+trade_id+'/'+status.val()+'/'+sort.val()+'/'+asc_value+'/';
    });

    // 报关状态过滤的函数
    status.change(function(){
        var status_id=$(this).val();
        window.location='/declaration_status_query/'+'1/'+trade.val()+'/'+status_id+'/'+sort.val()+'/'+asc_value+'/';
    });

    // 排序选择的函数
    sort.change(function(){
        var sort_id=$(this).val();
        window.location='/declaration_status_query/'+'1/'+trade.val()+'/'+status.val()+'/'+sort_id+'/'+asc_value+'/';
    });

    // 排序切换的函数
    asc.click(function(event){
        event.preventDefault();

        var want_code=$(this).attr('want_code');

        window.location='/declaration_status_query/'+'1/'+trade.val()+'/'+status.val()+'/'+sort.val()+'/'+want_code+'/';

    })


});

$(function(){
    var search_btn=$('.search_btn');

    search_btn.click(function(event){
        event.preventDefault();

        var search_content=$('input[name=search]').val();

        window.location='/declaration_status_query/1/0/0/5/1/?search='+search_content;
    })
});

$(function(){
    var refund_btn=$('.refund_btn');
    refund_btn.click(function(event){
        event.preventDefault();

        var declaration_model=$(this).attr('data_declaration_model');
        var declaration_uuid=$(this).attr('data_declaration_uuid');

        rhjajax.post({
            url:'/refund_reason/',
            data:{
                declaration_model:declaration_model,
                declaration_uuid:declaration_uuid,
            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertConfirm({
                        title:'退单原因',
                        text:data['data']['refund_reason'],
                    })
                }else{
                    xtalert.alertInfo(data['message'])
                };
            }

        })
    });

});