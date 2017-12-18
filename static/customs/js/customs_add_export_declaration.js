/**
 * Created by rhj231223 on 2017/11/13.
 */

'use strict';

//新增报关单保存功能的函数
$(function () {
    var save_btn=$('#save_btn');
    save_btn.click(function(event){
        event.preventDefault();

        var pre_entry_code=$('input[name=pre_entry_code]').val();
        var agreement_id=$('select[name=agreement_id]').val();
        var customs_date=$('input[name=customs_date]').val();
        var case_code=$('input[name=case_code]').val();
        var contract_code=$('input[name=contract_code]').val();
        var consignee=$('input[name=consignee]').val();
        var transport_mode_id=$('select[name=transport_mode]').val();
        var vessel_name=$('input[name=vessel_name]').val();
        var vessel_code=$('input[name=vessel_code]').val();
        var bl_code=$('input[name=bl_code]').val();
        var trade_mode_id=$('select[name=trade_mode]').val();
        var tax_mode_id=$('select[name=tax_mode]').val();
        var tax_rate=$('input[name=tax_rate]').val();
        var license_code=$('input[name=license_code]').val();
        var approval_code=$('input[name=approval_code]').val();
        var transaction_mode_id=$('select[name=transaction_mode]').val();
        var freight=$('input[name=freight]').val();
        var insurance_premiums=$('input[name=insurance_premiums]').val();
        var sundry_charges=$('input[name=sundry_charges]').val();
        var packages_num=$('input[name=packages_num]').val();
        var packing_type=$('input[name=packing_type]').val();
        var gross_weight=$('input[name=gross_weight]').val();
        var net_weight=$('input[name=net_weight]').val();
        var container_code=$('input[name=container_code]').val();
        var marks=$('textarea[name=marks]').val();

        var export_port=$('input[name=export_port]').val();
        var export_date=$('input[name=export_date]').val();
        var destination_country=$('input[name=destination_country]').val();
        var destination_port=$('input[name=destination_port]').val();
        var manufacturer=$('input[name=manufacturer]').val();
        var goods_origin_place=$('input[name=goods_origin_place]').val();
        var settlement_mode_id=$('select[name=settlement_mode]').val();

        var commodity_li=[];

        var commodity_trs=$('.commodity_tr');
        commodity_trs.each(function(){

            var item_code=$(this).find('input[name=item_code]').val();
            var hs_code=$(this).find('input[name=hs_code]').val();
            var commodity_name=$(this).find('input[name=commodity_name]').val();
            var commodity_type=$(this).find('input[name=commodity_type]').val();
            var quantity_and_unit=$(this).find('input[name=quantity_and_unit]').val();
            var country=$(this).find('input[name=country]').val();
            var unit_price=$(this).find('input[name=unit_price]').val();
            var total_price=$(this).find('input[name=total_price]').val();
            var currency_id=$(this).find('select[name=currency]').val();
            var tax_free_mode_id=$(this).find('select[name=tax_free_mode]').val();

            var commodity_dic={
                item_code:item_code,
                hs_code:hs_code,
                commodity_name:commodity_name,
                commodity_type:commodity_type,
                quantity_and_unit:quantity_and_unit,
                country:country,
                unit_price:unit_price,
                total_price:total_price,
                currency_id:currency_id,
                tax_free_mode_id:tax_free_mode_id,
            };

            commodity_li.push(JSON.stringify(commodity_dic));


        });

        console.log(commodity_li);

        var document_trs=$('.document_tr');
        var document_li=[];

        document_trs.each(function(){
            var document_type_id=$(this).find('select[name=document_type]').val();
            var name=$(this).find('input[name=document_name]').val();
            var url=$(this).find('.preview_btn').attr('href');
            var document_dic={
                document_type_id:document_type_id,
                name:name,
                url:url,
            };

            document_li.push(JSON.stringify(document_dic));

        });

        rhjajax.post({
            url:'/customs/add_export_declaration_ajax/',
            data:{
                pre_entry_code:pre_entry_code,
                agreement_id:agreement_id,
                customs_date:customs_date,
                case_code:case_code,
                contract_code:contract_code,
                consignee:consignee,
                transport_mode_id:transport_mode_id,
                vessel_name:vessel_name,
                vessel_code:vessel_code,
                bl_code:bl_code,
                trade_mode_id:trade_mode_id,
                tax_mode_id:tax_mode_id,
                tax_rate:tax_rate,
                license_code:license_code,
                approval_code:approval_code,
                transaction_mode_id:transaction_mode_id,
                freight:freight,
                insurance_premiums:insurance_premiums,
                sundry_charges:sundry_charges,
                packages_num:packages_num,
                packing_type:packing_type,
                gross_weight:gross_weight,
                net_weight:net_weight,
                container_code:container_code,
                marks:marks,

                export_port:export_port,
                export_date:export_date,
                destination_country:destination_country,
                destination_port:destination_port,
                manufacturer:manufacturer,
                goods_origin_place:goods_origin_place,
                settlement_mode_id:settlement_mode_id,


                commodity_li:commodity_li,
                document_li:document_li,


            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('报关单保存成功!');
                    setTimeout(function(){
                        window.location='/customs/export_declaration_list/1/0/1/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message']);
                }
            },
        })




    })
});


