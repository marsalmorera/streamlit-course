import streamlit as st # type: ignore
from utils import load_data

############ PAGE SETUP ############ 
# This is that the page title that changes. 
st.set_page_config(
    page_title="Superhero APP",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

############ DATA LOAD ############ 

ev_sales_df = load.data()

############   ############ 

st.bar_chart(ev_sales_df, x='year', y='value')