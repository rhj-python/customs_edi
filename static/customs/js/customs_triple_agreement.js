/**
 * Created by rhj231223 on 2017/10/26.
 */

'use strict';

$(function () {
    var cancel_btn=$('.cancel_btn');
    cancel_btn.click(function(event){
        event.preventDefault();

        var self=$(this);
        var agreement_id=self.attr('data_agreement_id');
        var agreement_zone_name=self.attr('data_agreement_zone_name');

        xtalert.alertConfirm({
            title:'确认解约',
            text:'解除合约后要签约需重新进行向海关进行申请,您确定要与 '+ agreement_zone_name+' 解除合约吗？',
            confirmColor:'#c00',
            confirmText:'我要解约',
            cancelText:'我在想想',
            confirmCallback:function(){
                 rhjajax.post({
                    url:'/customs/cancel_triple_agreement/',
                    data:{
                        agreement_id:agreement_id,
                    },
                    success:function(data){
                        if(data['code']==200){
                            setTimeout(function(){
                                xtalert.alertSuccessToast('解约成功');
                            },100);
                            setTimeout(function(){
                                window.location.reload();
                            },1200);

                        }else{
                            xtalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });

    })

});
