"""
Title:OCR
This file describes the streamlit page 'Extract'
File Location: OCR/Pages/Extract.py
"""

#ui pkgs
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

import OcrMethods as ocr
import mongoDB_methods as mongo
import pandas as pd



def page():
    col1,col2,col3 = st.columns([1,3,1],gap='large')
    with col2:
        st.markdown("### Upload a Business Card")
        upload = st.file_uploader("Upload a business card",
                                        label_visibility="collapsed",
                                        type=["png","jpeg","jpg"]
                                        )

    if upload is not None:
        #save the uploaded image into folder OCR/Cards/
        ocr.save_card(upload)

        col1,col2 = st.columns(2,gap="large")
        with col1:
            #preview
            st.markdown("## :violet[Uploaded Card Preview:]")
            st.image(upload)

        with col2:
            with st.spinner("## :orange[Please wait processing image...]"):
                st.set_option('deprecation.showPyplotGlobalUse', False)

                #detected text on image
                image,words = ocr.ocr_run(upload)
                st.markdown("## :green[Recognized Data]")
                st.pyplot(ocr.image_preview(image,words))

        #extract words from Recognized data
        result=[]
        for r in words:
            result.append(r[1])

        data = ocr.get_data(result)
        data.update({"image" : ocr.img_to_pix(upload)})

        df = pd.DataFrame(data)
        st.write(df)
        st.session_state['stored_data'] = data
