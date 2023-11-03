import streamlit as st
import pyperclip as pc

# Constant
SAMPLE_TEXT_1 = "직원 정보\n\n"
SAMPLE_TEXT_2 = "\n이상의 정보를 바탕으로 직원 검색을 요청합니다."

# Sidebar
st.sidebar.title("Create Sample Text")
st.sidebar.text("아래의 정보를 입력하여\nSample Text를 작성할 수 있습니다.")

code = st.sidebar.number_input("사원번호", value=12345)
name = st.sidebar.text_input("이름", "enrai")
email = st.sidebar.text_input("Email", "test@sample.com")
gender = st.sidebar.radio(
    "Gender", ["Male", "Female", "Others"], key="Male", horizontal=True
)
lang_list = st.sidebar.multiselect(
    "Languages", ["한국어", "English", "日本語", "中国語"], ["한국어", "English"]
)

if st.sidebar.button("샘플 텍스트 작성"):
    lang = ", ".join(lang_list)
    print(lang)

    sample = SAMPLE_TEXT_1
    sample += f"사원번호 : {code}\n"
    sample += f"이름 : {name}\n"
    sample += f"Email : {email}\n"
    sample += f"성별 : {gender}\n"
    sample += f"사용 언어 : {lang}\n"
    sample += SAMPLE_TEXT_2

    pc.copy(sample)
    st.sidebar.success("샘플 텍스트를 생성하였습니다. Question 입력란에 Ctrl + v 를 사용해 붙여넣기 해 주세요.")


# Main Page
text_value = st.text_area("Question", "")
st.write(f"You wrote {len(text_value)} characters.")

# Submit
if st.button("Submit"):
    st.toast(text_value)
