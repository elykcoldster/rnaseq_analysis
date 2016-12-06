import sys
from sklearn.externals import joblib

def quant(tcga, salmon, kallisto):
    tcga_kmeans = joblib.load(tcga);
    salmon_kmeans = joblib.load(salmon);
    kallisto_kmeans = joblib.load(kallisto);

    print('TCGA KMeans Labels:')
    print(tcga_means.labels_)
    print('Salmon KMeans Labels:')
    print(salmon_means.labels_)
    print('Kallisto KMeans Labels:')
    print(kallisto_means.labels_)

if len(sys.argv) == 4:
    tcga = sys.argv[0]
    salmon = sys.argv[0]
    kallisto = sys.argv[0]

    # quant(tcga, salmon, kallisto)
else:
    print('Invalid number of arguments.')