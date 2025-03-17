#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Superstore Data Analysis", layout="wide")

# Title of the app
st.title("📊 Superstore Data Analysis")

# Load the data
@st.cache_data  # Cache the data to improve performance
def load_data():
    data = pd.read_csv('data/superstore_dataset2011-2015.csv', encoding='ISO-8859-1')
    return data

data = load_data()

# Display the dataset
st.subheader("📂 Dataset Preview")
st.write(data.head(5))

# Display basic information about the dataset
st.subheader("ℹ️ Dataset Information")
st.write(f"Shape of the dataset: {data.shape}")
st.write("Columns in the dataset:")
st.write(data.columns)

# Drop unnecessary columns
data = data.drop(['Row ID', 'Order ID', 'Customer ID', 'Postal Code'], axis=1)

# Hypothesis 1: Technology products have the highest profit margin
st.markdown("---")
st.subheader("🔍 Hypothesis 1: Technology products have the highest profit margin")
st.markdown("**Hypothesis:** Technology products have the highest profit margin compared to other product categories.")
cat_profit = data.groupby('Category')['Profit'].sum()
fig1, ax1 = plt.subplots(figsize=(4, 3))  # Very small figure size
cat_profit.plot(kind='bar', ax=ax1, color=['skyblue', 'lightgreen', 'salmon'])
ax1.set_title("Profit by Category", fontsize=10)
ax1.set_xlabel("Category", fontsize=8)
ax1.set_ylabel("Total Profit", fontsize=8)
st.pyplot(fig1)
st.success("**Conclusion:** The hypothesis is supported as technology products have the highest profit margin of the three categories. ✅")

# Hypothesis 2: The East region has the highest sales
st.markdown("---")
st.subheader("🔍 Hypothesis 2: The East region has the highest sales")
st.markdown("**Hypothesis:** The East region has the highest sales compared to other regions.")
reg_sales = data.groupby('Region')['Sales'].sum()
fig2, ax2 = plt.subplots(figsize=(4, 3))  # Very small figure size
reg_sales.plot(kind='bar', ax=ax2, color=['skyblue', 'lightgreen', 'salmon', 'orange'])
ax2.set_title('Total Sales by Region', fontsize=10)
ax2.set_xlabel('Region', fontsize=8)
ax2.set_ylabel('Sales', fontsize=8)
st.pyplot(fig2)
st.warning("**Conclusion:** The hypothesis is not supported as the central region has the highest sales. ❌")

# Hypothesis 3: Sales are higher during certain months of the year
st.markdown("---")
st.subheader("🔍 Hypothesis 3: Sales are higher during certain months of the year")
st.markdown("**Hypothesis:** Sales are higher during certain months of the year.")
data['Order Month'] = pd.DatetimeIndex(data['Order Date']).month
sales_by_month = data.groupby('Order Month')['Sales'].sum()
fig3, ax3 = plt.subplots(figsize=(4, 3))  # Very small figure size
sales_by_month.plot(kind='line', ax=ax3, color='skyblue', marker='o')
ax3.set_title('Total Sales by Month', fontsize=10)
ax3.set_xlabel('Month', fontsize=8)
ax3.set_ylabel('Sales', fontsize=8)
st.pyplot(fig3)
st.success("**Conclusion:** The hypothesis is supported as sales are higher during certain months of the year. ✅")

# Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products
st.markdown("---")
st.subheader("🔍 Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products")
st.markdown("**Hypothesis:** Orders with same-day shipping have the lowest rate of returned products.")
total_orders_by_shipping_mode = data.groupby('Ship Mode').size()
returned_orders_by_shipping_mode = data[data['Profit'] < 0].groupby('Ship Mode').size()
returned_per_by_shipping_mode = (returned_orders_by_shipping_mode / total_orders_by_shipping_mode) * 100
st.write("Return percentage by shipping mode:")
st.write(returned_per_by_shipping_mode)
fig4, ax4 = plt.subplots(figsize=(4, 3))  # Very small figure size
returned_per_by_shipping_mode.plot(kind="bar", ax=ax4, color=['skyblue', 'lightgreen', 'salmon', 'orange'])
ax4.set_title('Return % by Shipping Mode', fontsize=10)
ax4.set_xlabel('Shipping mode', fontsize=8)
ax4.set_ylabel('Return %', fontsize=8)
st.pyplot(fig4)
st.success("**Conclusion:** The hypothesis is supported as orders with same-day shipping have the lowest rate of returned products. ✅")

# Hypothesis 5: The company's profit is more on weekdays than on weekends
st.markdown("---")
st.subheader("🔍 Hypothesis 5: The company's profit is more on weekdays than on weekends")
st.markdown("**Hypothesis:** The company's profit is more on weekdays than on weekends.")
data['Order Day'] = pd.DatetimeIndex(data['Order Date']).day_name()
day_profit = data.groupby('Order Day')['Profit'].sum()
fig5, ax5 = plt.subplots(figsize=(4, 3))  # Very small figure size
day_profit.plot(kind='bar', ax=ax5, color=['skyblue', 'lightgreen', 'salmon', 'orange', 'purple', 'pink', 'cyan'])
ax5.set_title('Total Profit by Day of the Week', fontsize=10)
ax5.set_xlabel('Day of the Week', fontsize=8)
ax5.set_ylabel('Total Profit', fontsize=8)
st.pyplot(fig5)
st.success("**Conclusion:** The hypothesis is supported as the company's profit is higher on weekdays compared to weekends. ✅")