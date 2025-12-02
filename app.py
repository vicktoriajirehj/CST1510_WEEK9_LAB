import streamlit as st
import pandas as pd
st.title("1. Basic Page elements")
st.header("Header and text")
st.subheader("This is a Subheader")
st.caption("Small, grey captoin text")
st.write("'st.write' is very flexible - you can pass string, numbers, dataframes, etc.")
st.text("Plain fixed-width text for code-like things")
st.markdown("Youi can use **markdown** here, including **italic** and 'code'.")
st.divider()
st.header("Display data")
df = pd.DataFrame({
    "name": ["alice", "bob", "charlie"],
    "age": [10, 20, 30]
})
st.write("Here is a small dataframe: ")
st.dataframe(df)

st.divider()

st.header("Images")
st.write("You can show images from url or local file")
st.image(
    "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
caption="Streamlit logo",)
