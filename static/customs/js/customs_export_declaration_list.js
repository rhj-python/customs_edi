/**
 * Created by rhj231223 on 2017/11/19.
 */

'use strict';

$(function () {
    var filter=$('select[name=filter]');
    var sort=$('select[name=sort]');
    var asc=$('button[name=asc]');

    var asc_id=asc.attr('data_code');

    //过滤函数
    filter.change(function(){
        var filter_id=$(this).val();
        window.location='/customs/export_declaration_list/1/'+filter_id+'/'+sort.val()+'/'+asc_id+'/';
    });

    //排序方法函数
    sort.change(function(){
        var sort_id=$(this).val();
        window.location='/customs/export_declaration_list/1/'+filter.val()+'/'+sort_id+'/'+asc_id+'/';
    });

    //顺序逆序函数
    asc.click(function(event){
        event.preventDefault();

        var want_code=$(this).attr('want_code');
        window.location='/customs/export_declaration_list/1/'+filter.val()+'/'+sort.val()+'/'+want_code+'/';
    })

});

$(function(){
    var search_btn=$('#search_btn');
    search_btn.click(function(event){
        event.preventDefault();

        var search=$('input[name=search]');

        window.location='/customs/export_declaration_list/1/0/1/1/?search='+search.val();
    })
});
