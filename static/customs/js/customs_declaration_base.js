/**
 * Created by rhj231223 on 2017/11/9.
 */

'use strict';

//选择委托协议的函数
$(function(){
    var choice_agreement_btn=$('#choice_agreement_btn');


    choice_agreement_btn.click(function(event){
        event.preventDefault();
        var proxy_agreement_id=$('select[name=proxy_agreement]').val();

        xtalert.alertConfirm({
            title:'确认选择',
            text:'您确定要选择ID为 '+proxy_agreement_id+' 的委托协议吗?',
            confirmText:'确认选择',
            confirmCallback:function(){
                setTimeout(function(){
                    xtalert.alertSuccessToast('选择成功!')
                },100);
                setTimeout(function(){
                    var old_src=window.location.href;
                    var new_src=xtparam.setParam(old_src,'agreement_id',proxy_agreement_id)
                    window.location=new_src;
                },1200)
            }
        })
    })
});

//添加货物与移除货物的函数
$(function () {
    var add_commodity_btn=$('#add_commodity_btn');
    var commodity=$('#commodity_group');
    var commodity_tbody=$('#commodity_tbody');
    add_commodity_btn.click(function(event){
        event.preventDefault();
        commodity_tbody.append(commodity.html());

        var remove_commodity_btn=$('.remove_commodity_btn');
        remove_commodity_btn.click(function(event){
        event.preventDefault();

        $(this).parent().parent().remove();
        })
    });

    var remove_commodity_btn=$('.remove_commodity_btn');
        remove_commodity_btn.click(function(event){
        event.preventDefault();

        $(this).parent().parent().remove();
        })
});

//添加与移除单据的函数
$(function () {

    var add_document_btn=$('#add_document_btn');
    var document=$('#document_group');
    var document_tbody=$('#document_tbody');

    add_document_btn.click(function(event){
        event.preventDefault();


        document_tbody.append(document.html());


         var upload_btn=$('.upload_btn');
            upload_btn.click(function(){
                event.preventDefault();
                $(this).attr('data_btn','1');
            });

         xtqiniu.setUp({
        browse_button:$('.upload_btn:last').get(),
        fileadded:function (up,files) {
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_status').hide();
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_div').show();
            $('.upload_btn').attr('disabled','disabled');
        },
        progress:function(up,file){
            var percent=file.percent;

            $(".upload_btn[data_btn='1']").parent().parent().find('.progress-bar').css({
                'width':percent+'%',
            });
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress-bar').text(percent+'%');
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress-bar').attr('aria-valuenow',percent);
        },

        complete:function(){
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_div').hide();
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_status').text('上传成功');
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_status').removeClass('label-warning');
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_status').addClass('label-success');
            $(".upload_btn[data_btn='1']").parent().parent().find('.progress_status').show();
            $(".upload_btn[data_btn='1']").parent().parent().find('.preview_btn').show();
            $('.upload_btn').attr('data_btn','0');
            $('.upload_btn').removeAttr('disabled')
            },
        success:function(up,file,info){
            $(".upload_btn[data_btn='1']").parent().parent().find('.preview_btn').attr('href',file.name);
        }

        });



        var remove_document_btn=$('.remove_document_btn');
        remove_document_btn.click(function(event){
        event.preventDefault();

        $(this).parent().parent().remove();
        })
    });

    var remove_document_btn=$('.remove_document_btn');
    remove_document_btn.click(function(event){
    event.preventDefault();

    $(this).parent().parent().remove();
    })






});


$(function(){



});


