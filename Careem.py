import pandas as pd
import numpy as np 
import streamlit as st
import seaborn as sns
import plotly.express as px



df = pd.read_excel('Careem_Data.xlsx')

df.info()


st.title("CAREEM PAKISTAN DATA ANALYSIS")
st.subheader("In this data analysis, we'll delve into the intricate details of cars, service areas, booking types, car types, discounts, and payment methods, providing a comprehensive view of my insights.")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("### Car types")

fig = px.treemap(df, path=['Car Type', 'Car Model'])
st.write("Car types along with their respective car names in Careem.")
fig.update_layout(width=900, height=800)
st.plotly_chart(fig)


st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("### Booking Type by Service Area")

st.bar_chart(df.groupby(['Service Area', 'Booking Type']).size().unstack(), width=900, height=600)
st.warning("To reset the chart, simply double-click on it ℹ", icon="⚠️")


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("### Payment Type")

# Create a selectbox
option = st.multiselect(
    'Select Payment Type',
    ('Credit Card', 'Cash')
)

# Filter the DataFrame based on the selected option
filtered_df = df[df['Payment Type'].isin(option)]

color = st.color_picker('Choose a color for the bars', '#1f77b4')

# Create a bar chart based on the filtered data
st.bar_chart(filtered_df['Payment Currency'].value_counts(), color=color)
st.write("The chart displays the frequency of payments made for each payment method.")

##Create a bar chart based on Car type count

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("### Count of Car Type")
st.bar_chart(filtered_df['Car Type'].value_counts(), width=1000, height=600, color='#228B22')


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.write("Thank you so much for checking my web app data analysis of Careem😊")
st.write("The EDA by **Abdullah Farooq**")
st.write("👔 You can find my LinkedIn profile by clicking on the link below:")
st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/abdullah-farooq-3b8794199/)")
