import streamlit as st
import numpy as np
import pandas as pd

# map
# https://docs.streamlit.io/library/api-reference/charts/st.map
# st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)

st.session_state.lat = st.sidebar.number_input(
    label="lat",
    step=0.01,
    value=35.542635,
    format="%f",
)
st.session_state.lon = st.sidebar.number_input(
    label="lon",
    step=0.01,
    value=139.445226,
    format="%f",
)

base_position = [st.session_state["lat"], st.session_state["lon"]]

map_data = pd.DataFrame(
    [base_position],
    columns=["lat", "lon"],
)

print(map_data)

st.code("st.map(map_data)")

st.subheader("Map")

st.map(map_data)
