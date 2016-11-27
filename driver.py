import numpy as np
import os
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.externals import joblib
from tcga_compile import extract_features
from tcga_compile import extract_single_features

# TODO: Be able to extract data from an entire brca/luad/blca/etc folder and cluster using kmeans
#brca_features = extract_features("../TCGA_data/brca/TCGA-A7-A0CE/TCGA-A7-A0CE-01/tcgaquant/data.txt", "../TCGA_data/brca/TCGA-A7-A0CE/TCGA-A7-A0CE-11/tcgaquant/data.txt")
#directories = ['brca'] # for Windows test
directories = ['../TCGA_data/brca', '../TCGA_data/luad', '../TCGA_data/blca', '../TCGA_data/prad'] # for cluster unix use

features = []
for i in range(0, len(directories)):
	subdirs = os.listdir(path=directories[i])
	for j in range(0, len(subdirs)):
		curr_path = directories[i] + '/' + subdirs[j]
		normcancer = os.listdir(path=curr_path)
		cancfiles = os.listdir(curr_path + '/' + normcancer[0] + '/tcgaquant')
		features.append(extract_single_features(curr_path + '/' + normcancer[0] + '/tcgaquant/' + cancfiles[0]))

pca = PCA(n_components=24)
pca.fit_transform(features)
kmeans = KMeans(n_clusters=len(directories)).fit(features)
joblib.dump(kmeans, 'kmeans.pkl')
joblib.dump(pca, 'pca.pkl')
print(kmeans.labels_)
