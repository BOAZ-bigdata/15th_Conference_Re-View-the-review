import streamlit as st

def page():
    global next
    st.title("✍🏻리뷰의 재발견")
    c1, c2 = st.columns([2,4])
    with c1 : st.image('../images/team.png')
    with c2 : st.markdown("#### 팀원 소개")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown("**문예진**")
        st.image('../images/문예진.png')
        st.markdown(""" 
        *서강대학교*  
        경제 / 빅데이터
        """)
    with c2:
        st.markdown("**이상민**")
        st.image('../images/이상민.png')
        st.markdown(""" 
        *경희대학교*   
        소프트웨어융합
        """) 
    with c3:
        st.markdown("**정수연**")
        st.image('../images/정수연.png')
        st.markdown(""" 
        *한양대학교*  
        파이낸스경영
        """)
    with c4:
        st.markdown("**정승연**")
        st.image('../images/정승연.png')
        st.markdown(""" 
        *연세대학교 대학원*  
        전산언어학""")
    with c5:
        st.markdown("**황의린**")
        st.image('../images/황의린.png')
        st.markdown(""" 
        *숙명여자대학교*  
        생명시스템 / 통계
        """)

    st.markdown("""----
#### Review? Re-View!""")
    c1, c2 = st.columns([1, 5])
    with c1: pass
    with c2: st.image("../images/home1.png", caption = '출처: 올리브영', width = 500)
    st.markdown("""
###### 물건 살 때 여러분이 보는 그 리뷰의 **⭐️유용성⭐️**, 저희가 알려드립니다! 

📌 리뷰 유용성 판단부터   
📌 군집화를 통한 대표 리뷰 추출까지

*우리 같이 Review를 Re-View해봐요♥️*
 """)
    # _, c2 = st.columns([16, 1])
    # with c2: next = st.button('Next')
    # return next