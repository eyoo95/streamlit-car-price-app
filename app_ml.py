import streamlit as st
import joblib

def run_ml():
    st.subheader('자동차 구매 가능 가격 예측')
    # 예측하기위해서 필요한 파일들을 불러와야 한다.
    # 인공지능파일과 스케일러 파일 2개

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')


# 사용자가 데이터 입력
# 얼마정도의 차를 구매할수 있는지?
# 여자, 나이 38, 연봉 78000, 카드빛 15000 자산 480000

# 성별, 나이 , 연봉, 카드빛, 자산

    gender = st.radio('성별을 고르세요', ['남자','여자'])
    if gender == '여자':
        gender = 0
    else:
        gender = 1
    st.number_input('나이를 입력하세요',0,120)
    st.number_input('연봉을 입력하세요',0)
    st.number_input('카드 빛을 입력하세요',0)
    st.number_input('자산을 입력하세요',0)

