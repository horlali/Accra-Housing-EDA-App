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

def main():
    
    # and Navigation bar
    #st.sidebar.title("Accommodation in Accra: An Exploratory Data Analysis")
    #st.sidebar.markdown("This application is an Accommodation Price in Accra Dashboard")

    # Title
    st.title("Accommodation in Accra: An Exploratory Data Analysis")
    st.header("This application is a Dashboard for Accommodation Prices in Accra")

    st.title("Data Exploration")
    st.header("Explore the Dataset with the option below")


    # DataFrame
    dataset = 'dataset.csv'


    # Enabling Cache
    @st.cache(persist=True, show_spinner=True)

    # Function to Load Dataset
    def load_data(data):
        df = pd.read_csv(os.path.join(dataset))
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
    data_dim = st.radio("What Dimension do you want to see?", ("All", "Rows","Columns"))
    if data_dim == "All":
        st.text("Showing shape of Dataset")
        st.write(data.shape)
    elif data_dim == "Rows":
        st.text("Showing rows")
        st.write(data.shape[0]) 
    else:
        st.text("Showing columns")
        st.write(data.shape[1])


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

    # Count of Categorical Variable
    st.subheader("Count Plots of Categorical Variable.")
    cat_vs = st.radio("Choose a categorical variable",["Furnishing Status","Amenities", "Location"])
    if cat_vs == "Furnishing Status":
        st.markdown("Number of Furnished Accommodation vs Not Furnished Accommodation")
        st.plotly_chart(data.furnished.value_counts().iplot(asFigure=True, kind='bar',xTitle='Furnishing Status',yTitle='No. of Occurances'))
    elif cat_vs == "Amenities":
        st.markdown("Number of Accommodation with Listed Amenites vs Not Listed Amenities")
        st.plotly_chart(data.amenities.value_counts().iplot(asFigure=True, kind='bar',xTitle='Furnishing Status',yTitle='No. of Occurances'))
    else:
        st.markdown("Location with the most Accomodation Listings")
        st.plotly_chart(data.location.value_counts().iplot(asFigure=True, kind='bar',xTitle='Furnishing Status',yTitle='No. of Occurances'))


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
    st.header("Bubble Plot - (Price, Bedrooms, Area)")
    if st.checkbox("A bubble plot of price and the number of bedrooms, with respect to floor area."):
        fig = data.iplot(asFigure=True, kind='bubble',x='bedrooms',y='price',size='area')
        st.plotly_chart(fig)


    # Pairplot of the Distribution
    st.header("Pairplot of the Distribution")
    if st.checkbox("Plot of the pairwise distribution of dataset"):
        st.pyplot(sns.pairplot(data))


    # Distribution of the Number of Bedrooms vs Price
    st.header("Distribution of Number of Bedrooms and Price")
    if st.checkbox("Distribution of Number of Bedrooms and Price"):
        fig, axis = plt.subplots(1,1, figsize = (15,10))
        sns.boxplot(data=data, x = 'bedrooms', y = 'price')
        axis.set_title('bedrooms Vs Price' )
        st.pyplot(fig)


    # Relationships between Price and other numerical variable.
    st.title("INSIGHT FROM DATA")
    st.header("This section reveals some of the most useful insight from the Dataset")

    st.markdown("Correlation Coefficient between Price, Floor Accra, Number of Bedrooms, etc.")
    st.write(data.corr())
    
    

    # Visualization of Insights
    st.header("Visualization of Insights")
    st.subheader("Relationship Between Price and Numerical Columns")
    insight_vs = st.selectbox("Select a feature to show relationship", ["Price vs Bedrooms", "Price vs Floor Area","Price vs Bathrooms","Price vs Garage"])
    if insight_vs == "Price vs Bedrooms":
        figure = data.iplot(asFigure=True, kind='scatter',x='price',y='bedrooms',mode='markers',xTitle='Price per month',yTitle='No. of Bedrooms')
        st.plotly_chart(figure)
    elif insight_vs == "Price vs Floor Area":
        figure = data.iplot(asFigure=True, kind='scatter',x='price',y='area',mode='markers',xTitle='Price per month',yTitle='Floor Area')
        st.plotly_chart(figure)
    elif insight_vs == "Price vs Bathrooms":
        figure = data.iplot(asFigure=True, kind='scatter',x='price',y='bathrooms',mode='markers',xTitle='Price per month',yTitle='No. of Bathrooms')
        st.plotly_chart(figure)
    else:
        figure = data.iplot(asFigure=True, kind='scatter',x='price',y='garage',mode='markers',xTitle='Price per month',yTitle='No. of Garage')
        st.plotly_chart(figure)
    

    # Locations with Affordable Accommodation
    st.header("Locations with Affordable Accommodation")
    st.markdown("This section explores the locations with affordable average price of accommodation in Accra")

    aver_price_locations = data.groupby(['bedrooms','location'],sort=True).mean().reset_index()
    
    one_br = aver_price_locations[aver_price_locations.bedrooms==1].sort_values(by=['price'])
    two_br = aver_price_locations[aver_price_locations.bedrooms==2].sort_values(by=['price'])
    three_br = aver_price_locations[aver_price_locations.bedrooms==3].sort_values(by=['price'])
    four_br = aver_price_locations[aver_price_locations.bedrooms==4].sort_values(by=['price'])
    five_br = aver_price_locations[aver_price_locations.bedrooms==5].sort_values(by=['price'])

    no_of_bedrooms = st.selectbox("Select number of Bedrooms", ["One Bedroom", "Two Bedrooms", "Three Bedrooms", "Four Bedrooms", "Five Bedrooms"])
    if no_of_bedrooms == "One Bedroom":
        st.plotly_chart(one_br.iplot(asFigure=True, kind='barh',x='location',y='price',title='One Bedroom Apartments',xTitle='price'))
    elif no_of_bedrooms == "Two Bedrooms":
        st.plotly_chart(two_br.iplot(asFigure=True, kind='barh',x='location',y='price',title='One Bedroom Apartments',xTitle='price'))
    elif no_of_bedrooms == "Three Bedrooms":
        st.plotly_chart(three_br.iplot(asFigure=True, kind='barh',x='location',y='price',title='One Bedroom Apartments',xTitle='price'))
    elif no_of_bedrooms == "Four Bedrooms":
        st.plotly_chart(four_br.iplot(asFigure=True, kind='barh',x='location',y='price',title='One Bedroom Apartments',xTitle='price'))
    else:
        st.plotly_chart(five_br.iplot(asFigure=True, kind='barh',x='location',y='price',title='One Bedroom Apartments',xTitle='price'))



    # INSIGHT
    st.title("Key Observation")
    st.text("VARIABLE THAT INFLUENCE THE PRICES OF ACCOMMODATION IN ACCRA")
    st.text("Some of the variable that influence the prices of accommodation in Accra includes")
    st.text("1. Location of the accommodation")
    st.text("2. The availability of the amenities")

    st.text("Other factors includes the following")

    st.text("The number of Bedrooms")
    st.text("The floor area measured in meter squared")
    st.text("The Number of garages")

    st.title("CONCLUSION")
    st.markdown("From the analysis and insight generated, we have learnt that there are various options for you if you need to rent accommodation in Accra.")
    st.markdown("Some of the main factors that influence the price of accommodation in Accra is the location, the availability of amenities.")
    st.markdown("The number of bedrooms and the size floor area only has a mid positive effect the price of accommodation.")
    st.markdown("It also goes without saying that at every price within the range of the dataset there is an available option except that you may have to sacrifice on some amenities and cater for furnishing the apartment.")
    st.markdown("The location of the accommodation will also determine how much your pay per month.")

    # About

    if st.button("About App"):
        st.subheader("Accommodation Prices in Accra")
        st.text("Built with Streamlit")

    if st.button("About Author"):
        st.text("Twitter: @_horlali")
        st.text("Github: wwww.github.com/horlali")
        




if __name__ == "__main__":
    main()