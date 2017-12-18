/**
 * Created by rhj231223 on 2017/12/5.
 */

'use strict';

$(function () {
    var url=window.location.href;
    var nav_tabs=$('#nav_tabs');
    if(url.indexOf('single')>=0){
        nav_tabs.children().eq(0).addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('group')>=0) {
        nav_tabs.children().eq(1).addClass('active').siblings().removeClass('active');
    }
});
