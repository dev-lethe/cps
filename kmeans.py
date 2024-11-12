# binary regression by k-means

kmeans = KMeans(n_cluster=2, random_state=0, n_init="auto").fit(X)
Y_pred = kmeans.label_