//新增报关单保存并提交功能的函数
$(function () {
    var save_btn=$('#submit_btn');
    save_btn.click(function(event){
        event.preventDefault();

        var pre_entry_code=$('input[name=pre_entry_code]').val();
        var agreement_id=$('select[name=agreement_id]').val();
        var customs_date=$('input[name=customs_date]').val();
        var case_code=$('input[name=case_code]').val();
        var contract_code=$('input[name=contract_code]').val();
        var consignee=$('input[name=consignee]').val();
        var transport_mode_id=$('select[name=transport_mode]').val();
        var vessel_name=$('input[name=vessel_name]').val();
        var vessel_code=$('input[name=vessel_code]').val();
        var bl_code=$('input[name=bl_code]').val();
        var trade_mode_id=$('select[name=trade_mode]').val();
        var tax_mode_id=$('select[name=tax_mode]').val();
        var tax_rate=$('input[name=tax_rate]').val();
        var license_code=$('input[name=license_code]').val();
        var approval_code=$('input[name=approval_code]').val();
        var transaction_mode_id=$('select[name=transaction_mode]').val();
        var freight=$('input[name=freight]').val();
        var insurance_premiums=$('input[name=insurance_premiums]').val();
        var sundry_charges=$('input[name=sundry_charges]').val();
        var packages_num=$('input[name=packages_num]').val();
        var packing_type=$('input[name=packing_type]').val();
        var gross_weight=$('input[name=gross_weight]').val();
        var net_weight=$('input[name=net_weight]').val();
        var container_code=$('input[name=container_code]').val();
        var marks=$('textarea[name=marks]').val();

        var export_port=$('input[name=export_port]').val();
        var export_date=$('input[name=export_date]').val();
        var destination_country=$('input[name=destination_country]').val();
        var destination_port=$('input[name=destination_port]').val();
        var manufacturer=$('input[name=manufacturer]').val();
        var goods_origin_place=$('input[name=goods_origin_place]').val();
        var settlement_mode_id=$('select[name=settlement_mode]').val();

        var commodity_li=[];

        var commodity_trs=$('.commodity_tr');
        commodity_trs.each(function(){

            var item_code=$(this).find('input[name=item_code]').val();
            var hs_code=$(this).find('input[name=hs_code]').val();
            var commodity_name=$(this).find('input[name=commodity_name]').val();
            var commodity_type=$(this).find('input[name=commodity_type]').val();
            var quantity_and_unit=$(this).find('input[name=quantity_and_unit]').val();
            var country=$(this).find('input[name=country]').val();
            var unit_price=$(this).find('input[name=unit_price]').val();
            var total_price=$(this).find('input[name=total_price]').val();
            var currency_id=$(this).find('select[name=currency]').val();
            var tax_free_mode_id=$(this).find('select[name=tax_free_mode]').val();

            var commodity_dic={
                item_code:item_code,
                hs_code:hs_code,
                commodity_name:commodity_name,
                commodity_type:commodity_type,
                quantity_and_unit:quantity_and_unit,
                country:country,
                unit_price:unit_price,
                total_price:total_price,
                currency_id:currency_id,
                tax_free_mode_id:tax_free_mode_id,
            };

            commodity_li.push(JSON.stringify(commodity_dic));


        });

        console.log(commodity_li);

        var document_trs=$('.document_tr');
        var document_li=[];

        document_trs.each(function(){
            var document_type_id=$(this).find('select[name=document_type]').val();
            var name=$(this).find('input[name=document_name]').val();
            var url=$(this).find('.preview_btn').attr('href');
            var document_dic={
                document_type_id:document_type_id,
                name:name,
                url:url,
            };

            document_li.push(JSON.stringify(document_dic));

        });

        rhjajax.post({
            url:'/customs/add_export_declaration_submit/',
            data:{
                pre_entry_code:pre_entry_code,
                agreement_id:agreement_id,
                customs_date:customs_date,
                case_code:case_code,
                contract_code:contract_code,
                consignee:consignee,
                transport_mode_id:transport_mode_id,
                vessel_name:vessel_name,
                vessel_code:vessel_code,
                bl_code:bl_code,
                trade_mode_id:trade_mode_id,
                tax_mode_id:tax_mode_id,
                tax_rate:tax_rate,
                license_code:license_code,
                approval_code:approval_code,
                transaction_mode_id:transaction_mode_id,
                freight:freight,
                insurance_premiums:insurance_premiums,
                sundry_charges:sundry_charges,
                packages_num:packages_num,
                packing_type:packing_type,
                gross_weight:gross_weight,
                net_weight:net_weight,
                container_code:container_code,
                marks:marks,

                export_port:export_port,
                export_date:export_date,
                destination_country:destination_country,
                destination_port:destination_port,
                manufacturer:manufacturer,
                good_origin_place:good_origin_place,
                settlement_mode_id:settlement_mode_id,

                commodity_li:commodity_li,
                document_li:document_li,


            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('报关单保存并提交成功!');
                    setTimeout(function(){
                        window.location='/customs/export_declaration_list/1/0/1/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message']);
                }
            },
        })




    })
});

