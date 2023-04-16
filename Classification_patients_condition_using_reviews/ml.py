import pandas as pd
import itertools
import string
import numpy as np
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None) #To display all the rows
df = pd.read_csv('C:\Python\Drugs\drugsComTrain_raw.tsv',sep='\t')

df.condition.value_counts()

#To train the model we first try on 4 conditions that are in majority
df_train = df[(df['condition'] == 'Birth Control') | (df['condition'] == 'Depression') | (df['condition'] == 'Anxiety') | (df['condition'] == 'Pain')] 

#I drop the columns that are not required for the model
X = df_train.drop(['Unnamed: 0','drugName','date','rating','usefulCount'],axis=1)

#Segregating the data for individual conditions
X_BrCtrl = X[(X['condition'] == 'Birth Control')]
X_Dep = X[X['condition'] == 'Depression']
X_Anx = X[X['condition'] == 'Anxiety']
X_Pain = X[X['condition'] == 'Pain']

#Now we will create word cloud it will give us frequency words so we will see what words are most important 
# in classifying the condition by ploting all the words together 
from wordcloud import WordCloud

#Tokenizing the sentences
def WordCloudCreation(data,name):
    plt.figure(figsize = (20,20))
    wc = WordCloud(max_words = 500 , width = 1600 , height = 800).generate(" ".join(data.review))
    plt.imshow(wc , interpolation = 'bilinear')
    plt.title('Word Cloud for ' + name)
    

WordCloudCreation(X_BrCtrl,'Birth Control') #Word cloud for Birth Control
WordCloudCreation(X_Dep,'Depression') #Word cloud for Depression
WordCloudCreation(X_Anx,'Anxiety') #Word cloud for Anxiety
WordCloudCreation(X_Pain,'Pain') #Word cloud for Pain

#Cleaning the reviews
for i, col in enumerate(X.columns):
    X.iloc[:, i ] = X.iloc[:, i].str.replace('"', '')
pd.set_option('max_colwidth', -1)


#Removing stopwords from reviews
#Stop words are words like 'the', 'a', 'an', 'in' etc. which are not useful in NLP
from nltk.corpus import stopwords
stopWords = stopwords.words('english')



####Cleaning reviews
#Removing punctuations
#Removing special characters/numbers
#Converting to lowercase
#Lemmitization
#Lemmitization is used to reduce the words to their root form
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import re
def Cleaningsentences(sentence):
    sentence = BeautifulSoup(sentence, 'html.parser').get_text()
    sentence = re.sub(r'[^a-zA-Z]', ' ', sentence)
    sentence = sentence.lower().split()
    meaningful_words = [w for w in sentence if not w in stopWords]
    lemmitized_words = [WordNetLemmatizer().lemmatize(w) for w in meaningful_words]
    return ' '.join(lemmitized_words)
X['cleanReview'] = X['review'].apply(Cleaningsentences)

X.head()




#Creating a bag of words model

#Applying ML algorithms Naive Bayes & Passive Aggressive Classifier

#Creating TFIDF model

#Applying ML algorithms Naive Bayes & Passive Aggressive Classifier

#Comparing the accuracy of both the models