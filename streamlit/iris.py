import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
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

st.subheader("Table")
st.table(df.head())

st.subheader("Data frame")
st.dataframe(df.head())


# Sidebar
st.sidebar.title("Iris Species")

# Selectbox
select_species = st.sidebar.selectbox("Species", ["setosa", "versicolor", "virginica"])

# df로부터 선택된 종류만 필터링되어 나오도록 일시적 데이터프레임을 생성
tmp_df = df[df["species"] == select_species]

st.subheader("Selected Species Data")
st.table(tmp_df.head())
