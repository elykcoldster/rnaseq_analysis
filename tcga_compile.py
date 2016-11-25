import atpy
import numpy as np

def extract_features(tumor_file, normal_file):
    tt = atpy.Table(tumor_file, type='ascii')
    tn = atpy.Table(normal_file, type='ascii')
    t_counts = tt.c
    n_counts = tn.c

    diff_counts = []
    
    for i in range(0, len(t_counts)):
        
        diff_counts = t_counts.astype(float) - n_counts.astype(float)
    
    # compile tpm data from atpy table -> normal and tumor table lengths should be equal
    diff_tpm = []
    for i in range(0,len(tt)):
        diff_tpm.append(tt.data[i][0] - tn.data[i][0])

    features = np.concatenate((diff_counts, diff_tpm), axis=1)
    return features
