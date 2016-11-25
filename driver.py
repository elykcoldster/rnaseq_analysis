import numpy as np
from sklearn.cluster import KMeans
from tcga_compile import extract_features

# TODO: Be able to extract data from an entire brca/luad/blca folder and cluster using kmeans (dimensionality reduction)
#brca_features = extract_features("../TCGA_data/brca/TCGA-A7-A0CE/TCGA-A7-A0CE-01/tcgaquant/data.txt", "../TCGA_data/brca/TCGA-A7-A0CE/TCGA-A7-A0CE-11/tcgaquant/data.txt")
brca_features = []
brca_features.append(extract_features("tumor_sample.txt", "normal_sample.txt"))
brca_features.append(extract_features("tumor_sample2.txt", "normal_sample2.txt"))

kmeans = KMeans(n_clusters=2).fit(brca_features)