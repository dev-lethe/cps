# binary regression by kNN

def regression(X, Y):
  from sklearn.neighbors import KNeighborsClassifier
  model = KNeighborsClassifier(n_neighbors=3)
  model.fit(X, y)
  return model

# Y_pred = knn.predict(X)
