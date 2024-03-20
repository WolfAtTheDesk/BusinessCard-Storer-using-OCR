"""
This file describes the streamlit page 'About'
Title:OCR
File Location: OCR/Pages/About.py
"""

#ui pkgs
import streamlit as st
from Backend import misc

def page():
    st.title(":rainbow[Business Card details Extarctor!]")
    st.divider()

    st.header(":red[What is this?]")
    st.markdown(misc.about_text)

    st.header(":green[How to use this tool]")
    st.write(misc.how_to_text)

    st.header(":violet[How it works:]")
    st.write(misc.how_it_works)
