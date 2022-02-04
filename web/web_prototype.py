import streamlit as st

import pandas as pd
from PIL import Image
import pickle
import os
import re

# Customize
from pages import home, models, product_page, yuyong
from pages.home import *
from pages.product_page import *




if __name__ == "__main__":
    pages = st.sidebar.selectbox('Navigation', ('Home', '리뷰 유용성 평가', '제품 리뷰 분석'))
    if pages == 'Home': home.page()
    if pages == '리뷰 유용성 평가': yuyong.page()
    if pages == '제품 리뷰 분석' : product_page.page()