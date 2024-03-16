"""
This file describes the streamlit page 'Upload'
Title:OCR
File Location: OCR/Pages/Upload.py
"""

#ui pkgs
import streamlit as st
import pandas as pd
from Backend import db_methods as db

def page():
    data = st.session_state.stored_data
    st.table(pd.DataFrame(data))
    if st.button("Upload to DB"):
        db.insert_into_pdb(data)
