from sklearn.decomposition import PCA

# 主成分の数
n_compo = 10

# 主成分分析
X = PCA(n_components=n_compo).fit(X)

model = regression(X, Y)
