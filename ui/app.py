import streamlit as st
from pipeline.run_pipeline import run_full_pipeline

st.title("AI Clerking Assistant")

image = st.file_uploader("Upload clerking note", type=["jpg","png"])

if image:
    with open("temp.jpg", "wb") as f:
        f.write(image.read())

    draft = run_full_pipeline("temp.jpg")

    st.text_area("Drafted Note", draft, height=300)
