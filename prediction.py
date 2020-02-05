import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
sns.set()

df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')

target = 'track_id'
features = df.columns.drop(['track_id', 'artist_name', 'track_name'])

X = X[features]
y = df[target]

knn = KNeighborsClassifier(n_neighbors=10, metric='euclidean')
knn.fit(X_train, y_train)

y = knn.kneighbors([X_train.iloc[30]])[1]
y = y.tolist()
y

for i in y:
    df['track_id'].loc[i]