import numpy as np
import pandas as pd

#For plotting
import matplotlib.pyplot as plt
import seaborn as sns

#For text processing
from textblob import TextBlob

df = pd.read_csv('C:\Python\Drugs\drugsComTrain_raw.tsv',sep='\t') # Reading the data
#Questions About Reviews
# How genuine is the review? (Using sentiment analysis)
# How many reviews are positive and how many are negative?
# Correlation between the rating and the review and users who found the review useful
# Distruibution of the rating
# Amont of review made per year and per month
# Which condition has the most reviews on drugs?
# Can you predict the rating based on the review?


#How genuine is the review? (Using sentiment analysis)

#print(df['review'])

def get_sentiment(review):
    return TextBlob(review).sentiment.polarity # Returns the polarity of the review

def get_sentiment_label(sentiment): # Function that returns if sentiment is positive, negative or neutral
    value_of_polarity = get_sentiment(sentiment)
    if value_of_polarity > 0:
        return 'Positive'
    elif value_of_polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
df['sentimentPolarity'] = df['review'].apply(get_sentiment) # Adding a new column to the dataframe that is polarity of the review
df['sentimentLabel'] = df['review'].apply(get_sentiment_label) # Adding a new column to the dataframe that is label of the review

print(df[['review','sentimentPolarity']].head(10)) # Printing the first 10 rows of the dataframe
