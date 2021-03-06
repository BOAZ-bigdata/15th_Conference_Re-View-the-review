import streamlit as st

def page():
    global next
    st.title("โ๐ป๋ฆฌ๋ทฐ์ ์ฌ๋ฐ๊ฒฌ")
    c1, c2 = st.columns([2,4])
    with c1 : st.image('../images/team.png')
    with c2 : st.markdown("#### ํ์ ์๊ฐ")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown("**๋ฌธ์์ง**")
        st.image('../images/๋ฌธ์์ง.png')
        st.markdown(""" 
        *์๊ฐ๋ํ๊ต*  
        ๊ฒฝ์  / ๋น๋ฐ์ดํฐ
        """)
    with c2:
        st.markdown("**์ด์๋ฏผ**")
        st.image('../images/์ด์๋ฏผ.png')
        st.markdown(""" 
        *๊ฒฝํฌ๋ํ๊ต*   
        ์ํํธ์จ์ด์ตํฉ
        """) 
    with c3:
        st.markdown("**์ ์์ฐ**")
        st.image('../images/์ ์์ฐ.png')
        st.markdown(""" 
        *ํ์๋ํ๊ต*  
        ํ์ด๋ธ์ค๊ฒฝ์
        """)
    with c4:
        st.markdown("**์ ์น์ฐ**")
        st.image('../images/์ ์น์ฐ.png')
        st.markdown(""" 
        *์ฐ์ธ๋ํ๊ต ๋ํ์*  
        ์ ์ฐ์ธ์ดํ""")
    with c5:
        st.markdown("**ํฉ์๋ฆฐ**")
        st.image('../images/ํฉ์๋ฆฐ.png')
        st.markdown(""" 
        *์๋ช์ฌ์๋ํ๊ต*  
        ์๋ช์์คํ / ํต๊ณ
        """)

    st.markdown("""----
#### Review? Re-View!""")
    c1, c2 = st.columns([1, 5])
    with c1: pass
    with c2: st.image("../images/home1.png", caption = '์ถ์ฒ: ์ฌ๋ฆฌ๋ธ์', width = 500)
    st.markdown("""
###### ๋ฌผ๊ฑด ์ด ๋ ์ฌ๋ฌ๋ถ์ด ๋ณด๋ ๊ทธ ๋ฆฌ๋ทฐ์ **โญ๏ธ์ ์ฉ์ฑโญ๏ธ**, ์ ํฌ๊ฐ ์๋ ค๋๋ฆฝ๋๋ค! 

๐ ๋ฆฌ๋ทฐ ์ ์ฉ์ฑ ํ๋จ๋ถํฐ   
๐ ๊ตฐ์งํ๋ฅผ ํตํ ๋ํ ๋ฆฌ๋ทฐ ์ถ์ถ๊น์ง

*์ฐ๋ฆฌ ๊ฐ์ด Review๋ฅผ Re-Viewํด๋ด์โฅ๏ธ*
 """)
    # _, c2 = st.columns([16, 1])
    # with c2: next = st.button('Next')
    # return next