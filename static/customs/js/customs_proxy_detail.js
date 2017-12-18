/**
 * Created by rhj231223 on 2017/11/8.
 */

'use strict';

$(function () {
    var filter=$('select[name=filter]');
    var proxy_id=filter.attr('data_proxy_id');

    filter.change(function(){
        var value=$(this).val();

        window.location='/customs/proxy_detail/'+proxy_id+'/'+value+'/';
    })
});
