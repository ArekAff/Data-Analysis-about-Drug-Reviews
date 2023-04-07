import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Python\Drugs\drugsComTrain_raw.tsv',sep='\t') # Reading the data
#---------------1. Which is the most popular drug?----------------

#How many drugs do we have?

print(len(df['drugName'].unique()))
#-------Result: 3436

#That means that we have 3436 different drugs

#What is the most popular drug?

print(df['drugName'].value_counts().head(20)) #The top 20 drugs
#Result:
# Levonorgestrel                        3657
# Etonogestrel                          3336
# Ethinyl estradiol / norethindrone     2850
# Nexplanon                             2156
# Ethinyl estradiol / norgestimate      2117
# Ethinyl estradiol / levonorgestrel    1888
# Phentermine                           1543
# Sertraline                            1360
# Escitalopram                          1292
# Mirena                                1242
# Implanon                              1102
# Gabapentin                            1047
# Bupropion                             1022
# Venlafaxine                           1016
# Miconazole                            1000
# Medroxyprogesterone                    995
# Citalopram                             995
# Lexapro                                952
# Bupropion / naltrexone                 950
# Duloxetine                             934

#So the most popular drug is Levonorgestrel

plt.figure(figsize=(20,10))
df['drugName'].value_counts().nlargest(20).plot(kind='bar') 
plt.title("Top 20 Most used drugs based on number of reviews")
plt.show()

#After the research i concluded that the most popular drugs are hormonal contraceptives

#What are the least popular drugs based on reviews?
print(df['drugName'].value_counts().nsmallest(20)) #The top 20 lest popular drugs

# Clemastine                         1
# Topicort LP                        1
# Smoothie Readi-Cat 2               1
# Ipratropium Inhalation Solution    1
# Olux-E                             1
# Hexachlorophene                    1
# Pedi-Dri                           1
# Ginseng                            1
# Lincocin                           1
# EnLyte                             1
# Tums Smoothies                     1
# Purinethol                         1
# Aldomet                            1
# Midol Extended Relief              1
# Travel-Eze                         1
# Ponatinib                          1
# Wal-finate                         1
# Ciclodan                           1
# Niacinamide                        1
# Fragmin                            1
#Based on this result we cannot coclude anything because we have only 1 review for each drug so we cannot say if they are top 20 lest popular drugs

#This concludes our question about which is the most popular drug