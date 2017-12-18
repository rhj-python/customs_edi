/**
 * Created by rhj231223 on 2017/11/13.
 */

'use strict';

//编辑报关单保存功能的函数
$(function () {
    var save_btn=$('#save_btn');
    save_btn.click(function(event){
        event.preventDefault();

        var declaration_uuid=$(this).attr('data_declaration_uuid');

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

        var import_port=$('input[name=import_port]').val();
        var import_date=$('input[name=import_date]').val();
        var departure_country=$('input[name=departure_country]').val();
        var loading_port=$('input[name=loading_port]').val();
        var domestic_destination=$('input[name=domestic_destination]').val();
        var use_id=$('select[name=use]').val();

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
            url:'/customs/edit_import_declaration_ajax/',
            data:{
                declaration_uuid:declaration_uuid,
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

                import_port:import_port,
                import_date:import_date,
                departure_country:departure_country,
                loading_port:loading_port,
                domestic_destination:domestic_destination,
                loading_port:loading_port,
                use_id:use_id,

                commodity_li:commodity_li,
                document_li:document_li,


            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('报关单保存成功!')
                    setTimeout(function(){
                        window.location='/customs/import_declaration_list/1/0/1/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message']);
                }
            },
        })




    })
});

//编辑报关单功能保存并提交的函数
$(function () {
    var save_btn=$('#submit_btn');
    save_btn.click(function(event){
        event.preventDefault();

        var declaration_uuid=$(this).attr('data_declaration_uuid');

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

        var import_port=$('input[name=import_port]').val();
        var import_date=$('input[name=import_date]').val();
        var departure_country=$('input[name=departure_country]').val();
        var loading_port=$('input[name=loading_port]').val();
        var domestic_destination=$('input[name=domestic_destination]').val();
        var use_id=$('select[name=use]').val();

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
            url:'/customs/edit_import_declaration_submit/',
            data:{
                declaration_uuid:declaration_uuid,
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

                import_port:import_port,
                import_date:import_date,
                departure_country:departure_country,
                loading_port:loading_port,
                domestic_destination:domestic_destination,
                loading_port:loading_port,
                use_id:use_id,

                commodity_li:commodity_li,
                document_li:document_li,


            },
            success:function(data){
                if(data['code']==200){
                    xtalert.alertSuccessToast('报关单保存并提交成功!');
                    setTimeout(function(){
                        window.location='/customs/import_declaration_list/1/0/1/1/';
                    },1200)
                }else{
                    xtalert.alertInfo(data['message']);
                }
            },
        })




    })
});

