# Streamlit Library
import streamlit as st

# Standard EDA Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Imaging Library
from PIL import Image

# Interactive Visualization Library
import cufflinks as cf
from plotly.offline import download_plotlyjs,plot,iplot
cf.go_offline()


# Enabling Cache
@st.cache(persist=True)


# Title
st.title("Accommodation in Accra: An Exploratory Data Analysis")
st.header("Built with Streamlit")

st.title("Data Exploration")
st.header("Explore the Dataset with the option below")


# DataFrame
dataset = 'accra_housing_dataset.xlsx'


# Function to Load Dataset
def load_data(data):
    df = pd.read_excel(os.path.join(dataset))
    return df

data = load_data(dataset)


# Showing heads and tails of Dataset
show_data = st.radio("What section of the Dataset do you want to see",("Head","Tails","Sample","Whole"))
if show_data == 'Head':
    st.text("Showing the first 5 entries of the Dataset")
    st.write(data.head())
elif show_data == 'Tails':
    st.text('Showing the last 5 entries of the Dataset')
    st.write(data.tail())
elif show_data == 'Sample':
    st.text('Showing some 5 random entries from the Dataset')
    st.write(data.sample(5))
else:
    st.text('Show entire Dataset')
    st.dataframe(data)


# Show Column Names
if st.checkbox("Show column Names"):
    st.write(data.columns)


# Show Dimensions
data_dim = st.radio("What Dimension do you want to see?", ("Rows","Columns","All"))
if data_dim == "Rows":
    st.text("Showing Rows")
    st.write(data.shape[0])
elif data_dim == "Columns":
    st.text("Showing Colums")
    st.write(data.shape[1]) 
else:
    st.text("Showing shape of Dataset")
    st.write(data.shape)


# Show Summary
data_summary = st.radio("This show a summary of the Dataset, both Numeric and Categorical",("Numeric","Categorical"))
if data_summary == "Numeric":
    st.text("Show Summary of Numerical Columns in Dataset")
    st.write(data.describe().transpose())
else:
    st.text("Show Summary of Categorical Columns in Dataset")
    st.write(data.describe(exclude='number').transpose())


# Select A Column
col_option = st.selectbox("Select Column",("price","categories","bedrooms",
"bathrooms","garage","area","location","amenities","furnished"))
if col_option == "price":
    st.write(data['price'])
elif col_option == "categories":
    st.write(data['categories'])
elif col_option == "bedrooms":
    st.write(data['bedrooms'])
elif col_option == "bathrooms":
    st.write(data['bathrooms'])
elif col_option == "garage":
    st.write(data['garage'])
elif col_option == "area":
    st.write(data['area'])
elif col_option == "location":
    st.write(data['location'])
elif col_option == "amenities":
    st.write(data['amenities'])
elif col_option == "furnished":
    st.write(data['furnished'])
else:
    st.write("Select a Column to show dataset")




# Data Visualization

st.title("Data Visualization")
st.header("Explore this easy to understand interactive chart to understand accommodation pricing in Accra")

# World Cloud of Location
st.header("WordCloud of Location of Apartment Listing")
from wordcloud import WordCloud
texts = " ".join(location for location in data.location)
wordcloud = WordCloud(width=3000,height=1800,margin=1,max_font_size=150).generate(texts)

if st.checkbox("Word Cloud of Locations"):
    fig, ax = plt.subplots()
    st.write(plt.imshow(wordcloud))
    st.write(plt.axis('off'))
    st.pyplot(fig)


# Distribution of Prices
st.header("Distribution of Prices")
dist_option = st.selectbox('Select option',["Boxplot","Histogram"])
if dist_option == "Boxplot":
    fig1 = data['price'].iplot(asFigure=True, kind='box',title='Distribution of Price')
    st.plotly_chart(fig1)
elif dist_option == "Histogram":
    fig2 = data['price'].iplot(asFigure=True, kind='hist',bins=15,title='Distribution of Price')
    st.plotly_chart(fig2)


# A bubble plot of price and the number of bedrooms, with respect to floor area.
st.header("Bubble Plot - [Price, Bedrooms, Area]")
if st.checkbox("A bubble plot of price and the number of bedrooms, with respect to floor area."):
    fig = data.iplot(asFigure=True, kind='bubble',x='bedrooms',y='price',size='area')
    st.plotly_chart(fig)