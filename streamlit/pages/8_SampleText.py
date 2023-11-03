import streamlit as st
import pyperclip as pc

# Constant
SAMPLE_TEXT = "아래와 같이 입력해 주세요.\n - Name : idenrai\n - Email : test@sample.com\n - Tel: 00-1111-2222"

# Sidebar
st.sidebar.title("Sample Text")
st.sidebar.text("샘플 텍스트 버튼을 누르면\n샘플 텍스트를 취득할 수 있습니다.")

# Logic Tests
#
# Try 1. 텍스트를 그대로 Teax Area에 반영
# 결과 : 실패
# 이유(추정) : 버튼의 효과는 중복되지 않음. 샘플 텍스트 버튼으로 얻은 효과는 Submit에서 사라짐
# if st.sidebar.button("샘플 텍스트"):
#     text = SAMPLE_TEXT
# else:
#     text = ""

# text_value = st.text_area("Question", text)

# Try 2. Session State 이용
# 결과 : 실패
# 이유(추정) : 상기와 동일. 버튼의 효과는 중복되지 않음. 샘플 텍스트 버튼으로 얻은 효과는 Submit에서 사라짐
# st.session_state.text = ""

# if st.sidebar.button("샘플 텍스트"):
#     st.session_state.text = SAMPLE_TEXT

# text_value = st.text_area("Question", st.session_state["text"])
# st.write(f"You wrote {len(text_value)} characters.")

# Try 3. Text Area에의 반영을 포기하고 클립보드 복사를 이용
# 결과 : 성공
# 이유 : text area에 직접적인 영향을 미치지 않음. 복사 붙여넣기는 유저 입력으로 인식되어 버튼과 관계 없음
text_value = st.text_area("Question", "")

if st.sidebar.button("샘플 텍스트"):
    pc.copy(SAMPLE_TEXT)
    st.sidebar.success("샘플 텍스트를 복사하였습니다.\n Teax Area에 Ctrl + v 를 사용해 붙여넣기 해 주세요.")


# Main Page
st.write(f"You wrote {len(text_value)} characters.")

# Submit
if st.button("Submit"):
    st.text(text_value)
