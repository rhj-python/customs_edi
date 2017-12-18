/**
 * Created by rhj231223 on 2017/12/7.
 */

'use strict';

//进出口数量表
$(function () {
    rhjajax.get({
        url:'/chart/trade_num_chart/',
        success:function(data){
            $('#trade_num_chart').highcharts({
                chart:{
                    type:'areaspline'
                },
                title:{
                    text:'2016年报关数量统计',
                },
                xAxis:{
                    categories:['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'],
                    labels:{
                        formatter:function(){
                            return this.value;
                        }
                    }
                },
                yAxis:{
                    title:{
                        text:'进出口报关',
                    }
                },
                tooltip:{
                    pointFormat:'{series.name} 申报了 <b>{point.y:,.0f}</b> 票货物'
                },
                plotOptions:{
                    areaspline:{
                        // dataLabels:{
                        //     enabled:true,
                        // },
                        marker:{
                            enabled:false,
                            symbol:'circle',
                            radius:2,
                            states:{
                                hover:{
                                    enabled:true
                                }
                            }
                        }
                    }
                },
                credits: {
                    enabled: false
                },
                series:data['data']
            })
                }
            })
});

$(function(){
    rhjajax.get({
        url:'/chart/user_chart/',
        success:function(data){
            var chart=null;
            $('#user_chart').highcharts({
                chart:{
                    plotBackgroundColor:null,
                    plotBorderWidth:null,
                    plotShadow:null,
                    spacing:[100,0,40,0],
                },
                title:{
                    floating:true,
                    text:'用户种类对比图',
                },
                tooltip:{
                    pointFormat:'{series.name}:<b>{point.percentage:.1f}%</b>'

                },
                plotOptions:{
                    pie:{
                        allowPointSelect:true,
                        cursor:'pointer',
                        dataLabels:{
                            enabled:true,
                            format:'<br>{series.name}</br>:{point.percentage:.1f}%',
                            style:{
                                color:(Highcharts.theme && Highcharts.theme.constrastTextColor)|| 'black'
                            },
                        },

                        point:{
                            events:{
                                mouseOver:function(e){
                                   chart.setTitle({
                                        text: e.target.name+ '\t'+ e.target.y + ' %'
                                    });

                                },
                                click:function(e) { // 同样的可以在点击事件里处理
                                    chart.setTitle({
                                        text: e.point.name+ '\t'+ e.point.y + ' %'
                                    });
                                    }
                            }
                        }

                    }
                },
                credits: {
                    enabled: false
                },

                series:[{
                    type:'pie',
                    innerSize:'80%',
                    name:'占网站用户比例',
                    data:data['data']
                }]


            },function(c){
                var centerY=c.series[0].center[1];
                var titleHeight=parseInt(c.title.styles.fontSize);
                c.setTitle({
                    y:centerY+titleHeight/2
                });
                chart=c;
            })
        }
    })

});

//2015 2016报关情况对比
$(function(){
    rhjajax.get({
        url:'/chart/trade_contrast_chart/',
        success:function(data){
            $('#trade_contrast_chart').highcharts({
                chart: {
                    type: 'column'
                },
                title: {
                    text: '2015与2016报关情况对比图'
                },
                xAxis: {
                    categories: ['进口','出口','总数']
                },
                yAxis:{
                    title:{
                        text:'申报单据数量'
                    }
                },

                credits: {
                    enabled: false
                },
                plotOptions:{
                    column:{
                        borderRadius:5,
                    },
                },

                series:data['data']
                        })
        },
    })
});

$(function(){
    rhjajax.get({
        url:'/chart/budget_spend_chart/',
        success:function(data){
            $('#budget_spend_chart').highcharts({
                chart:{
                    polar:true,
                    type:'area',
                },
                title:{
                    text:'2016年预算与收入对比图',
                    x:-80,
                },
                 pane: {
                    size: '80%'
                },

                xAxis: {
                    categories: ['销售', '市场', '客户支持', '人事',
                            '研发', '管理'],
                    tickmarkPlacement: 'on',
                    lineWidth: 0
                },

                yAxis: {
                    gridLineInterpolation: 'polygon',
                    lineWidth: 0,
                    min: 0
                },

                tooltip: {
                    shared: true,
                    pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
                },

                plotOption:{
                    area:{
                        dataLabel:{
                            enabled:true,
                        }
                    }
                },

                legend: {
                    align: 'right',
                    verticalAlign: 'top',
                    y: 70,
                    layout: 'vertical'
                },

                credits: {
                    enabled: false
                },

                series:data['data']
                        })
            }
    })
});

$(function(){
    rhjajax.get({
        url:'/chart/message_info_chart/',
        success:function(data){
            $('#message_info_chart').highcharts({
                chart:{
                    type:'areaspline',
                },
                title:{
                    text:'最近一周网站活跃情况',
                },
                xAxis:{
                    categories:data['li'],
                    labels:{
                        formatter:function(){
                            return this.value
                        }
                    },
                },
                yAxis:{
                    title:{
                        text:'消息数量',
                    },
                    label:{
                        formatter:function(){
                            return this.value
                        },
                    },
                },
                tooltip:{
                    pointFormat:'<span style="color:{{series.color}}">{series.name} 产生了</span>'+
                        '<b>{point.y:,0f} 条消息</b>'
                },
                plotOptions:{
                    areaspline:{
                        fillColor : {
                                linearGradient : {
                                    x1: 0,
                                    y1: 0,
                                    x2: 0,
                                    y2: 1,
                                },
                                stops : [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                                ]
                            },
                            marker:{
                                enabled:false,
                                symbol:'circle',
                                radius:2,
                                events:{
                                    hover:{
                                        enabled:true,
                                    }
                                },

                        },

                    },
                },
                 series:data['data']
                    })
                }
    })
});