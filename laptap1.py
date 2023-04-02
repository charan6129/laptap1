import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random

from PIL import Image
logo = Image.open('logo1.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 

st.set_page_config(page_title="Laptap  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6162-v.Praneeth", "21A21A6138-M.Ankammarao", "21A21A6129-k.reshi charan","21A21A6141-murali","21A21A6124-Gopi","21A21A6135-Dinesh"]
st.title("Exploratory Data Analysis on laptap Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a  laptap Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    pd.DataFrame(data)
    st.title("laptap Data Analysis")
if st.checkbox("Get the head of the data"):
    st.write(data.head())
if st.checkbox("Get the mean of the all the laptaps"):
    st.write(data['price(in Rs.)'].mean())
if st.checkbox("Get the maimum price of the laptap"):
    st.write(data['price(in Rs.)'].max())
    
if st.checkbox("Get the minimum price of the laptap"):
     st.write(data['price(in Rs.)'].min())
if st.checkbox("Get the columns of the Dataset"):
    st.write(data.columns)
if st.checkbox("Get the shape of the Dataset"):
    st.write(data.shape)
if st.checkbox("Get the unique values of the DataSet"):
    st.write(data['name'].unique())
if st.checkbox("Get the null value of the dataset"):
    st.write(data.isnull().sum())
if st.checkbox("Get the None_null value of the dataset"):
    st.write(data.notnull().sum())
if st.checkbox("Get the index of the Dataset"):
    st.write(data.index)
if st.checkbox("Rename the price(in Rs.) to the price"):
    A=data.rename(columns={'price(in Rs.)':'price'},inplace=True)
    st.write(A)
    st.write(data.head())

if st.checkbox("Get the corr of the dataset"):
    n=(data.corr())
    st.write(n)

