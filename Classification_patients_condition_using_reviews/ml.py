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

####Tokenizing the sentences
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


###Creating features and Target Variable
X_feat = X['cleanReview']
Y = X['condition']

X_train, X_test, y_train, y_test = train_test_split(X_feat, Y, stratify = Y, test_size=0.2, random_state=0)

def plot_confusion_matrix(cm, classes, normalize = False, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
        
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j], horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

#Naive Bayes Classifier
def Naive_Bayes(train , test):
    mnb = MultinomialNB()
    mnb.fit(train, y_train)
    pred = mnb.predict(count_test)
    score = metrics.accuracy_score(y_test, pred)
    print("accuracy:   %0.3f" % score)
    cm = metrics.confusion_matrix(y_test, pred, labels=['Birth Control', 'Depression', 'Anxiety', 'Pain'])
    plot_confusion_matrix(cm, classes=['Birth Control', 'Depression', 'Anxiety', 'Pain'])


#Passive Aggressive Classifier
from sklearn.linear_model import PassiveAggressiveClassifier,LogisticRegression
def Passive_Aggressive(train , test):
    passive = PassiveAggressiveClassifier()
    passive.fit(train, y_train)
    pred = passive.predict(test)
    score = metrics.accuracy_score(y_test, pred)
    print("accuracy:   %0.3f" % score)
    cm = metrics.confusion_matrix(y_test, pred, labels=['Birth Control', 'Depression', 'Anxiety', 'Pain'])
    plot_confusion_matrix(cm, classes=['Birth Control', 'Depression', 'Anxiety', 'Pain'])

####Creating a bag of words model
count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train)
count_test = count_vectorizer.transform(X_test)


#Applying ML algorithms Naive Bayes & Passive Aggressive Classifier with bag of words model
Naive_Bayes(count_train,count_test) #Result: 0.932 accuracy
Passive_Aggressive(count_train,count_test) #Result: 0.941 accuracy



####Creating TFIDF model
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8) 
#max_df is used for removing terms that appear too frequently, also known as 
# "corpus-specific stop words"
tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test= tfidf_vectorizer.transform(X_test)


#Applying ML algorithms Naive Bayes & Passive Aggressive Classifier with TFIDF model
Naive_Bayes(tfidf_train,tfidf_test) #Result: 0.887 accuracy Accuracy is less than the previous model
Passive_Aggressive(tfidf_train,tfidf_test) #Result: 0.948 accuracy ------------Highest accuracy

#Passive agressive classifier is generaly giving better results in accuracy

#TDIDF Bi-gram model
tfidf_vectorizer_2 = TfidfVectorizer(stop_words='english', max_df=0.8 ,ngram_range=(1,2))
tfidf_train_2 = tfidf_vectorizer_2.fit_transform(X_train)
tfidf_test_2 = tfidf_vectorizer_2.transform(X_test)

#Passive Aggressive Classifier with TDIDF Bi-gram model
Passive_Aggressive(tfidf_train_2,tfidf_test_2) #Result: 0.964 accuracy

#TDIDF Tri-gram model
tfidf_vectorizer_3 = TfidfVectorizer(stop_words='english', max_df=0.8 ,ngram_range=(1,3))
tfidf_train_3 = tfidf_vectorizer_3.fit_transform(X_train)
tfidf_test_3 = tfidf_vectorizer_3.transform(X_test)
#Passive Aggressive Classifier with TDIDF Bi-gram model
Passive_Aggressive(tfidf_train_3,tfidf_test_3) #Result: 0.964 accuracy --- Accuracy is same as Bi-gram model

X.tail()

passive = PassiveAggressiveClassifier()
passive.fit(tfidf_train_3, y_train)
pred = passive.predict(tfidf_test_3)
score = metrics.accuracy_score(y_test, pred)


text = ["This is the third med I&#039;ve tried for anxiety and mild depression. Been on it for a week and I hate it so much. I am so dizzy, I have major diarrhea and feel worse than I started. Contacting my doc in the am and changing asap."]
test = tfidf_vectorizer_3.transform(text)
pred1 = passive.predict(test)[0]
#Result: 'Depresion' that means the model is predicting the correct class
