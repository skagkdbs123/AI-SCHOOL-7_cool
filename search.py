import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

mpg = sns.load_dataset("mpg")

st.sidebar.header('')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(mpg.model_year.min(),mpg.model_year.max())))
   )

