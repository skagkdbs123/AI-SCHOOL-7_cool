import streamlit as st
import streamlit.components.v1 as components


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
