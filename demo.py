from pymongo import MongoClient
import pymongo
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb://localhost:27017"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
mydb = client["dataLogging"]
mycol = mydb["dataLogging"]

def main_page():
    st.sidebar.markdown("ภาพรวม")
    m = folium.Map(location=[13.677939, 100.561034],zoom_start=13)
    # station IN01
    tooltip = "IN01 สถานีวัดกองแก้ว"
    IN01_detail="วันที่: 14/4/2020 11:00 ความเค็ม: 11.91 ppt"
    folium.Marker(
            [13.6852 ,100.5625], popup=folium.Popup(IN01_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station IN02
    tooltip = "IN02 สถานีสวนศรีนครเขื่อนขันธ์"
    IN02_detail="วันที่: 1/3/2020 1:00 ความเค็ม: 5.95 ppt"
    folium.Marker(
            [13.6965 ,100.5634], popup=folium.Popup(IN02_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station IN04
    tooltip = "IN04 สถานีคลองลัดบางยอ"
    IN04_detail="วันที่: 1/3/2020 0:00 ความเค็ม: 15.19 ppt"
    folium.Marker(
            [13.6649 ,100.5650], popup=folium.Popup(IN04_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station OT01
    tooltip = "OT01 สถานีประตูระบายน้ำคลองตาสัก"
    OT01_detail="วันที่: 19/3/2020 1:00 ความเค็ม: 3.47 ppt"
    folium.Marker(
            [13.6681 ,100.5742], popup=folium.Popup(OT01_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station OT02
    tooltip = "OT02 สถานีประตูระบายน้ำคลองยายบ่าย"
    OT02_detail="วันที่: 19/3/2020 0:00 ความเค็ม: 3.98 ppt"
    folium.Marker(
            [13.6897 ,100.5549], popup=folium.Popup(OT02_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station OT03
    tooltip = "OT03 สถานีประตูระบายน้ำคลองบางน้ำผึ้งนอก"
    OT03_detail="วันที่: 19/3/2020 0:00 ความเค็ม: 1.31 ppt"
    folium.Marker(
            [13.6819,100.5863 ], popup=folium.Popup(OT03_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station OT04
    tooltip = "OT04 สถานีประตูระบายน้ำคลองยายบ่าย"
    OT04_detail="วันที่: 19/3/2020 0:00 ความเค็ม: 10.13 ppt"
    folium.Marker(
            [13.6603,100.5520 ], popup=folium.Popup(OT04_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
        # station OT05
    tooltip = "OT05 สถานีประตูระบายน้ำคลองแพ"
    OT05_detail="วันที่: 3/3/2020 1:00 ความเค็ม: 9.18 ppt"
    folium.Marker(
            [13.6950,100.5822 ], popup=folium.Popup(OT05_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
            # call to render Folium map in Streamlit
    folium_static(m)

    cols = st.columns(4)
    cols[0].write('สถานี')
    cols[0].write('IN01')
    cols[0].write('IN02')
    cols[0].write('IN04')
    cols[0].write('OT01')
    cols[0].write('OT02')
    cols[0].write('OT03')
    cols[0].write('OT04')
    cols[0].write('OT05')
    cols[1].write('ความเค็ม (ppt)')
    cols[1].write('11.91')
    cols[1].write('5.95')
    cols[1].write('15.19')
    cols[1].write('3.47')
    cols[1].write('3.98')
    cols[1].write('1.31')
    cols[1].write('10.13')
    cols[1].write('9.18')
    cols[2].write("ระดับน้ำ")
    cols[2].write('-1.29')
    cols[2].write('-1.81')
    cols[2].write('-1.25')
    cols[2].write('-0.32')
    cols[2].write('-0.14')
    cols[2].write('-0.48')
    cols[2].write('-0.52')
    cols[2].write('-1.00')
    cols[3].write("สถานะ")
    for i in range(1, 9):
        cols[3].write("online")

def page2():
    st.sidebar.markdown("สถานีวัดกองแก้ว")
    m = folium.Map(location=[13.6852 ,100.5625],zoom_start=13)
    # station IN01
    tooltip = "IN01 สถานีวัดกองแก้ว"
    IN01_detail="วันที่: 14/4/2020 11:00 ความเค็ม: 11.91 ppt"
    folium.Marker(
            [13.6852 ,100.5625], popup=folium.Popup(IN01_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
    folium_static(m)

    df = pd.read_csv("./in01.csv")
    mean_salinity=df['Salinity'].mean()
    mean_level=df['Level'].mean()

    st.markdown("<h1 style='text-align: center;'>IN01 สถานีวัดกองแก้ว</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("ระดับน้ำเฉลี่ย", str(mean_level))
    col2.metric("ความเค็มเฉลี่ย", str(mean_salinity))
    col3.metric("สถานะ", "Online")

    st.dataframe(df,1000,730)

    df=df.rename(columns=df["Date"]).set_index(df["Date"])
    st.line_chart(df["Salinity"])

def page3():
    st.sidebar.markdown("สถานีสวนศรีนครเขื่อนขันธ์")
    m = folium.Map(location=[13.6965 ,100.5634],zoom_start=13)
    # station IN02
    tooltip = "IN02 สถานีสวนศรีนครเขื่อนขันธ์"
    IN01_detail="วันที่: 1/3/2020 1:00 ความเค็ม: 5.95 ppt"
    folium.Marker(
        [13.6965 ,100.5634], popup=folium.Popup(IN01_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
    folium_static(m)

    df = pd.read_csv("./in02.csv")
    mean_salinity=df['Salinity'].mean()
    mean_level=df['Level'].mean()

    st.markdown("<h1 style='text-align: center;'>IN02 สถานีสวนศรีนครเขื่อนขันธ์</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("ระดับน้ำเฉลี่ย", str(mean_level))
    col2.metric("ความเค็มเฉลี่ย", str(mean_salinity))
    col3.metric("สถานะ", "Online")

    st.dataframe(df,1000,730)

    df=df.rename(columns=df["Date"]).set_index(df["Date"])
    st.line_chart(df["Salinity"])

def page4():
    st.sidebar.markdown("สถานีคลองลัดบางยอ")
    m = folium.Map(location=[13.6649 ,100.5650],zoom_start=13)
    # station IN04
    tooltip = "IN04 สถานีคลองลัดบางยอ"
    IN01_detail="วันที่: 1/3/2020 0:00 ความเค็ม: 15.19 ppt"
    folium.Marker(
        [13.6649 ,100.5650], popup=folium.Popup(IN01_detail,max_width=300,min_width=200), tooltip=tooltip
        ).add_to(m)
    folium_static(m)

    df = pd.read_csv("./in04.csv")
    mean_salinity=df['Salinity'].mean()
    mean_level=df['Level'].mean()

    st.markdown("<h1 style='text-align: center;'>IN04 สถานีคลองลัดบางยอ</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("ระดับน้ำเฉลี่ย", str(mean_level))
    col2.metric("ความเค็มเฉลี่ย", str(mean_salinity))
    col3.metric("สถานะ", "Online")

    st.dataframe(df,1000,730)

    df=df.rename(columns=df["Date"]).set_index(df["Date"])
    st.line_chart(df["Salinity"])

def page5():
    st.markdown("OT01")
    st.sidebar.markdown("สถานีประตูระบายน้ำคลองตาสัก")

def page6():
    st.markdown("OT02")
    st.sidebar.markdown("สถานีประตูระบายน้ำคลองยายบ่าย")

def page7():
    st.markdown("OT03")
    st.sidebar.markdown("สถานีประตูระบายน้ำคลองบางน้ำผึ้งนอก")

def page8():
    st.markdown("OT04")
    st.sidebar.markdown("สถานีประตูระบายน้ำคลองยายบ่าย")

def page9():
    st.markdown("OT05")
    st.sidebar.markdown("สถานีประตูระบายน้ำคลองแพ")

page_names_to_funcs = {
    "หน้าหลัก": main_page,
    "IN01": page2,
    "IN02": page3,
    "IN04": page4,
    "OT01": page5,
    "OT02": page6,
    "OT03": page7,
    "OT04": page8,
    "OT05": page9,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()