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
                const WeiboText =  [
                  {
                    text: '这是微博内容',
                    likes: 120,
                    score: 7.5
                  },
                  {
                    text: '这是另一个微博内容',
                    likes: 300,
                    score: 9.2
                  },
                  {
                    text: '这是第三个微博内容',
                    likes: 210,
                    score: 8.6
                  },
                  // ...
                ]
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
    var WeiboText_data =  [
      {
        text: '【F-16详解】最畅销的战斗机 空中多面手',
        likes: 11000,
        score: 9.5
      },
      {
        text: '【C-5详解】美军现役最大运输机 全球空中机动战略支柱',
        likes: 300,
        score: 9.2
      },
      {
        text: '【F-22】这是一架来自30年前的飞机',
        likes: 210,
        score: 8.6
      },
      {
        text: '【硬抗飞机】世界最安全的办公楼？五角大楼有多特别？',
        likes: 2400,
        score: 8.3
      },
      // ...
    ]
    var Comment_Text_data =  [
      {
        text: '一个个弹幕里喊着我们造不出来的简直了，，tm现在运20载重60吨朝上 有啥代差？ 问题是我们搞出个类似b52的拿来干啥？？？ 你看美国敢拿b52对付我们吗？',
        likes: 10,
        score: 0.5
      },
      {
        text: '评论区怎么这么多反讽，嘲讽的，简直没法看，就没有评论评论飞机的吗',
        likes: 20,
        score: 3.2
      },
      {
        text: '话说还在吹？醒醒吧！这玩意早就过时了，用这玩意废人费钱，是无人机不香吗？一样的功能，无人机不费人造价也比这玩意便宜，咋滴？你们真当阿美莉卡的国防部是吃干饭？',
        likes: 10,
        score: 1.6
      },
      {
        text: '别踏马刷图160了，图160抄袭者，b1是70年代出现，图160是80年代出现，而且图160选不如B1，傻大黑粗，走的还是高空高速路线，不能低空突防，完全不隐身，RCS大的吓人，只能远远的射巡航导弹，本质上跟B52没区别，B1b好歹能低空突防规避雷达',
        likes: 20,
        score: 2.6
      },
      // ...
    ]
    var map_B_Data = [
      {name: '北京', value: 100},
      {name: '天津', value: 82},
      {name: '上海', value: 95},
      {name: '重庆', value: 70},
      {name: '河北', value: 46},
      {name: '河南', value: 55},
      {name: '云南', value: 67},
      {name: '辽宁', value: 75},
      {name: '黑龙江', value: 42},
      {name: '湖南', value: 87},
      {name: '安徽', value: 60},
      {name: '山东', value: 80},
      {name: '新疆', value: 45},
      {name: '江苏', value: 92},
      {name: '浙江', value: 88},
      {name: '江西', value: 75},
      {name: '湖北', value: 78},
      {name: '广西', value: 55},
      {name: '甘肃', value: 40},
      {name: '山西', value: 61},
      {name: '内蒙古', value: 69},
      {name: '陕西', value: 60},
      {name: '吉林', value: 50},
      {name: '福建', value: 70},
      {name: '贵州', value: 60},
      {name: '广东', value: 92},
      {name: '青海', value: 45},
      {name: '西藏', value: 30},
      {name: '四川', value: 81},
      {name: '宁夏', value: 50},
      {name: '海南', value: 60},
      {name: '台湾', value: 70},
      {name: '香港', value: 85},
      {name: '澳门', value: 75}
  ];

    var map_option = {
        title: {
            text: 'Fans Distribution',
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
                name: 'Fans Distribution',
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
                data: map_B_Data
            },
        ],
    };
    var date_option = {
        title: {
          text: '一周内视频总播放量'
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Email',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: 'Union Ads',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310]
          },
          {
            name: 'Video Ads',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410]
          },
          {
            name: 'Direct',
            type: 'line',
            stack: 'Total',
            data: [320, 332, 301, 334, 390, 330, 320]
          },
          {
            name: 'Search Engine',
            type: 'line',
            stack: 'Total',
            data: [820, 932, 901, 934, 1290, 1330, 1320]
          }
        ]
      };
    var option_Figure_Aly  = {
        color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
        title: {
          text: '用户画像'
        },
        radar: [
          {
            indicator: [
              { text: 'Indicator1' },
              { text: 'Indicator2' },
              { text: 'Indicator3' },
              { text: 'Indicator4' },
              { text: 'Indicator5' }
            ],
            center: ['50%', '50%'],
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

        ]
      };
    var Emotions_option =  {
      title: {
        text: '公关危机指数'
      },
      series: [
        {
          type: 'gauge',
          title: {
            text: 'My Chart Title',
            left: 'center',
            top: 'top'
          },
          axisLine: {
            lineStyle: {
              width: 30,
              color: [
                [0.3, '#67e0e3'],
                [0.7, '#37a2da'],
                [1, '#fd666d']
              ]
            }
          },
          
          pointer: {
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            distance: -30,
            length: 8,
            lineStyle: {
              color: '#fff',
              width: 2
            }
          },
          splitLine: {
            distance: -30,
            length: 30,
            lineStyle: {
              color: '#fff',
              width: 4
            }
          },
          axisLabel: {
            color: 'inherit',
            distance: 40,
            fontSize: 20
          },
          detail: {
            valueAnimation: true,
            formatter: '{value} 低风险',
            color: 'inherit'
          },
          data: [
            {
              value: 40
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
                        option={option_Figure_Aly}
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
                    <PostList data={WeiboText_data} title={"up主热门视频"} source={"Chris 的军事基地"}/>
                </div>
                <div className='echart-container-3'>
                  <ReactECharts option={Emotions_option} title = "公关危机指数" 
                      style={{
                            height: "40vh",
                            width: "32vw",
                        }}/>
                </div>
                <div className='echart-container-3'>
                    <PostList data={Comment_Text_data} title={"Most Popular Negative Weibo Posts"} source={"恶意评论"}/>
                </div>
            </div>
            
            
        </div>
    )
}