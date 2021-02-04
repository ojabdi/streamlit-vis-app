# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 04:59:14 2021

@author: umarj
"""
#import necessary packages
import pandas as pd
import streamlit as st 
import numpy as np, seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# configuration settings

st.set_option('deprecation.showfileUploaderEncoding', False)

#set the title for the app
st.title("Data Visualizations App")

#add sub header
st.sidebar.subheader("Visualization settings - New updates!! ")

#set upt the file upload
file_uploaded = st.sidebar.file_uploader(
    label = "Upload or Drop your data here",  
    type = ['csv','xlsx'])


#validate the uploaded file
global df

if file_uploaded is not None:
    try:
        df = pd.read_csv(file_uploaded)
    except Exception as e:
        print(e)
        df = pd.read_excel(file_uploaded)

#print the dataframe on 
global numeric_columsn
try:
    df = df[:2000]
    st.write(df.head())
    #filter numeric datatypes
    numeric_columsn = df.select_dtypes(
        ['float','int','int64','float64']).columns.tolist()

except Exception as e:
    print(e)
    st.write("PLEASE  upload a file to the system!")

#add a select widgets
chart_selections = st.sidebar.selectbox(
    label = "Slect Chart Type from drop-down lists",
    options = ["ScatterPlot","LinePlots","Histogram","BoxPlots"]
)

#correlations coefiicen
def corr_heatmap(xval,yval):
    df_col = df[[xval,yval]]
    fig, ax = plt.subplots(figsize=(5,4))
    sns.heatmap(df_col.corr(), annot=True, linewidths=.5, ax=ax)
    st.write(fig)
    return



if chart_selections =="ScatterPlot":
    st.sidebar.subheader('ScatterPlot')
    try:

        x_values = st.sidebar.selectbox('X axis', options=numeric_columsn)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columsn)
        plot = px.scatter(data_frame= df, x = x_values, y = y_values)

        #display the plots 
        st.plotly_chart(plot)

        #heatmap
        selecct_box = st.sidebar.checkbox("HeatMap")
        if selecct_box:
            corr_heatmap(x_values,y_values)

    except Exception as e:
        print(e)

#line plot
if chart_selections =="LinePlots":
    st.sidebar.subheader('LinePlots')
    try:

        x_values = st.sidebar.selectbox('X axis', options=numeric_columsn)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columsn)
        plot = px.line(data_frame= df, x = x_values, y = y_values)

        #display the plots 
        st.plotly_chart(plot)

        #heatmap
        selecct_box = st.sidebar.checkbox("HeatMap")
        if selecct_box:
            corr_heatmap(x_values,y_values)

    except Exception as e:
        print(e)
