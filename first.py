"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': ["ㄱ","ㄴ","ㄷ","ㄹ"],
  'second column': [10, 20, 30, 40]
})

df

from PIL import Image
image = Image.open('pages/qwe.png')

st.image(image)