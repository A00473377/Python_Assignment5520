#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:53:59 2023

@author: zaidshaikh
Description: SOLUTION FOR QUESTION2
    The current file contains the code to handle the function of counting vowels from a dataset. 
    Here the data set can be uploaded using a csv file. And the output is also a csv file with an additional column added that contains
    the number of vowels in the title.
"""

import pandas as pd

#Sample dataset beinaken from a csv file
data = pd.read_csv("titles.csv")

df = pd.DataFrame(data)

#Function to count the number of vowels in a given text.
def count_vowels(text):
    if isinstance(text, str):  # Checking if the value is a string
        vowels = set("aeiouAEIOU")
        return sum(1 for char in text if char in vowels)
    else:
        return 0  # Returning 0 if the title column is empty

# Applying the count_vowels function to the 'title' column
df['vowel_count'] = df['title'].apply(count_vowels)

# Displaying the DataFrame with the added 'vowel_count' column
print(df)

#exporting the data in csv
df.to_csv('output3.csv', index=False)
