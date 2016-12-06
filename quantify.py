from tcga_compile import quant
import numpy as np
import sys

if len(sys.argv) == 4:
    tcga = sys.argv[1]
    salmon = sys.argv[2]
    kallisto = sys.argv[3]

    quant(tcga, salmon, kallisto)
else:
    print('Invalid number of arguments.')