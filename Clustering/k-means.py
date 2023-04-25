import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
df = pd.read_csv('drugsComTrain_raw.tsv',sep='\t')

# Sample a subset of the data
df = df.sample(frac=0.1, random_state=42)
# I keep only 10% of the original dataset because of memory issues 

# Convert categorical variables into numerical features
le = LabelEncoder()
df['drugName'] = le.fit_transform(df['drugName'])
df['condition'] = le.fit_transform(df['condition'])

# Normalize numerical features
scaler = StandardScaler()
df['rating'] = scaler.fit_transform(df['rating'].values.reshape(-1, 1))
df['usefulCount'] = scaler.fit_transform(df['usefulCount'].values.reshape(-1, 1))
df['drugName'] = scaler.fit_transform(df['drugName'].values.reshape(-1, 1))
df['condition'] =  scaler.fit_transform(df['condition'].values.reshape(-1, 1))



X = pd.concat([df[['condition', 'rating', 'usefulCount', 'drugName']]], axis=1)

# Impute missing values with the mean of the corresponding feature
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X.columns = X.columns.astype(str)
X = imputer.fit_transform(X)


# Choose the optimal number of clusters
inertia = []
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))
    
# Plot the elbow curve and silhouette scores
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
ax[0].plot(range(2,11), inertia, marker='o')
ax[0].set_xlabel('Number of Clusters')
ax[0].set_ylabel('Inertia')
ax[0].set_title('Elbow Curve')
ax[1].plot(range(2, 11), silhouette_scores, marker='o')
ax[1].set_xlabel('Number of Clusters')
ax[1].set_ylabel('Silhouette Score')
ax[1].set_title('Silhouette Score')
plt.show()
#after running the code i concluded that optimal number of clusters is 6


kmeans = KMeans(n_clusters=6, random_state=42).fit(X)

# assign cluster labels to new variable
labels = kmeans.labels_

# concatenate labels with X and other columns
clustered_df = pd.concat([df[['condition', 'rating', 'usefulCount', 'drugName']].reset_index(drop=True), pd.DataFrame(labels, columns=['cluster_label'])], axis=1)


# Define colors for each data point based on cluster label
colors = ['r', 'g', 'b']
cluster_colors = [colors[label] for label in clustered_df['cluster_label']]

# Plot data points with different colors for each cluster
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.scatter(clustered_df['condition'], clustered_df['rating'], clustered_df['usefulCount'], c=cluster_colors)

# Add labels to axes
ax.set_xlabel('Condition')
ax.set_ylabel('Rating')
ax.set_zlabel('Useful Count')
plt.title('K-Means Clustering')

plt.show()




