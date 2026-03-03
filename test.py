import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

# ================= 页面基础设置 =================
# 设置网页标题、图标和宽屏模式，默认深色主题更有科技感
st.set_page_config(
    page_title="AI时代的国土数据保卫战",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= 顶部：引言与痛点 =================
st.title("🛡️ 你随手拍的风景，可能正在出卖国家坐标？")
st.markdown("### —— 警惕AI开源情报（OSINT）对国土安全的威胁")

# 警示框
st.error(
    "⚠️ **核心痛点**：作为大学生，你以为发在朋友圈的只是一张‘打卡照’，但在敌对势力的 AI 大模型眼里，这是精准的地理坐标、三维地形和高价值的军事情报！")

st.markdown("---")

# ================= 第一板块：真实案例警示 =================
st.header("📍 那些不知不觉的“泄密者”")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    🚨 **案例一：‘高薪测绘兼职’陷阱**  
    某高校大学生小李，在网上接单了一份“街景拍摄”兼职。他使用特定APP在某港口、重点科研所周边打卡拍照。最终查明，该APP后台将带有高精度GPS数据的照片实时传给了境外情报机构。小李因涉嫌为境外刺探、非法提供国家秘密罪被依法审查。
    """)

with col2:
    st.info("""
    🚨 **案例二：运动APP轨迹泄露军事基地**  
    某外军秘密基地曾因士兵使用运动手环跑步打卡，其上传至公开平台的GPS轨迹被AI大数据爬虫抓取。通过热力图叠加分析，该秘密基地的精确轮廓、内部建筑布局甚至巡逻路线被全球网民一览无余。
    """)

st.markdown("---")

# ================= 第二板块：专业科普（体现你们的AI专业特色） =================
st.header("🤖 硬核解密：AI是如何“拼凑”出机密地图的？")
st.markdown("敌对势力无需派间谍潜入，只需写几行爬虫代码，结合以下 **人工智能与智能科学** 技术，就能完成情报窃取：")

tab1, tab2, tab3 = st.tabs(["🧩 第一步：EXIF数据挖掘", "👁️ 第二步：CV目标检测", "🗺️ 第三步：SLAM与3D重建"])

with tab1:
    st.subheader("EXIF：藏在照片里的‘身份证’")
    st.write(
        "每一张用手机原相机拍摄的照片，都自带EXIF（可交换图像文件格式）数据。即便你没有拍到地标建筑，敌对势力用简单代码就能提取出你拍照时的**精确经纬度、海拔高度、拍摄时间和手机型号**。")
    st.code("纬度: 39° 54' 27\" N\n经度: 116° 23' 17\" E\n设备: iPhone 14 Pro", language="text")

with tab2:
    st.subheader("计算机视觉（Computer Vision）：从背景里找雷达")
    st.write(
        "当你拍下一张风景照，人眼看的是风景，但 **目标检测算法（如YOLOv8）** 会在毫秒级别内扫描照片的每一个像素。它可以自动识别出远处模糊的军车型号、雷达天线样式，甚至通过分析植物特征判断当季的气候条件。")

with tab3:
    st.subheader("NeRF与SLAM：碎照片变3D军事沙盘")
    st.write(
        "这是最可怕的一步。只要抓取到成百上千名游客在同一地点不同角度拍的照片，AI就能利用**神经辐射场（NeRF）或多视图几何技术**，全自动生成该区域的高精度三维模型，也就是‘数字克隆’。")

st.markdown("---")

# ================= 第三板块：数据可视化（高分核心！） =================
st.header("📊 数据洞察：数据泄露的隐秘角落")
st.write("下面我们通过数据可视化，直观感受涉军、涉密地理信息泄露的风险。")

col3, col4 = st.columns(2)

with col3:
    # 制作一个模拟的条形图：近年来利用AI和开源情报窃取我国数据的案件趋势
    # (注：此处为模拟展示数据，请在答辩时向老师说明这是用于演示图表功能的模拟数据)
    trend_data = pd.DataFrame({
        "年份": ["2019", "2020", "2021", "2022", "2023"],
        "因网络分享导致的地理泄密风险指数": [120, 180, 250, 410, 680]
    })
    fig_bar = px.bar(trend_data, x="年份", y="因网络分享导致的地理泄密风险指数",
                     title="📈 近5年开源网络地理情报泄露风险激增趋势",
                     color="因网络分享导致的地理泄密风险指数",
                     color_continuous_scale="Reds")
    st.plotly_chart(fig_bar, use_container_width=True)

with col4:
    # 制作一个极具“智能科学专业”逼格的 3D 散点图，模拟 AI 点云重建效果
    st.markdown("#### 🌐 AI多视图三维重建模拟演示(Point Cloud)")
    st.caption("拖动鼠标可以旋转查看。这模拟了AI如何用网民零散的2D照片，生成立体的军港地形模型。")

    # 生成模拟的3D坐标点
    np.random.seed(42)
    x = np.random.standard_normal(500)
    y = np.random.standard_normal(500)
    z = np.exp(-(x ** 2 + y ** 2) / 2) * 10  # 模拟一个小山丘/雷达罩的形状

    fig_3d = px.scatter_3d(x=x, y=y, z=z, color=z,
                           color_continuous_scale="Viridis",
                           opacity=0.7)
    fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig_3d, use_container_width=True)

st.markdown("---")

# ================= 第四板块：防范互动 =================
st.header("✅ 大学生防范指南：从我做起，守护国土坐标")
st.write("请自查并勾选以下防范措施（完成打卡有惊喜）：")

check1 = st.checkbox("📱 我已关闭手机相机默认的‘记录地理位置’权限。")
check2 = st.checkbox("🚫 我承诺：绝不在军事管理区、国防军工单位、边境线附近拍照。")
check3 = st.checkbox("🙅‍♂️ 我承诺：发社交媒体前，尽量发送抹除EXIF信息的‘压缩图’，不随意发送‘原图’。")
check4 = st.checkbox("🕵️‍♀️ 我承诺：警惕网络上‘采集街景’、‘道路测绘’等不明高薪兼职。")

if check1 and check2 and check3 and check4:
    st.success("🎉 恭喜！你已具备优秀的国土安全保密意识！国家安全，你我共筑！")
    st.balloons()  # 触发气球特效

st.markdown("---")

# ================= 底部：作业硬性要求（必须保留） =================
st.markdown("### 📚 信息来源与参考文献")
st.caption("1. 《中华人民共和国国家安全法》第七十七条：公民和组织应当履行维护国家安全的义务。")
st.caption("2. 《中华人民共和国测绘法》：未经批准，擅自从事测绘活动的，依法追究法律责任。")
st.caption("3. 国家安全部微信公众号文章：《警惕！你随手拍的风景，可能出卖国家秘密》（模拟新闻来源，请替换真实链接）")

st.markdown("<br>", unsafe_allow_html=True)

st.info(
    "👨‍💻 **本网页为《XXX课程》期中科普作业**  \n**所属专业**：人工智能/智能科学与技术  \n**小组成员**：[组长你的名字] (内容统筹/汇报)、[组员甲名字] (文献与数据)、[组员乙名字] (前端与可视化)")