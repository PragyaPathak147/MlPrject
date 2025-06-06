import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.title ("Song Recommender")
with open("movies.pkl",'rb') as f:
    movies=pickle.load(f)

option = st.selectbox(
    "Choose a category:",
     movies['title'].values()
)

# Display the selected option
st.write("You selected:", option)