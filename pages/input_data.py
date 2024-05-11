import streamlit as st
from pages.data import *
import pandas as pd


st.set_page_config(
    page_title="GeoGenix",
    page_icon="🌍",
    initial_sidebar_state="collapsed"
)




st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.write("# 🌍 GeoGenix")
st.write("## Profile Metadata")
st.write("Name: ",SurveyName)
st.write("Longitude: ",Longitude,"    Lattitude: ",Lattitude,"Elevation :",Elevation)
st.write("### Electrode Position")
st.write("P1: ",p1) 
st.write(" P2: ",p2)
st.divider()


rrd1 = st.number_input("Reading 1",key='rrd1')
rrd2 = st.number_input("Reading 2",key='rrd2')

def clear_all_text_inputs():
    add_data(rrd1,rrd2)
    #st.write(dataset)
    st.session_state['rrd1'] = 0  # Clear inphase text input
    # Clear other text input elements:
    st.session_state['rrd2'] = 0  # Clear outphase number input
st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    insert_button = st.button("Add Dataset", type='primary', key='insert_button', on_click=clear_all_text_inputs)
with col2:
    if (st.button("Datasheet View")):
        st.switch_page("pages/export_data.py")


