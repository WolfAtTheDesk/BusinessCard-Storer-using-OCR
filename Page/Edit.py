"""
This file describes the streamlit page 'Edit'
Title:OCR
File Location: OCR/Pages/Edit.py
"""

#ui pkgs
import streamlit as st
import pandas as pd

from Backend import db_methods as db

def page():
    data = st.session_state.stored_data
    Flag = True
    st.image(data["image"],width=480)
    with st.form("Edit the data"):
        col1,col2,col3,col4 = st.columns([1,1,1,1],gap='large')

        with col1:
            Name    = st.text_input("Name", data['Name'][0])
            Company = st.text_input("Company", data['Company'][0])
        with col2:
            Designation = st.text_input("Designation", data['Designation'][0])
            Phone       = st.text_input("Phone", data['Phone'][0])
        with col3:
            Email   = st.text_input("Email", data['Email'][0])
            Website = st.text_input("Website", data['Website'][0])
        with col4:
            Address = st.text_input("Address", data['Address'][0])
            Other   = st.text_input("Other", data['Other'][0])

        if st.form_submit_button("Update the information"):
            data["Name"][0]        = Name
            data["Designation"][0] = Designation
            data["Company"][0]     = Company
            data["Phone"][0]       = Phone
            data["Email"][0]       = Email
            data["Website"][0]     = Website
            data["Address"][0]     = Address
            data["Other"][0]       = Other
            data["time"][0]        = data["time"][0]

            df = pd.DataFrame(data)
            st.session_state.stored_data = data
            Flag = False
            st.write("Data Updated, You can now upload Upload Tab")

    st.table(pd.DataFrame(data))
    if st.button("Upload to DB",disabled=Flag):
        db.insert_into_pdb(data)
