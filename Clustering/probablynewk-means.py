from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from scipy.sparse import hstack
import numpy as np
df = pd.read_csv(r'C:\Users\Pendo\Desktop\MAD\Data-Analysis-about-Drug-Reviews\Clustering\drugsComTrain_raw.tsv',sep='\t')
df = df.sample(frac=0.4, random_state=42)
stopWords = stopwords.words('english')
def Cleaningsentences(sentence):
    sentence = BeautifulSoup(sentence, 'html.parser').get_text() #Removing HTML tags
    sentence = re.sub(r'[^a-zA-Z]', ' ', sentence) #Removing special characters
    sentence = sentence.lower().split() #Converting to lowercase
    meaningful_words = [w for w in sentence if not w in stopWords] #Removing stopwords
    lemmitized_words = [WordNetLemmatizer().lemmatize(w) for w in meaningful_words] #Lemmitization
    return ' '.join(lemmitized_words) #Joining the words to form a sentence

le = LabelEncoder()
df['drugName'] = le.fit_transform(df['drugName'])
df['condition'] = le.fit_transform(df['condition'])


df['cleanReview'] = df['review'].apply(Cleaningsentences)

vectorizer = TfidfVectorizer(stop_words='english')
cleanReview = vectorizer.fit_transform(df['cleanReview'].values.astype("U"))



X = hstack([cleanReview, 
            df['drugName'].values.reshape(-1, 1), 
            df['condition'].values.reshape(-1, 1)])


X = pd.concat([df[['condition', 'drugName']]], axis=1)

# # Elbow method
# wcss = []
# for i in range(1, 20):
#     kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
#     kmeans.fit(cleanReview)
#     wcss.append(kmeans.inertia_)
# plt.plot(range(1, 20), wcss)
# plt.title('Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()

# # Silhouette score
# silhouette_scores = []
# for n_clusters in range(2, 10):
#     kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
#     cluster_labels = kmeans.fit_predict(cleanReview)
#     silhouette_avg = silhouette_score(cleanReview, cluster_labels)
#     silhouette_scores.append(silhouette_avg)

# Elbow method
"""wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(cleanReview)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()"""

# Silhouette score
silhouette_scores = []
for n_clusters in range(880, 885):
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    cluster_labels = kmeans.fit_predict(cleanReview)
    silhouette_avg = silhouette_score(cleanReview, cluster_labels)
    silhouette_scores.append(silhouette_avg)

    
# plt.plot(range(2, 60), silhouette_scores)
# plt.title('Silhouette Score Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Silhouette score')
# plt.show()


def Cluster(X,n,s): 
    k = n
    model = KMeans(n_clusters=n, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    df['cluster'] = model.labels_

    labels = model.labels_

    clustered_df = pd.concat([df[['drugName', 'condition']].reset_index(drop=True), pd.DataFrame(labels, columns=['cluster'])], axis=1)

    u_labels = np.unique(labels)

    clustered_df[clustered_df['cluster'] == 0]

    for i in u_labels:
        clus = clustered_df[clustered_df['cluster'] == i]
        plt.scatter(clus['drugName'], clus['condition'] , label = i)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=12)
    plt.figsize=(20,60)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.xlabel("Leki",fontsize=20)
    plt.ylabel("Choroby",fontsize=20)
    plt.title(f"Klastrowanie K-means na podstawie {s}, {n} klastrów",fontsize=24)
    plt.show()

"""Cluster(cleanReview, 5, 'recenzji')
input()
Cluster(cleanReview, 10,'recenzji')
input()
Cluster(cleanReview, 15, 'recenzji')

X = pd.concat([df[['condition', 'drugName']]], axis=1)
Cluster(X, 5, 'chorób oraz nazw leków')
input()
Cluster(X, 10, 'chorób oraz nazw leków')
input()
Cluster(X, 15, 'chorób oraz nazw leków')

X = hstack([cleanReview, 
            df['drugName'].values.reshape(-1, 1), 
            df['condition'].values.reshape(-1, 1)])
Cluster(X, 5, 'recenzji, chorób oraz nazw leków')
input()
Cluster(X, 10, 'recenzji, chorób oraz nazw leków')
input()
Cluster(X, 15, 'recenzji, chorób oraz nazw leków')"""

def ClusterW(X,n,s): 
    k = n

    model = AgglomerativeClustering(n_clusters=n)
    model.fit(X)

    df['cluster'] = model.labels_


    labels = model.labels_

"""k = 60
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)


    clustered_df = pd.concat([df[['drugName', 'condition']].reset_index(drop=True), pd.DataFrame(labels, columns=['cluster'])], axis=1)

    u_labels = np.unique(labels)

    clustered_df[clustered_df['cluster'] == 0]

    for i in u_labels:
        clus = clustered_df[clustered_df['cluster'] == i]
        plt.scatter(clus['drugName'], clus['condition'] , label = i)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=12)
    plt.figsize=(20,60)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.xlabel("Leki",fontsize=20)
    plt.ylabel("Choroby",fontsize=20)
    plt.title(f"Klastrowanie aglomeracyjne na podstawie {s}, algorytmem ward'a dla {n} klastrów",fontsize=22)
    plt.show()



ClusterW(X, 5, "recenzji, chorób oraz nazw leków")
=======
for i in u_labels:
    clus = clustered_df[clustered_df['cluster'] == i]
    plt.scatter(clus['drugName'], clus['condition'] , label = i)
plt.legend()
plt.figsize=(20,100)
plt.show()"""

