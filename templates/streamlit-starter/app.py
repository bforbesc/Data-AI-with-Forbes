"""Teaching template: question -> table -> filter -> chart -> check.

Run from this folder with: python -m streamlit run app.py
The records are fictional; no upload, secret key, or external data is needed.
"""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="My first data app", page_icon="📊")
st.title("📊 My first data app")
st.write("Question: how does the value of fictional orders compare by category?")
st.caption("A teaching example from Data & AI with Forbes. All records are invented.")

# 1. DATA: each row is one order; the amount is the whole order's value.
orders = pd.DataFrame([
    {"category": "Books", "order_value_eur": 10},
    {"category": "Books", "order_value_eur": 20},
    {"category": "Books", "order_value_eur": 30},
    {"category": "Games", "order_value_eur": 25},
    {"category": "Games", "order_value_eur": 35},
    {"category": "Games", "order_value_eur": 40},
])

# 2. INPUT: a web control stores the visitor's choice.
category = st.selectbox("Choose a category", ["All", "Books", "Games"])

# 3. TRANSFORM: select rows, then summarize the matching values.
filtered = orders if category == "All" else orders[orders["category"] == category]
totals = filtered.groupby("category", as_index=False)["order_value_eur"].sum()

# 4. OUTPUT: show the numbers behind the picture as well as the picture.
st.metric("Total order value (EUR)", f"{filtered['order_value_eur'].sum():.0f}")
st.dataframe(filtered, hide_index=True)
figure = px.bar(
    totals, x="category", y="order_value_eur",
    labels={"category": "Category", "order_value_eur": "Total order value (EUR)"},
    title="Total order value by category",
)
st.plotly_chart(figure)
st.info("Check: All = EUR 160; Books = EUR 60; Games = EUR 100.")
st.markdown("[Explore more lessons](https://github.com/bforbesc/Data-AI-with-Forbes)")
