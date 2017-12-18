/**
 * Created by renhuijun on 2017/10/20.
 */

'use strict';

$(function () {
    var green_btn=$('.green_btn');
    green_btn.click(function() {
        event.preventDefault();
        $(this).parent().find('.unfold').slideToggle();
        $(this).find('.gly').toggleClass('glyphicon-minus','glyphicon-plus')
    })
});


//左边菜单栏选中函数
$(function(){
    var href=window.location.href;

    if(href.indexOf('zone')>=0){
        var zone=$('.zone');
        zone.parent().parent().find('.green_btn').click();
        zone.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('agreement_list')>=0){
        var agreement_list=$('.agreement_list');
        agreement_list.parent().parent().find('.green_btn').click();
        agreement_list.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('customs_import')>=0){
        var customs_import=$('.customs_import');
        customs_import.parent().parent().find('.green_btn').click();
        customs_import.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('customs_export')>=0){
        var customs_export=$('.customs_export');
        customs_export.parent().parent().find('.green_btn').click();
        customs_export.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('triple_agreement')>=0){
        var triple_agreement=$('.triple_agreement');
        // triple_agreement.parent().parent().find('.green_btn').click();
        triple_agreement.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('proxy')>=0){
        var proxy=$('.proxy');
        // proxy.parent().parent().find('.green_btn').click();
        proxy.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('import_declaration')>=0){
        var import_declaration=$('.import_declaration');
        import_declaration.parent().parent().find('.green_btn').click();
        import_declaration.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('export_declaration')>=0){
        var export_declaration=$('.export_declaration');
        export_declaration.parent().parent().find('.green_btn').click();
        export_declaration.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('profile')>=0){
        var profile=$('.profile');
        profile.parent().parent().find('.green_btn').click();
        profile.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('reset_pwd')>=0){
        var reset_pwd=$('.reset_pwd');
        reset_pwd.parent().parent().find('.green_btn').click();
        reset_pwd.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('reset_email')>=0){
        var reset_email=$('.reset_email');
        reset_email.parent().parent().find('.green_btn').click();
        reset_email.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('user_manage')>=0){
        var user_manage=$('.user_manage');
        user_manage.parent().parent().find('.green_btn').click();
        user_manage.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('client_company_list')>=0){
        var client_company_list=$('.client_company_list');
        client_company_list.parent().parent().find('.green_btn').click();
        client_company_list.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('employee_manage')>=0){
        var employee_manage=$('.employee_manage');
        employee_manage.parent().parent().find('.green_btn').click();
        employee_manage.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('role_manage')>=0){
        var role_manage=$('.role_manage');
        role_manage.parent().parent().find('.green_btn').click();
        role_manage.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('permission_manage')>=0){
        var permission_manage=$('.permission_manage');
        permission_manage.parent().parent().find('.green_btn').click();
        permission_manage.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('msg')>=0){
        var msg=$('.msg_nav');
        msg.addClass('g_active').siblings().removeClass('g_active');
    }else if(href.indexOf('chart')>=0){
        var chart=$('.chart');
        chart.addClass('g_active').siblings().removeClass('g_active');
    }
});

