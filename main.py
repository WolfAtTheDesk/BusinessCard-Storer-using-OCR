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

from Page import Extract
from Page import Edit
from Page import Upload

#------------------------------Streamlit Setup----------------------------------#
st.set_page_config(
                    layout="wide",
                    menu_items={'About' : "[My Github Link!](https://github.com/WolfAtTheDesk)"})

st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    st.title('Test')
    tabs = on_hover_tabs(tabName=['About',
                                  'Extract',
                                  'Edit',
                                  'Upload',
                                  'View'],
                         iconName=['info',
                                   'browser_updated',
                                   'analytics',
                                   'analytics'
                                   ],
                         default_choice=0)

#-----------------------------Streamlit Pages-----------------------------------#
if tabs == 'About':
    st.write("OMain page")
if tabs == 'Extract':
    Extract.page()
if tabs == 'Edit':
    Edit.page()
if tabs == 'Upload':
    Upload.page()
# if tabs == 'View':
#     View.page()
