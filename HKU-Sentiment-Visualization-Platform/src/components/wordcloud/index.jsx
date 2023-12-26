import WordCloud from 'react-d3-cloud';
import React, { useState, useEffect } from 'react';
import './wordcloud.css'; // 导入样式文件
import axios, { all } from 'axios';
export default function MyWordCloud(props){
    const [Clould_Data, setCloudData] = useState([]); // 使用useState给Cloud_Data设置初始值为[]

    useEffect(() => {        // 使用useEffect在组件挂载后获取数据
        axios.get('http://127.0.0.1:5000/commentData')
        .then(response => {
                console.log(response.data);
                setCloudData(response.data); // 将获取的数据设置到Cloud_Data中
        })
        .catch(error => {
                console.log(error);
        });
    }, []);// 初始化

    console.log("cloudData",Clould_Data)
    var data = [];
    if (Clould_Data) {
        data = Object.keys(Clould_Data).map(item => ({
          text: item,
          value: Clould_Data[item]
        }));
    }
    
    return(
        <div className='cloud-container'>
            <WordCloud
                data={data}
                width={260}
                height={205}
                font="Times"
                fontWeight="bold"
            />
        </div>
        
    )
}