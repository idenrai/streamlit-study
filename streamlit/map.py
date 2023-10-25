import streamlit as st
import numpy as np
import pandas as pd

# map
# https://docs.streamlit.io/library/api-reference/charts/st.map
# st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)

base_position = [35.542635, 139.445226]


map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position, columns=["lat", "lon"]
)

print(map_data)

st.code("st.map(map_data)")

st.subheader("Map")
st.map(map_data)
