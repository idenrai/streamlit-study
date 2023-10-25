import streamlit as st
import plotly.express as px

# plotly_chart
# https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart

# st.plotly_chart(figure_or_data, use_container_width=False, theme="streamlit", **kwargs)
# - figure_or_data : plotly로 생성한 그림
# - theme : 테마 설정. 인자는 “streamlit” or None
# - use_container_width : 레이아웃으로 지정한 사이즈에 넣을 그림의 해상도 조절 여부

df = px.data.gapminder()

print(df)

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
# fig.show()

tab1, tab2 = st.tabs(["Streamlit theme(default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
