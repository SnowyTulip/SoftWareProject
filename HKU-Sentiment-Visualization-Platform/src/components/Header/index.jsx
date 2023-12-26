import React from 'react';
import USTC_logo from '../../assets/USTC.png'
import './Header.css'; // 导入样式文件

const Header = () => {
  return (
    <header>
      <div className="logo">
        {/* 在这里放置你的 logo */}
        <img src={USTC_logo} alt="Logo" />
      </div>
      <div className="title">
        {/* 在这里展示项目的标题 */}
        <h1>USTC Software Engineering Self-Publishing Analytics</h1>
      </div>
      <div className="search-box">
        {/* 在这里放置搜索框 */}
        <input type="text" placeholder="Search by keywords, e.g. USTC" />
      </div>
      <div className="about">
        {/* 在这里放置关于链接或按钮 */}
        <a href="/about">Models</a>
      </div>
      <div className="about">
        {/* 在这里放置关于链接或按钮 */}
        <a href="/about">Dataset</a>
      </div>
      <div className="about">
        {/* 在这里放置关于链接或按钮 */}
        <a href="/about">About</a>
      </div>
    </header>
  );
};

export default Header;
