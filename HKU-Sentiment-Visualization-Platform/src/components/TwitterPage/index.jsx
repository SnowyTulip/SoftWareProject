import { useState, useEffect } from 'react';
import React from 'react';
import './index.css'; // 导入样式文件
import axios, { all } from 'axios';
import MyWordCloud from '../wordcloud';
import PostList from '../PostList';
import ReactECharts from 'echarts-for-react';

export default function TwitterPage(props) {
    const { tweetDateVal, tweetHotVal, xAxis } = props;
    const [cloudData, setCloudData] = useState([]);
    const [tweetText, setTweetText] = useState([]);
    const [tweetPositiveText, setTweetPositiveText] = useState([]);
    const [tweetNegativeText, setTweetNegativeText] = useState([]);
    // 第一行：两个柱状图 + 词云
    // 第二行：三个博文组件
    // 第三行：地图
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://8.130.120.233:8088/tweet');
                const allData = response.data.data;
                console.log(allData)

                // 1. 词云数据
                const cloudOriginal = allData.TweetCloud;
                console.log("cloudOriginal",cloudOriginal)

                // 2. 帖子数据
                const TweetTextOri = allData.TweetText.TweetText;
                const TweetPositiveTextOri = allData.TweetPositiveText.TweetPositiveText;
                const TweetNegativeTextOri = allData.TweetNegativeText.TweetNegativeText;
                // 微博：text，likes，score
                // 推特：text favoriteCount score，推特的洗一下，把favoriteCount变成 likes，都按 text, likes, score 的格式去传
                // 处理数据：
                const TweetText = TweetTextOri.map(item => {
                    const { text, favoriteCount, score } = item;
                    return {
                      text,
                      likes: favoriteCount,
                      score,
                    };
                });
                const TweetPositiveText = TweetPositiveTextOri.map(item => {
                    const { text, favoriteCount, score } = item;
                    return {
                      text,
                      likes: favoriteCount,
                      score,
                    };
                });
                const TweetNegativeText = TweetNegativeTextOri.map(item => {
                    const { text, favoriteCount, score } = item;
                    return {
                      text,
                      likes: favoriteCount,
                      score,
                    };
                });

                // 设置数据：
                // 1. 设置词云数据
                setCloudData(cloudOriginal);

                // 2. 设置帖子数据
                setTweetText(TweetText);
                setTweetNegativeText(TweetNegativeText);
                setTweetPositiveText(TweetPositiveText);

            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, [])
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
            text: '粉丝分布图',
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
                name: '粉丝分布',
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
                                color: "rgba(0,0,0,1)",
                                fontSize:13,
                            },
                            formatter: '{b}\n{c}' //b代表区域的名字，c代表数据的值
                        },
                    },
                },
                // aspectScale: mapType === "china" ? 0.75 : 1,
                top: "5%",     //将component top值调低
                left: "10%",     //将component left值调低
                right: "0%",    //将component right值调低
                bottom: "10%",  //将component bottom值调低
                data: map_B_Data
            },
        ],
    };
    return (
        <div>
            <div className='echart-container-4'>
                <ReactECharts
                    option={map_option}
                    style={{
                        height: "50vw",
                        width: "65vw",
                    }} 
                />
            </div>
        </div>
    )
}