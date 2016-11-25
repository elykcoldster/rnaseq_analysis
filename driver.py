import numpy as np
import sklearn as sk
from tcga_compile import extract_features

brca_features = extract_features("../TCGA_data/brca/TCGA-A7-A0CE/TCGA-A7-A0CE01/tcgaquant/data.txt", "../TCGA_data/brca/TCGA-A7-A0CE/TCGA-A7-A0CE11/tcgaquant/data.txt")