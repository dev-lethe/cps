# binary regression by k-means

from sklearn.cluster import Kmeans
Y_pred = KMeans(n_cluster=2, random_state=0, n_init="auto").fit_predict(X)
