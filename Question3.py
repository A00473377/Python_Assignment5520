#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:15:07 2023

Description:    This code implements the functionality to plot ahistogram based on provided csv file. The csv file is 
                expected to have a column titled "Age". then the code plots a histogram based on the data of age column
@author: zaidshaikh
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot histogram
def plot_histogram(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Age'], bins=20, kde=True)
    plt.title('Histogram of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    st.pyplot()

# Streamlit app
def main():
    st.title('CSV File Uploader and Histogram Plotter')

    # File upload section
    uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Check if the DataFrame has at least two columns
        if len(df.columns) >= 2:
            # Plot histogram if the DataFrame is valid
            plot_histogram(df)
        else:
            st.error('The uploaded file must have at least two columns.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
