import { useState, useEffect } from 'react';
import React from 'react';
import * as echarts from 'echarts';
import './index.css'; // 导入样式文件
import axios, { all } from 'axios';
import MyWordCloud from '../wordcloud';
import PostList from '../PostList';
import ReactECharts from 'echarts-for-react';

export default function WeiboPage(props) {
    const { weiboHotVal, weiboDateVal, xAxis } = props;
    const [cloudData, setCloudData] = useState([]);
    const [mapData, setMapData] = useState([]);
    const [weiboText, setWeiboText] = useState([]);
    const [tweetPositiveText, setTweetPositiveText] = useState([]);
    const [tweetNegativeText, setTweetNegativeText] = useState([]);
    // 第一行：两个柱状图 + 词云
    // 第二行：三个博文组件
    // 第三行：地图
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://8.130.120.233:8088/weibo');
                const allData = response.data.data;
                console.log(allData)

                // 1. 词云数据
                const cloudOriginal = allData.WeiboCloud;

                // 2. 帖子数据
                const WeiboText = allData.WeiboText.WeiboText;
                const TweetPositiveText = allData.TweetPositiveText.TweetPositiveText;
                const TweetNegativeText = allData.TweetNegativeText.TweetNegativeText;
                // 微博：text，likes，score
                // 推特：text favoriteCount score，推特的洗一下，把favoriteCount变成 likes，都按 text, likes, score 的格式去传

                // 3. 地图数据
                const locationMap = allData.locationMap;
                // 使用 Object.keys() 获取 locationMap 中所有的省份
                const provinces = Object.keys(locationMap);
                // 使用 map 方法转换数组格式
                const mapChange = provinces.map(province => {
                    return { name: province, value: locationMap[province] };
                });

                // 设置数据：
                // 1. 设置词云数据
                setCloudData(cloudOriginal);

                // 2. 设置帖子数据
                setWeiboText(WeiboText);
                setTweetNegativeText(TweetNegativeText);
                setTweetPositiveText(TweetPositiveText);

                // 3. 设置地图数据
                setMapData(mapChange);

            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, [])

    var map_option = {
        title: {
            text: 'Weibo Map',
            left: "center",
            top: 10,
        },
        tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2
        },
        visualMap: {
            left: 'right',
            min: 1,
            max: 100,
            inRange: {
                color: [
                    '#313695',
                    '#4575b4',
                    '#74add1',
                    '#abd9e9',
                    '#e0f3f8',
                    '#ffffbf',
                    '#fee090',
                    '#fdae61',
                    '#f46d43',
                    '#d73027',
                    '#a50026'
                ]
            },
            text: ['High', 'Low'],
            calculable: true
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: { readOnly: false },
                restore: {},
                saveAsImage: {}
            }
        },
        series: [
            {
                name: 'Weibo Posts',
                type: "map",
                // mapType,
                map: "china",
                itemStyle: {
                    //地图区域的多边形 图形样式
                    normal: {
                        //是图形在默认状态下的样式
                        label: {
                            show: true, //是否显示标签
                            textStyle: {
                                color: "rgba(255,255,255,0)",
                            },
                        },
                    },
                },
                // aspectScale: mapType === "china" ? 0.75 : 1,
                top: "10%", //组件距离容器的距离
                data: mapData
            },
        ],
    };
    var hot_option = {
        title: {
            text: 'Hot-Val of Weibo Posts in Last Week ',
            x: 'center',
            top: 10
        },
        grid: { top: 50, right: 30, bottom: 30, left: 50 },
        xAxis: {
            type: 'category',
            data: xAxis
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: weiboHotVal,
                type: 'bar'
            }
        ]
    };
    var date_option = {
        title: {
            text: 'Number of HKU-related Weibo Posts in Last Week',
            x: 'center',
            top: 10
        },
        grid: { top: 50, right: 30, bottom: 30, left: 50 },
        xAxis: {
            type: 'category',
            data: xAxis
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: [
                    {
                      value: [3, 5, 8, 2, 0],
                      name: 'Data B',
                    }
                  ],
                type: 'bar'
            }
        ]
    };
    var option_Aly  = {
        color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
        title: {
          text: 'Customized Radar Chart'
        },
        legend: {},
        radar: [
          {
            indicator: [
              { text: 'Indicator1' },
              { text: 'Indicator2' },
              { text: 'Indicator3' },
              { text: 'Indicator4' },
              { text: 'Indicator5' }
            ],
            center: ['25%', '50%'],
            radius: 120,
            startAngle: 90,
            splitNumber: 4,
            shape: 'circle',
            axisName: {
              formatter: '【{value}】',
              color: '#428BD4'
            },
            splitArea: {
              areaStyle: {
                color: ['#77EADF', '#26C3BE', '#64AFE9', '#428BD4'],
                shadowColor: 'rgba(0, 0, 0, 0.2)',
                shadowBlur: 10
              }
            },
            axisLine: {
              lineStyle: {
                color: 'rgba(211, 253, 250, 0.8)'
              }
            },
            splitLine: {
              lineStyle: {
                color: 'rgba(211, 253, 250, 0.8)'
              }
            }
          },
          {
            indicator: [
              { text: 'Indicator1', max: 150 },
              { text: 'Indicator2', max: 150 },
              { text: 'Indicator3', max: 150 },
              { text: 'Indicator4', max: 120 },
              { text: 'Indicator5', max: 108 },
              { text: 'Indicator6', max: 72 }
            ],
            center: ['75%', '50%'],
            radius: 120,
            axisName: {
              color: '#fff',
              backgroundColor: '#666',
              borderRadius: 3,
              padding: [3, 5]
            }
          }
        ],
        series: [
          {
            type: 'radar',
            emphasis: {
              lineStyle: {
                width: 4
              }
            },
            data: [
              {
                value: [100, 8, 0.4, -80, 2000],
                name: 'Data A'
              },
              {
                value: [60, 5, 0.3, -100, 1500],
                name: 'Data B',
                areaStyle: {
                  color: 'rgba(255, 228, 52, 0.6)'
                }
              }
            ]
          },
          {
            type: 'radar',
            radarIndex: 1,
            data: [
              {
                value: [120, 118, 130, 100, 99, 70],
                name: 'Data C',
                symbol: 'rect',
                symbolSize: 12,
                lineStyle: {
                  type: 'dashed'
                },
                label: {
                  show: true,
                  formatter: function (params) {
                    return params.value;
                  }
                }
              },
              {
                value: [100, 93, 50, 90, 70, 60],
                name: 'Data D',
                areaStyle: {
                  color: new echarts.graphic.RadialGradient(0.1, 0.6, 1, [
                    {
                      color: 'rgba(255, 145, 124, 0.1)',
                      offset: 0
                    },
                    {
                      color: 'rgba(255, 145, 124, 0.9)',
                      offset: 1
                    }
                  ])
                }
              }
            ]
          }
        ]
      };
    return (
        <div>
            {/* 第一行：词云 + 两个柱状图 */}
            <div className='overview-row'>
                <div className='echart-container-3'>
                    <MyWordCloud cloudData={cloudData} />
                </div>
                <div className='echart-container-3'>
                    <ReactECharts
                        option={option_Aly}
                        style={{
                            height: "40vh",
                            width: "32vw",
                        }} />
                </div>
                <div className='echart-container-3'>
                    <ReactECharts
                        option={date_option}
                        style={{
                            height: "40vh",
                            width: "32vw",
                        }} />
                </div>
            </div>

            {/* 第二行：列表 */}
            <div className='overview-row'>
                <div className='echart-container-3'>
                    <PostList data={weiboText} title={"Most Popular Overall Weibo Posts"} source={"Weibo"}/>
                </div>
                <div className='echart-container-3'>
                    <PostList data={tweetPositiveText} title={"Most Popular Positive Weibo Posts"} source={"Weibo"}/>
                </div>
                <div className='echart-container-3'>
                    <PostList data={tweetNegativeText} title={"Most Popular Negative Weibo Posts"} source={"Weibo"}/>
                </div>
            </div>
            

            {/* 第三行：地图 */}
            <div className='echart-container-4'>
                <ReactECharts
                    option={map_option}
                    style={{
                        height: "60vh",
                        width: "90vw",
                    }} 
                />
            </div>
            
        </div>
    )
}