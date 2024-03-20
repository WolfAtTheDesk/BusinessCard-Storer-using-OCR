"""
This program is to extract data from business cards using Optical Character Recognition.
- Recognize elements in an uploaded image.
- It extract data from the Phonepe pulse Github repository.
- Transform it into a suitable format
- Creates a PostGres database
- Provides options for users to select different facts and figures to display on the dashboard.

Author: WolfAtTheDesk [https://www.github.com/WolfAtTheDesk]
Github: https://www.github.com/WolfAtTheDesk/
"""
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from Page import About
from Page import Extract
from Page import Edit
from Page import View

#------------------------------Streamlit Setup----------------------------------#
st.set_page_config(
                    layout="wide",
                    menu_items={'About' : "[My Github Link!](https://github.com/WolfAtTheDesk)"})

st.markdown('<style>' + open('Backend/style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    st.title(':violet[OCR]')
    tabs = on_hover_tabs(tabName=['About',
                                  'Extract',
                                  'Edit',
                                  'View'],
                         iconName=['info',
                                   'pageview',
                                   'edit',
                                   'preview'
                                   ],
                         default_choice = 0)

#-----------------------------Streamlit Pages-----------------------------------#
if tabs == 'About':
    About.page()
if tabs == 'Extract':
    Extract.page()
if tabs == 'Edit':
    Edit.page()
if tabs == 'View':
    View.page()
