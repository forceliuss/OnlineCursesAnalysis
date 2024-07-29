import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#Import data
df = pd.read_csv('../data/raw/udemy_courses.csv')

#Page Configuration
st.set_page_config(
    page_title="Udemy Curses",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")