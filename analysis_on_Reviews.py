from tools import *

#Questions About Reviews
# How genuine is the review? (Using sentiment analysis)
# How many reviews are positive and how many are negative?
# Correlation between the rating and the review and users who found the review useful
# Distruibution of the rating
# Amont of review made per year and per month
# Which condition has the most reviews on drugs?
# Can you predict the rating based on the review?


#-------------------How genuine is the review? (Using sentiment analysis)

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

df[['review','sentimentPolarity','sentimentLabel']] # Printing the first 10 rows of the dataframe
#Result:
# 0	"It has no side effect, I take it in combinati...	0.000000	Neutral
# 1	"My son is halfway through his fourth week of ...	0.168333	Positive
# 2	"I used to take another oral contraceptive, wh...	0.067210	Positive
# 3	"This is my first time using any form of birth...	0.179545	Positive
# 4	"Suboxone has completely turned my life around...	0.194444	Positive
# ...	...	...	...
# 161292	"I wrote my first report in Mid-October of 201...	0.262917	Positive
# 161293	"I was given this in IV before surgey. I immed...	-0.276389	Negative
# 161294	"Limited improvement after 4 months, developed...	-0.223810	Negative
# 161295	"I&#039;ve been on thyroid medication 49 years...	0.212597	Positive
# 161296	"I&#039;ve had chronic constipation all my adu...	0.085417	Positive

#How many positive and nagative reviews are there?

df['sentimentLabel'].value_counts()
# Positive    101041
# Negative     53303
# Neutral       6953

df['sentimentLabel'].value_counts().plot(kind='bar')

#So we can see that magority of the reviews are positive

sns.lineplot(data=df, x='rating', y='sentimentPolarity')
plt.title('Correlation between the rating and the review polarity')
plt.show()
#As we can see there is a positive correlation between the rating and the review polarity
# So as the rating increases the review polarity also increases

#Correlation between rating and sentiment
sns.lineplot(data=df, x='rating', y='sentimentPolarity', hue='sentimentLabel')
plt.show()
#From the graph we can see that when the rating rises sentiment polarity 
# increases even when sentiment in considered negative

# How many reviews are genuine as compared to the rating
# I assume that geunine positive reviews shoud accoure when rating is between
# 10 - 6 netural should be at 5 and negative should be at 4 and below

# Genunine positive rating
goodReview = df[(df['rating'] >= 6) & (df['sentimentLabel'] == 'Positive')]

# Genunine negative rating
badReview = df[(df['rating'] <= 4) & (df['sentimentLabel'] == 'Negative')]

goodReview.iloc[1]['review']
# Example of good review:
#'"My son is halfway through his fourth week of Intuniv. We became 
# concerned when he began this last week, when he started taking the 
# highest dose he will be on. For two days, he could hardly get out of bed, 
# was very cranky, and slept for nearly 8 hours on a drive home from school 
# vacation (very unusual for him.) I called his doctor on Monday morning and 
# she said to stick it out a few days. See how he did at school, and with 
# getting up in the morning. The last two days have been problem free. 
# He is MUCH more agreeable than ever. He is less emotional (a good thing), 
# less cranky. He is remembering all the things he should. Overall his 
# behavior is better. \r\nWe have tried many different medications and 
# so far this is the most effective."'
