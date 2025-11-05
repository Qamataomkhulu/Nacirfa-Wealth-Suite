"""
app.py
------
Streamlit dashboard for Nacirfa Wealth Suite.
Displays charts and basic metrics.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Nacirfa Wealth Suite", layout="wide")

st.title("💹 Nacirfa Wealth Suite")
st.markdown("Empowering African investors through open tools and data.")

# Sidebar
st.sidebar.header("Select Data")
available_files = [f for f in os.listdir("datahub/output") if f.endswith(".csv")]
selected_file = st.sidebar.selectbox("Choose a dataset", available_files)

if selected_file:
    df = pd.read_csv(f"datahub/output/{selected_file}")
    st.subheader(f"📊 {selected_file.replace('_', '/').replace('.csv','')} Chart")
    fig = px.line(df, x='timestamp', y='close', title="Price Over Time")
    st.plotly_chart(fig, use_container_width=True)

    st.write("### Descriptive Stats")
    st.write(df.describe())

    st.sidebar.write("Data preview:")
    st.sidebar.dataframe(df.tail())

