# Description: This file contains the code for the drugs dataset
import numpy as np
import pandas as pd

#For plotting
import matplotlib.pyplot as plt
import seaborn as sns

#For text processing
from textblob import TextBlob

df = pd.read_csv('C:\Python\Drugs\drugsComTrain_raw.tsv',sep='\t') # Reading the data

#The usefull count is number of users who found review useful 


###-------------------Questions for usefulCount
# number of users who found review useful
# Top UsefulCount By DrugClass
# Best drugs based usfulCount

df.groupby('drugName')['usefulCount'].value_counts()# Grouping the data by drugName and usefulCount and counting the number of reviews for each drugName and usefulCount
#result:
# A + D Cracked Skin Relief             6              1
# A / B Otic                            20             1
# Abacavir / dolutegravir / lamivudine  9              6
#                                       1              5
#                                       12             5
#                                                     ..
# ella                                  32             1
#                                       42             1
# femhrt                                0              1
#                                       2              1
#                                       42             1

# Top Drugs per UsefulCount
df.groupby('drugName')['usefulCount'].nunique().sort_values(ascending=False).head(20)
#Top 10 drugs based on usefulCount
# Gabapentin       181
# Fluoxetine       181
# Bupropion        177
# Citalopram       176
# Sertraline       172
# Zoloft           171
# Escitalopram     171
# Prozac           171
# Lexapro          169
# Celexa           166
# Amitriptyline    162
# Lorcaserin       157
# Trazodone        157
# Duloxetine       153
# Phentermine      150
# Belviq           148
# Alprazolam       146
# Cymbalta         144
# Venlafaxine      144
# BuSpar           141

#Plotting the top 20 drugs based on usefulCount
df.groupby('drugName')['usefulCount'].nunique().sort_values(ascending=False).head(20).plot(kind='bar',figsize=(15,5))

df.groupby('drugClass')['usefulCount'].nunique().sort_values(ascending=False).head(20)
#Top 10 drugs based on usefulCount
# Selective serotonin reuptake inhibitors                                 222
# tricyclic antidepressant (TCA)                                          179
# diazepam derivatives                                                    178
# anti-inflammatory agents, ibufenac derivatives                          176
# antidepressant                                                          174
# psychoactive                                                            157
# Loop diuretics                                                          154
# Nondepolarizing paralytics                                              150
# Benzodiazepinea                                                         146
# tricyclic compounds                                                     145
# Phosphodiesterase inhibitors                                            142
# antihypertensives, clonidine derivatives                                139
# anxiolytics, buspirone derivatives                                      139
# analgesics                                                              132
# monoclonal antibodies                                                   131
# angiotensin II receptor antagonists, antihypertensive (non-peptidic)    129
# b-adrenoreceptor antagonists                                            123
# HMG-CoA reductase inhibitors                                            122
# Azole antifungals                                                       119
# female hormone (progestin)                                              116

df.groupby('drugClass')['usefulCount'].nunique().sort_values(ascending=False).head(20).plot(kind='bar',figsize=(15,5))
