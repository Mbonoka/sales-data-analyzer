import streamlit as st
import pandas as pd
from src.clean_data import clean_data
import matplotlib.pyplot as plt

st.title("📊 Sales Data Dashboard")

# Load data
df = clean_data("data/sales.csv")

# ✅ FILTER GOES HERE
product = st.selectbox("Select Product", ["All"] + list(df['product'].unique()))

if product != "All":
    df = df[df['product'] == product]

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Total revenue
total_revenue = df['revenue'].sum()
st.metric("Total Revenue", f"${total_revenue}")

# Revenue by product
revenue_by_product = df.groupby('product')['revenue'].sum()

st.subheader("Revenue by Product")
st.bar_chart(revenue_by_product)

# Matplotlib chart
fig, ax = plt.subplots()
revenue_by_product.plot(kind='bar', ax=ax)
ax.set_title("Revenue by Product")
st.pyplot(fig)