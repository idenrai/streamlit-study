import streamlit as st
import time

with st.spinner("Wait a minute..."):
    time.sleep(3)
    st.success("Done!")
    st.balloons()
