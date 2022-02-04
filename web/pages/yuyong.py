import streamlit as st
from . import models

def page():
    st.title("리뷰 유용성 평가")
    review = st.text_input("새로운 리뷰를 입력하세요.")
    _, c2 = st.columns([6, 1])
    with c2:
        rv_btn = st.button('평가하기')
    
    if rv_btn:
        result = models.kcelectra(review)
        st.write(result)
        if result['prediction'] == "유용 (useful)":
            st.markdown(f"이 리뷰는 {result['useful_percent'] * 100:.2f}%의 확률로 **유용**한 리뷰입니다.")
        else:
            st.markdown(f"이 리뷰는 {result['useless_percent'] * 100:.2f}%의 확률로 **유용하지 않은** 리뷰입니다.")
