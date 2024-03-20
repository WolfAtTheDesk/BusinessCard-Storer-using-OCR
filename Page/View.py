"""
This file describes the streamlit page 'View'
Title:OCR
File Location: OCR/Pages/View.py
"""

#ui pkgs
import streamlit as st
import pandas as pd

from Backend import db_methods as db

def page():
    st.header("Select Card to View:")

    #fetch a list of all the cards in the DB
    list = db.getlist()
    user_input = st.selectbox("Select channel",options= list)

    if user_input is not None:
        col1,col2 = st.columns(2,gap="large")
        with col1:
            #fetch the details of the card based on the users selection
            card = db.fetch_card(user_input)
            st.table(card)
        with col2:
            #preview the card
            st.image(card["image"])

        col1,col2, col3,col4 = st.columns(4,gap="small")

        with col2:
            #donwload the details of the card as a text file
            op = card.copy()
            op.pop("image")
            op.pop("id")
            st.download_button('Download the details', f"{op}", use_container_width = True)
        with col3:
            #download the card as an image
            with open(card["image"], "rb") as file:
                st.download_button('Download the card',
                                    data=file,
                                    file_name=card["image"],
                                    use_container_width = True)
        with col4:
            st.markdown("# ")
            st.markdown("# ")
            #delete the card from DB
            if st.button('Delete Card', type="primary",):
                status = db.delete_card(card)
                if status:
                    st.write(":red[The card is deleted]")
