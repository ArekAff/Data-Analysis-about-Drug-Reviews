import numpy as np
import pandas as pd

#For plotting
import matplotlib.pyplot as plt
import seaborn as sns

#For text processing
from textblob import TextBlob

df = pd.read_csv('drugsComTrain_raw.tsv',sep='\t')

#---------------Questions about Ratings----------------
#Distribution of ratings
# Avarage Rating per Count

#Distribution of ratings by Size 
print(df.groupby('rating').size())
#Result:
# 1.0     21619
# 2.0      6931
# 3.0      6513
# 4.0      5012
# 5.0      8013
# 6.0      6343
# 7.0      9456
# 8.0     18890
# 9.0     27531
# 10.0    50989

#df.groupby('rating').size().plot(kind='bar')
#plt.title("Distribution of ratings")
#plt.show()

#Distrubution of ratings by Size using histogram
#plt.figure(figsize=(20,10))
#df['rating'].hist()
#plt.title("Distrubution of ratings by Size using histogram")
#plt.grid(True)
#plt.show()

#Based on the data most people retes the drugs with 10,9,8 or 1 so we can say that poeple are more likely to rate the drugs within the extremes 

#What is the average rating of every drug?
average_rating = df['rating'].groupby(df['drugName']).mean()
print(average_rating)

plt.figure(figsize=(20,10))
average_rating.hist()
plt.title("Average rating of every drug")
plt.grid(True)
plt.show()

#Result:
#Based on the histogram we can see that most drugs have an average rating of 8-10
#So most people dont rate drugs low because the hisogram has an upward trend excludind the 1 rating


#Which class of drugs has the highest average rating?
#THIS QUESTION IS ANSWERED IN "classyfing_drugs.py"

#Which drug has the highest average rating?
print(average_rating.sort_values(ascending=False).head(20))
#Result:
# A + D Cracked Skin Relief    10.0
# Busulfan                     10.0
# Lesinurad                    10.0
# Bupivacaine liposome         10.0
# Buprenex                     10.0
# Lazanda                      10.0
# Vitafol-OB+DHA               10.0
# A / B Otic                   10.0
# SymlinPen 60                 10.0
# Synalar                      10.0
# Lidocaine / menthol          10.0
# Lanoxicaps                   10.0
# Lanolin                      10.0
# Lamivudine / zidovudine      10.0
# Synjardy                     10.0
# Lactic acid                  10.0
# Lac-Hydrin                   10.0
# Visine Original              10.0
# Leustatin                    10.0
# Sulfur                       10.0

