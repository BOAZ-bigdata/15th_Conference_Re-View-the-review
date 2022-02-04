import streamlit as st
from home import *

def one_product(i):
    st.title(PRODUCT_NAME[i])
    # 새로운 리뷰 평가
    st.subheader("리뷰 유용성 평가")

    
    c1, c2 = st.columns(2)
    # 유용성 판단
    with c1:
        st.markdown('#### 리뷰 필터링')
        btn = st.button('유용한 순')
        df = DATA[DATA['상품명'] == PRODUCT_NAME[i]][['리뷰', '평균']]
        df['유용성'] = (df['평균'] / 5 * 100).astype('str') + '%'
        if btn : 
            # st.write(df.sort_values(by = '유용성'))
            # st.write(df)
            st.dataframe(df.sort_values(by = '평균', ascending=False)[['리뷰', '유용성']])
        else:
            st.dataframe(df[['리뷰', '유용성']])
            # st.set_option('wideMode', True)
            # st.write(df)
    
    # with c2:
        # (임시) WordCloud
        

    # 군집화 결과
    st.markdown('#### 군집화 결과')
    cluster = st.radio('분류된 군집을 선택하세요', ('A : 패드, 좁쌀, 수분', 
                                              'B : 끈적, 건성, 흡수', 
                                              'C : 따가움, 염증, 피부'))
    if cluster == 'A : 패드, 좁쌀, 수분':
        st.dataframe(df[df['평균'].astype('float') >= 3]['리뷰'].head(5))
    else:
        pass

