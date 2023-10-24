import streamlit as st
from PIL import Image

# Streamlit의 기능 일부 테스트

# Text Element
# https://docs.streamlit.io/library/api-reference/text

# Title
st.title("The app title")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a text")

# Divider
st.divider()

# Layouts and containers
# https://docs.streamlit.io/library/api-reference/layout

# Sidebar
st.sidebar.title("Side Menu")
st.sidebar.checkbox("Sidebsr Checkbox")

# Column을 2:3분할
col1, col2 = st.columns([2, 3])

with col1:
    # col1에 담을 내용
    st.title("Column1")
with col2:
    # col2에 담을 내용
    st.title("Column2")
    st.checkbox("Col2 Checkbox")

# with구문 말고도 사용 가능
col1.subheader("Col1 Subheader")
col2.checkbox("Col2 Checkbox2")

st.divider()

# Tabs생성
tab1, tab2, tab3 = st.tabs(["Tab A", "Tab B", "Tab C"])

with tab1:
    st.write("Hello")
with tab2:
    st.write("World")

st.divider()

# 이미지 불러오기
yuna_img = Image.open("./image/yuna.jpeg")
tab3.image(yuna_img)
