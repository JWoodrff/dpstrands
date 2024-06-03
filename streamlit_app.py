import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

"""
# strands editor
"""
circle1 = plt.Circle(( 0.5, 0.5 ), 0.2 )

st.button("Reset", type="primary")
if st.button("o"):
    st.write(circle1)
else:
    st.write("no")
