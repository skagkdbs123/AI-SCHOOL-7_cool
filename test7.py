import streamlit as st
import streamlit.components.v1 as components


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

components.iframe("https://docs.streamlit.io/library/api-reference",width=800, height=1200, scrolling=True)
