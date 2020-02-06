import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pickle

df = pd.read_csv('spotify2019.csv')

target = 'track_id'
features = df.columns.drop(['track_id', 'artist_name', 'track_name', 'key', 'mode', 'time_signature' 'duration_ms'])

X = df[features].values
y = df[target].values

#Value normalization and dimensionality reduction
pca = PCA(n_components=2)
X = StandardScaler().fit_transform(X)
principalComponents = pca.fit_transform(X)
X = pd.DataFrame(data = principalComponents
                           , columns = ['x', 'y'])

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X, y)

y = knn.kneighbors([X.iloc[25173]])[1]
y = y.tolist()
y

for i in y:
    df['track_id'].loc[i]

for i in y:

# # Pickle the model
# filename = 'knn'
# pickle.dump(knn, open(filename, 'wb'))
