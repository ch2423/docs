import streamlit as st

row1, row2, row3 = st.rows(3)
row1.metric("Temperature", "70 °F", "1.2 °F")
row2.metric("Wind", "9 mph", "-8%")
row3.metric("Humidity", "86%", "4%")
