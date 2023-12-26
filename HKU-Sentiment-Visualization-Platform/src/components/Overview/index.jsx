import React, { useEffect, useRef, useState } from 'react';
import echarts from 'echarts';
import 'echarts/lib/chart/line';
import 'echarts/lib/chart/pie';
import './App.css';  // Assuming you put your css in App.css 

function ChartComponent() {
  const chartRef = useRef(null);
  const chart2Ref = useRef(null);
  const [previousButton, setPreviousButton] = useState(null);
  const data = {
    "播放量": [120, 200, 150, 80, 70, 110, 130],
    "粉丝数": [220, 182, 191, 234, 290, 330, 310],
    "点赞": [220, 182, 123, 234, 290, 330, 123],
    "收藏": [220, 182, 191, 234, 290, 330, 310],
    "评论": [220, 182, 191, 23, 290, 330, 310],
    "弹幕": [123, 182, 191, 34, 290, 330, 310],
    "分享": [220, 182, 191, 234, 12, 330, 310],
    "投币": [220, 182, 191, 234, 31, 12, 310],
  };
//   const aggregate = Object.keys(data).reduce((acc, key) => {
//     return { ...acc, [key]: data[key].reduce((a, b) => a + b, 0) }
//   }, {});

  const updateData = (type) => {
    // Rest of button code...
    if (previousButton) {
      previousButton.style.background = "rgba(0, 0, 0, 0.6)";
    }
    var button = document.getElementById(type);
    button.style.background = "rgba(255,70,132,0.6)";
    setPreviousButton(button);

    const chart = echarts.getInstanceByDom(chartRef.current);
    const chart2 = echarts.getInstanceByDom(chart2Ref.current);
    chart.setOption({
      title: {
        text: "近七天" + type
      },
      xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        data: data[type],
        type: 'line'
      }]
    });
    var total = data[type].reduce((a, b) => a + b, 0);
    chart2.setOption({
      series: [{
        name: type,
        type: 'pie',
        data: [
          { value: total, name: type },
          { value: 100 - total, name: '其它' }
        ]
      }]
    });
  }

  useEffect(() => {
    // Initialize charts
    const chart = echarts.init(chartRef.current);
    const chart2 = echarts.init(chart2Ref.current);

    // Set chart options here...

    // Add window resize listener
    window.addEventListener('resize', () => { chart.resize(); chart2.resize(); });
    updateData('播放量');
    // Clear listener on component unmount
    return () => { window.removeEventListener('resize', () => { chart.resize(); chart2.resize(); }) };
    
  }, []);

  return (
    <div>
      <div id="buttons">
        <div className="rowStyle">
          <button id="播放量" className="buttonStyle" onClick={() => updateData('播放量')}>
            <div className="buttonContent">
              播放量
                <div className="buttonData">0.5万</div>
            </div>
          </button>
          {/* Add button for each data type */}
        </div>
      </div>
      <div id="chart" ref={chartRef} style={{ width: 750, height: 400, clear: "both" }}></div>
      <div id="chart2" ref={chart2Ref} style={{ width: 375, height: 400 }}></div>
    </div>
  );
}

export default ChartComponent;