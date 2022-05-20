import streamlit as st
import pandas as pd
import seaborn as sb

def run_eda():
    st.subheader('데이터 분석')
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    # 라디오 버튼을 이용하여 데이터프레임과 통계치를 선택래서 볼수있게 한다.

    radio_menu = ['데이터프레임','통계치']
    selected = st.radio('보고 싶은 데이터프레임을 선택하세요', radio_menu)

    if selected == radio_menu[0]:
        st.dataframe(df)

    if selected == radio_menu[1]:
        st.dataframe(df.describe())
