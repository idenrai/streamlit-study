import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import streamlit as st

iris_dataset = load_iris()

df = pd.DataFrame(data=iris_dataset.data, columns=iris_dataset.feature_names)
df.columns = [col_name.split(" (cm)")[0] for col_name in df.columns]
df["species"] = iris_dataset.target

species_dict = {0: "setosa", 1: "versicolor", 2: "virginica"}


def mapp_species(x):
    return species_dict[x]


df["species"] = df["species"].apply(mapp_species)
print(df)

st.subheader("Selected Species Data")

# Sidebar
st.sidebar.title("Iris Species")

# Multiselect
select_species = st.sidebar.multiselect(
    "Species", ["setosa", "versicolor", "virginica"]
)

# Radio
radio_select = st.sidebar.radio(
    "Key Column",
    ["sepal length", "sepal width", "petal length", "petal width"],
    horizontal=True,
)

# Slider
# 시작값 0, 종료값 10, 기본 선택값 2.5~7.5
slider_range = st.sidebar.slider("Key Column Range", 0.0, 10.0, (2.5, 7.5))

# Button
filter_button = st.sidebar.button("적용")

# 버튼을 누르면 위의 필터를 적용하도록 한다
if filter_button:
    # df로부터 선택된 종류만 필터링되어 나오도록 일시적 데이터프레임을 생성
    # Multiselect
    tmp_df = df[df["species"].isin(select_species)]

    # Slider & Radio
    tmp_df = tmp_df[
        (tmp_df[radio_select] >= slider_range[0])
        & (tmp_df[radio_select] <= slider_range[1])
    ]

    # 데이터 수
    st.write(str(len(tmp_df)) + " / " + str(len(df)))

    # 테이블 표시
    st.table(tmp_df)

    # 성공 메시지
    st.sidebar.success("Filter Applied")
    st.balloons()
