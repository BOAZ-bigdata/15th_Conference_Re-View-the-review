import streamlit as st
import pandas as pd
import re

from . import models

DATA_URL = "./"

@st.cache()
def load_data():
    data = pd.read_csv(DATA_URL+"labeling_합본.csv")
    data = data[['평가', '상품명', '리뷰']]
    data['상품명'] = data['상품명'].apply(lambda x: re.sub(" ", " ", x))
    data['평가'] = data['평가'].apply(lambda x: round(x, 1))
    return data

DATA = load_data()
PRODUCT_NAME = DATA['상품명'].unique()
LINK10 = pd.read_csv("./files/review_link10.csv")

def page():
    global PRODUCT_NAME
    global LINK10

    st.title("올리브영 제품 리뷰 분석")

    st.subheader("분석 상품 목록")
    st.markdown('''현재 분석 가능한 상품 목록입니다.  원하는 상품을 선택해주세요!''')

    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0015/A00000015329101ko.jpg?l=ko", caption = PRODUCT_NAME[0])
        b1 = st.button("선택", key = 1)

    with c2:
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0015/A00000015525301ko.jpg?l=ko", caption = PRODUCT_NAME[1])
        st.markdown("""
          
           \n""")
        b2 = st.button("선택", key = 2)
    with c3:
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0014/A00000014557912ko.jpg?l=ko", caption = PRODUCT_NAME[2])
        b3 = st.button('선택', key = 3)
    with c4:
        st.image("https://image.oliveyoung.co.kr/uploads/images/goods/550/10/0000/0013/A00000013718012ko.jpg?l=ko", caption = PRODUCT_NAME[3])
        b4 = st.button('선택', key = 4)

    st.markdown("""
      
      """)
    
    if b1 == True:
        st.markdown(f"##### {PRODUCT_NAME[0]}")
        st.markdown("> **제품 리뷰 (유용한 순)**")
        st.write(pd.read_csv(f"./files/{PRODUCT_NAME[0]}.csv").drop(columns = 'Unnamed: 0').sort_values(by = 'yuyong', ascending= False))
 
        st.markdown('----')
        clst = st.radio("리뷰 군집화 결과", (
            "'토너, '피부', '사용', '진정', '어성', '제품', '화장', '아누아', '구매', '효과'",
            "'좁쌀', '여드름', '좁쌀 여드름', '구매', '효과', '피부', '진정', '스킨', '사용'",
            "'사용', '스킨', '자극', '피부', '구매', '만족', '화장', '제품', '느낌', '정착'"
        ))
        if clst == "'토너, '피부', '사용', '진정', '어성', '제품', '화장', '아누아', '구매', '효과'":
            st.markdown(f"""> **대표 리뷰** . 
            {LINK10.loc[1633, '리뷰']}""")
        if clst == "'좁쌀', '여드름', '좁쌀 여드름', '구매', '효과', '피부', '진정', '스킨', '사용'":
           st.markdown(f"""> **대표 리뷰**     
            {LINK10.loc[1645, '리뷰']}""")
        if clst == "'사용', '스킨', '자극', '피부', '구매', '만족', '화장', '제품', '느낌', '정착'":
            st.markdown(f"""> **대표 리뷰**   
            {LINK10.loc[1656, '리뷰']}""")

    
    elif b2:
        st.markdown(f"##### {PRODUCT_NAME[1]}")
        st.markdown("> **제품 리뷰 (유용한 순)**")
        st.write(pd.read_csv(f"./files/{PRODUCT_NAME[1]}.csv").drop(columns = 'Unnamed: 0').sort_values(by = 'yuyong', ascending= False))
 
        st.markdown('----')
        # clst = st.radio("리뷰 군집화 결과", (
        #     "'토너, '피부', '사용', '진정', '어성', '제품', '화장', '아누아', '구매', '효과'",
        #     "'좁쌀', '여드름', '좁쌀 여드름', '구매', '효과', '피부', '진정', '스킨', '사용'",
        #     "'사용', '스킨', '자극', '피부', '구매', '만족', '화장', '제품', '느낌', '정착'"
        # ))
        # if clst == "'토너, '피부', '사용', '진정', '어성', '제품', '화장', '아누아', '구매', '효과'":
        #     st.markdown(f"""> **대표 리뷰**   
        #     {LINK10.loc[1633, '리뷰']}""")
        # elif clst == "'좁쌀', '여드름', '좁쌀 여드름', '구매', '효과', '피부', '진정', '스킨', '사용'":
        #    st.markdown(f"""> **대표 리뷰**   
        #     {LINK10.loc[1645, '리뷰']}""")
        # else:
        #     st.markdown(f"""> **대표 리뷰**   
        #     {LINK10.loc[1656, '리뷰']}""")
