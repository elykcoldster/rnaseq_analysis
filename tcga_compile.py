import atpy
import numpy as np

def extract_single_features(tumor_file):
    tt = atpy.Table(tumor_file, type='ascii')
    data = tt.data

    tpm_col = 0
    for i in range(0, len(data[0])):
        if (is_float(data[0][i])):
            tpm_col = i
    
    tpm = []
    for i in range(0, len(data)):
        tpm.append(data[i][tpm_col])
    return tpm

def extract_features(tumor_file, normal_file):
    tt = atpy.Table(tumor_file, type='ascii')
    tn = atpy.Table(normal_file, type='ascii')
    t_counts = tt.c
    n_counts = tn.c

    diff_counts = []
    
    for i in range(0, len(t_counts)):
        if isinstance(t_counts[i], np.int32) and isinstance(n_counts[i], np.int32):
            diff_counts.append(t_counts[i].astype(float) - n_counts[i].astype(float))
    
    # compile tpm data from atpy table -> normal and tumor table lengths should be equal
    #diff_tpm = []
    #for i in range(0,len(tt)):
    #    diff_tpm.append(tt.data[i][0] - tn.data[i][1])

    #features = np.concatenate(([diff_counts], [diff_tpm]), axis=0)
    return diff_counts

def is_float(s):
    try:
        int(s)
    except ValueError:
        try:
            float(s)
            return True
        except ValueError:
            return False
    return False