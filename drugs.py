# Description: This file contains the code for the drugs dataset
import numpy as np
import pandas as pd

#For plotting
import matplotlib.pyplot as plt
import seaborn as sns

#For text processing
from textblob import TextBlob

#Attribute Information:
#drugName (categorical): name of drug
#condition (categorical): name of condition
#review (text): patient review
#rating (numerical): 10 star patient rating
#date (date): date of review entry
#usefulCount (numerical): number of users who found review useful


###Questions we want to answer
#1. Which is the most popular drug? -
#2. What are the groups/classification of drugs? -
#3. Which drug has the best review? 
#4. How many drugs do we have? -
#5. The number of drugs per condition -
#6. Number of patients that searched for particular drug
# Analysis the usefullCount column 
# Also questions about the reviews -
# and ratings -


#Loading the data
df = pd.read_csv('drugsComTrain_raw.tsv',sep='\t') # Reading the data
#The data is not in the csv format but we can read it using the sep='\t' parameter


#Previewing the data
print(df.head())


#We want to check what columns have null values
print(df.isnull().sum())

#-----------------Results-----------------
#We can see that the condition column has 899 null values
# Unnamed: 0       0
# drugName         0
# condition      899
# review           0
# rating           0
# date             0
# usefulCount      0
#-----------------------------------------
#So every missing value is in the condition column
#That means that most of people don't know what condition they have or dont want to share it







